# Bloodstone-bot
bot de cura em python para bloodstone
usar sandboxie classic https://sandboxie-plus.com/downloads/
cura vida com bandagens , cura vida com potion , cura mana , renova buff de corrida , troca mana ring , é possivel criar novos buffs.
bot inicia fora do protection zone.

#### requerimentos
- Python 3.7
- libs : pip install numpy==1.18 , pip install opencv-python , pip install pywin32 , pip install pyautogui
- abrir pasta do bot e com botao direito abrir com powershell e executar :  python  main.py

##### Configurando as hotkeys
##### Arquivo autoblood:
-   def __init__(self, hk_vel, hk_mana_ring, hk_cura, hk_cura_media, hk_vida_pot, hk_mana_pot, hk_food, hk_troca_ring, loc_top_status, loc_bot_status):
##### Arquivo main.py :
- iniciar = AutoHealer("f5", "0", "f1", "f2", "f3", "f4", "0", "0", [230,118], [374,181])

- a ordem dos indices do inicio da função exemplo hk_vel está no indice 0 e no indice 0 do AutoHealer do arquivo main.py está a tecla ' f5 ' então o buff de velocidade está na tecla f5 isso pode alterar avontade .
os paramentros [230,118], [374,181]) é as cordenadas da barras de hp e icones de buff , para descobrir a cordenada de acordo com a resolução do monitor tirar print com o jogo aberto e colar no paint . e com o cursor verificar onde é as cordenadas , 

- no arquivo autoblood.py  a linha 46
self.wincap = WindowCapture('[#] BloodStone - The Ancient Curse [v1.25] [#]')
é o nome da versao do cliente com a janela do jogo aberto. o [#] é quando o jogo está rodando pelo sandbox

Essas configurações recentes estão nos arquivos da pasta do barbaro ' barb ' 
no arquivo autoblood.py da pasta barb cheguei a importar essa lib  import pydirectinput que é uma opção ao pyautogui mas não é necessario no bloodstone , essa lib usa as mesmas funcões do pyautogui porem funciona em jogos que o pyautogui nao funciona . mas no bloodstone os 2 so funciona dentro do sandbox
