# Даны два строковых представления чисел A и B. Нужно максимизировать A, заменив в нём любую
# цифру на цифру из B. Каждую цифру B можно использовать только один раз.

A = "12345"
B = "43536"

dA = [int(i) for i in A]
dB = [int(i) for i in B]
sort_dB = sorted(dB, reverse = True)

for i in range (len(A)):
    if sort_dB[i]> dA[i]:
        dA[i]=sort_dB[i]
    
print(dA)

print(sort_dB)
print(dA)
print(dB)