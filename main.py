def recursive_max_min(arr, low, high):
    # Caso base: se houver apenas um elemento
    if low == high:
        return arr[low], arr[low]
    # Caso base: se houver dois elementos
    elif high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    else:
        # Dividir o array em duas partes
        mid = (low + high) // 2
        min1, max1 = recursive_max_min(arr, low, mid)
        min2, max2 = recursive_max_min(arr, mid + 1, high)
        # Combinar os resultados
        return min(min1, min2), max(max1, max2)


def max_min_select(arr):
    if not arr:
        return None, None
    return recursive_max_min(arr, 0, len(arr) - 1)


def obter_numeros_do_usuario():
    while True:
        try:
            quantidade = int(input("Digite a quantidade de números na lista: "))
            if quantidade <= 0:
                print("Por favor, insira um número válido.")
                continue
            
            numeros = []
            
            for i in range(quantidade):
                try:
                    numero = float(input(f"Digite o número {i + 1}: "))
                    numeros.append(numero)
                    
                except ValueError:
                    print("Entrada inválida")
            return numeros
        
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

if __name__ == "__main__":
    elementos = obter_numeros_do_usuario()
    # elementos = [378, 5451, 4, 1, 5, 95, 2, 66799, 5, 3, -5]  
    menor, maior = max_min_select(elementos)
    print(f"Menor elemento: {menor}, Maior elemento: {maior}")
