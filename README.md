# OSRS Hiscores API Library

## STATUS
This Package is no longer supported and instead has been implemented into [OSRSBytes](https://github.com/Coffee-fueled-deadlines/OSRSBytes)

NOTE: I, Matt, am currently maintaining this fork for use with the [bot-detector-discord-bot](https://github.com/Bot-detector/bot-detector-discord-bot), but the upstream repo is in fact dead.

## Purpose
  The purpose of this library is to interface with Old School Runescape (OSRS)'s Hiscores page and allow developers to access stat levels, ranks, and experience levels in a more intuitive way (via dictionary).  This library accesses this information via a `http.client` request and parses the information accordingly.	
***

### __Installation and Upgrades__

#### Installation
```
pip install git+https://github.com/ThorntonMatthewD/osrs-hiscores.git@master
```
#### Upgrade
```
python -m pip install git+https://github.com/ThorntonMatthewD/osrs-hiscores.git@master --upgrade
```
***

## New Features (v0.6?)


Newest features include:

* You can enter usernames with spaces now and it won't break (wow)
* Boss KC, Tournament Points and Minigame Completions (as well as accompanying rankings) are available at your leisure!

-Matt

```python
from OSRS_Hiscores import Hiscores

username = 'Zezima'
user = Hiscores(username, 'N')

# Lets get our attack level, rank, and experience the new way
print("Current level:", user.skill('attack', 'level'))
print("Current rank:", user.skill('attack', 'rank'))
print("Current exp:", user.skill('attack', 'experience'))

# Lets say we want to now the exact experience needed for the next level... simple
print("Total XP to Next Level:", user.skill('attack','next_level_exp'))

# What if we want the Experience remaining until next level?  We can do that too!
print("XP Remaining:", user.skill('attack','exp_to_next_level'))

#Want to see your Vorkath KC? Your ranking perhaps? It's ez pz!
print(f"Vorkath KC: {user.boss('vorkath', 'killcount')} | Vorkath Rank: {user.boss('vorkath', 'rank')} )

```

## Example Usage
```Python
from OSRS_Hiscores import Hiscores

# User to lookup
username = 'Zezima'

# Initialize user object, if no account type is specified, we assume 'N'
user = Hiscores(username, 'N')

# Get the entire stat dictionary
user.stats

# Get total Levels
user.skill('total')

# Get a specific skill's ranking, level, and experience
user.stats['runecrafting']

# Get skill's level, ranking, and experience separately
user.stats['runecrafting']['level']
user.stats['runecrafting']['rank']
user.stats['runecrafting']['experience']

# NEW
user.stats['runecrafting']['next_level_experience'] # Total Exp needed for next level
user.stats['runecrafting']['exp_to_next_level'] # Exp remaining til next level

# A simpler way to just get a skill's attributes
print("Current level:", user.skill('attack', 'level'))
print("Current rank:", user.skill('attack', 'rank'))
print("Current exp:", user.skill('attack', 'experience'))
print("Exp remaining:", user.skill('attack','exp_to_next_level'))
```
