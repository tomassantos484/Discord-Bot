#Importing Libraries
import discord
from discord import app_commands
from discord.ext import commands
from randomszn import *
from randomszn import random_stats
from dotenv import load_dotenv
import os
import giphy_client
from giphy_client.rest import ApiException

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
APP_ID = os.getenv("APP_ID")
PUBLIC_KEY = os.getenv("PUBLIC_KEY")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
GIPHY_KEY = os.getenv("GIPHY_KEY")


client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Mike Trout is ready to bat!")
    try:
        synced = await client.tree.sync()
    except Exception as e: 
        print(e)

@client.tree.command(name="hello", description="Mike Trout says hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello, {interaction.user.mention}! I am Mike Trout, the best baseball player in the world!", ephemeral=True)

@client.tree.command(name="goodbye", description="Mike Trout says goodbye!")
async def goodbye(interaction: discord.Interaction):
    await interaction.response.send_message(f"Goodbye, {interaction.user.mention}! I hope to see you again soon!", ephemeral=True)

@client.tree.command(name="randomgif", description="Mike Trout sends a random gif!")
async def randomgif(interaction: discord.Interaction, q: str="Mike Trout"):
    api_instance = giphy_client.DefaultApi()

    try:
        api_response = api_instance.gifs_search_get(GIPHY_KEY, q, rating="g")
        random_gif_list = list(api_response.data)
        gif_selection = random.choice(random_gif_list)

        emb = discord.Embed(title=q, color=0x3498db)
        emb.set_image(url=f'https://media.giphy.com/media/{gif_selection.id}/giphy.gif')

        await interaction.response.send_message(embed=emb, ephemeral=True)

    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_random_get: %s\n" % e)

@client.tree.command(name="troutstats", description="Mike Trout sends his Baseball-Reference page!")
async def troutstats(interaction: discord.Interaction):
    await interaction.response.send_message("https://www.baseball-reference.com/players/t/troutmi01.shtml", ephemeral=True)

@client.tree.command(name="troutfacts", description="Mike Trout sends some facts about himself!")
async def troutfacts(interaction: discord.Interaction):
    await interaction.response.send_message("https://www.mlb.com/news/mike-trout-facts", ephemeral=True)

@client.tree.command(name="ping", description="Mike Trout sends his ping!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! {round(client.latency * 1000)}ms", ephemeral=True)

@client.tree.command(name="randomseason", description="Generate a random player and a random season based on the stats of the 2022 MLB season.")
async def generate_random_season(
    interaction: discord.Interaction,
    first_name: str,
    last_name: str,
    age: int,
    team: str,
    position: str
):
    
    player_info = {
        "firstname": first_name if first_name.lower() != 'random' else random.choice(MLB_FirstNames),
        "lastname": last_name if last_name.lower() != 'random' else random.choice(MLB_LastNames),
        "age": age if age != -1 else random.randint(18, 49),
        "team": team if team.lower() != 'random' else random.choice(list(Teams.values())),
        "position": position if position.lower() != 'random' else random.choice(list(Positions.values())),
        **random_stats()  # Call your function to generate randomized stats
    }

    # Embed object
    embed = discord.Embed(title=f"{player_info['firstname']} {player_info['lastname']} - {player_info['team']} ({player_info['position']})", color=0x3498db)

    # Add fields for player information
    embed.add_field(name="Age", value=player_info['age'], inline=True)
    embed.add_field(name="Team", value=player_info['team'], inline=True)
    embed.add_field(name="Position", value=player_info['position'], inline=True)

    # Add a separator
    embed.add_field(name="\u200b", value="\u200b", inline=False)

    # Add fields for player statistics
    for stat_name, stat_value in random_stats().items():
        embed.add_field(name=stat_name.capitalize(), value=stat_value, inline=True)

    # Send the response as an ephemeral message
    await interaction.response.send_message(embed=embed, ephemeral=True)

client.run(DISCORD_TOKEN)
