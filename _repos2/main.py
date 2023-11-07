import sys
import os
import random

# import math
# mOG = Mode Of Game
# gO = Game Over
# cG = Continue Game
# cI = Computer Input
# uI = User Input
# nOCA = Number Of Correct Answer
# nOCp = Number Of Correct Position
mOG = int(input("Please Choose Your Play Mode , (1)Automatic or (2)Manual?"))
round = 1
gO = False  # gameOver = 0
cG = "Y"

if (mOG) == 1:
    # Random Num:Step 1
    print("Mastermind")
    print("Automatic Started")
    print("!!Rule:Please Input Four Different Number Of The List.")
    list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("list :", list1)
    random.shuffle(list1)
    n = (list1[0:4])  # N is a list
    cI = str(n[0]) + str(n[1]) + str(n[2]) + str(n[3])
    # print (cI)
    nOCA = 0
    nOCP = 0
    while gO == False:
        # Let the player input the number:step 2
        print("Round " + str(round) + " Please Input Number :", end='')
        uI = input()
        # Checking Number:step 3
        for i in range(len(cI)):
            if cI[i] == uI[i]:
                nOCA = nOCA + 1
        for i in range(len(uI)):
            for j in range(len(cI)):
                if uI[i] == cI[j]:
                    nOCP = nOCP + 1
        print("In Wrong Position Number : " + str(nOCP - nOCA))
        print("In Right Position Number :" + str(nOCA))
        nOCA = 0
        nOCP = 0
        round = round + 1
        if cI == uI:
            round = round - 1
            print("You Win! In Round " + str(round) + "!")
            gO = True
            round = 11
        # limit round :step 4
        if round > 10:
            print("Sorry,You Can't Answer This Number : " + cI + " In Round 10.")
            cG = input("Restart?(Y/N)?")
            if cG == "N":
                print("Game Over , Bye! ")
                gO = True
            elif cG == "Y":
                round = 1
                nOCA = 0
                gO = False
        else:
            cG = input("Continue(Y/N)?")
            if cG == "N":
                print("The Answer Is " + cI)
                gO = True
                print("Game Over , Bye! ")
            elif cG == "Y":
                nOCA = 0
            else:
                print("Input Error!")
                gO = True
# Manual mode
elif mOG == 2:
    cI = input("Please Input Four Different Number : ")
    print("Mastermind")
    print("Manual Started")
    print("!!Rule:Please Input Four Different Number.")
    nOCA = 0
    nOCP = 0
    while gO == False:
        print("Round " + str(round) + " Please Input Number :", end='')
        uI = input()
        for i in range(len(cI)):
            if cI[i] == uI[i]:
                nOCA = nOCA + 1
        for i in range(len(uI)):
            for j in range(len(cI)):
                if uI[i] == cI[j]:
                    nOCP = nOCP + 1
        print("In Wrong Position Number : " + str(nOCP - nOCA))
        print("In Right Position Number :" + str(nOCA))
        nOCA = 0
        nOCP = 0
        round = round + 1
        if cI == uI:
            round = round - 1
            print("You Win! In Round " + str(round) + "!")
            gO = True
            round = 11

        if round > 10:
            cG = input("Restart?(Y/N)?")
            if cG == "N":
                print(cI)
                print("Game Over , Bye! ")
                gO = True
            elif cG == "Y":
                round = 1
                nOCA = 0
                gO = False
        else:
            cG = input("Continue(Y/N)?")
            if cG == "N":
                print("The Answer Is " + cI)
                print("Game Over , Bye! ")
                gO = True
            elif cG == "Y":
                nOCA = 0
            else:
                print("Input Error!")
                gO = True
else:
    print("Input Error!")
