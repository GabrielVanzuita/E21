
array = [10, -3, 5, 0, 5, -8, 2, 10, -1, 7]

def merge_sort(array):                  #Recebe como parâmetro um array
    if len(array) <= 1:                 #Se o tamanho do array for menor ou igual a 1:
        return array                    #Retorna o array

    mid = len(array) // 2               #Define o meio como o número de objetos do array divido por dois
    left = merge_sort(array[:mid])      #Define left como tudo antes do elemento central (mid)
    right = merge_sort(array[mid:])     #Define right como tudo depois do elemento central (right)

    return merge(left, right)           #(Retorna a função merge com os parâmetros dos arrays da esquerda e da direita

def merge(left, right):
    result = []
    i = j = 0
    # Combina os dois arrays ordenados (merge)
    while i < len(left) and j < len(right): #Enquanto ainda houver elementos não comparados em ambos os arrays left e right

        if left[i] <= right[j]:             # Se o elemento atual do array esquerdo for menor ou igual ao do direito
            result.append(left[i])          # Adiciona esse elemento (do array esquerdo) ao array resultado

            i += 1                          # Avança o índice da esquerda para o próximo elemento

        else:
            result.append(right[j])         # Adiciona o elemento do array direito ao resultado

            j += 1                          # Avança o índice da direita

    # Adiciona ao resultado qualquer elemento restante em left ou right
    result.extend(left[i:])
    # Adiciona todos os elementos restantes do lado esquerdo (se houver)
    result.extend(right[j:])
    # Adiciona todos os elementos restantes do lado direito (se houver)

    return result
    # Retorna o array resultante, agora completamente ordenado

sorted_array = merge_sort(array)

print("Original:", array)
print("Ordenado:", sorted_array)