import pyautogui
import time
from autoblood import AutoHealer

pyautogui.FAILSAFE = False

print('Iniciando em 3s...')
time.sleep(3)
iniciar = AutoHealer("f5", "f7", "f1", "f2", "f3", "f4", "", "", "f6", [230,118], [374,181])
while 1:
    pz = iniciar.batalha()
    if pz == 1 :
        iniciar.cura_vida()
        #iniciar.cura_vida_media()
        iniciar.cura_vida_pot()
        iniciar.curar_mana_pot()
        #iniciar.cura_mana_ring()
        iniciar.usar_vel()
        iniciar.usar_prlz()
        #iniciar.usar_food()
        #iniciar.usar_arm()
        #iniciar.usar_ferro()
