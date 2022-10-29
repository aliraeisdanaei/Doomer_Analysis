
import pandas as pd
import json
import snscrape

filename = "doomer_scraped_18_10_2022.json"
filename_proc = "doomer_scraped_18_10_2022_proc.json"


def preprocess(filename: str, filename_proc: str):
	"""Preprocesses the snscraper file into readable json of file name processed

	Args:
		filename (str): name of the preprocess file
		filename_proc (str): name of the postprocess file
	"""
	# json_str = '{ "doomer_posts": [\n'
	json_str = '[\n'
	with open(filename, 'r') as file:
		lines = file.readlines()
		for ln in lines:
			ln = ln.replace('\n', '')
			json_str += f'{ln},\n'
		
	json_str += ']'

	with open(filename_proc, 'w') as file:
		file.write(json_str)


if(__name__ == "__main__"):
	preprocess(filename, filename_proc)



