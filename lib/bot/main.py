  
import requests
import json
import os
from dotenv import load_dotenv
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

#Status
@client.event
async def on_ready():
    print('We have logged in as {0.user}'
    .format(client))

#command
@client.command()
async def ping(ctx):
    await ctx.send('Pong!')


#specific keyword prompt
@client.listen('on_message')
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content
    
    if msg.startswith('quote'):
        quote = get_quote()
        await message.channel.send(quote)
    
    if msg.startswith('test'):
        await message.channel.send('I am fully functional!')


#get function
def get_quote():
    response = requests.get("Https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

load_dotenv()
client.run(os.environ.get("SECRET_KEY"))