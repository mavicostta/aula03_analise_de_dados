print("CÁLCULO")
nome=input("Nome: ")
salario_bruto=float(input("Salário bruto: ").replace(".",","))
if(salario_bruto >= 3000):
    desconto = salario_bruto*0.11
elif(salario_bruto >= 2000):
    desconto = salario_bruto*0.09
else:
    desconto = salario_bruto*0.08

if(salario_bruto >= 2000):
    descontovt = salario_bruto*0.06
else:
    descontovt = salario_bruto*0.05

if(salario_bruto >= 3000):
    plus =  300
else:
    plus = 200

if(salario_bruto >= 3000):
   cargo =  "ACIONSTA"
elif(salario_bruto >= 2000):
    cargo =  "GERENTE"
else:
    cargo = "VENDEDOR"


vale_transporte = salario_bruto - descontovt
salario_liquido = salario_bruto - desconto - descontovt + plus
plus0 = salario_bruto + plus
print(f"Nome: {nome}")
print(f"Cargo: {cargo}")
print(f"INSS: R$ {desconto:.2f}".replace(".",","))
print(f"Vale transporte: R$ {descontovt:.2f}".replace(".",","))
print(f"Bônus: R$ {plus}".replace(".",","))
print(f"Salário líquido: R$ {salario_liquido:.2f}".replace(".",","))


