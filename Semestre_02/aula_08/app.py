from aluno import Aluno
from disciplina import Disciplina


aluno01 = Aluno("Joao", "123456", "ccp")

dsa = Disciplina("Data Structures", "alvaro")
model_linear = Disciplina("Modelagem Linear", "Rodolfo")

aluno01.matricular(dsa)
aluno01.matricular(model_linear)
print(aluno01.disciplinas[1].nome)

aluno01.adicionarNota(dsa, 10)
aluno01.adicionarNota(dsa, 8.5)
aluno01.adicionarNota(model_linear, 10)
aluno01.adicionarNota(model_linear, 9.5)
print(aluno01.notas_por_disciplinas)

print(aluno01.calcular_media(dsa))
print(aluno01.calcular_media(model_linear))






