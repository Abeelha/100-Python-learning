# Theodoro Bertol Dev (Abeelha) #
# || Day 45 of #100DaysOfCode || #

from bs4 import BeautifulSoup
import os

content = open('./website.html','r')

soup = BeautifulSoup(content, "html.parser")

print(soup.title)