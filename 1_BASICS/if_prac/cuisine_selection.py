fast_food = ["burger", "shawarma", "makroni"]
vegeterian = ["daalmash","saag","handi"]
desi = ["makan rooti","malai ","lassi"]

dish = input("enter  you dish name :")
if dish in fast_food:
    print("your dish is fast_food")
elif dish in vegeterian:
    print("your dish is vegeterian")
elif dish in desi:
    print("your dish is desi")
else:
    print("Sorry we dont know about your dish type !")

