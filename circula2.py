import calculadora as c

churrasco = c.calculadora()  #churrasco é o objeto

#Entrada de dados
raio = float(input("Digite o valor do raio: "))

#Processamento de dados
circunferencia = churrasco.circunferencia(raio)
area = churrasco.area(raio)

#Saída de dados
print(f"""Circunferência: {circunferencia:.2f} 
      Area: {area}
      PI: {churrasco.PI}""")