=int(input("Pickup Location:"))
y=int(input("Drop Location:"))
print("1: 'micro', 2: 'mini', 3: 'auto'")
z=int(input("mode:"))
rate=""
if(z==1):
    rate=(y-x)*3
    print(rate)
if(z==2):
    rate=(y-x)*5
    print(rate)
if(z==3):
    rate=(y-x)*2
    print(rate)
