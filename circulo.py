PI = 3.14

#Entrada de dados
raio = float(input("Digite o valor do raio: ")) #raio da circunferência

#Processamento de dados
circurferencia = 2 * PI * raio
area = PI * raio**2 #area da circunferência

#Saída de dados
print(f"""Circunferência: {circurferencia:.2f} 
      Area: {area}
      PI: {PI}""")