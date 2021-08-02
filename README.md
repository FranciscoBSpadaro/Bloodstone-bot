# Bloodstone-bot
bot de cura em python para bloodstone
usar sandboxie classic https://sandboxie-plus.com/downloads/
cura vida com bandagens , cura vida com potion , cura mana , renova buff de corrida , troca mana ring , é possivel criar novos buffs.
bot inicia fora do protection zone.

#### requerimentos
- Python 3.7
- libs : pip install numpy==1.18 , pip install opencv-python  or just pip install opencv-python==3.4.10.37  que ja instala numpy 1.18  , pip install pywin32 , pip install pyautogui
- abrir pasta do bot e com botao direito abrir com powershell e executar :  python  main.py

##### Configurando as hotkeys
##### Arquivo autoblood:
-   def __init__(self, hk_vel, hk_mana_ring, hk_cura, hk_cura_media, hk_vida_pot, hk_mana_pot, hk_food, hk_troca_ring, loc_top_status, loc_bot_status):
##### Arquivo main.py :
- iniciar = AutoHealer("f5", "0", "f1", "f2", "f3", "f4", "0", "0", [230,118], [374,181])

- a ordem dos indices do inicio da função exemplo hk_vel está no
