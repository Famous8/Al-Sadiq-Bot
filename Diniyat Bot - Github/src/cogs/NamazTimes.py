from discord.ext import commands
import src.web_driver
import discord

class NamazTimes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def fajr(self, ctx):
        WebScraper = src.web_driver.WebScraper()
        embed = discord.Embed(title='Fajr Time:', description=WebScraper.fajr_time(), colour=discord.Colour.dark_green())
        embed.set_footer(text=f"Requested By: {ctx.message.author}")

        await ctx.send(embed=embed)

    @commands.command()
    async def sunrise(self, ctx):
        WebScraper = src.web_driver.WebScraper()
        embed = discord.Embed(title='Sunrise Time:', description=WebScraper.sunrise_time(), colour=discord.Colour.dark_green())
        embed.set_footer(text=f"Requested By: {ctx.message.author}")

        await ctx.send(embed=embed)

    @commands.command()
    async def dhuhr(self, ctx):
        WebScraper = src.web_driver.WebScraper()
        embed = discord.Embed(title='Dhuhr Time:', description=WebScraper.dhuhr_time(), colour=discord.Colour.dark_green())
        embed.set_footer(text=f"Requested By: {ctx.message.author}")

        await ctx.send(embed=embed)

    @commands.command()
    async def asr(self, ctx):
        WebScraper = src.web_driver.WebScraper()
        embed = discord.Embed(title='Asr Time:', description=WebScraper.asr_time(), colour=discord.Colour.dark_green())
        embed.set_footer(text=f"Requested By: {ctx.message.author}")

        await ctx.send(embed=embed)

    @commands.command()
    async def maghrib(self, ctx):
        WebScraper = src.web_driver.WebScraper()
        embed = discord.Embed(title='Maghrib Time:', description=WebScraper.maghrib_time(), colour=discord.Colour.dark_green())
        embed.set_footer(text=f"Requested By: {ctx.message.author}")

        await ctx.send(embed=embed)

    @commands.command()
    async def isha(self, ctx):
        WebScraper = src.web_driver.WebScraper()
        embed = discord.Embed(title='Isha Time:', description=WebScraper.isha_time(), colour=discord.Colour.dark_green())
        embed.set_footer(text=f"Requested By: {ctx.message.author}")

        await ctx.send(embed=embed)

    @commands.command()
    async def prayer_times(self, ctx):
        WebScraper = src.web_driver.WebScraper()
        embed = discord.Embed(title='Prayer Times:', description=f"""
        Fajr: {WebScraper.fajr_time()}
        Sunrise: {WebScraper.sunrise_time()}
        Dhuhr: {WebScraper.dhuhr_time()}
        Asr: {WebScraper.asr_time()}
        Maghrib: {WebScraper.maghrib_time()}
        Isha: {WebScraper.isha_time()}""", colour=discord.Colour.dark_green())
        embed.set_footer(text=f"Requested By: {ctx.message.author}")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(NamazTimes(bot))
    print("Loaded Namaz Times")