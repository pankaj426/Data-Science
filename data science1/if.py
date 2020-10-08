indian = ["samosa", "daal", "panir"]
italian = ["pasta", "burger", "pizza"]
chinese = ["rool", "choaumene", "momos"]

dish = input("enter a dish ")

if dish in indian:
    print("indiam")
elif dish in italian:
    print("italian")
elif dish in chinese:
    print("chinese")
else:
    print("beyond mys rang", dish)