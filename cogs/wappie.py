import discord
from discord import message
from discord import channel
from discord.ext import commands
from discord.ext.commands import bot, context
import praw
import random

wappiesubs = [
    'TokkieFeesboek',
    'wappiesinhetwild'
]

class Wappie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = praw.Reddit(client_id='KznKzuMauTSjXQ',
            client_secret=  'ZFS3rFLdYpjQ6MvuUNS86e06q6TssA',
            user_agent= 'Test bot 2:%s:1.0'%'KznKzuMauTSjXQ')
    
    @commands.command(pass_context = True)
    async def shame(self,  ctx):
        channels = ctx.message.guild.text_channels
        await ctx.send(channels)

    @commands.command()
    async def buikpijn(self, ctx):
        print("Activated")
        async with ctx.channel.typing():
            if self.reddit:
                chosensub = random.choice(wappiesubs)

                submisions = self.reddit.subreddit(chosensub).hot()

                post_to_pick = random.randint(1, 20)
                for i in range(0, post_to_pick):
                    submission = next(x for x in submisions if not x.stickied and not x.is_self)
                await ctx.send(submission.title + submission.url)
            else:
                await ctx.send("There was an error if this keeps happening, please contact the bot developer or a server admin.")
                


def setup(bot):
    bot.add_cog(Wappie(bot))