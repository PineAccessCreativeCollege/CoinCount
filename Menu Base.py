def Main():
    def MainLoop():
        try:
            nameInput = str(input("Please enter your name: "))
        except ValueError:
            print("Value Error: Terminating")
        try:
            bagWeight = float(input("Enter the weight of the bag: "))
        except ValueError:
            print("Value Error: Terminating")


    def DataMenu():
        print("Place")
    
    
    def Menu():
        menuChoice = 0
        print("Place")
        menuTitle = """--Coin Count--
1 - Main Loop
2 - Data Menu"""
        print(menuTitle)

        try:
            menuChoice = int(input("Enter the number refering to a menu item: "))
        except ValueError:
            print("Value Error: Terminating")

        if menuChoice is 1:
            print("Loading Main Loop")
            MainLoop()
        elif menuChoice is 2:
            print("Loading Data Menu")
        else:
            print("Error: Out of range")
    
    Menu()
Main()
