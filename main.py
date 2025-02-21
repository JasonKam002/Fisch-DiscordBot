import discord
import time
from discord.ext import commands
from discord import app_commands
from game import fishing, sell, fish_list, rarity, calculate_level
from bot_token import token

inventory = []
bank = 0
xp = 0

class Client(commands.Bot):

  async def on_ready(self):
    print(f'Logged on as {self.user}!')

    try:
      guild = discord.Object(id=1320230407157055598)
      synced = await self.tree.sync(guild=guild)
      print(f"Synced {len(synced)} command to guild {guild.id}")

    except Exception as e:
      print(f'Error syncing commands: {e}')


intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

GUILD_ID = discord.Object(id=1320230407157055598)

# fishing
@client.tree.command(name="fish", description="Start fishing", guild=GUILD_ID)
async def startGame(interaction: discord.Interaction):
  global xp
  fish_rarity, fish, xp = fishing(rarity, fish_list, inventory, xp)
  level, remaining_xp, level_up = calculate_level(xp)
  embed = discord.Embed(title='Fishing', description='...', color=discord.Color.blue())
  await interaction.response.send_message(embed=embed)
  
  time.sleep(1)
  if level_up == True:
    embed = discord.Embed(title='Fisch', description=f'Congratulations, you caught a {fish_rarity} {fish}\n\nYou gained 10xp\n\nYou levelled up! You are now level {level}', color=discord.Color.blue())
  else:
    embed = discord.Embed(title='Fisch', description=f'Congratulations, you caught a {fish}\n\nYou gained 10xp', color=discord.Color.blue())
  await interaction.edit_original_response(embed=embed)

# show inventory
@client.tree.command(name="inv", description="Shows your inventory", guild=GUILD_ID)
async def showInventory(interaction: discord.Interaction):
  embed = discord.Embed(title='Inventory', description=f'Your inventory: {inventory}', color=discord.Color.blue())
  await interaction.response.send_message(embed=embed)

# sell
@client.tree.command(name="sell", description= "Sell your fishes", guild=GUILD_ID)
async def sellFishes(interaction: discord.Interaction, sell_fish: str):
  cash = sell(inventory, fish_list, bank, sell_fish)
  time.sleep(1)
  if sell_fish == 'all':
    embed = discord.Embed(title='Sell', description=f'You sold {sell_fish} \nYour bank: ${cash}', color=discord.Color.blue())
  else:
    embed = discord.Embed(title='Sell', description=f'You sold a {sell_fish} \nYour bank: ${cash}', color=discord.Color.blue())
    
  await interaction.response.send_message(embed=embed)

# show level
@client.tree.command(name="level", description="Shows your level", guild=GUILD_ID)
async def showLevel(interaction: discord.Interaction):
  level, remaining_xp, level_up = calculate_level(xp)
  embed = discord.Embed(title='Level', description=f'Level: {level}\nxp needed to level up: {100-remaining_xp}', color=discord.Color.blue())
  await interaction.response.send_message(embed=embed)

client.run(token)
