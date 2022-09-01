from assets.plugin.common.base import *

def idtotoken():

    rpc("Idtotoken")
    clear()
    idtoken_banner()
    userid = input(f"{y}[{b}#{y}]{w}Entrez le user id:\n>>> ")
    encodedBytes = b64encode(userid.encode("utf-8"))
    encodedStr =str(encodedBytes ,"utf-8")
    clear()
    idtoken_banner()
    input(f'\n{y}[{b}LOGS{y}]{w}Première partie du token: {encodedStr}.*******.**************\n{y}[{b}#{y}]{w}Appuyez sur entrée pour quitter...')
    
