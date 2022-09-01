from assets.plugin.common.base import *


def DM_deleter():
    rpc("Dm deleter")
    clear()
    dm_cleaner_banner()
    token = input(f"{y}[{b}#{y}]{w}Entre le token du compte discord que tu veux nettoyer:\n>>> ")
    def deleter(token, channels):
        for channel in channels:
            try:
                delete(f"https://discord.com/api/v7/channels/{channel['id']}", headers = getheaders(token))
                print(f"{y}[{w}>{y}]{w}DM supprimé: {channel['id']}")
            except:
                error(f"Delete channel {channel['id']}")
                pass

    channelIds = get("https://discord.com/api/v9/users/@me/channels", headers = getheaders(token)).json()
    if not channelIds:
        clear()
        dm_cleaner_banner()
        input(f"{y}[{w}INFO{y}]{w} Aucun salon n'a été trouvé !")
    
    clear()
    dm_cleaner_banner()
    for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
        deleter(token, channel)
    input(f"{y}[{b}#{y}]{w}Nettoyage terminé !")
