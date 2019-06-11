import discord
from discord.ext import commands
import asyncio
import Database_helpers


class WaifuGacha(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        Database_helpers.initialize(str(self.bot.guilds[0].id))




    @commands.command(name="roll")
    async def roll(self, context):
        PRICE = 10
        user_id = context.message.author.id
        user = self.bot.get_user(user_id)
        username = user.name
        database_helper.adjust_pity(user_id)
        details = database_helper.get_user_details(user_id)





def setup(bot):
    bot.add_cog(WaifuGacha(bot))
