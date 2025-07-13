
class Shop:
    """
    --------------------------------------------BLACK FRIDAY CLOUDX SALE------------------------------------------------------

                            SPEND $200 or more on 5+ Items to unlock a $50 discount at checkout!

    --------------------------------------------------HOW TO SHOP-------------------------------------------------------------
        > add_item("Item name","Amount"(optional))        - Adds selected item(s) to basket

        > remove_item("Item name","Amount"(optional))     - Removes selected item(s) from basket

        > check_basket()                                  - Returns the contents of basket

        > check_item_count()                              - Returns number of items in basket

        > check_total()                                   - Returns total price of basket

        > pay()                                           - Pay for items in basket (discount applied automatically if eligible)

    ------------------------------------------------STORE INVENTORY------------------------------------------------------------

        > boxing gloves :    $65
        > football :         $50
        > running shoes:     $120
        > kayak :            $300
        > mouthguard :       $15
        > hocket stick :     $85      
        > dumbbell :         $30
        > water bottle :     $20
        > gym Bag :          $45
        > yoga mat :         $35
        > sweatband :        $12
        > skateboard :       $160  


    """
    def __init__(self):
        #Can add new items to inventory if needed
        self._store_inventory = {
            "boxing gloves":65,
            "football":50,
            "running shoes":120,
            "kayak":300,
            "mouthguard":15,
            "hockey stick":85,
            "dumbbell":30,
            "water bottle":20,
            "gym bag":45,
            "yoga mat":35,
            "sweatband":12,
            "skateboard":160
        }
        self._basket={} #format: {"item name": {"quantity": x, "price": y}}
    
    def add_item(self,item,amount=1):
        """
        ---------------Add an item to your basket---------------

        !!! item names are case-sensitive - use lowercase only !!!

        :param item: name of item you want to add - refer to store inventory
        :type item: string
        :param amount: quantity of item(s) you want to add (optional)
        :type amount: integer
        """
        if item not in self._store_inventory:
            print(f"{item} not found in store")
            return   
        _price = self._store_inventory[item]
        if item in self._basket:
            self._basket[item]["quantity"] += amount
        else:
            self._basket[item] = {"quantity": amount, "price":_price}
    

    def remove_item(self,item,amount=1):
        """
        --------------Remove item from your basket--------------

        :param item: name of item you want to remove from basket
        :type item: string
        :param amount: quantity of item(s) you want to remove (optional)
        :type amount: integer
        """
        if item in self._basket:
            self._basket[item]["quantity"] -= amount
            if self._basket[item]["quantity"] <= 0:
                del self._basket[item]
        else:
            print(f"{item} not found in basket")
    
    def check_basket(self):
        """
        Return contents and prices of your basket
        """
        if not self._basket:
            return "Your basket is empty"
        print("Basket contents:")
        basket_summary = ""
        for item, info in self._basket.items():
            basket_summary += f"{item.title()} x{info['quantity']} @ ${info['price']} each \n"
        return basket_summary.strip()

    
    def check_item_count(self):
        """
        Returns count of items in your basket
        """
        count = sum(item["quantity"] for item in self._basket.values())
        print(f"Number of items in your basket: {count} items")
        return count

    def check_total(self):
        """
        Returns total price of your basket before discount
        """
        total = sum(details["quantity"] * details["price"] for details in self._basket.values())
        print(f"Total price of basket: ${total}")
        return total
    
    def pay(self):
        """
        Pay for your basket - Discount automatically applied if eligible
        """
        total = self.check_total()
        count = self.check_item_count()
        if total >= 200 and count >= 5:
            total -= 50
            print("Discount Applied!")
        else:
            print("No Discount Appplied.")

        print(f"Youre total is: ${total}")
        self._basket.clear() #reset basket
        return total






    
