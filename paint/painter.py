import pyautogui
import time
import cv2

time.sleep(5)
frame = cv2.imread("yin-yang.jpg")
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
frame = cv2.resize(frame, (100,100))
image = []
for row in frame:
    newRow = []
    for item in row:
        if item < 150:
            newRow.append(1)
        else:
            newRow.append(0)
    image.append(newRow)
y = 228
pyautogui.PAUSE = 0.001
for row in image:
    pyautogui.moveTo(73, y)
    for item in row:
        if item == 1:
            pyautogui.click()
        pyautogui.moveRel(3, 0)
    y+= 3
