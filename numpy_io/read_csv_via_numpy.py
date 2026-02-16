import numpy as np

x = np.loadtxt("data.csv", delimiter = ",",skiprows= 1)



print("---------------Year wise data-------------------")

for item in x:
    print(f"{item[0]}'s Data")
    print(f"Mean  was {np.mean(item[1:])}")
    print(f"Max was {np.max(item[1:])}")
    print(f"Min was {np.min(item[1:])}")



print("--------------Month wise data ------------------")

months = ["Jan", "Feb","March", "April", "May","June","July","Aug","Sep","Oct","Nov","Dec"]
count = 0
for item in x.T[1:]:
    print(f"{months[count]}'s data")
    count +=1 
    print(f"Mean  was {np.mean(item[1:])}")
    print(f"Max was {np.max(item[1:])}")
    print(f"Min was {np.min(item[1:])}")
    print()
    print()

