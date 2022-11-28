print("Введите длину массива:")
l = int(input())
a = []
print("Введите элементы массива")
for i in range(0,l):   
    element = int(input())
    a.append(element)

print("Максимум массива:",min(a))