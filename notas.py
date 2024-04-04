#IF

idade = int(input('Digite sua idade: '))

if idade > 18:
    print('Você já é maior de idade')
else:
    print('Pode Voltar pra casa')

#exemplo de if e elif

altura = float(input('Digite a sua altura: '))
if altura > 3:
    print('Você não pode andar no brinquedo')

elif altura < 1.2:
    print('Você não pode andar no brinquedo')

else:
    print('Divirta-se :)')