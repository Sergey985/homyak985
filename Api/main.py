from Apishka import dnp_dev_details
from Apishka import dnp_dev_calculate
print("Print 1 for start dnp dev recalculation")
print("Print 2 for start dnp dev details")
print("Print 3 for exit")



val = input("Select method")
if val == 1:
    dnp_dev_calculate()
elif val == 2:
    dnp_dev_details()
elif val ==3:
    exit()
else:
    print("undefined param")

