from pygame import *
from PyQt6.QtWidgets import QFileDialog, QWidget, QApplication

# Test
file_app = QApplication([])
file_win = QWidget()

W, H = 600, 400
sc = display.set_mode((W, H))
display.set_caption("Моя первая программа на PyGame")
display.set_icon(image.load("/Users/andreyshumkov/Desktop/Новая папка/1446659200_1.jpeg"))

clock = time.Clock()
FPS = 60

draw.rect(sc, (255, 255, 255), (10, 10, 50, 100))
display.flip()

isRunning = True
while isRunning:
    for e in event.get():
        if e.type == QUIT:
            exit()

    clock.tick(FPS)


    # erettert

