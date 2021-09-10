name = "OSRS_Hiscores"

import http.client
import math
from sys import exit

__status__ = "Closed (Unsupported)"

class Error(Exception):
	pass

class InvalidSTypeError(Error):
	pass

class InvalidPlayerType(Error):
	pass

class Hiscores(object):
	"""Hiscores class
	
	The Hiscores class deals with collecting the required
	information needed to fetch user information from in-game
	API.  After being supplied necessary information, Hiscores
	class then sets self.stats dictionary with user information.
	
	Args:
		self,
		username str: The username of the account that you
			      want to look up information on.
		actype   str: The account type of the account that
		              you want to lookup.  If not supplied
			      this argument defaults to 'N' Normal.
			      
	Returns:
		This object returns nothing.  Instead it sets the 
		value of self.stats with a dictionary of values
		keyed by the skill type. Example: self.stats['attack']
		
	Example Invocation:
		from OSRS-Hiscores import Hiscores
		account = Hiscores('Zezima', 'N')
		print(account.stats['attack']['level']) # displays attack level
	"""
	def __init__(self, username: str, actype='N'):
		self.username = username.replace(" ", "_")
		self.accountType = actype.upper()
		self.getHTTPResponse()

	def getHTTPResponse(self):
		"""getHTTPResponse() method
		
		The getHTTPResponse() method communicates with the OSRS Hiscores API
		and supplies the required information from self.username and
		self.actype to pull the given users stats and hiscore information.
		
		Args:
			self
			
		Returns:
			None
			
		Triggers:
			self.processResponse(): This method is always triggered, regardless
			                        of whether or not the query to the API returned
						successfully or not.
		"""
		conn = http.client.HTTPSConnection('secure.runescape.com')

		if self.accountType == 'N':
			conn.request("GET", f"/m=hiscore_oldschool/index_lite.ws?player={self.username}")
			self.response = conn.getresponse()
			self.status = self.response.status
		elif self.accountType == 'IM':
			conn.request("GET", f"/m=hiscore_oldschool_ironman/index_lite.ws?player={self.username}")
			self.response = conn.getresponse()
			self.status = self.response.status
		elif self.accountType == "UIM":
			conn.request("GET", f"/m=hiscore_oldschool_ultimate/index_lite.ws?player={self.username}")
			self.response = conn.getresponse()
			self.status = self.response.status
		elif self.accountType == "HIM":
			conn.request("GET", f"/m=hiscore_oldschool_hardcore_ironman/index_lite.ws?player={self.username}")
			self.response = conn.getresponse()
			self.status = self.response.status
		elif self.accountType == "S":
			conn.request("GET", f"/m=hiscore_oldschool_seasonal/index_lite.ws?player={self.username}")
			self.response = conn.getresponse()
			self.status = self.response.status
		else:
			self.status = 999
		self.processResponse()

	def processResponse(self):
		"""processResponse() method
		
		The processResponse() method processes the response received during the
		getHTTPResponse() method.  It handles potential 404 errors, 403 errors
		and the like and sets self.errorMsg accordingly.  On successful Response
		data is stored in self.data and sent to the self.parseData() method.
		
		Args:
			self
			
		Returns:
			None
			
		Triggers:
			self.error(): This method is triggered whenever the self.status of
			              a request is not 200 (failed).
				      
			self.parseData(): This method is called when self.status is 200 (success)
		"""
		if self.status != 200:
			if self.status == 999:
				raise InvalidPlayerType("Valid account types are, 'N' (Normal), 'IM' (Iron Man), 'UIM' (Ultimate Iron Man), 'HIC' (Hardcore Iron Man)")
			else:
				raise http.client.HTTPException(f"Status Code: {self.status}", f"Player name given might not be able to be found with account type provided (current selection: {self.accountType}), or hiscores are unreachable.")
		else:
			self.data = self.response.read().decode('ascii')
			self.parseData()

	def parseData(self):
		"""parseData() method
		
		The parseData() method parses the self.data processed in the processResponse()
		method.  Data parsed in placed in the self.stats dictionary.
		
		Args:
			self
			
		Returns:
			None
			
		Triggers:
			None
		"""
		self.data = self.data.replace('\n',',')
		self.data = self.data.split(',')

		skills_subset = {}
		bosses_subset = {}

		# Totals
		info = {}
		info['rank']       = self.data[0]
		info['level']      = self.data[1]
		info['experience'] = self.data[2]
		skills_subset['total']    = info

		skills = [
					'attack',
					'defense',
					'strength',
					'hitpoints',
					'ranged',
					'prayer',
					'magic',
					'cooking',
					'woodcutting',
					'fletching',
					'fishing',
					'firemaking',
					'crafting',
					'smithing',
					'mining',
					'herblore',
					'agility',
					'thieving',
					'slayer',
					'farming',
					'runecrafting',
					'hunter',
					'construction'
		]

		#also includes minigames and tournament points
		bosses = [
					'league',
					'bounty_hunter_hunter',
					'bounty_hunter_rogue',
					'cs_all',
					'cs_beginner',
					'cs_easy',
					'cs_medium',
					'cs_hard',
					'cs_elite',
					'cs_master',
					'lms_rank',
					'soul_wars_zeal',
					'abyssal_sire',
					'alchemical_hydra',
					'barrows_chests',
					'bryophyta',
					'callisto',
					'cerberus',
					'chambers_of_xeric',
					'chambers_of_xeric_challenge_mode',
					'chaos_elemental',
					'chaos_fanatic',
					'commander_zilyana',
					'corporeal_beast',
					'crazy_archaeologist',
					'dagannoth_prime',
					'dagannoth_rex',
					'dagannoth_supreme',
					'deranged_archaeologist',
					'general_graardor',
					'giant_mole',
					'grotesque_guardians',
					'hespori',
					'kalphite_queen',
					'king_black_dragon',
					'kraken',
					'kreearra',
					'kril_tsutsaroth',
					'mimic',
					'nightmare',
					'phosanis_nightmare',
					'obor',
					'sarachnis',
					'scorpia',
					'skotizo',
					'tempoross',
					'the_gauntlet',
					'the_corrupted_gauntlet',
					'theatre_of_blood',
					'theatre_of_blood_hard',
					'thermonuclear_smoke_devil',
					'tzkal_zuk',
					'tztok_jad',
					'venenatis',
					'vetion',
					'vorkath',
					'wintertodt',
					'zalcano',
					'zulrah'
		]


		counter = 0
		for i in range(len(skills)):
			info = {}
			info['rank']       = int(self.data[counter+3])
			info['level']      = int(self.data[counter+4])
			info['experience'] = int(self.data[counter+5])
			level = int(info['level']+1)
			info['next_level_exp'] = math.floor(sum((math.floor(level + 300 * (2 ** (level / 7.0))) for level in range(1, level)))/4)
			info['exp_to_next_level'] = int(info['next_level_exp'] - info['experience'])
			skills_subset[skills[i]] = info
			counter += 3

		for i in range(len(bosses)):
			info = {}
			info['rank']		= int(self.data[counter+3])
			info['killcount']	= int(self.data[counter+4])
			bosses_subset[bosses[i]] = info
			counter += 2

		# set stats and bosses dicts
		self.stats = skills_subset
		self.bosses = bosses_subset

	def skill(self, skill: str, stype: str = 'level') -> str:
		"""skill() method
		
		The skill() method is a more dynamic, intuitive way to access stats
		than the self.stats dictionary variable.  It allows for a user to
		provide the skill and stype (level, rank, experience) of the skill
		they wish information on.
		
		Args:
			skill (str): The OSRS skill to get information on
			
			stype (str): One of 'level', 'rank', or 'experience'
			             to receive information for.  If not
				     supplied, stype is assumed to be
				     'level'
		Returns:
			self.stats[skill][stype] (int): The info you requested
		
		"""
		try:
			if stype.lower() not in ['rank','level','experience','exp_to_next_level']:
				raise InvalidSTypeError("stype must be 'rank','level', 'experience' or 'exp_to_next_level'")
			else:
				return self.stats[skill.lower()][stype.lower()]
		except KeyError as KE:
			print(f"ERROR: skill {KE} does not exist")
			raise KeyError()


	def boss(self, boss: str, stype: str = 'killcount') -> str:
		"""boss() method
		
		Allows users to directly access an individual boss/minigame/tournament's
		information for a given RSN.
		
		Args:
			boss (str): The OSRS boss/minigame/tournament name 
			
			stype (str): One of 'killcount' or 'rank'
			             to receive information for.  If not
				     supplied, stype is assumed to be
				     'killcount'
		Returns:
			self.bosses[boss][stype] (int): The info you requested
		"""
		try:
			if stype.lower() not in ['killcount', 'rank']:
				raise InvalidSTypeError("stype must be 'killcount' or 'rank'")
			else:
				return self.bosses[boss.lower()][stype.lower()]
		except KeyError as KE:
			print(f"ERROR: boss {KE} does not exist")
			raise KeyError()