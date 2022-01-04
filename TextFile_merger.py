first=input("Enter the name of first file: ")+".txt"
second=input("Enter the name of second file: ")+".txt"
third=input("Enter the name of third file: ")+".txt"

with open(first) as f1:
    t1=f1.read()

with open(second) as f2:
    t2 = f2.read()

with open(third) as f3:
    f3.write(t1+"\n"+t2)
