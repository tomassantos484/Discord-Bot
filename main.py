#Importing Libraries
import discord
import os
import giphy_client
import requests
import random
import json
from pybaseball import *
from pybaseball import cache
from discord.ext import commands
from randomszn import *
from randomstatements import *
from dotenv import load_dotenv
from giphy_client.rest import ApiException

#Cache for pybaseball
cache.enable()

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
APP_ID = os.getenv("APP_ID")
PUBLIC_KEY = os.getenv("PUBLIC_KEY")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
GIPHY_KEY = os.getenv("GIPHY_KEY")
TENOR_KEY = os.getenv("TENOR_KEY")
OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")

client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Mike Trout is ready to bat!")
    await client.change_presence(activity=discord.Game(name="Baseball"))
    try:
        synced = await client.tree.sync()
    except Exception as e:
        print(e)

@client.tree.command(name="hello", description="Mike Trout says hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello, {interaction.user.mention}! I am Mike Trout, the best baseball player in the world!", ephemeral=False)

@client.tree.command(name="goodbye", description="Mike Trout says goodbye!")
async def goodbye(interaction: discord.Interaction):
    await interaction.response.send_message(f"Goodbye, {interaction.user.mention}! I hope to see you again soon!", ephemeral=False)
    
@client.tree.command(name="ping", description="Mike Trout sends his ping!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! {round(client.latency * 1000)}ms", ephemeral=False)

@client.tree.command(name="randomgifgiphy", description="Mike Trout sends a random gif from GIPHY!")
async def randomgifgiphy(interaction: discord.Interaction, q: str="Mike Trout"):
    api_instance = giphy_client.DefaultApi()

    try:
        api_response = api_instance.gifs_search_get(GIPHY_KEY, q, rating="g")
        random_gif_list = list(api_response.data)
        gif_selection = random.choice(random_gif_list)

        attribution_image = discord.File("giphy_attribution_logo.gif", filename="image.gif")

        emb = discord.Embed(
            title=q, 
            color= discord.Color.red()
            )
        emb.set_image(url=f'https://media.giphy.com/media/{gif_selection.id}/giphy.gif')
        emb.set_footer(text = "Powered by GIPHY", icon_url = "attachment://image.gif")

        await interaction.response.send_message(embed=emb, file= attribution_image, ephemeral=False)

    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_random_get: %s\n" % e)

@client.tree.command(name="randomgiftenor", description="Mike Trout sends a random gif from Tenor!")
async def randomgiftenor(interaction: discord.Interaction, q: str = "Mike Trout"):
    try:
        params = {
            "q": q,
            "key": TENOR_KEY,
            "limit": 50
        }

        result = requests.get(f"https://tenor.googleapis.com/v2/search?", params=params)
        data = result.json()

        number = random.randint(0,49)
        url = data["results"][number]["media_formats"]["gif"]["url"]

        embed = discord.Embed(
            title = q,
            color = discord.Color.blue()
        )

        embed.set_image(url=url)
        embed.set_footer(text="Via Tenor")
        await interaction.response.send_message(embed=embed)

    except Exception as e:
        print("Error!")

@client.tree.command(name="playerlookup", description="Mike Trout sends info about a player of your choice!")
async def playerlookup(interaction: discord.Interaction, first_name: str = "Mike", last_name: str = "Trout"):
    player = playerid_lookup(last_name, first_name)
    if player.empty:
        await interaction.response.send_message("Player not found!")
        return

    mlb_key = player['key_mlbam'].iloc[0]
    retro_key = player['key_retro'].iloc[0]
    bbref_key = player['key_bbref'].iloc[0]
    fangraphs_key = player['key_fangraphs'].iloc[0]
    first_season = int(player['mlb_played_first'].iloc[0])
    last_season = int(player['mlb_played_last'].iloc[0])

    mlb_url = f"https://www.mlb.com/player/{first_name.lower()}-{last_name.lower()}-{mlb_key}"
    retrosheet_url = f"https://www.retrosheet.org/boxesetc/{last_name[0].upper()}/P{retro_key}.htm"
    bbref_url = f"https://www.baseball-reference.com/players/{last_name[0].lower()}/{bbref_key}.shtml"
    fangraphs_url = f"https://www.fangraphs.com/players/{first_name}-{last_name}/{fangraphs_key}"

    embed = discord.Embed(title=f"{first_name} {last_name}", description=f"Player ID: {mlb_key}", color=discord.Color.blue())
    embed.add_field(name="First MLB Season", value=first_season, inline=False)
    embed.add_field(name="Last MLB Season", value=last_season, inline=False)
    embed.add_field(name="MLB.com:", value=mlb_url, inline=False)
    embed.add_field(name="Retrosheet:", value=retrosheet_url, inline=False)
    embed.add_field(name="Baseball Reference:", value=bbref_url, inline=False)
    embed.add_field(name="Fangraphs:", value=fangraphs_url, inline=False)

    await interaction.response.send_message(embed=embed, ephemeral=False)

@client.tree.command(name="randomseason", description="Generate a random player and a random season based on the stats of the 2022 MLB season.")
async def generate_random_season(
    interaction: discord.Interaction,
    first_name: str,
    last_name: str,
    age: int,
    team: str,
    position: str
):
    
    #Fetch player names from text file:
    first_names = []
    last_names = []
    
    with open('player_names.txt', 'r') as file:
        for line in file:
            parts = line.split().split()
            lastname = parts[-1]
            firstname = ''.join(parts[:-1])
            first_names.append(firstname)
            last_names.append(lastname)

    
    player_info = {
        "firstname": first_name if first_name.lower() != 'random' else random.choice(first_names),
        "lastname": last_name if last_name.lower() != 'random' else random.choice(last_names),
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
    await interaction.response.send_message(embed=embed, ephemeral=False)

@client.tree.command(name="randomstatement", description="Mike Trout sends a random statement!")
async def randomstatement(interaction: discord.Interaction, player: str = "Mike Trout", team: str = "Los Angeles Angels"):
    # Fetching player names
    # Open the text file containing player names
    with open('player_names.txt', 'r') as file:
    # Read all lines from the file
        player_names = file.readlines()

    # Remove leading and trailing whitespaces from each player name
        player_names = [name.strip() for name in player_names]

    #Convert MLBTeams dict to list
    teams_list = list(Teams.keys())

    player1 = random.choice(player_names)
    player2 = random.choice(player_names)
    teams_list1 = random.choice(teams_list)
    teams_list2 = random.choice(teams_list)
    randomYears = random.randint(0, 999)
    randomStat = random.choice(["home runs", "hits", "runs", "RBIs", "walks", "strikeouts", "stolen bases", "batting average", "on-base percentage", "slugging percentage", "OPS", "ERA", "wins", "losses", "saves", "innings pitched", "strikeouts", "walks", "WHIP", "FIP", "WAR"])
    randomMinorLeague = random.choice(["AAA", "AA", "A+","A", "Rookie"])
    randomDivisionFinish = random.choice(["first", "second", "third", "fourth", "fifth"])
    randomWins = random.randint(0, 162)
    randomHomeRuns = random.randint(0, 100)

    statement = random.choice(statement_prompts)
    statement = statement.replace("{player}", player1)
    statement = statement.replace("{player1}", player1)
    statement = statement.replace("{player2}", player2)
    statement = statement.replace("{MLBTeam}", teams_list1)
    statement = statement.replace("{MLBTeam1}", teams_list1)
    statement = statement.replace("{MLBTeam2}", teams_list2)
    statement = statement.replace("{randomYears}", str(randomYears))
    statement = statement.replace("{randomStat}", randomStat)
    statement = statement.replace("{randomMinorLeague}", randomMinorLeague)
    statement = statement.replace("{randomDivisionFinish}", randomDivisionFinish)
    statement = statement.replace("{randomWins}", str(randomWins))
    statement = statement.replace("{randomHomeRuns}", str(randomHomeRuns))

    await interaction.response.send_message(statement, ephemeral=False)

@client.tree.command(name="troutify", description="Mike Trout sends a random statement about himself!")
async def troutify(interaction: discord.Interaction):

    # Immediately defer the interaction to indicate processing is happening
    # and to get more time for sending the response.
    await interaction.response.defer(ephemeral=False)


    def getResponse(model, query):
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_KEY}",
            },
            data=json.dumps({
                "model": model,
                "messages": [{"role": "user", "content": query}],
            })
        )
        if response.status_code == 200:
            return response.json()
        else:
            print(f"API call failed with status code {response.status_code}")
            return None

    # Call the function and store the response
    response = getResponse("gryphe/mythomist-7b:free", "Generate a random funny/semi-satirical baseball-related statement about Mike Trout.")

    if response and 'choices' in response and len(response['choices']) > 0:
        # Access and send the statement
        statement = response['choices'][0]['message']['content']
        await interaction.followup.send(statement, ephemeral=False)
    else:
        # Handle error or empty response
        error_message = "Sorry, I couldn't fetch a statement for Mike Trout at the moment."
        await interaction.followup.send(error_message, ephemeral=False)


@client.tree.command(name="yogism", description="Mike Trout produces a yogism based on uploaded image!")
async def yogism(interaction: discord.Interaction):

    def getResponse(model, query, image_url):
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_KEY}",
            },
            data=json.dumps({
                "model": model,
                "messages": [{"role": "user", "content": query}],
                "image": image_url
            })
        )
        if response.status_code == 200:
            return response.json()
        else:
            print(f"API call failed with status code {response.status_code}")
            return None

    #upload image
    await interaction.response.send_message("Please upload the image you want to use for the yogism.", ephemeral=True)

    def check(message):
        return message.author == interaction.user and message.attachments
    
    message = await client.wait_for('message', check=check)

    if message.attachments:
        image_url = message.attachments[0].url
        response = getResponse("gryphe/mythomist-7b:free", "Generate a random funny/semi-satiricall yogism from baseball player Yogi Berra based on the uploaded image.", image_url)

    if response and 'choices' in response and len(response['choices']) > 0:
        # Access and send the statement
        statement = response['choices'][0]['message']['content']
        await interaction.followup.send(statement, ephemeral=False)

    else:
        # Handle error or empty response
        error_message = "Sorry, I couldn't fetch a yogism at the moment."
        await interaction.followup.send(error_message, ephemeral=False)

client.run(DISCORD_TOKEN)
