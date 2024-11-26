import unittest
import pandas as pd
import csv
from pathlib import Path

def Main():

   
    def MainLoop():

        lookupData = {
        "coin type": ["£2", "£1", "50p", "20p", "10p", "5p", "2p", "1p"],
        "bag value": [20, 20, 10, 10, 5, 5, 1, 1],
        "weight each coin": [12.00, 8.75, 8.00, 5.00, 6.50, 2.35, 7.12, 3.56],
        "total bag weight": [120, 175, 160, 250, 325, 235, 356, 356]
        }

        lookupTable = pd.DataFrame(lookupData)
        print(lookupTable)


        def FileReader():
            pass


        def CoinDataValidation(coinType, bagWeight, lookupData):
            typeCheck = coinType
            inputBagWeight = bagWeight
            bagValid = False
            coinValidated = None
            activeIndex = None
        
            # match case
            match typeCheck:
                # £1
                case "£2":
                    print("One")
                    coinValidated = True
                    activeIndex = 0
                # £2
                case "£1":
                    print("Two")
                    coinValidated = True
                    activeIndex = 1
                # 50p
                case "50p":
                    print("Three")
                    coinValidated = True
                    activeIndex = 2
                # 20p
                case "20p":
                    print("Four")
                    coinValidated = True
                    activeIndex = 3
                # 10p
                case "10p":
                    print("Five")
                    coinValidated = True
                    activeIndex = 4
                # 5p
                case "5p":
                    print("Six")
                    coinValidated = True
                    activeIndex = 5
                # 2p
                case "2p":
                    print("Seven")
                    coinValidated = True
                    activeIndex = 6
                # 1p
                case "1p":
                    print("Eight")
                    coinValidated = True
                    activeIndex = 7
                # default pattern
                case _:
                    print("Invalid Coin Entered")
                    coinValidated = False
                    return coinValidated, bagValue


            properBagWeight = (lookupTable.iloc[activeIndex]["total bag weight"])
            bagValue = (lookupTable.iloc[activeIndex]["bag value"])
            if inputBagWeight == properBagWeight:
                bagValid = True
                if bagValid == True:
                    return coinValidated, bagValue
            else:
                coinValidated = False
                bagValid = False
                difference = abs(properBagWeight - inputBagWeight)
                print("A value difference of " + str(difference) + " has been detected")
                singleCoinWeight = (lookupTable.iloc[activeIndex]["weight each coin"])
                if abs(singleCoinWeight % difference) == 0:
                    coinsNeeded = difference/singleCoinWeight
                    print(str(coinsNeeded) + " coin/s need to be added")
                    return bagValid, bagValue
                else:
                    print("Coin type error, remainder weight not divisible by weight per coin")
                    return bagValid, bagValue

        allValidated = False
        bagsCheckedCurrentSession = 0
        sessionValue = 0
        runningTData = {'Bags Checked': 0,
                        'Total Value': 0}

                    
        while allValidated == False:

            try:
                nameInput = str(input("Please enter your name: "))
            except ValueError:
                print("Value Error: Terminating")
            try:
                bagWeight = float(input("Enter the weight of the bag: "))
            except ValueError:
                print("Value Error: Terminating")
            try:
                coinType = str(input("What type of coin is in the bag? [£2, £1, 50p, 20p, 10p, 5p, 2p, 1p]: "))
            except ValueError:
                print("Value Error: Terminating")



            
            inputValidated, value = CoinDataValidation(coinType, bagWeight, lookupData)
            bagsCheckedCurrentSession += 1

            if inputValidated == True:
                sessionValue += value
                print("yay")
                choiceAllValidated = input("Are you Finished Adding Data? [Y] or [N]: ")
                if choiceAllValidated == "Y":
                    allValidated = True
                elif choiceAllValidated == "N":
                    allValidated = False
                else:
                    print("Error: Returning to menu (Progress will be saved)")
                    allValidated = True
            else:
                allValidated = False

        runningTData["Bags Checked"] = bagsCheckedCurrentSession
        runningTData["Total Value"] = sessionValue
        runningTotal = pd.DataFrame(runningTData, index=[0])
        runningTotal.to_csv('RunningTotalData.csv')

        Menu()

    def DataMenu():
        pass
    def RunningTotal():
        runningTotalTXT = """--Running Total--
Your running total is as follows: """
        print(runningTotalTXT)

        with open('RunningTotalData.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    #print(f'Column names are {", ".join(row)}')
                    line_count += 1
                print(f'{row["Bags Checked"]} bag(s) have been checked. With a total value of £{row["Total Value"]}.')
                line_count += 1
            #print(f'Processed {line_count} lines.')
            Menu()

    def EndProgram():

        with open('RunningTotalData.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    #print(f'Column names are {", ".join(row)}')
                    line_count += 1
                BagsCounted = row["Bags Checked"]
                
                line_count += 1
            #print(f'Processed {line_count} lines.')
            Menu()

    def Initial():
        pass
    
    def Menu():
        menuChoice = 0
        print("Place")
        menuTitle = """--Coin Count--
1 - Main Loop
2 - Data Menu
3 - Running Total
4 - End Program"""
        print(menuTitle)

        try:
            menuChoice = int(input("Enter the number refering to a menu item: "))
        except ValueError:
            print("Value Error: Terminating")

        if menuChoice == 1:
            print("Loading Main Loop")
            MainLoop()
        elif menuChoice == 2:
            print("Loading Data Menu")
            DataMenu()
        elif menuChoice == 3:
            print("Loading Running Total")

            my_file = Path("RunningTotalData.csv")
            if my_file.is_file():
                RunningTotal()
            else:
                runningTData = {'Bags Checked': 0,
                        'Total Value': 0}
                runningTotal = pd.DataFrame(runningTData, index=[0])
                runningTotal.to_csv('RunningTotalData.csv')
                
        elif menuChoice == 4:
            print("Ending session... Please do not close the program")
            EndProgram()
        else:
            print("Error: Out of range")
    
    Initial()
    Menu()
Main()
