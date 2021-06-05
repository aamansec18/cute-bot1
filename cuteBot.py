import discord
import os
import requests
import json
import random


client = discord.Client()
hockey_words =["offense", "vegas", "knights", "pls", "vibing"]
response_quotes =["You're still cute", "Pandas and flowers are cute together!", 
                    "Fuck the sharks"]

# quote function
def get_quote():
    quote_list = [ "You are cute!", 
                    "You are the cutest!", "Why are you so cute?", 
                    "Let's be cute together!", "No one can match your cuteness"]
    return(random.choice(quote_list))

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('c!greet'):
        quote = get_quote()
        await message.channel.send(quote)
    
    if any(word in message.content for word in hockey_words):
         await message.channel.send(random.choice(response_quotes))

client.run('ODQ4NzU5MDEwODA2MDcxMjk2.YLRSbQ.6wH-rCHl3GxMtQpRjqANzqZMXqY')