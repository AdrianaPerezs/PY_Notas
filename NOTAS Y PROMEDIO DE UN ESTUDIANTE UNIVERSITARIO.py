letras_a_numeros = {'A': 91, 'B': 81, 'C': 71, 'D': 61, 'F': 60}
def calcular_promedio(notas):
    total_puntos = sum(letras_a_numeros[nota] for nota in notas)
    promedio = total_puntos / len(notas)
    return promedio
num_notas = int(input("Ingrese la cantidad de notas parciales: "))
notas = []

for i in range(num_notas):
    nota = input(f"Ingrese la nota {i + 1} (A, B, C, D, F): ").upper()
    if nota in letras_a_numeros:
        notas.append(nota)

if 0 <= num_notas <= 100:
    promedio = calcular_promedio(notas)
    print("sus notas son:", notas)
    print("su promedio es:", promedio)

