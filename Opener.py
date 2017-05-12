# Shree KRISHNAya Namaha

import os

fileName = "Trial01.txt"

commandString = 'start chrome /new-window "'
file = open(fileName)
urls = file.readlines()
urls = [url.strip() for url in urls]
commandString += '" "'.join(urls) + '"'
print(commandString)
os.system(commandString)