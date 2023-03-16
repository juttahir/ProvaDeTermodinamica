import matplotlib.pyplot as plt
import numpy as np

V = float(input("Digite a velocidade do vento em km/h: "))
H = float(input("Digite a altura da estação eólica em metros: "))

V = V /3.6

# Cálculo da energia do vento
E = 0.5 * V**2 + (H*9.8)

# Cálculo da energia por unidade de massa
m = 1 # kg
E_m = float(E / m)

print('\nConsiderando a pergunta, determine a energia do vento:'
      '\nA. por unidade de massa')
print("A energia por unidade de massa é de {:.2f} J/kg".format(E_m))

energia_massa = []
energia_fluxo = []
i=0
while True:
    massa = float(input('\nDigite uma massa de ar: '))

    energia_massa.append(float(round(E_m * massa)))

    print('A energia para essa massa é: ', energia_massa)

    i += 1

    if input('Deseja terminar a questão?S/N: ').upper() == 'S':
        break

# Massas a serem plotadas
massas = [10, 30, 70, 135, 1230]

# Energias correspondentes
energias = [E_m * m for m in massas]

# Gráfico da energia em relação à massa
plt.subplot(2, 1, 1)
plt.plot(massas, energias, 'bo-')
plt.xlabel('Massa (kg)')
plt.ylabel('Energia (J)')

# Energias específicas correspondentes
energias_especificas = [E_m for m in massas]

# Gráfico da energia específica em relação à massa
plt.subplot(2, 1, 2)
plt.plot(massas, energias_especificas, 'ro-')
plt.xlabel('Massa (kg)')
plt.ylabel('Energia específica (J/kg)')

plt.show()