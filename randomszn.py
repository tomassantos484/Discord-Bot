import random
from namesAL import *
from namesNL import *
from MLBTeams import *
from baseballPositions import *                                                                                                                                           

# Function to generate a random player
def random_player():
    # List of player names
    first_name = (MLB_FirstNames)
    last_name = (MLB_LastNames)

    #List of MLB Teams
    MLBTeam = (Teams)

    PlayerAge = random.randrange(17,49) #Mel Ott (youngest HOF to play at 17 in 1926) and Julio Franco (oldest player to receive regular playing time at age 49 in 2007) are the extremes in this age range.


    return {
        "firstname": random.choice(first_name),
        "lastname": random.choice(last_name),
        "age": PlayerAge,
        "team": random.choice(MLBTeam),
        "position": random.choice(Positions)
    }

# Function to generate random statistics (batters)
def random_stats():
    #Variables/Stats
    QualifiedPA = 600 #Avg amount of plate appearances among all qualified batters in 2022, rounded up from 597.44 (77,668 total PAs)

    AvgAB = 530 # Avg amount of ABs among all qualified batters in 2022, rounded down from 532.71 (Approx. 69,253 total ABs)

    SacFlies = int(round(QualifiedPA * (random.uniform(0.00,0.0138))))

    SacBunts = int(round(QualifiedPA * (random.uniform(0.00,0.0134))))

    Strikeouts = int(round(AvgAB * (random.uniform(0.0710,0.3430))))

    Groundouts = int(round(AvgAB * (random.uniform(0.1620,0.3260))))

    Popouts = int(round(AvgAB * (random.uniform(0.0113,0.1230))))

    Flyouts = int(round(AvgAB * (random.uniform(0.1008,0.2230))))

    Lineouts = int(round(AvgAB * (random.uniform(0.0354,0.1101))))

    HBP = int(round(QualifiedPA* (random.uniform(0.00,0.0516))))

    ROE = int(round(AvgAB*random.uniform(0.00,0.0182)))

    Outs = int(Strikeouts + Groundouts + Popouts + Flyouts + Lineouts)

    Singles = int(round(AvgAB * (random.uniform(0.0824,0.2206))))

    Doubles = int(round(AvgAB * (random.uniform(0.0437,0.0663))))

    Triples = int(round(AvgAB * (random.uniform(0.00,0.0134))))

    HomeRuns = int(round(AvgAB* (random.uniform(0.00,0.09))))

    Walks = int(round(QualifiedPA*(random.uniform(0.0330,0.2030))))

    Hits = int(Singles + Doubles + Triples + HomeRuns)

    TB = int((Singles) + (Doubles * 2) + (Triples * 3) + (HomeRuns * 4))

    AB = int(Hits + ROE + Outs)

    PA = int(Hits + ROE + Outs + Walks + HBP + SacFlies + SacBunts)

    Runs = int(round(HomeRuns + (PA * random.uniform(0.07,0.18))))

    BA = round(Hits/AB, 4)

    OBP =  round((Hits + Walks + HBP)/(AB + Walks + HBP + SacFlies), 3)

    Slugging = round(TB/AB,3)

    lgOBP = .312

    lgSLG = .395

    lgOPS = lgOBP + lgSLG

    ops_plus = int(round(100*((OBP/lgOBP)+(Slugging/lgSLG) -1)))

    RBI = int(round(HomeRuns + (AB * random.uniform(0.07,0.24))))

    SBAttempts = 37 #Top 10 Base Stealers by Total Stolen Bases attempted an avg of 37 SB Attempts in 2022.

    SB = int(round(SBAttempts * (random.uniform(0,0.90))))

    CS = int(round(SBAttempts * (random.uniform(0,0.30))))

    OPS = round(OBP + Slugging, 3)

    ##################################################################          



    return {
        "PA": PA,
        "AB": AB,
        "Batting Average": BA,
        "Home Runs": HomeRuns,
        "RBI": RBI,
        "SO": Strikeouts,
        "BB": Walks,
        "HBP": HBP,
        "Runs": Runs,
        "Hits": Hits,
        "2B": Doubles,
        "3B": Triples,
        "TB": TB,
        "OPS+": ops_plus,
        "OBP": OBP,
        "SLG": Slugging,
        "OPS": OPS,
        "SB": SB,
        "CS": CS

    }