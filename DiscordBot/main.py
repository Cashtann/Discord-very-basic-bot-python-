import discord
from discord.ext import commands, tasks
from time import sleep
from random import randint
from discord import FFmpegPCMAudio
import os

client = commands.Bot(command_prefix='kierowniku ')
client.remove_command('help')

@client.command()
async def help(ctx):
    await ctx.channel.send("""Available commands: 
    Every command starts with bot prefix

    ~ losuj \{num1\} \{num2\}
    ~ help 
    ~ ping \{username\} \{ping amount\}
    ~ play \{song name\} \{channel\} 
        if in channel name is space, repalce it with underline _
    ~ songindex
    ~ leave
    ~ pause
    ~ resume
    ~ stop

    
    """)

# this section is weird, its about valorant commands xd

@client.command()
async def valw(ctx):
    a = randint(1, 19)
    b = randint(1, 3)
    if b == 1: await ctx.channel.send('0 Armor') 
    if b == 2: await ctx.channel.send('25 Armor')
    if b == 3: await ctx.channel.send('50 Armor')
    #############
    if a == 1: await ctx.channel.send('Classic') 
    if a == 2: await ctx.channel.send('Shorty')
    if a == 3: await ctx.channel.send('Frenzy')
    if a == 4: await ctx.channel.send('Ghost')
    if a == 5: await ctx.channel.send('Sheriff')
    if a == 6: await ctx.channel.send('Stinger')
    if a == 7: await ctx.channel.send('Bulldog')
    if a == 8: await ctx.channel.send('Marshal')
    if a == 9: await ctx.channel.send('Spectre')
    if a == 10: await ctx.channel.send('Guardian')
    if a == 11: await ctx.channel.send('Operator')
    if a == 12: await ctx.channel.send('Bucky')
    if a == 13: await ctx.channel.send('Phantom')
    if a == 14: await ctx.channel.send('Ares')
    if a == 15: await ctx.channel.send('Judge')
    if a == 16: await ctx.channel.send('Vandal')
    if a == 17: await ctx.channel.send('Odin')
    if a == 18: await ctx.channel.send('( ͡° ͜ʖ ͡°) Knife ( ͡° ͜ʖ ͡°)')
    if a == 19: await ctx.channel.send('( ͡° ͜ʖ ͡°) Knife ( ͡° ͜ʖ ͡°)')

@client.command()
async def vala(ctx):
    a = randint(1, 19)
    if a == 1: await ctx.channel.send('Astra') 
    if a == 2: await ctx.channel.send('Breach')
    if a == 3: await ctx.channel.send('Brimstone')
    if a == 4: await ctx.channel.send('Chamber')
    if a == 5: await ctx.channel.send('Cypher')
    if a == 6: await ctx.channel.send('Fade')
    if a == 7: await ctx.channel.send('Jett')
    if a == 8: await ctx.channel.send('KAY/O')
    if a == 9: await ctx.channel.send('Killjoy')
    if a == 10: await ctx.channel.send('Neon')
    if a == 11: await ctx.channel.send('Omen')
    if a == 12: await ctx.channel.send('Phoenix')
    if a == 13: await ctx.channel.send('RAze')
    if a == 14: await ctx.channel.send('Reyna')
    if a == 15: await ctx.channel.send('Sage')
    if a == 16: await ctx.channel.send('Skye')
    if a == 17: await ctx.channel.send('Sova')
    if a == 18: await ctx.channel.send('Viper')
    if a == 19: await ctx.channel.send('Yoru')
    


############################## LOSU LOSU ##########################################

@client.command()
async def losuj(ctx, num1:int, num2:int):
    await ctx.channel.send('Losu losu.')
    await ctx.channel.send('Losu losu..')
    await ctx.channel.send('Losu losu...')
    await ctx.channel.send(str(randint(num1,num2)))


@client.command()
async def songindex(ctx):
    await ctx.channel.send("""

tiger1
szklanki
elevator
    
    """)


@client.command()
async def WhoIsTheBest(ctx):
    await ctx.channel.send('Oczywiście że ty')





############################## LOSU LOSU ###############################################

############################## MUZYKA ##############################################






@client.command()
async def play(ctx, songname:str, channel : str):
    channel1 = channel.replace('_', ' ')
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel1)
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    voice.play(discord.FFmpegPCMAudio(str(songname+".mp3")))






@client.command()
async def play1(ctx, channel : str):
    channel1 = channel.replace('_', ' ')
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel1)
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def play2(ctx, channel : str):
    channel1 = channel.replace('_', ' ')
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel1)
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    voice.play(discord.FFmpegPCMAudio("szklanki.mp3"))


@client.command()
async def play3(ctx, channel : str):
    channel1 = channel.replace('_', ' ')
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel1)
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    voice.play(discord.FFmpegPCMAudio("elevator.mp3"))
















@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()





################################# MUZYKA #############################################
########################### PING BOT ###################################################



@client.command()
async def ping(ctx, username : str, amountofping : int):
    if amountofping >= 10:
        await ctx.channel.send('Nie dla psa')
        return
    if cashtan in username or range1 in username or range2 in username:
        await ctx.channel.send('Nie dla psa')
        return
    for i in range(amountofping):
        await ctx.channel.send(username)
        print(username)


 
############################### PING BOT ##############################################




client.run('   YOUR DISCORD APP KEY (do NOT share this code to public!)   ')



