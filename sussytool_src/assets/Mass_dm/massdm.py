from assets.plugin.common.base import *

def massdm():

    rpc("MassDM")
    clear()
    massdm_banner()
    token = input(f"{y}[{b}#{y}]{w}Entre le token du compte discord que tu veux utiliser pour spam DM\n>>> ")
    clear()
    massdm_banner()
    Message = input(f"{y}[{b}#{y}]{w}Quel message veut tu spammer ?\n>>> ")
    clear()
    massdm_banner()
    amount = int(input(f"{y}[{b}#{y}]{w}Combien de messages veut tu envoyer ? (base=1)\n>>> "))
    
    if amount == None:
        amount = 1
    
    x=0
    headers = {'Authorization': token}
    
    try:
        channelIds = get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token}).json()
    except:
        input(f"{y}[{b}ERROR{y}]{w}Token invalide !")
        massdm()
    
    print(f"\n\n{y}[{b}LOG{y}]{w}Spam DM en cours......")
    for channel in channelIds:
        for _ in range(1,amount+1):
            try:
                post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages', 
                headers=headers,
                data={"content": f"{Message}"})
                x+=1
                time_print(f"{y}[{b}LOG{y}]{w} ID du channel: {channel['id']} #{x}")
            except Exception as e:
                time_print(f"{y}[{b}LOG{y}]{w} Impossible d'enoyer un message à {channel['id']}; {e}")
    input(f"{y}[{b}#{y}]{w}Message envoyé à tout les amis disponibles.{w}\n")
