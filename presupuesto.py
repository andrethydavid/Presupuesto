# proyecto de presupuesto  de tres meses <codigo basico>

Enero = 10000
Febrero = 15000
Marzo = 12000

promedio= ((Enero + Febrero + Marzo)/3)
print(promedio)

# presupuesto de tres meses  con input  

x = input("Dime el primer gasto: ")
y = input("Dime el segundo gasto: ")
z = input("Dime el tercer gasto: ")

promedio = round(((int(x) + int(y) + int(z)) / 3),2)
print(f'El promedio de gastos es: {promedio}') #se usa la funcion "f" para imprimir el resultado de la variable

#proyecto de presupuesto de tres neses 

budget_january = int(input("¿Cuál es tu presupuesto para enero?: "))
budget_february = int(input("¿Cuál es tu presupuesto para febrero?: "))
budget_march = int(input("¿Cuál es tu presupuesto para marzo?: "))

budget_total = [budget_january, budget_february, budget_march]
print("La suma total de los presupuestos es: ", sum(budget_total))

avg_budget = sum(budget_total)/len(budget_total)
print("El promedio es: ", avg_budget)