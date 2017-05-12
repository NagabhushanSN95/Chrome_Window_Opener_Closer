# Shree KRISHNAya Namaha

import os

fileName = "Trial01.txt"

commandString = 'start chrome /new-window "'
file = open(fileName)
urls = file.readlines()
urls = [url.strip() for url in urls]
commandString += '" "'.join(urls) + '"'
print(commandString)
# Execute command in Command Prompt to start new Chrome window and open the URLs
os.system(commandString)
