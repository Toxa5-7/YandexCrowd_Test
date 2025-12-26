# Даны два строковых представления чисел A и B. Нужно максимизировать A, заменив в нём любую
# цифру на цифру из B. Каждую цифру B можно использовать только один раз.

A = "12355"
B = "36"

dA = [int(i) for i in A]
dB = [int(i) for i in B]
sort_dB = sorted(dB, reverse = True)

pos_b = 0
for i in range (len(A)):
    if pos_b < len(dB) and sort_dB[pos_b]> dA[i]:
        dA[i]=sort_dB[pos_b]
        pos_b+=1
    
print(dA)
