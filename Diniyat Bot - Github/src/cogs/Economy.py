import discord
import random
from discord.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient as MotorClient

mongo = MotorClient("mongodb+srv://Famous8:<password>@famous8c1.pse2r.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = mongo["Al-SadiqBot"]

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def work(self, ctx):
            user = str(ctx.message.author.id)
            jobs = ("Moulana", "Developer", "Sunday School Teacher", "Murderer", "Horse Rider", "Messenger")
            job = random.choice(jobs)
            money = (random.randint(20, 100) * 10)
            r1 = (f"You found a job! **{job}** You made **{money}** coins.")
            r2 = ("You failed to find a job :frowning:")
            rs = (r1, r2)
            r = random.choice(rs)

            if r == r1:
                await db["SadiqEconomy"].update_one({"id": (user)}, {"$inc": {"wallet": money}})

            else:
                pass

            await ctx.send(r)

    @work.error
    async def work_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            amount_left = (str(error.retry_after / 60))
            head, sep, tail = amount_left.partition('.')
            await ctx.send(f"**Please wait {head} minutes for your next work-hour**")
        else:
            raise error

    @commands.command(aliases=['bal'])
    async def balance(self, ctx, member:discord.Member):
        find = await db["SadiqEconomy"].find_one({"id": str(member.id)})
        bank = find["bank"]
        wallet = find["wallet"]

        embed = discord.Embed(title=f"**{member}\'s Balance**", colour = discord.Colour.dark_green())
        embed.add_field(name="Bank:",value=f"{bank} coins")
        embed.add_field(name="Wallet:", value = f"{wallet} coins")

        await ctx.send(embed=embed)

    @balance.error
    async def balance_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            find = await db["SadiqEconomy"].find_one({"id": str(ctx.message.author.id)})
            bank = find["bank"]
            wallet = find["wallet"]

            embed = discord.Embed(title=f"**{ctx.message.author}\'s Balance**", colour=discord.Colour.dark_green())
            embed.add_field(name="Bank:", value=f"{bank} coins")
            embed.add_field(name="Wallet:", value=f"{wallet} coins")

            await ctx.send(embed=embed)

    @commands.command(aliases=['dep'])
    async def deposit(self, ctx, amount):
        user = str(ctx.message.author.id)
        find = await db["SadiqEconomy"].find_one({"id": str(ctx.message.author.id)})
        wallet = find["wallet"]
        amounts = int(amount)
        print(wallet)

        if amount == "all":
            await db["SadiqEconomy"].update_one({"id": (user)}, {"$inc": {"wallet": -wallet}})
            await db["SadiqEconomy"].update_one({"id": (user)}, {"$inc": {"bank": +wallet}})
            await ctx.send(f"**Successfully deposited {amount} coins!**")

        if amounts <= wallet:
                await db["SadiqEconomy"].update_one({"id": (user)}, {"$inc": {"wallet": -amounts}})
                await db["SadiqEconomy"].update_one({"id": (user)}, {"$inc": {"bank": +amounts}})
                await ctx.send(f"**Successfully deposited {amount} coins!**")



        else:
                await ctx.send("**You don't have enough money in your wallet to complete this transaction**")




    @deposit.error
    async def deposit_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send("**Please give the amount you would like to deposit** Example: w!deposit <amount>")



    @commands.command(aliases=['with'])
    async def withdraw(self, ctx, amount):
        user = str(ctx.message.author.id)
        find = await db["SadiqEconomy"].find_one({"id": str(ctx.message.author.id)})
        bank = find["bank"]
        amounts = int(amount)

        if amount == "all":
            await db["SadiqEconomy"].update_one({"id": (user)}, {"$inc": {"wallet": +bank}})
            await db["SadiqEconomy"].update_one({"id": (user)}, {"$inc": {"bank": -bank}})
            await ctx.send(f"**Successfully withdrawed {amount} coins!**")

        if amounts <= bank:
                await db["SadiqEconomy"].update_one({"id": (user)}, {"$inc": {"wallet": +amounts}})
                await db["SadiqEconomy"].update_one({"id": (user)}, {"$inc": {"bank": -amounts}})
                await ctx.send(f"**Successfully withdrawed {amount} coins!**")





        else:
                await ctx.send("**You don't have enough money in your bank to complete this transaction**")




    @withdraw.error
    async def withdraw_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send("**Please give the amount you would like to withdraw** Example: w!withdraw <amount>")


    @commands.command(aliases=['bankrob'])
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def rob(self, ctx, member:discord.Member):
        if member != ctx.message.author:
            findauth = await db["SadiqEconomy"].find_one({"id": str(ctx.message.author.id)})
            bankauth = int(findauth['bank'])
            if bankauth < 500:
                await ctx.send("**Wow, Mashallah, you Haram boy!** You need at least 500 coins to rob someone")

            else:
                user = str(ctx.message.author.id)
                find = await db["SadiqEconomy"].find_one({"id": str(member.id)})
                bank = find['bank']
                if bank == 0:
                    await ctx.send("**Wow, Mashallah, you Haram boy!** This Member has no money, why bother stealing from them")

                else:
                    bankint = int(bank)
                    amount = (random.randint(1, bankint))
                    a = f"**Wow, Mashallah, you Haram boy!** You successfully stole {amount} from {member.mention}!"
                    b = f"**Wow, Mashallah, you Haram boy!** You were caught stealing from {member.mention} :frowning: and have to pay 500 coins to avoid jail"
                    c = (a, b)
                    responses = random.choice(c)

                    if responses == a:
                        await db["SadiqEconomy"].update_one({"id": str(member.id)}, {"$inc": {"bank": -amount}})
                        await db["SadiqEconomy"].update_one({"id": (user)}, {"$inc": {"bank": +amount}})
                        await ctx.send(a)

                    if responses == b:
                        await db["SadiqEconomy"].update_one({"id": str(member.id)}, {"$inc": {"bank": +500}})
                        await db["SadiqEconomy"].update_one({"id": (user)}, {"$inc": {"bank": -500}})
                        await ctx.send(b)

    @rob.error
    async def rob_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send("**Wow, Mashallah, you Haram boy!** You must specify who you would like to rob.")

        if isinstance(error, commands.CommandOnCooldown):
            amount_left = (str(error.retry_after / 60))
            head, sep, tail = amount_left.partition('.')
            await ctx.send(f"**Wow, Mashallah, you Haram boy!** Please wait, this command is on cooldown for {head} minutes")

    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def pickpocket(self, ctx, member: discord.Member):
        if member != ctx.message.author:
            findauth = await db["SadiqEconomy"].find_one({"id": str(ctx.message.author.id)})
            wallauth = int(findauth['wallet'])
            if wallauth < 500:
                await ctx.send("**Wow, Mashallah, you Haram boy!** You need at least 500 coins to pickpocket someone")

            else:
                user = str(ctx.message.author.id)
                find = await db["SadiqEconomy"].find_one({"id": str(member.id)})
                wallet = find['wallet']
                if wallet == 0:
                    await ctx.send("**Wow, Mashallah, you Haram boy!** This Member has no money, why bother stealing from them")

                else:
                    walletint = int(wallet)
                    amount = (random.randint(1, walletint))
                    a = f"**Wow, Mashallah, you Haram boy! **You successfully pickpocketed {amount} from {member.mention}!"
                    b = f"**Wow, Mashallah, you Haram boy! **You were caught pickpocketing from {member.mention} :frowning: and have to pay 500 coins to avoid jail"
                    c = (a, b)
                    responses = random.choice(c)

                    if responses == a:
                        await db["SadiqEconomy"].update_one({"id": str(member.id)}, {"$inc": {"wallet": -amount}})
                        await db["SadiqEconomy"].update_one({"id": (user)}, {"$inc": {"wallet": +amount}})
                        await ctx.send(a)

                    if responses == b:
                        await db["SadiqEconomy"].update_one({"id": str(member.id)}, {"$inc": {"wallet": +500}})
                        await db["SadiqEconomy"].update_one({"id": (user)}, {"$inc": {"wallet": -500}})
                        await ctx.send(b)

    @pickpocket.error
    async def pickpocket_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send("**Wow, Mashallah, you Haram boy! **You must specify who you would like to pickpocket.")

        if isinstance(error, commands.CommandOnCooldown):
            amount_left = (str(error.retry_after / 60))
            head, sep, tail = amount_left.partition('.')
            await ctx.send(f"**Wow, Mashallah, you Haram boy! **Please wait, this command is on cooldown for {head} minutes")


    @commands.command()
    async def give(self, ctx, member:discord.Member, amount):
            user = (ctx.message.author)
            find = await db["SadiqEconomy"].find_one({"id": str(user.id)})
            awallet = find["wallet"]
            amounts = int(amount)

            if amount == "all":
                await db["SadiqEconomy"].update_one({"id": str(user.id)}, {"$inc": {"wallet": -awallet}})
                await db["SadiqEconomy"].update_one({"id": str(member.id)}, {"$inc": {"wallet": +awallet}})
                await ctx.send(f"**Wow, Mashallah! Successfully gifted {amount} coins to {member.mention}!**")

            if amounts <= awallet:
                await db["SadiqEconomy"].update_one({"id": str(user.id)}, {"$inc": {"wallet": -amounts}})
                await db["SadiqEconomy"].update_one({"id": str(member.id)}, {"$inc": {"wallet": +amounts}})
                await ctx.send(f"**Wow, Mashallah! Successfully gifted {amount} coins to {member.mention}!**")




            else:
                await ctx.send("**Wow, Mashallah!** But, you don't have enough money in your wallet to complete this transaction")

    @deposit.error
    async def deposit_error(self, ctx, error):
            if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
                await ctx.send("**Please give the amount you would like to give and the member you would like to give to.** Example: w!give @<member> <amount>")


    @commands.command()
    async def add_member(self, ctx, member:discord.Member):
        record = {"id": str(member.id), "wallet": 0, "bank": 0}
        level = {"id": str(member.id), "level": 1}
        await db["SadiqEconomy"].insert_one(record)
        await db["SadiqLevels"].insert_one(level)

        await ctx.send(f"**Successfully added {member.mention} to the database**")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def set_balance(self, ctx, member: discord.Member, amount:int, reason=None):
            user = (ctx.message.author)
            find = await db["SadiqEconomy"].find_one({"id": str(user.id)})
            wallet = find["wallet"]
            await db["SadiqEconomy"].update_one({"id": str(member.id)}, {"$inc": {"wallet": +amount}})
            await db["SadiqEconomy"].update_one({"id": str(member.id)}, {"$inc": {"wallet": -wallet}})
            await ctx.send(f"**Wow, Mashallah! Your Balance was set to {amount}, {member.mention}! Reason: {reason}**")

def setup(bot):
  bot.add_cog(Economy(bot))
  print("Loaded Economy")
