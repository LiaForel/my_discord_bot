import discord
import asyncio

# creating an API instance of an object
client = discord.Client()


@client.event
# async running multiple things at same time
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    # await discord.Client().change_presence(activity=None, status="Type !commands to get started!", afk=False)


@client.event
async def on_message(message):
    # message content
    content = message.content
    content = content.lower()

    if message.content.startswith('!type'):
        await message.channel.send('Rahil is awesome!')
    if message.content.startswith('!drink'):
        await message.channel.send('I owe Rahil a drink!')
    if message.content.startswith('!image'):
        await message.channel.send(file=discord.File('images/meme_one.jpg'))



client.run('NjIyMTgyNDI4MDgxMTI3NDQ0.XYBQWQ.nSaCx6FbjXwlboTPpBVQFa9g1gM')
