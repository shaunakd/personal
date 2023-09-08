class SalesForDay:
    
    #constructor
    def __init__(self, numOfDays: int, salesDict: dict[str, float]) -> None:
        self.__numOfDays_ = numOfDays
        self.__salesDict_ = salesDict
        
    #methods to get the number of days and the sales dictionary
    getNumOfDays = lambda self: self.__numOfDays_
    getSalesDict = lambda self: self.__salesDict_