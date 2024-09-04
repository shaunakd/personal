from LemonadeStand import LemonadeStand
from MenuItem import MenuItem

class LemonadeStandTester:
    
    def test(self):
                
        stand = LemonadeStand('Lemons R Us') # Create a new LemonadeStand called 'Lemons R Us'
        item1 = MenuItem('lemonade', 0.5, 1.5) # Create lemonade as a menu item (wholesale cost 50 cents,
        stand.addMenuItem(item1) # Add lemonade to the menu for 'Lemons R Us'
        item2 = MenuItem('nori', 0.6, 0.8) # Create nori as a menu item (wholesale cost 60 cents, selling I
        stand.addMenuItem(item2) # Add nori to the menu for "Lemons R Us'
        item3 = MenuItem('cookie', 0.2, 1) # Create cookie as a menu item (wholesale cost 20 cents, selling
        stand.addMenuItem(item3)
        # Add cookie to the menu for "Lemons R Us'
        # This dictionary records that on day zero, 5 lemonades were sold, 2 cookies were sold, and no nori
        day_0_sales = {'lemonade': 5,'cookie': 2}
        stand.enterSalesForToday(day_0_sales) # Record the sales for day zero
        print(f"Lemonade profit: {stand.totalProfitForMenuItem('lemonade')}")
        print(f"Nori profit: {stand.totalProfitForMenuItem('nori')}")
        print(f"Cookie profit: {stand.totalProfitForMenuItem('cookie')}")
        print(f"Total profit: {stand.totalProfitForStand()}")
        # print the total profit

LemonadeStandTester().test()