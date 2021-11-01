import discord
import os
from discord.ext import commands
import youtube_dl
import announcements
import chatlog
import MisatoCop
import music
from keep_alive import keep_alive

token = os.environ['token']
client = discord.Client()
client = commands.Bot(command_prefix='mommy ')
cog = [announcements, chatlog, MisatoCop]

for i in range(len(cog)):
    cog[i].setup(client)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name='you'))
    print(f'\n\nLogged in as: {client.user.name} - {client.user.id}\nVersion: {discord.__version__}\n')   

# music 
@client.command()
async def play(ctx, url):
  if ctx.message.author.voice:
    channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await channel.connect()
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format':"bestaudio"}
    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download=False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
      vc.play(source)
  else:
    await ctx.send("You aren't in a voice channel idiot")


@client.command()
async def pause(ctx):
  if ctx.voice_client:
    await ctx.voice_client.pause()
    await ctx.send('Paused')
  else:
    await ctx.send("I can't do that if I'm not in a voice channel silly <:misatodrink:901105700246274058>")


@client.command()
async def start(ctx):
  if ctx.voice_client:
    await ctx.voice_client.resume()
    await ctx.send('Resumed')
  else:
    await ctx.send("I can't do that if I'm not in a voice channel silly <:misatodrink:901105700246274058>")


@client.command()
async def leave(ctx):
  if ctx.voice_client:
    await ctx.voice_client.disconnect()
    await ctx.send('Bye bye :misatoprayer:')
  else:
    await ctx.send("I can't do that if I'm not in a voice channel silly <:misatodrink:901105700246274058>")


keep_alive()
client.run(token)
