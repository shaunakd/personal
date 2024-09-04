class MenuItem:
    
    #constructor
    def __init__(self, itemName, wholesaleCost, sellingPrice) -> None:
        self.__itemName_ = itemName
        self.__wholesaleCost_ = wholesaleCost
        self.__sellingPrice_ = sellingPrice
    
    #methods to get the item name, wholesale cost and selling price
    def getItemName(self):
        return self.__itemName_
    def getWholesaleCost(self):
        return self.__wholesaleCost_
    def getSellingPrice(self):
        return self.__sellingPrice_