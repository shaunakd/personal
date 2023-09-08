class MenuItem:
    
    #constructor
    def __init__(self, itemName, wholesaleCost, sellingPrice) -> None:
        self.__itemName_ = itemName
        self.__wholesaleCost_ = wholesaleCost
        self.__sellingPrice_ = sellingPrice
    
    #methods to get the item name, wholesale cost and selling price
    getItemName = lambda self: self.__itemName_
    getWholesaleCost = lambda self: self.__wholesaleCost_
    getSellingPrice = lambda self: self.__sellingPrice_