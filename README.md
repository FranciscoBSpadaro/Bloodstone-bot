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
-   def __init__(self, hk_vel, hk_mana_ring, hk_cura, hk_cura_media, hk_vida_pot, hk_mana_pot, hk_food, hk_troca_ring, hk_prlz, loc_top_status, loc_bot_status):
##### Arquivo main.py :
- iniciar = AutoHealer("f5", "f7", "f1", "f2", "f3", "f4", "0", "0", "f6", [230,118], [374,181])

- a ordem dos indices do inicio da função autoblood def_init exemplo hk_vel está no f5 do AutoHealer

[230,118], [374,181])  é a cordenada dos pixel da barras de hp 

![alt text](https://fbsdevuploads.s3.amazonaws.com/botpixelcfg.png)

230,118 é ponto azul e o  374,181 é o ponto vermelho  em uma resoluçao  1920 x 1080

191 ,100 é ponto azul e o  312 , 153 é o ponto vermelho em uma resoluçao  1600 x 900

163,85  é ponto azul e o  265,129  é o ponto vermelho em uma resoluçao  1360 x 768

#### a pasta BloodAuto - barb está atualizada e com cura paralize as outras pastas estão desatualizadas
- f1 cura curativo
- f2 cura media 
- f3 cura potion hp
- f4 cura mana potion
- f5 auto magia de velocidade
- f6 cura paralisia
- f7 anel barreira de mana
- para habilitar ou desabilitar uma funçao basta deixar o ' #  '  na frente do codigo no arquivo  main.py
