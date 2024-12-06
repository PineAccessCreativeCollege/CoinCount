import unittest
import pandas as pd
import csv
from pathlib import Path
import os

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
        countingErrors = 0
        sessionValue = 0
        runningTData = {'Bags Checked': 0,
                        'Total Value': 0,
                        'Bags Check Fails': 0,
                        'User Name': ""}
                
        while allValidated == False:
            

            try:
                nameInput
            except NameError:
                nameInput = Login()
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
                countingErrors += 1
                choiceAllValidated = input("Are you Finished Adding Data? [Y] or [N]: ")
                if choiceAllValidated == "Y":
                    allValidated = True
                elif choiceAllValidated == "N":
                    allValidated = False
                else:
                    print("Error: Returning to menu (Progress will be saved)")
                    allValidated = True

        runningTData["User Name"] = nameInput
        runningTData["Bags Checked"] = bagsCheckedCurrentSession
        runningTData["Total Value"] = sessionValue
        runningTData["Bags Check Fails"] = countingErrors
        
        my_file = Path("MainLoopDataCSV.csv")
        if my_file.is_file():
                runningTSession = pd.DataFrame(runningTData, index=[0])
                runningTPrev = pd.read_csv('MainLoopDataCSV.csv', index_col=0)
                print(runningTPrev)
                runningTConcat = pd.concat([runningTPrev, runningTSession])
                runningTCond = runningTConcat.groupby(['User Name']).sum()
                os.remove('MainLoopDataCSV.csv')
                #print(runningTSession)
                #print(runningTPrev)
                #print(runningTConc)
                runningTCond.to_csv('MainLoopDataCSV.csv')
        else:
            runningTSession = pd.DataFrame(runningTData, index=[0])
            runningTSession.to_csv('MainLoopDataCSV.csv')
            
            


        """Check for existance of MainLoopDataCSV.csv and if it exists then convert to a dataframe and add a new row
        to the csv using data from runningTData and or runningTotal it depends already done this so just copy code
        OK now this works I need to use isin to check whether the session name is already contained inside of the ru
        nning total from the previous session and combine the data values"""
        

        
        print("Returning to Menu")
        Menu(None)

    def Login():
        try:
            nameInput = str(input("Please enter your name: "))
            return nameInput
        except ValueError:
            print("Value Error: Terminating")
            Menu(None)


    def DataMenu():
        pass
    def RunningTotal():
        runningTotalTXT = """--Running Total--
Your running total is as follows: """
        print(runningTotalTXT)
        with open('MainLoopDataCSV.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    #print(f'Column names are {", ".join(row)}')
                    line_count += 1
                print(f'{row["Bags Checked"]} bag(s) have been checked. With a total value of £{row["Total Value"]} by user {row["User Name"]}.')
                line_count += 1
            #print(f'Processed {line_count} lines.')
            Menu(None)


    ##Program Termination
    def EndProgram():
        
        my_file = Path("MainLoopDataCSV.csv")
        if my_file.is_file():
            
            totalData = pd.read_csv('CoinCountMediator.csv', index_col=0)
            print(totalData)

            with open('MainLoopDataCSV.csv', mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        #print(f'Column names are {", ".join(row)}')
                        line_count += 1
                    bagsCountedSession = row["Bags Checked"]
                    bagCheckFailsSession = row["Bags Check Fails"]
                    sessionName = row["User Name"]
                    
                    ##Runs if name has data in dataset
                    if sessionName not in totalData['Name'].values:
                        print(f"{sessionName} does not exist in the 'Name' column. Creating user data")

                        percentageCorrectCU = (int(bagCheckFailsSession) / int(bagsCountedSession)) * 100
                        percentageCorrectCU = 100-percentageCorrectCU

                        userData = {'Name': sessionName,
                                    'Bags Checked': bagsCountedSession,
                                    'Percentage Correct': percentageCorrectCU,
                                    'Check Fails': bagCheckFailsSession}

                        userDataDF = pd.DataFrame(userData, index=[0])
                        coinCountDataCentral = pd.read_csv('CoinCountMediator.csv', index_col=0)
                        concatUserData = pd.concat([coinCountDataCentral, userDataDF])
                        os.remove('CoinCountMediator.csv')
                        concatUserData.to_csv('CoinCountMediator.csv', index=[0])

                        #df = df.append({'Name': new_name}, ignore_index=True)
                    ##Runs if data
                    else:
                        print(f"{sessionName} already exists in the 'Name' column. Updating user data")

                        coinCountDataCentral = pd.read_csv("CoinCountMediator.csv", index_col=0)
                        #print(coinCountDataCentral)
                        
                        
                        
                        
                        rowIndex = coinCountDataCentral[coinCountDataCentral['Name'] == sessionName].index
                        sessionDataGrab = coinCountDataCentral.loc[rowIndex]
                        #Remath
                        bagsCheckedOriginal = sessionDataGrab['Bags Checked']
                        bagsCheckedTotal = int(bagsCheckedOriginal.iloc[0]) + int(bagsCountedSession)
                        bagsWrongOriginal = sessionDataGrab['Check Fails']
                        bagsWrongTotal = int(bagsWrongOriginal.iloc[0]) + int(bagCheckFailsSession)
                        
                        percentageCorrectCU = (int(bagsWrongTotal) / int(bagsCheckedTotal)) * 100
                        percentageCorrectCU = 100-int(percentageCorrectCU)
                        
                        userData = {'Name': sessionName,
                                    'Bags Checked': bagsCountedSession,
                                    'Percentage Correct': percentageCorrectCU,
                                    'Check Fails': bagCheckFailsSession}
                        
                        userDataDF = pd.DataFrame(userData, index=[0])
                        print(userDataDF)
                        print(coinCountDataCentral)
                        #print(coinCountDataCentral)
                        concatData = pd.concat([coinCountDataCentral, userDataDF])
                        
                        concatData = concatData.reset_index(drop=True)
                        
                        concatData['Bags Checked'] = pd.to_numeric(concatData['Bags Checked'], errors='coerce')
                        concatData['Check Fails'] = pd.to_numeric(concatData['Check Fails'], errors='coerce')
                        concatData['Percentage Correct'] = pd.to_numeric(concatData['Percentage Correct'], errors='coerce')
                        
                        finalData1 = concatData.groupby(['Name'], as_index=False).sum()
                        finalData1.loc[rowIndex,'Percentage Correct'] = percentageCorrectCU

                        os.remove('CoinCountMediator.csv')
                        #print(runningTSession)
                        #print(runningTPrev)
                        #print(runningTConc)
                        finalData1.to_csv('CoinCountMediator.csv', index=True)
                    line_count += 1
            os.remove('MainLoopDataCSV.csv')
        else:
            print("No Data To add or update")
    def Initial():
        pass
    
    
    ##Main Menu System
    def Menu(name):
        menuChoice = 0
        #print("Place")
        menuTitle = """--Coin Count--
1 - Main Loop
2 - Data Menu
3 - Running Total
4 - End Program
5 - Login"""
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

            my_file = Path("MainLoopDataCSV.csv")
            if my_file.is_file():
                RunningTotal()
            else:
                runningTData = {'Bags Checked': 0,
                                'Total Value': 0,
                                'Bags Check Fails': 0,
                                'User Name': ""}
                runningTotal = pd.DataFrame(runningTData, index=[0])
                runningTotal.to_csv('RunningTotalData.csv')

        elif menuChoice == 4:
            print("Ending session... Please do not close the program")
            EndProgram()
        else:
            print("Error: Out of range")
            Menu(None)
    
    Initial()
    name = None
    Menu(name)
Main()
