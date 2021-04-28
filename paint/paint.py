import random
import pyautogui
import time
pyautogui.PAUSE = 0.0001
seed = input("Input a random integer seed: ")
lineCt = int(input("How many lines do you want? "))
time.sleep(2)
tl = (5, 145)
br = (724, 985)
# 720x840
#br = (963, 683)
# 1920x1080
red = (829, 62)
yellow = (875, 62)
green = (892, 62)
blue = (915, 62)
purple = (960, 62)
pink = (824, 87)
black = (761, 62)
darkblue = (938, 62)

colors = [red, yellow, green, darkblue, purple, black, blue, pink]
lastColor = yellow
size = (636, 81)
size1 = (675, 140)
size2 = (675, 180)
size3 = (675, 215)
size4 = (675, 260)

sizes = [size1, size2, size3, size4]
lines = 0
r = random.Random(seed)
while lines < lineCt:
    color = r.choice(colors)
    if color[0] == lastColor[0]:
        continue
    lastColor = color
    pyautogui.click(color)
    pyautogui.click(color)


    pyautogui.click(size)
    brushSize = r.randint(1,4)
    pyautogui.press("down", presses = brushSize)
    pyautogui.press("enter")

    for i in range(1, r.randint(4, 10)):
        x = r.randint(tl[0], br[0])
        y = r.randint(tl[1], br[1])
        brushStart = (x, y)
        xRange = [5-x, 724-x]
        yRange = [145-y, 985-y]
        if xRange[0] < -250:
            xRange[0] = -250
        if xRange[1] > 250: 
            xRange[1] = 250

        if yRange[0] < -250:
            yRange[0] = -250
        if yRange[1] > 250: 
            yRange[1] = 250
        brushStroke = (r.randint(xRange[0], xRange[1]), r.randint(yRange[0], yRange[1]))
        pyautogui.moveTo(brushStart)
        pyautogui.dragRel(brushStroke)
    lines += 1