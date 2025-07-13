from JadenMamea_20250936_MC_Full_Stack_Python_Assessement_One import Shop

#Unit testing done using Pytest
#7 tests -> 7 passed

def test_add_item():
    cart1 = Shop()
    cart1.add_item("running shoes")
    cart1.add_item("mouthguard",2)
    assert cart1._basket["running shoes"]["quantity"]==1
    assert cart1._basket["running shoes"]["price"]==120
    assert cart1._basket["mouthguard"]["quantity"]==2
    assert cart1._basket["mouthguard"]["price"]==15

def test_remove_item():
    cart2 = Shop()
    cart2.add_item("football",3)
    assert cart2._basket["football"]["quantity"]==3
    cart2.remove_item("football")
    assert cart2._basket["football"]["quantity"]==2

def test_check_item_count():
    cart1 = Shop()
    cart1.add_item("running shoes")
    cart1.add_item("mouthguard",2)
    assert cart1.check_item_count() == 3

def test_check_total():
    cart1 = Shop()
    cart1.add_item("running shoes")
    cart1.add_item("mouthguard",2)
    assert cart1.check_total() == 150

def test_discount_not_applied_price():
    cart1 = Shop()
    cart1.add_item("running shoes")    #120
    cart1.add_item("mouthguard",2)     #2 x 15
    total = cart1.pay()
    assert total == 150 #No Discount applied (120 + (2 x 15)))

def test_discount_not_applied_quantity():
    cart3 = Shop()
    cart3.add_item("kayak")            #300
    cart3.add_item("water bottle",3)   #3 x 20
    total = cart3.pay()
    assert total == 360 #No Discount applied (300 + (3 x 20))

def test_discount_applied():
    cart4 = Shop()
    cart4.add_item("boxing gloves")    #65
    cart4.add_item("gym bag",2)        #2 x 45
    cart4.add_item("water bottle")      #20
    cart4.add_item("dumbbell")         #30
    total = cart4.pay()
    assert total == 155 #Discount applied (65 + (2 x 45) + 20 + 30 - 50)
