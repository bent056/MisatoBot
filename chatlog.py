import discord
from discord.ext import commands
from discord.utils import get
client = discord.Client()

class chatlog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        
        # we are watching
        if (message.channel.id == 897678466974113875) or (message.channel.id == 900601620683964437):
            self.target_channel = self.client.get_channel(903295849008861264)
            await self.target_channel.send(f'''***{message.author}***''')
            for attachment in message.attachments:
                if 'image' in attachment.content_type:
                    file = message.attachments[0]
                    file.filename = f"{file.filename}"
                    img = await file.to_file()
                    await self.target_channel.send(file=img)
                if 'video' in attachment.content_type:
                    file = message.attachments[0]
                    file.filename = f"{file.filename}"
                    vid = await file.to_file()
                    await self.target_channel.send(file=vid)
            await self.target_channel.send(message.content)

def setup(client):
  client.add_cog(chatlog(client))