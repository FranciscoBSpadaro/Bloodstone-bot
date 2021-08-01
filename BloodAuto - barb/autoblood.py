import cv2 as cv
import numpy as np
import os
import pyautogui
import pydirectinput
import time
from windowcapture import WindowCapture
from vision import Vision

class AutoHealer:
    # properties
    hk_vel = ""
    hk_mana_ring = ""
    hk_cura = ""
    hk_mana_pot = ""
    hk_vida_pot = ""
    hk_food = ""
    hk_cura_media = ""
    loc_top_status = []
    loc_bot_status = []
    # constructor
    #("8", "f4", "f3", "1", "7", "5", "f8", [230,118], [355,156])
    def __init__(self, hk_vel, hk_mana_ring, hk_cura, hk_cura_media, hk_vida_pot, hk_mana_pot, hk_food, hk_troca_ring, loc_top_status, loc_bot_status):
        #imagens
        self.pz = Vision('pz.jpg')
        self.food = Vision('food_blood.jpg')
        self.vida = Vision('hp.jpg')
        self.vel = Vision('vel.jpg')
        #hotkeys
        self.hk_vel = hk_vel
        self.hk_cura = hk_cura
        self.hk_vida_pot = hk_vida_pot
        self.hk_mana_pot = hk_mana_pot
        self.hk_mana_ring = hk_mana_ring
        self.hk_troca_ring = hk_troca_ring
        self.hk_food = hk_food
        self.hk_cura_media = hk_cura_media
        self.loc_top_status = loc_top_status
        self.loc_bot_status = loc_bot_status
        #localização barra de status
        self.y_1 = self.loc_top_status[1]
        self.y_2 = self.loc_bot_status[1]
        self.x_1 = self.loc_top_status[0]
        self.x_2 = self.loc_bot_status[0]
        #pegar tela
        self.wincap = WindowCapture('[#] BloodStone - The Ancient Curse [v1.25] [#]')
        #tirar print
        self.screenshot = self.wincap.get_screenshot()
        #debugar o print
        loc_vida = self.vida.findLoc(self.screenshot, 0.99)
        if loc_vida[0]!=-1:
            #print(loc_vida[0]+90, loc_vida[1],(r,g,b))
            self.loc_vida = [loc_vida[0]+11 , loc_vida[1]+4]
            self.loc_mana = [loc_vida[0]+11, loc_vida[1]+21]
            #self.loc_status_ = loc_status
        else:
            print('Erro: Não achou as barras de status')

    def cura_vida(self):
        self.screenshot = self.wincap.get_screenshot()
        #curar vida
        b, g, r = self.screenshot[self.loc_vida[1], self.loc_vida[0]+111]
        #print(r, g, b, self.loc_vida[0], self.loc_vida[1])

        if r > 160 and r < 200:
            print('vida cheia')
        else:
            print('curar vida')
            #pydirectinput.press(self.hk_cura)
            #pydirectinput.keyUp(self.hk_cura)
            pyautogui.keyDown(self.hk_cura)
            pyautogui.keyUp(self.hk_cura)


    def cura_vida_media(self):
        self.screenshot = self.wincap.get_screenshot()
        #curar vida
        b, g, r = self.screenshot[self.loc_vida[1], self.loc_vida[0]+99]
        #print(r, g, b, self.loc_vida[0], self.loc_vida[1])

        if r > 160 and r < 200:
            print('vida cheia')
        else:
            print('curar vida')
            pyautogui.keyDown(self.hk_cura_media)
            pyautogui.keyUp(self.hk_cura_media)



    def cura_vida_pot(self):
        self.screenshot = self.wincap.get_screenshot()
        #curar vida
        b, g, r = self.screenshot[self.loc_vida[1], self.loc_vida[0]+62]
        #print(r, g, b, self.loc_vida[0], self.loc_vida[1])

        if r > 160 and r < 200:
            print('vida cheia')
        else:
            print('curar vida')
            pyautogui.keyDown(self.hk_vida_pot)
            pyautogui.keyUp(self.hk_vida_pot)

    def curar_mana_pot(self):
        self.screenshot = self.wincap.get_screenshot()
        #A barra de mana tem 116px, são 11,6px para cada 10% de mana
        b, g, r = self.screenshot[self.loc_mana[1], self.loc_mana[0]+59]
        #print(self.loc_mana[0]+58, self.loc_mana[1])
        #print(r, g, b)
        if r != 0 and g != 93:
            print('usar mana')
            pyautogui.keyDown(self.hk_mana_pot)
            pyautogui.keyUp(self.hk_mana_pot)

    def cura_mana_ring(self):
        self.screenshot = self.wincap.get_screenshot()
        #curar vida
        b, g, r = self.screenshot[self.loc_vida[1], self.loc_vida[0]+60]
        #print(r, g, b, self.loc_vida[0], self.loc_vida[1])

        if r > 160 and r < 200:
            print('vida cheia trocar ring')
            #pyautogui.keyDown(self.hk_troca_ring)
            #pyautogui.keyUp(self.hk_troca_ring)
        else:
            print('usar ring')
            pyautogui.keyDown(self.hk_mana_ring)
            pyautogui.keyUp(self.hk_mana_ring)
 

    '''def usar_food(self):
        self.screenshot = self.wincap.get_screenshot()
        area_status = self.screenshot[self.y_1:self.y_2, self.x_1:self.x_2]
        loc_food = self.food.find(area_status, 0.8)
        if loc_food == 1:
            print('usar food')
            pyautogui.keyDown(self.hk_food)
            pyautogui.keyUp(self.hk_food) '''

    def usar_vel(self):
        self.screenshot = self.wincap.get_screenshot()
        area_status = self.screenshot[self.y_1:self.y_2, self.x_1:self.x_2]
        loc_arm = self.vel.find(area_status, 0.8)
        if loc_arm == 1:
            print('usar velocidade')
            pyautogui.keyDown(self.hk_vel)
            pyautogui.keyUp(self.hk_vel)

    '''def batalha(self):
        self.screenshot = self.wincap.get_screenshot()
        area_status = self.screenshot[self.y_1:self.y_2, self.x_1:self.x_2]
        loc_bt = self.bt.find(area_status, 0.8)
        loc_btpvp = self.btpvp.find(area_status, 0.8)
        if loc_bt == 0 or loc_btpvp == 0 :
            print('Entrou em batalha')
            return 1 '''

    def batalha(self):
        self.screenshot = self.wincap.get_screenshot()
        area_status = self.screenshot[self.y_1:self.y_2, self.x_1:self.x_2]
        loc_pz = self.pz.find(area_status, 0.8)
        if loc_pz == 1 :
            print('saiu pz')
            return 1
