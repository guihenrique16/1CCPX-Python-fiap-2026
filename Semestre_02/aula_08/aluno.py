from disciplina import Disciplina

class Aluno:
    def __init__(self, nome, rm, curso ):
        self.nome = nome
        self.nome = rm
        self.nome = curso
        self.disciplinas = []
        self.notas_por_disciplinas = {}
        
    def matricular(self, disciplina: Disciplina):
        self.disciplinas.append(disciplina)
        self.notas_por_disciplinas.setdefault(disciplina.nome, [])

    def adicionarNota(self, disciplina: Disciplina, nota: float):
        self.notas_por_disciplinas[disciplina.nome].append(nota)

    def calcular_media(self, d: Disciplina) -> float:
        notas = self.notas_por_disciplinas.get(d.nome, [])
        return sum(notas) / len(notas)
        