# Shree KRISHNAya Namaha

import pyautogui
from tkinter import Tk
from time import sleep

SLEEP_TIME = 0.5
MAX_DUPLICATE_COUNT = 5
links = []
filename = "Trial01.txt"

def readURLs():
	pyautogui.hotkey('win', '4')
	sleep(SLEEP_TIME)
	# pyautogui.position() # To read current mouse position
	# pyautogui.moveTo(298, 69)
	pyautogui.hotkey('ctrl', '1')
	duplicateCount = 0
	while(duplicateCount < MAX_DUPLICATE_COUNT):
		pyautogui.click(x=1000, y=70, button='left')
		sleep(SLEEP_TIME)
		pyautogui.hotkey('ctrl', 'a')
		sleep(SLEEP_TIME)
		pyautogui.hotkey('ctrl', 'c')
		sleep(SLEEP_TIME)
		link = Tk().clipboard_get()
		if len(links) > 0 and link in links:
			duplicateCount += 1
			print('Duplicate ' + str(duplicateCount) + ' found: ' + link)
		else:
			links.append(link)
		print(link)
		sleep(SLEEP_TIME)
		pyautogui.hotkey('ctrl', 'tab')
		sleep(SLEEP_TIME)
	
def saveToFile():
	file = open(filename, 'w')
	file.write('\n'.join(links))
	file.close()

readURLs()
saveToFile()
pyautogui.hotkey('win', 'd')