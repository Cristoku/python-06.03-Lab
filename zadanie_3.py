import faker

print(pesel_num)

pesel = "19232448069" # lub input
pesel = [int(number) for number in pesel]
if pesel[2] == 4:
    print("błedny pesel")
year = pesel[0] * 10 + pesel[1]
month = pesel[2] * 10 + pesel[3]
if month < 20:
    year += 1900
else: # month > 20
    year += 2000
    month -= 20
day = pesel[4] * 10 + pesel[5]

print("Data urodzenia to", day, month, year)

gender = "kobieta" if pesel[9]%2==0 else "mezczyzna"
print("Plec to", gender)


from faker import Faker
fake = Faker()
for _ in range(5):
    print(fake.pesel())