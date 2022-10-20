import time
import os
import board
import digitalio
import pygame
pygame.mixer.init()
pygame.mixer.music.load("halotheme_clip.wav")
pygame.mixer.music.play()

s1 = digitalio.DigitalInOut(board.D17)
s1.direction = digitalio.Direction.INPUT
s1.pull = digitalio.Pull.DOWN

isopen = s1.value


while True:
        #if (s1.value) == True:
        #       print("closed")
        #else:
        #        print("open")
        if (s1.value != isopen):
                isopen = s1.value
                if isopen == True:
                        print("closed")
                else:
                        print("open")
                       

        time.sleep(0.05)