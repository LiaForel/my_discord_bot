import discord
import asyncio
from pymongo import MongoClient

# creating an API instance of an object
client = discord.Client()
mongo_client = MongoClient("mongodb")
db = mongo_client.my_database

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
      # flag 
      exists = False
      result = ''
      content = content[content.find(' ')+1:] #removing the command line and space in !test
      for item in db.myTable.find():
        # message as a key
        if(content == item['message'].lower()):
          exists = True
          result = item['message']
      if (exists == True):
        await message.channel.send(result)
      else:
        await message.channel.send('The query does not exist')
      
    if message.content.startswith('!remove '):
      #remove item from my_database
      exists = False
      remove = ''
      content = content[content.find(' ')+1:]
      for i in db.myTable.find():
        if(content == item['message'].lower()):
          exists = True
          remove = item['message']
      if (exists = True):
        db.myTable.delete_one(remove)
      else:
        await message.channel.send('The query does not exist in the data base to be removed')
        






      
      
# add delete from the database

client.run('KEY')
