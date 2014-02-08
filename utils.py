import re

def remove_urls(string):
	return re.sub(r'((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', ' ', string)

def remove_symbols(string):
	return re.sub(r'[^\w]', ' ', string)