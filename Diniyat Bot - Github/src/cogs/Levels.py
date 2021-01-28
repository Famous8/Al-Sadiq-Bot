import discord
from discord.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient as MotorClient

mongo = MotorClient("mongodb+srv://Famous8:2fawztzt@famous8c1.pse2r.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = mongo["Al-SadiqBot"]


class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def on_message(self, message):
        if message.author.id != 804342273248198666:
            find = await db["SadiqLevels"].find_one({"id": str(message.author.id)})
            get = find["level"]

            user = str(message.author.id)

            await db["SadiqLevels"].update_one({"id": (user)}, {"$inc": {"level": 1}})

            if get % 30 == 0:
                channel = message.channel
                person = await self.bot.fetch_user(str(message.author.id))
                level = str(get / 30).replace(".0", "")
                leveled_up = (f"**Subhanallah! {person.mention} has leveled up to level {level}**")
                await channel.send(leveled_up)

            else:
                pass

    @commands.command()
    async def rank(self, ctx, member:discord.Member):
        find = await db["SadiqLevels"].find_one({"id": str(member.id)})
        get = find["level"]

        rank = str(get / 30)
        head, sep, tail = rank.partition('.')

        try:
            embed = discord.Embed(title=f"**{member}'s current level is: {head}**", colour=discord.Colour.dark_green())
            url = member.id
            url_ = await self.bot.fetch_user(url)
            icon_url = url_.avatar_url
            embed.set_thumbnail(url=icon_url)

            await ctx.send(embed=embed)


        except Exception as e:
            raise e
            embed = discord.Embed(title=f"**{member}'s current level is: 0**", colour=discord.Colour.dark_green())
            url = ctx.author.id
            url_ = await self.bot.fetch_user(url)
            icon_url = url_.avatar_url
            embed.set_thumbnail(url=icon_url)
            await ctx.send(embed=embed)

    @rank.error
    async def rank_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            find = await db["SadiqLevels"].find_one({"id": str(ctx.message.author.id)})
            get = find["level"]

            rank = str(get / 30)
            head, sep, tail = rank.partition('.')

            try:
                embed = discord.Embed(title=f"**{ctx.author}'s current level is: {head}**", colour=discord.Colour.dark_green())
                url = ctx.author.id
                url_ = await self.bot.fetch_user(url)
                icon_url = url_.avatar_url
                embed.set_thumbnail(url=icon_url)

                await ctx.send(embed=embed)


            except Exception as e:
                raise e
                embed = discord.Embed(title=f"**{ctx.author}'s current level is: 0**", colour=discord.Colour.dark_green())
                url = ctx.author.id
                url_ = await self.bot.fetch_user(url)
                icon_url = url_.avatar_url
                embed.set_thumbnail(url=icon_url)
                await ctx.send(embed=embed)

    @commands.command()
    async def leaderboard(self, ctx):

        def key(d):
            return d["level"]

        leaderboard = []

        async for find in db["SadiqLevels"].find():
            leaderboard.append(find)

        leaderboard.sort(key=key, reverse=True)
        leaderboard = leaderboard[:5]

        ID1 = await self.bot.fetch_user(leaderboard[0]['id'])
        level1 = str(leaderboard[0]['level'] / 30)
        head1, sep, tail = level1.partition('.')

        ID2 = await self.bot.fetch_user(leaderboard[1]['id'])
        level2 = str(leaderboard[1]['level'] / 30)
        head2, sep, tail = level2.partition('.')

        ID3 = await self.bot.fetch_user(leaderboard[2]['id'])
        level3 = str(leaderboard[2]['level'] / 30)
        head3, sep, tail = level3.partition('.')

        ID4 = await self.bot.fetch_user(leaderboard[3]['id'])
        level4 = str(leaderboard[3]['level'] / 30)
        head4, sep, tail = level4.partition('.')

        ID5 = await self.bot.fetch_user(leaderboard[4]['id'])
        level5 = str(leaderboard[4]['level'] / 30)
        head5, sep, tail = level5.partition('.')

        text = f"""
        1. **{ID1}** - Level {head1}
        2. **{ID2}** - Level {head2}
        3. **{ID3}** - Level {head3}
        4. **{ID4}** - Level {head4}
        5. **{ID5}** - Level {head5}
        """

        embed = discord.Embed(title="Leaderboard for Al-Sadiq Bot levels:", description=text, colour=discord.Colour.dark_green())

        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Levels(bot))
    print("Loaded Levels")