def reverse_list(liste):
    reverse_list = []
    boyut = len(liste)
    for i in range(0,boyut):
        reverse_list.append(liste[boyut-i-1][::-1])
    return reverse_list

liste = [[1, 2], [3, 4], [5, 6, 7]]
print(reverse_list(liste))