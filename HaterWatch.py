import requests

class HaterWatch():
	def __init__(self, key: str):
		self.key = key
		self.url = 'https://na1.api.riotgames.com'
		self.default_header = {'X-Riot-Token': self.key}

	def _request(self, request_url: str, header=None):
		if header == None:
			header = self.default_header
		return requests.get(self.url + request_url, headers=header)

	def ranked_info(self, summoner_name: str):
		return self._request('/lol/league/v4/entries/by-summoner/' + self.summoner_id(summoner_name))

	def summoner_info(self, summoner_name: str):
		return self._request('/lol/summoner/v4/summoners/by-name/' + summoner_name)

	def summoner_id(self, summoner_name: str) -> str:
		return self.summoner_info(summoner_name).json()['id']


if __name__ == '__main__':
	api = HaterWatch(open('key.txt', 'r').read())
	response = api.ranked_info('beanmaster300000')
	print(response.text)