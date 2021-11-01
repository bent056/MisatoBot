import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
  def __init__(self, bot):
    self.client = bot


@commands.command()
async def play(self, ctx, url):
  if ctx.message.author.voice:
    channel = ctx.author.voice.channel
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


@commands.command()
async def pause(self, ctx):
  await ctx.voice_client.pause()
  await ctx.send('Paused')


@commands.command()
async def resume(self, ctx):
  await ctx.voice_client.resume()
  await ctx.send('Resumed')


@commands.command()
async def leave(self, ctx):
  if ctx.voice_client:
    await ctx.voice_client.disconnect()
    await ctx.send('Bye bye :misatoprayer:')
  else:
    await ctx.send("I'm not in a voice channel")


def setup(bot):
  bot.add_cog(music(bot))