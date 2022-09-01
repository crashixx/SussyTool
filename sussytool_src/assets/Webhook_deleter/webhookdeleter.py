from assets.plugin.common.base import *

def webhook_remover():
    rpc("Webhook Deleter")
    try:
        clear()
        wb_deleter__banner()
        webhook = input(f"{y}[{b}#{y}]{w}Entre l'url du webhook que tu veux supprimer:\n>>>")
        
        delete(webhook.rstrip())
        
        clear()
        wb_deleter__banner()
        input(f"""\n{y}[{b}INFO{y}]{w}Le webhook à été supprimé avec succès !""")

    except:
        clear()
        wb_deleter__banner()
        input(f"""{y}[{b}LOG{y}]{w} Impossible de supprimer le webhook !""")

       