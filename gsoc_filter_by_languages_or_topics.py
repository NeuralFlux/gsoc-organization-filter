from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from random import randint
from time import sleep
import neat

url = 'https://summerofcode.withgoogle.com/archive/2018/organizations/'

response = get(url)
soup = BeautifulSoup(response.text, 'html.parser')

org_cards = soup.findAll('a', class_ = 'organization-card__link')  # Get all the organization cards
orgs, org_links = [], []
for org_card in org_cards:
	orgs += [org_card.find('md-card').div.h4.text]  # Name of Org
	org_links += [org_card["href"].split('/')[-2]]

out = open("output.txt", "w+")

for org in range(len(orgs)):
	sleep(randint(2,5))  # Control crawl rate

	print(orgs[org] + ', ' + url + org_links[org] + ', ', file=out)

	org_response = get(url + org_links[org])
	soup_org = BeautifulSoup(org_response.text, 'html.parser')

	tags = soup_org.find_all('li', class_ = "organization__tag")
	techs, topics = [], []
	for tag in tags:
		if tag.a != None:
			topics += [tag.a.text.strip()]
		elif "technology" in tag["class"][-1]:
			techs += [tag.text.strip()]
		else:
			topics += [tag.text.strip()]

	print(', '.join(techs), file=out)
	print(', '.join(topics) + '\n', file=out)
	if org > 1:
		break

out.close()
neat.make_table("output.txt")  # Make HTML table
