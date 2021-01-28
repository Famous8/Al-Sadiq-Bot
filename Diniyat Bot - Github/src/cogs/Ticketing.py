from discord.ext import commands
import discord

class Ticketing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def open_ticket(self, ctx):
        head, sep, tail = str(ctx.message.author).partition('#')
        category = discord.utils.get(ctx.guild.categories, id=752739573628534914)

        name = f"{head}'s ticket"

        await ctx.message.guild.create_text_channel(name, category=category)

        channel = discord.utils.get(ctx.message.guild.channels, name=name, type="ChannelType.text")
        teacher = discord.utils.get(ctx.message.guild.roles, id=752726284928548924)


        await channel.set_permissions(teacher, send_messages=True, read_messages=True, add_reactions=True,
                                             embed_links=True, attach_files=True, read_message_history=True,
                                             external_emojis=True)


        await channel.set_permissions(ctx.message.author, send_messages=True, read_messages=True, add_reactions=True,
                                             embed_links=True, attach_files=True, read_message_history=True,
                                             external_emojis=True)

        embed=discord.Embed(title=f"{ctx.message.author.mention} has created a ticket.",
        description=f"Please wait until {teacher.mention} comes to help.", colour=discord.Colour.dark_green())

        await channel.send(embed=embed)

    @commands.command()
    async def close_ticket(self, ctx):
            head, sep, tail = str(ctx.message.author).partition('#')
            name = f"{head}'s ticket"
            await ctx.channel.delete(name)
            embed=discord.Embed(title="Your Ticket has been Closed", description="To Open another ticket, just use the command !create_ticket", colour=discord.Colour.dark_green())
            await ctx.message.author.send(embed=embed)

    @commands.command()
    async def rename_ticket(self, ctx, channel:discord.TextChannel, name):
        await channel.edit(name)

    @rename_ticket.error
    async def rename_ticket_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send("Please format your command like this !rename_ticket #channel new_name")



def setup(bot):
    bot.add_cog(Ticketing(bot))



