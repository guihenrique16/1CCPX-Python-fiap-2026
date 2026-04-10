import pygame
import time

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load('seu_arquivo.mp3')

# Reproduz o arquivo
pygame.mixer.music.play()

# Mantém o script rodando enquanto a música toca
while pygame.mixer.music.get_busy():
    time.sleep(1)

