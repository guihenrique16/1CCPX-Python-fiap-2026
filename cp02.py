# Uma escola está testando um sistema simples de monitoramento ambiental para
# identificar salas com possível risco de calor excessivo.

# Você recebeu uma matriz em que cada linha representa uma sala e cada
# coluna representa a temperatura registrada em um horário diferente do dia.

temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

sala_mais_critica = 0
max_criticos = -1

for i in range(len(temperaturas)):
    sala = temperaturas[i]
    media = sum(sala) / len(sala)
    criticos = 0
    for t in sala:
        if t >=33:
            criticos+= 1

        print(f"Sala {i+1}")
        print(f"Media: {media}")
        print(f"Registros criticos: {criticos}")

        if criticos > max_criticos:
            max_criticos = criticos
            sala_mais_critica = i + 1

    print(f"Sala com maior quantidade de registros criticos: Sala {sala_mais_critica}")

