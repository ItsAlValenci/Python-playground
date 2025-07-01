class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    pass

import discord

TOKEN = 'your-bot-token'
CHANNEL_ID = 123456789012345678

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send("This is a custom bot notification!")
    await client.close()

client.run(TOKEN)