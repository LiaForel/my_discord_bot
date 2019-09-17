import discord
import asyncio
from pymongo import MongoClient


# creating an API instance of an object
client = discord.Client()
mongo_client = MongoClient("mongodb+srv://liaForel:admin123@liacluster-dlc08.mongodb.net/test?retryWrites=true&w=majority")
db = mongo_client.my_database

# mongodb+srv://liaForel:admin123@liacluster-dlc08.mongodb.net/test?retryWrites=true&w=majority

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
    if message.content.startswith('!test'):
        req_data = {'message' : content}
        db.myTable.insert_one(req_data)
        await message.channel.send('process is complete!')




client.run('NjIyMTgyNDI4MDgxMTI3NDQ0.XYBQWQ.nSaCx6FbjXwlboTPpBVQFa9g1gM')
