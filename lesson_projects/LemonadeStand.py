from MenuItem import MenuItem
from lesson_projects.SalesForDay import SalesForDay

class InvalidSalesItemError(Exception):
    pass

class LemonadeStand:
    
    #constructor
    def __init__(self, standName: str) -> None:
        self.__standName_ = standName
        self.__currentDay_ = 0
        self.__menu_ = {}
        self.__salesRecord_ = []
    
    #method to get stand name
    def getStandName(self):
        return self.__standName_
    
    #method to add menu item
    def addMenuItem(self, objMenuItem: dict) -> None:
        menuItemName = objMenuItem.getItemName()
        self.__menu_[menuItemName] = objMenuItem
    
    #method to enter sales for today
    def enterSalesForToday(self, salesForToday: dict[str, int]):
        for name in salesForToday.keys():
            try:
                if name not in self.__menu_.keys():
                    raise InvalidSalesItemError
            except InvalidSalesItemError:
                print("One of the items is not on the menu.")
                break
        else:
            objSFD = SalesForDay(self.__currentDay_, salesForToday)
            self.__salesRecord_.append(objSFD)
            self.__currentDay_ += 1
    
    #method for sales of menu item for day
    def salesOfMenuItemForDay(self, day, menuItemName: str):
        salesDict = self.__salesRecord_[day].getSalesDict()
        numSales = 0
        if menuItemName in salesDict.keys():
            numSales = salesDict[menuItemName]
        return numSales
        

    #method for total sales of a menu item
    def totalSalesForMenuItem(self, menuItemName: str):
        totalSales = 0
        for day in range(len(self.__salesRecord_)):
            totalSales += self.salesOfMenuItemForDay(day, menuItemName)
        return totalSales
    
    #method for total profit of a menu item
    def totalProfitForMenuItem(self, menuItemName: str):
        wholesaleCost = self.__menu_[menuItemName].getWholesaleCost()
        profit = self.totalSalesForMenuItem(menuItemName) - wholesaleCost
        return profit
    
    #method for total profit of stand
    def totalProfitForStand(self):
        totalProfit = 0
        for menuItem in self.__menu_:
            totalProfit += self.totalProfitForMenuItem(menuItem)
        return totalProfit