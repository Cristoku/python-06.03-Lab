productList = input("Podaj listę produktów oddzielonych przecinkami: ")
productListUnique = productList.split(",")
productDict = dict()
for product in productListUnique:
    price = float(input("Podaj cenę produktu " + product + ": "))
    productDict[product] = price

print(productDict)