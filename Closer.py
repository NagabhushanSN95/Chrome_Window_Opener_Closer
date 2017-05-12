# Shree KRISHNAya Namaha

import pyautogui
from tkinter import Tk
from time import sleep

SLEEP_TIME = 0.5
MAX_DUPLICATE_COUNT = 5
links = []
filename = "Trial01.txt"


def readURLs():
	pyautogui.hotkey('win', '4')		# Open Google Chrome
	sleep(SLEEP_TIME)
	# pyautogui.position() 				# To read current mouse position
	# pyautogui.moveTo(298, 69)
	pyautogui.hotkey('ctrl', '1')		# Open 1st Tab
	duplicate_count = 0
	while duplicate_count < MAX_DUPLICATE_COUNT:
		pyautogui.click(x=1000, y=70, button='left')		# Click on URL Bar
		sleep(SLEEP_TIME)
		pyautogui.hotkey('ctrl', 'a')						# Select complete URL
		sleep(SLEEP_TIME)
		pyautogui.hotkey('ctrl', 'c')						# Copy URL
		sleep(SLEEP_TIME)
		link = Tk().clipboard_get()							# Read from Clipboard
		if len(links) > 0 and link in links:				# Check if the URL has already been saved
			duplicate_count += 1
			# print('Duplicate ' + str(duplicate_count) + ' found: ' + link)
		else:
			links.append(link)								# Else append the URL to list
		print(link)
		sleep(SLEEP_TIME)
		pyautogui.hotkey('ctrl', 'tab')						# Switch to next tab
		sleep(SLEEP_TIME)
	
def saveToFile():
	file = open(filename, 'w')
	file.write('\n'.join(links))
	file.close()

readURLs()
saveToFile()
pyautogui.hotkey('win', 'd')								# Close all windows: indicates end of script
