print("_______________________________________________________")
print("      \    /\    /   __  |    ___  ___  |\    /|   __  ")
print("       \  /  \  /   |__  |   |     |  | | \  / |  |__  ")
print("        \/    \/    |__  |__ |___  |__| |  \/  |  |__  ")
print("_______________________________________________________")

def strw():
    idr = float(input("....1) Find Avg\n....2) Find Qty\n\n....Enter no.:- "))
    if idr == float(1):
        data()

    if idr == float(2):
        data2()


def data():
    bpr = float(input("....Enter buy price: "))
    bq = float(input("....Enter qty Buy: "))
    abpr = float(input("....Enter 2nd Buy price: "))
    abq = float(input("....Enter 2nd Buy qty: "))
    so = int(input("....1)if All Data is Correct:\n....2)rest Data:\n....Enter no.- "))
    if so == int(1):
        for1(bpr, bq, abpr, abq)
    else:
        data()

def for1(x, y, z, a):
    ap = ((x*y)+(z*a))/(y+a)
    fu = z * ap
    print("....Avg price is:- ", ap)
    print("....Fund Used: ", fu)
    a = float(input("....1) exit:\n....2) reset:\n....:- "))
    exre(a)

def data2():
    bpr = float(input("....Enter buy price: "))
    bq = float(input("....Enter qty Buy: "))
    abpr = float(input("....Enter 2nd Buy price: "))
    ap = float(input("....Enter Avg price : "))
    so = float(input("....1)if All Data is Correct:\n....2)rest Data:\n....Enter no.- "))
    if so == float(1):
        for2(bpr, bq, abpr, ap)
    else:
        data2()

def for2(x, y, z , a):
    abq = ((a*y)-(x*y))/(z-a)
    fu = z * abq
    print("....qty is:- ", abq)
    print("....Fund Used:- ", fu)
    a = float(input("....1) exit:\n....2) reset:\n....:- "))
    exre(a)

def exre(x):
    if x == float(1):
        exit()
    else:
        strw()

strw()