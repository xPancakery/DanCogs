import random
import discord
from redbot.core import commands


class magic8ball(commands.Cog):

    @commands.command()
    async def magic_ball(self, ctx: commands.Context, question):
        message = (await ctx.channel.history(limit=2).flatten())[1].content
        if not message:
            message = "You must ask a question to the Magic 8 Ball."
        else:
            await type_message(
                ctx.channel,
                self.qna(ctx, question),
                allowed_mentions=discord.AllowedMentions(
                    everyone=False, users=False, roles=False),
            )
        

    def qna(self, ctx, question)
        choices = ['As I see it, yes.','Ask again later.','Better not tell you now.','Cannot predict now.','Concentrate and ask again.',
        "Don't count on it.",'It is certain.','It is decidedly so.','Most likely','My reply is no.',
        'My sources say no.','Outlook not so good.','Outlook good.','Reply hazy, try again.','Signs point to yes.',
        'Very doubtful','Without a doubt.','Yes.','Yes - definitely.','You may rely on it.']
        if '?' in question[:-1]:
            return(random.choice(choices))
        else:
            return("Ask a question to the Magic 8 Ball.")
        