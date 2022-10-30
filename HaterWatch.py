import requests

class HaterWatch():
	def __init__(self, key: str):
		self.key = key
		self.url = 'https://na1.api.riotgames.com'
		self.default_header = {'X-Riot-Token': self.key}

	''' 
		Rate Limit:
		20 requests every 1 seconds(s)
		100 requests every 2 minutes(s)
	'''
	def _request(self, request_url: str, header=None):
		if header == None:
			header = self.default_header
		return requests.get(self.url + request_url, headers=header)

	''' returns ranked information from each summoner in list '''
	def ranked_info(self, summoner_names: list) -> list:
		ranked_info = []
		for name in summoner_names:
			ranked_info.append(self._request('/lol/league/v4/entries/by-summoner/' + self.summoner_id(name)))
		return ranked_info

	''' this method makes two requests, one for summonerId, and one for ranked info about summoner '''
	def summoner_id(self, summoner_name: str) -> str:
		return self.summoner_info(summoner_name).json()['id']

	def summoner_info(self, summoner_name: str):
		return self._request('/lol/summoner/v4/summoners/by-name/' + summoner_name)

'''
returns rank info in the following format:

Faker
RANKED_SOLO_5x5
SILVER II 81 LP
57 W : 61 L
'''
def beautify(summoner_ranked_info: list):
	summoner_ranks = ""
	for rank in summoner_ranked_info:
		queue_rank = "{}\n{}\n{} {} - {} LP\n{} W : {} L".format(
			rank['summonerName'],
			rank['queueType'],
			rank['tier'], rank['rank'], rank['leaguePoints'],
			rank['wins'], rank['losses'])
		summoner_ranks += queue_rank

	return summoner_ranks


if __name__ == '__main__':
	api = HaterWatch(open('key.txt', 'r').read())
	response = api.ranked_info(['beanmaster300000', 'gnatt'])
	for elem in response:
		print(beautify(elem.json()))
