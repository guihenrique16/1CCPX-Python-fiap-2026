# Operadores de atribuiçao
from sqlalchemy.sql.operators import truediv

num = 15
print(num)

num = num +2
print(num)

num += 2
print(num)

# relacionais
print()
print(6 == 3)
print(6 != 3)

idade = 20
print(idade == 20)

maiorIdade = idade >= 18
print(maiorIdade)

# Logicos
print()

VerifiaEmail = True
VerifiaSena = False

login = VerifiaEmail and VerifiaSena
print(login)

if not login:
    print("Po ara aerta ai")


print()
nota_final = 4
if nota_final < 4:
    print("reproado")
elif nota_final < 6 :
    print("reuperaao")
else:
    print("Aproados")

print("FIM")
