a = float(input("Podaj pierwsa liczbe: "))
operator = input("Podaj dzialanie (+, -, ", /): ")
b = float(input("Podaj druga liczbe: "))

if operator == "+";
wynik = a + b
elif operator == "-":
wynik  = a - b
elif operator == "*":
wynik = a * b
elif operator == "/":
if b !=0:
wynik = a/ b
else:
wynik = "Blad: dzielenie przez zero!"
else:
wynik = "Blad: nieznany operator!"
print("Wynik:", wynik)
