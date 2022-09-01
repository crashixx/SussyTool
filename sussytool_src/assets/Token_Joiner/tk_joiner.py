from assets.plugin.common.base import *

def tk_joiner():
    rpc("Token Joiner")
    clear()
    tjoiner_banner()
    link = input(f"{y}[{b}#{y}]{w}Entre l'invitation du serveur:\n>>>")

    if os.path.exists(f"{getcwd()}\\tokens.txt") == False:
        with open('tokens.txt','w') as f:
            f.write("")
            f.close

    clear()
    tjoiner_banner()
    input(f"{y}[{b}#{y}]{w}Insère les tokens que tu veux faire rejoindre dans le fichier puis appuie sur entrée:\n{y}[{b}>{y}]{w}Fichier:{getcwd()}/tokens.txt")

    if len(link) > 6:
        link = link[19:]

    with open(f'{getcwd()}\\tokens.txt','r') as file:
            tokens = file.readlines()
            file.close
            clear()
            tjoiner_banner()
            if tokens == "":
                input(f"{y}[{b}#{y}]{w}Veuillez insérer les tokens dans le bon fichier et réessayer...\n{y}[{b}>{y}]{w}Fichier:{getcwd()}/tokens.txt")
                tk_joiner()
            for x in tokens:
                token = x.rstrip()
                headers={'Authorization': token}
                post(f"https://discordapp.com/api/v6/invite/{str(link)}", headers=headers)
                input(f"{y}[{b}LOG{y}]{w} A rejoint le serveur: {x}")
            clear()
            tjoiner_banner()    
            input(f"{y}[{b}#{y}]{w}Tous les tokens ont rejoint !")
            remove(f"{getcwd()}\\tokens.txt")