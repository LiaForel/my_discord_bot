import discord
import asyncio
from pymongo import MongoClient


# creating an API instance of an object
client = discord.Client()
mongo_client = MongoClient("mongodb+srv://liaForel:admin123@liacluster-dlc08.mongodb.net/test?retryWrites=true&w=majority")
db = mongo_client.my_database

# MongoClient("mongodb+srv://puistori:gebit%40worker92@incidental-acquisition-caxuy.mongodb.net/test?retryWrites=true&w=majority")

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
    if message.content.startswith('!test '):
        # put content anything after space " "in !test
        content = content[content.find(" ")+1:]
        req_data = {'message' : content}
        db.myTable.insert_one(req_data)
        await message.channel.send('process is complete!')
    if message.content.startswith('!search '):
        for item in db.myTable.find():
          await message.channel.send(item['message'])
    

client.run('NjIyMTgyNDI4MDgxMTI3NDQ0.XYBQWQ.nSaCx6FbjXwlboTPpBVQFa9g1gM')
