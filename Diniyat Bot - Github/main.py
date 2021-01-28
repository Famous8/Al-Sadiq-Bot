from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command('help')
bot.load_extension('jishaku')

@bot.event
async def on_ready():
    print("Bot is Now Online!")

token_file = open('./src/token.txt', 'r')
TOKEN = token_file.read()

cogs = ['src.cogs.Economy', 'src.cogs.NamazTimes', 'src.cogs.Other', 'src.cogs.Levels', 'src.cogs.Fun', 'src.cogs.Ticketing', 'src.cogs.AutoRole', 'src.cogs.Moderation']

for cog in cogs:
    bot.load_extension(cog)

bot.run(TOKEN)