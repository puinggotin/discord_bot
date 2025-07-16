import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# 関数の呼び出し
from functions_utils.random_functions import new_random_weapon

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)


# ---------- コマンド定義 ---------
@bot.tree.command(name="new_random", description="バンカラコレクション全30種からランダムで1つ選びます")
async def match_command(interaction: discord.Interaction):
    weapon = new_random_weapon()
    await interaction.response.send_message(f"リクエストブキは {weapon} です！！")

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Log in as: {bot.user}")

bot.run(TOKEN)