from discord.ext import commands
import discord

class AutoRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, id=802940443401650186)
        await member.add_roles(role)

def setup(bot):
    bot.add_cog(AutoRole(bot))
    print("Loaded AutoRole")