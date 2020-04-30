#Execise to training repetition structure (while)
#Cash machine simulator

money = int(input('How much money do you want to withdraw?'))
residual = money
v50 = v20 = v10 = v1 = 0

v50 = residual // 50
residual -= v50*50
v20 = residual // 20
residual -= v20*20
v10 = residual // 10
residual -= v10*10
v1 = residual // 1

print (f'{v50} notas de 50 / {v20} notas de 20 / {v10} notas de 10 / {v1} notas de 1')

#resolution using while
residual_while = money
v50 = v20 = v10 = v1 = 0

while residual_while >= 50:
    v50 += 1
    residual_while -= 50

while residual_while >= 20:
    v20 += 1
    residual_while -= 20

while residual_while >= 10:
    v10 += 1
    residual_while -= 10

while residual_while >= 1:
    v1 += 1
    residual_while -= 1

print(f'{v50} notas de 50 / {v20} notas de 20 / {v10} notas de 10 / {v1} notas de 1')

#resolution whith while and break

v = 50
rest = money
money_notes = 0
while True:
    if rest >= v:
        rest -= v
        money_notes += 1
    else:
        if money_notes > 0:
            print(f'{money_notes} money notes of {v}')
        if v == 50:
            v = 20
        elif v == 20:
            v = 10
        elif v == 10:
            v = 1
        else:
            break
        money_notes = 0
