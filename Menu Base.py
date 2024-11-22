import unittest
import pandas as pd

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
                    return coinValidated


            properBagWeight = (lookupTable.iloc[activeIndex]["total bag weight"])
            if inputBagWeight == properBagWeight:
                bagValid = True
                if bagValid == True:
                    return coinValidated
            else:
                coinValidated = False
                bagValid = False
                difference = abs(properBagWeight - inputBagWeight)
                print("A value difference of " + str(difference) + " has been detected")
                singleCoinWeight = (lookupTable.iloc[activeIndex]["weight each coin"])
                if abs(singleCoinWeight % difference) == 0:
                    coinsNeeded = difference/singleCoinWeight
                    print(str(coinsNeeded) + " coin/s need to be added")
                    return bagValid
                else:
                    print("Coin type error, remainder weight not divisible by weight per coin")
                    return bagValid

        def FileWrite():
            pass


        allValidated = False
            
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


            runningTData = {"Bags Checked": [0],
                            "Total Value": [0]}

            runningTotal = pd.DataFrame(runningTData)
            print(runningTotal)

            
            inputValidated = CoinDataValidation(coinType, bagWeight, lookupData)

            if inputValidated == True:
                print("yay")
                allValidated = True
            else:
                allValidated = False

        Menu()

    def DataMenu():
        print("Place")
    
    
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
        elif menuChoice == 3:
            print("Loading Running Total")
        elif menuChoice == 4:
            print("Ending session... Please do not close the program")
        else:
            print("Error: Out of range")
    
    Menu()
Main()
