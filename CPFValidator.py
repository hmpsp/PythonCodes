import re

entrada = input('Digite seu CPF: ')
cpf = re.sub(
    r'[^0-9]',
    '',
    entrada
)

nove_digitos = cpf[:9]
multiplicador_1 = 10
resultado_1 = 0
resultado_2 = 0

for digito_1 in nove_digitos:
    resultado_1 += int(digito_1) * multiplicador_1
    multiplicador_1 -=1

digito_1 = (resultado_1 * 10) % 11    
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
multiplicador_2 = 11

for digito_2 in dez_digitos:
    resultado_2 += int(digito_2) * multiplicador_2
    multiplicador_2 -=1
    
digito_2 = (resultado_2 * 10) % 11    
digito_2 = digito_2 if digito_2 <= 9 else 0

novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'

if cpf == novo_cpf:
    print(f'o CPF {novo_cpf} é válido')
else:
    print('CPF inválido')    
