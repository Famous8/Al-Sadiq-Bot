from discord.ext import commands
import discord

class Other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="My Prefix is !", colour=discord.Colour.dark_green())
        embed.add_field(name="Namaz Times:", value="``fajr``, ``sunrise``, ``dhuhr``, ``asr``, ``maghrib``,  ``isha``, ``prayer_times``")
        embed.add_field(name="Economy:", value="``work``, ``balance``, ``deposit``, ``withdraw``, ``rob``, ``pickpocket``, ``give`` ")
        embed.add_field(name="Levels:", value="``rank``, ``leaderboard``")
        embed.add_field(name="Fun:", value="``meme``, ``halalmeme``, ``facepalm``, ``gunfight``, ``ko``")
        embed.add_field(name="Ticketing:", value="``open_ticket``, ``close_ticket``, ``rename_ticket``")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Other(bot))
    print("Loaded Other")
