import requests
import json
import discord
import asyncio
import time

token = "Enter Your token here"     # Read readme to understand how to get your token
if token == "Enter Your token here":
    token = input("Please enter your token here: ")
    
client = discord.Client()

def delete_server(token, id):
    useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36"
    headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': useragent}

    print(id.rstrip())

    data = {}

    src = requests.post("https://discordapp.com/api/v6/guilds/{}/delete".format(id.rstrip()), json=data, headers=headers)
    try:
        print(json.loads(src.content.decode()))
    except:
        pass

@client.event
@asyncio.coroutine
def on_ready():
    print("You are currently on {} servers".format(len(client.servers)))
    for s in client.servers:
        if s.name == "All hail Anarchy!":
            delete_server(token, s.id)
            time.sleep(1)

client.run(token, bot=False)