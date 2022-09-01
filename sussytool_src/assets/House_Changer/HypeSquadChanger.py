from assets.plugin.common.base import *

def hypesquadchanger():
    rpc("House Changer")
    clear()
    Hsquad_banner()
    print(f"""{y}[{b}+{y}]{w} De quelle maison veut tu faire partie ?:                                        
\n{y}[{w}01{y}]{w} Bravery    
\n{y}[{w}02{y}]{w} Brilliance   
\n{y}[{w}03{y}]{w} Balance         
\n""")
    house = input(f"""{y}[{b}#{y}]{w} Choix: """)
    clear()
    Hsquad_banner()
    token = input(f"{y}[{w}#{y}]{w}Entre le token du compte auquel tu veux changer la maison:\n>>>")

    headers = {'Authorization': token}  
    r = get('https://discord.com/api/v8/users/@me', headers=headers)
    
    if r.status_code == 200:
      headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
        }
      if house == "1" or house == "01":
          payload = {'house_id': 1}
      elif house == "2" or house == "02":
          payload = {'house_id': 2}
      elif house == "3" or house == "03":
          payload = {'house_id': 3}
      else:
          input(f"{y}[{w}INFO{y}]{w} Choix invalide !")
          hypesquadchanger()

      r = post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
      
      if r.status_code == 204:
        clear()
        Hsquad_banner()
        input(f"{y}[{b}#{y}]{w}Statut HypeSquad changé avec succès !")
    
    else: 
        clear()
        Hsquad_banner()
        input(f"{y}[{b}INFO{y}]{w} Token invalide !")
    
  
