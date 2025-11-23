
import discord
from groq import Groq

DISCORD_TOKEN = "BOT_TOKEN_"
import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

client = discord.Client(intents=intents)
groq_client = Groq(api_key=GROQ_API_KEY)

async def get_groq_reply(text):
    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are Nayan ki GF. Talk cute, funny, flirty."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Reply only when someone mentions the bot
    if client.user in message.mentions:
        user_msg = message.content.replace(f"<@{client.user.id}>", "").strip()
        if user_msg == "":
            user_msg = "Hi!"

        reply = await get_groq_reply(user_msg)
        await message.reply(reply)

client.run(DISCORD_TOKEN)
