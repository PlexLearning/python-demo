import MyPythonLibrary

def MainMenu():
    MenuItems = [
        (1, "ATM Cash-Machine V00"), (2, "ATM Cash-Machine V01"),
        (3, "Roll Dice"), (4, "ATM Cash-Machine V02"),
        (5, "Future Value Balance"), (6, "Exit this Dashboard")
        ] 
    MenuString = "\n      Main DashBoard Menu\n"   
    for MenuNumber, MenuItem in MenuItems:
        MenuString += (f"{MenuNumber:02d} - {MenuItem}\n")
    return MenuString

# Main  Dashboard
def MainDashboard():
    DashBoard = True
    while DashBoard not in (0,6): # DashBoard != 0 or DashBoard != 6:
        print (MainMenu())
        DashBoard = eval(input("Enter a valid number: "))
        if DashBoard == 0 or DashBoard == 6:  # if DashBoard in (0,6) 
            continue    
        elif DashBoard == 1:    
            MyPythonLibrary.cash_machine()
        elif DashBoard == 3:    
            MyPythonLibrary.dice()
        elif DashBoard == 5:    
            MyPythonLibrary.MainFutureValue()     
        else:    
            print("Please enter a valid number from the menu") 
            input("Press Enter to continue...")
    else:      
            print("Exiting Main Dashboard - Have a nice day")

if __name__ == '__main__':
    MainDashboard()
