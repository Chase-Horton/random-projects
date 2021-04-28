import pyautogui as p
import time
import random
while 1:
	p.click(1289, 379)
	time.sleep(1)
	if(random.randint(1,2)==2):
		p.click(1470,270)
	else:
		p.click(1866, 734)