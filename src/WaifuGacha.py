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




def setup(bot):
    bot.add_cog(WaifuGacha(bot))
