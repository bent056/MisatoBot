import discord
from discord.ext import commands
import datetime
client = discord.Client()

sus_words = ["diona", "sayu", "klee", "qiqi", "loli"]

class MisatoCop(commands.Cog):
    def __init__(self, client):
        self.client = client
  
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.author.id == 439524693234548738:
            if any(word in message.content.lower() for word in sus_words):
                sus = discord.Embed(title = "**Suspicious Activity Detected**", url = "", description = f"Suspicious activity has been detected from user {message.author.mention} in {message.channel.mention} in server **{message.guild.name}**. The corresponding authorities have been notified.",color=discord.Color.red())
                sus.set_author(name="MisatoCop", url="https://evangelion.fandom.com/wiki/Misato_Katsuragi", icon_url="https://i1.sndcdn.com/artworks-000608460694-vas0jy-t500x500.jpg")
                sus.set_thumbnail(url="https://64.media.tumblr.com/f33efa4b07f6b67b918a84807dbae316/tumblr_owa7qyiSbC1r3ew35o2_r1_1280.png")
                sus.add_field(name="**Suspicious Message**", value=f"`{message.content}`", inline=True)
                sus.add_field(name="**Authorities Notified**", value="[United States Department of Justice](https://www.justice.gov/criminal-ceos/report-violations#reportchildcustody)\n(202) 514-5780")
                sus.timestamp = datetime.datetime.utcnow()
                sus.set_footer(text="MisatoCop | Keeping minors (that aren't Shinji) safe.")
                await message.channel.send(embed=sus)
                user = message.author
                await user.send("balls in my face")
                await user.send("https://tenor.com/view/misato-cry-about-it-gif-22649325")
      

def setup(client):
    client.add_cog(MisatoCop(client))