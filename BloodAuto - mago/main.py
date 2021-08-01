import cv2 as cv
import numpy as np
import os
import pyautogui
import time
from windowcapture import WindowCapture
from vision import Vision
from autoblood import AutoHealer

pyautogui.FAILSAFE = False

print('Iniciando em 3s...')
time.sleep(3)
iniciar = AutoHealer("f5", "0", "f2", "f3", "f4", "", "f1", "1", [230,118], [374,181])
while 1:
    pz = iniciar.batalha()
    if pz == 1 :
        iniciar.cura_vida()
        iniciar.cura_vida_media()
        iniciar.cura_vida_pot()
        iniciar.curar_mana_pot()
        iniciar.cura_mana_ring()
        iniciar.usar_vel()
        #iniciar.usar_food()
        #iniciar.usar_arm()
        #iniciar.usar_ferro()