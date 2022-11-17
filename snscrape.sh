#!/bin/bash

snscrape -n 400000 --progress --jsonl reddit-subreddit doomer > Data/r_doomer_scraped.json
snscrape -n 400000 --progress --jsonl reddit-subreddit loneliness > Data/r_loneliness_scraped.json
snscrape -n 100000 --progress --jsonl reddit-subreddit lonely > Data/r_lonely_scraped.json
snscrape -n 400000 --progress --jsonl reddit-subreddit depression > Data/r_depression_scraped.json