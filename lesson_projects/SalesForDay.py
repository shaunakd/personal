class SalesForDay:
    
    #constructor
    def __init__(self, numOfDays: int, salesDict: dict[str, float]) -> None:
        self.__numOfDays_ = numOfDays
        self.__salesDict_ = salesDict
        
    #methods to get the number of days and the sales dictionary
    def getNumOfDays(self):
        return self.__numOfDays_
    def getSalesDict(self):
        return self.__salesDict_