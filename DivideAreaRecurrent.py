# Oblicza dlugosc boku kwadratu jakimi mozna wypelnic dana figure
def divide_area(short, long):
    print(f"{long} x {short}")
    if long % short == 0:
        return short
    else:
        newShort = long % short
        long = short
        short = newShort
        return divide_area(short, long)

shortL = 120
longL = 2460
divL = divide_area(shortL, longL)
print (divL)
sDiv = shortL / divL
lDiv = longL / divL
count = int(sDiv * lDiv)
print(f"{count} kwadratow o wymiarze {divL} x {divL}")