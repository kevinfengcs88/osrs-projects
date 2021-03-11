barPrice = int(input("Enter the price of a bar: "))
dartTipPrice = int(input("Enter the price of a dart tip: "))

def calcMargins(price1, price2):
    return (dartTipPrice * 10) - barPrice

def calcHourly(price1, price2):
    return calcMargins(price1, price2) * 950
print("Gp margin per bar: " + str(calcMargins(barPrice, dartTipPrice)))
print("Gp/hr: " + str(calcHourly(barPrice, dartTipPrice)))
