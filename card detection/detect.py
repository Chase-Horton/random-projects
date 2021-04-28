# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:17:07 2020

@author: Chase
"""
import glob
import cv2
import imutils
ranks = []
suits = []
rankFiles = [
    "pictures/rank/a.jpg", "pictures/rank/k.jpg", "pictures/rank/q.jpg", "pictures/rank/j.jpg", "pictures/rank/ten.jpg",
    "pictures/rank/nine.jpg", "pictures/rank/eight.jpg", "pictures/rank/seven.jpg", "pictures/rank/six.jpg", "pictures/rank/five.jpg",
    "pictures/rank/four.jpg", "pictures/rank/three.jpg", "pictures/rank/two.jpg", "pictures/rank/one.jpg"]
suitFiles = ["pictures/suit/spades.jpg", "pictures/rank/clubs.jpg", "pictures/rank/diamonds.jpg", "pictures/rank/hearts.jpg"]
#def getCard(rank, suit):
for myFile in ranks:
    print(myFile)
    image = cv2.imread(myFile)
    ranks.append(image)
for myFile in suits:
    print(myFile)
    image = cv2.imread(myFile)
    ranks.append(image)