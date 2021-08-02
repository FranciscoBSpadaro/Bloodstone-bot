# Bloodstone-bot
bot de cura em python para bloodstone
usar sandboxie classic https://sandboxie-plus.com/downloads/
cura vida com bandagens , cura vida com potion , cura mana , renova buff de corrida , troca mana ring , é possivel criar novos buffs.
bot inicia fora do protection zone.

#### requerimentos
- Python 3.7   https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe
- libs : pip install numpy==1.18 , pip install opencv-python  or just pip install opencv-python==3.4.10.37  que é compativel com numpy 1.18  , pip install pywin32 , pip install pyautogui
- abrir pasta do bot e com botao direito abrir com powershell e executar :  python  main.py

##### Configurando as hotkeys
##### Arquivo autoblood:
-   def __init__(self, hk_vel, hk_mana_ring, hk_cura, hk_cura_media, hk_vida_pot, hk_mana_pot, hk_food, hk_troca_ring, loc_top_status, loc_bot_status):
##### Arquivo main.py :
- iniciar = AutoHealer("f5", "0", "f1", "f2", "f3", "f4", "0", "0", [230,118], [374,181])

- a ordem dos indices do inicio da função exemplo hk_vel está no

[230,118], [374,181])  é a cordenada dos pixel da barras de hp 

![alt text]()

230,118 é ponto azul e o  374,181 é o vermelho  da resoluçao  1920 x 1080
