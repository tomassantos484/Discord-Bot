import pandas as pd
from MLBTeams import *
import random

#Random Statements
statement_prompts = [
    "The things I'd do for {player} to be in a {MLBTeam} uniform....",
    "Trade proposal: {player} for {player}. What do we think?",
    "Don't talk to me if you don't think {player} is going to lead the league in {randomStat}",
    "{MLBTeam}  fans, mental health check???",
    "When I become commissioner, I will remove the {MLBTeam} from existence",
    "Scheduled {player} success",
    "{player} truthers are being rewarded!",
    "Watching the {MLBTeam}  makes me reconsider being a baseball fan",
    "MLB would be better off without the {MLBTeam}",
    "{MLBTeam}  v {MLBTeam} is the best rivalry in baseball!",
    "Absolutely disgraceful performance. In all my years as a fan of the {MLBTeam}, I have never seen a group of players so lazy and pathetic. I'm taking my fanhood to the {MLBTeam} where it looks like they know how to run a baseball team.",
    "Personally, I think the {MLBTeam} should try to win this baseball game",
    "I love {player}!",
    "I hate {player}.",
    "{player}: future {MLBTeam} player.",
    "{MLBTeam} has the best fanbase.",
    "{player}: future MVP.",
    "We need to start appreciating the things {player} does",
    "For personal reasons, I will be fighting {player}",
    "Today is a great day to love and appreciate {player}",
    "Wait, people actually think {player} is good?",
    "Wait, people actually think the {MLBTeam} are good?",
    "The next {MLBTeam} World Series championship will be in {randomYears} years!",
    "The {MLBTeam} have been so bad this season that they're being demoted to {randomMinorLeague}",
    "There are fans of the {MLBTeam}?",
    "There are fans of {player}?",
    "I'm gonna tell my kids that {player} was Barry Bonds",
    "For his sake, {player} should really request a trade to the {MLBTeam}",
    "Watching the {MLBTeam} makes me reconsider being a baseball fan",
    "{player} just hit a home run off your team. Tear down the franchise.",
    "The {MLBTeam} may never lose again!",
    "The {MLBTeam} may never win again!",
    "Scheduled {MLBTeam} success!",
    "Scheduled {player} success!",
    "Scheduled {MLBTeam} failure!",
    "Scheduled {player} failure!",
    "I am a {player} enjoyer.",
    "I am a {player} hater.",
    "{player} just sucks dude. I need him off of my team immediately",
    "You just can't hate {player}.",
    "{player} is going to hit {randomHomeRuns} home runs this season!",
    "Don't talk to me if you don't think {player} is going to lead the league in {randomStat}",
    "I can't believe people still think the {MLBTeam} aren't going to win the World Series",
    "Born too late to explore the world, born too early to explore space, but born just in time to watch {player} play baseball",
    "If I was the GM of the {MLBTeam} for a day, I would trade for {player}.",
    "The {MLBTeam} are on pace for {randomWins} wins this season!",
    "The {MLBTeam} are a {randomDivisionFinish} place team.",
    "I’m gatekeeping {player}",
    "Do people actually spend 3 hours of their day watching the {MLBTeam}?"
]

def random_statements():
    # Fetching player names
    # Open the text file containing player names
    with open('player_names.txt', 'r') as file:
    # Read all lines from the file
        player_names = file.readlines()

    # Remove leading and trailing whitespaces from each player name
        player_names = [name.strip() for name in player_names]

    #Convert MLBTeams dict to list
    teams_list = list(Teams.keys())

    player = random.choice(player_names)
    teams_list = random.choice(teams_list)
    randomYears = random.randint(0, 999)
    randomStat = random.choice(["home runs", "hits", "runs", "RBIs", "walks", "strikeouts", "stolen bases", "batting average", "on-base percentage", "slugging percentage", "OPS", "ERA", "wins", "losses", "saves", "innings pitched", "strikeouts", "walks", "WHIP", "FIP", "WAR"])
    randomMinorLeague = random.choice(["AAA", "AA", "A+","A", "Rookie"])
    randomDivisionFinish = random.choice(["first", "second", "third", "fourth", "fifth"])
    randomWins = random.randint(0, 162)
    randomHomeRuns = random.randint(0, 100)

    statement = random.choice(statement_prompts)
    statement = statement.replace("{player}", player)
    statement = statement.replace("{MLBTeam}", teams_list)
    statement = statement.replace("{randomYears}", str(randomYears))
    statement = statement.replace("{randomStat}", randomStat)
    statement = statement.replace("{randomMinorLeague}", randomMinorLeague)
    statement = statement.replace("{randomDivisionFinish}", randomDivisionFinish)
    statement = statement.replace("{randomWins}", str(randomWins))
    statement = statement.replace("{randomHomeRuns}", str(randomHomeRuns))

    print(statement)
    
if __name__ == "__main__":
    random_statements()