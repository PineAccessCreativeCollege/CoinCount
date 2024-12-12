import unittest
import pandas as pd
import csv
from pathlib import Path
import os

def Main():

   
    def MainLoop():
        
        #Asks for user inputs relating to name bag weight and coin type and checks these values agaians the lookupData table
        #Stores the data for one name before sending the data to a texporary csv file to be transfered to final data saving
        #Multiple User Names can be concatonated into the CSV file

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

        
        #Validates User Inputs and informs the user of the type of error
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

            #Runs if the bag was counted correctly
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
                    
            #Runs if the bag was counted incorrectly
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
        
        #Runs if the file already exists to concat data
        if my_file.is_file():
                runningTSession = pd.DataFrame(runningTData, index=[0])
                runningTPrev = pd.read_csv('MainLoopDataCSV.csv', index_col=0)
                print(runningTPrev)
                runningTConcat = pd.concat([runningTPrev, runningTSession])
                runningTCond = runningTConcat.groupby(['User Name']).sum()
                os.remove('MainLoopDataCSV.csv')
                runningTCond.to_csv('MainLoopDataCSV.csv')
                
        #Runs if the file doesnt exist to create and add data
        else:
            runningTSession = pd.DataFrame(runningTData, index=[0])
            runningTSession.to_csv('MainLoopDataCSV.csv')
            
            

        #A writup so i could do some logical thinking about the problem
        """Check for existance of MainLoopDataCSV.csv and if it exists then convert to a dataframe and add a new row
        to the csv using data from runningTData and or runningTotal it depends already done this so just copy code
        OK now this works I need to use isin to check whether the session name is already contained inside of the ru
        nning total from the previous session and combine the data values"""
        

        
        print("Returning to Menu")
        Menu(None)

    def Login():
        
        #Unimplamented: Please Ignore
        try:
            nameInput = str(input("Please enter your name: "))
            return nameInput
        except ValueError:
            print("Value Error: Terminating")
            Menu(None)

    
    #Outputs the total data from the previous session/viewing and saving of data requires the respective menu item to be run
    def DataMenu():
        userDataDF = pd.read_csv('CoinCount.txt', index_col=[0])
        print("\n---Sorted User Data---")
        print("\n",userDataDF)
        Menu(None)
        
    
    #Outputs the running total created in the temporary csv created in the MainLoop() area
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



    ##Program Termination and data saving, concatanation, and remathing of values
    def EndProgram():
        
                
        my_file = Path("CoinCount.txt")
        if my_file.is_file():
            pass
        else:
            f = open("CoinCount.txt", "x")
            f.close()
        
        my_file1 = Path("MainLoopDataCSV.csv")
        if my_file1.is_file():
            
            totalData = pd.read_csv('CoinCountMediator.csv', index_col=0)
            #print(totalData)

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
                        
                        #Remaths percentage values
                        percentageCorrectCU = (int(bagCheckFailsSession) / int(bagsCountedSession)) * 100
                        percentageCorrectCU = 100-percentageCorrectCU

                        userData = {'Name': sessionName,
                                    'Bags Checked': bagsCountedSession,
                                    'Percentage Correct': percentageCorrectCU,
                                    'Check Fails': bagCheckFailsSession}

                        userDataDF = pd.DataFrame(userData, index=[0])
                        
                        coinCountDataCentral = pd.read_csv('CoinCountMediator.csv', index_col=0)
                        
                        #Data Concatanation
                        
                        concatUserData = pd.concat([coinCountDataCentral, userDataDF])
                        os.remove('CoinCountMediator.csv')
                        concatUserData.to_csv('CoinCountMediator.csv', index=[0])

                        
                    ##Runs if name doesnt have data in dataset
                    else:
                        print(f"{sessionName} already exists in the 'Name' column. Updating user data")

                        coinCountDataCentral = pd.read_csv("CoinCountMediator.csv", index_col=0)
                        
                        rowIndex = coinCountDataCentral[coinCountDataCentral['Name'] == sessionName].index
                        sessionDataGrab = coinCountDataCentral.loc[rowIndex]
                        
                        #Remaths percentage values
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
                        
                        #Data Concatanation
                        
                        concatData = pd.concat([coinCountDataCentral, userDataDF])
                        concatData = concatData.reset_index(drop=True)
                        
                        concatData['Bags Checked'] = pd.to_numeric(concatData['Bags Checked'], errors='coerce')
                        concatData['Check Fails'] = pd.to_numeric(concatData['Check Fails'], errors='coerce')
                        concatData['Percentage Correct'] = pd.to_numeric(concatData['Percentage Correct'], errors='coerce')
                        
                        finalData1 = concatData.groupby(['Name'], as_index=False).sum()
                        finalData1.loc[rowIndex,'Percentage Correct'] = percentageCorrectCU

                        os.remove('CoinCountMediator.csv')
                        finalData1.to_csv('CoinCountMediator.csv', index=True)
                    line_count += 1
            os.remove('MainLoopDataCSV.csv')
        else:
            print("\nNo Data To add or update")
            
        #Gathers data into a txt file
        #This implementation is lazy and inefficient for large datasets.
        #I am not fixing it :3
        
        txtData = pd.read_csv('CoinCountMediator.csv', index_col=[0])
        txtData['Percentage Correct'] = pd.to_numeric(txtData['Percentage Correct'], errors='coerce')
                        
        sortedValues = txtData.sort_values(by=['Percentage Correct'], ascending=[False])
        
        sortedRows = []

        for index, row in sortedValues.iterrows():
            sortedValuesCurrentRow = {
                "Name": row["Name"],
                "Bags Checked": row["Bags Checked"],
                "Percentage Correct": row["Percentage Correct"]
            }
            
            sortedRows.append(sortedValuesCurrentRow)

        userDataDF = pd.DataFrame(sortedRows)
        os.remove('CoinCount.txt')
        userDataDF.to_csv('CoinCount.txt', index=True)

        print("---Sorted Data---")
        print("\n",userDataDF)
        
        
        
    def Initial():
        pass
    
    
    ##Main Menu System
    def Menu(name):
        menuChoice = 0
        #print("Place")
        menuTitle = """--Coin Count--
1 - Main Loop
2 - Data Menu
3 - Running Total: View Running Total
4 - End Program/SaveData
5 - Login"""
        print("\n",menuTitle)

        try:
            menuChoice = int(input("\nEnter the number refering to a menu item: "))
        except ValueError:
            print("\nValue Error: Terminating")

        if menuChoice == 1:
            print("\nLoading Main Loop")              
            MainLoop()
        elif menuChoice == 2:
            print("\nLoading Data Menu")
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
                print("\nNo Data Generated: go make some!!")
                Menu(None)

        elif menuChoice == 4:
            print("\nEnding session... Please do not close the program")
            EndProgram()
            
        elif menuChoice == 5:
            print("\nUnimplemented")
            Menu(None)
        else:
            print("\nError: Out of range")
            Menu(None)
    
    Initial()
    name = None
    Menu(name)
Main()
