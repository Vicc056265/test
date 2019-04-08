print("Podaj dowolna liczbe")
a = float(input())
print("Podaj jeszcze jedna liczbe")
b = float(input())

lista  = []

for i in range(10):
	lista.append(a+b)
print("lista 10 tych samych wynikow", lista)
