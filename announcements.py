import discord
from discord.ext import commands
from discord.utils import get
client = discord.Client()

class announcements(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.channel.id == 870508980970065950:
            self.target_channel = self.client.get_channel(900115512753811456)
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
    client.add_cog(announcements(client))


# fat balls id : 870508980970065950
# mmfnf id : 900115512753811456