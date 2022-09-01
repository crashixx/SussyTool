from assets.plugin.common.base import *

def webhook_spammer():
    rpc("Webhook Spammer")

    def id_generator(size=6, chars=ascii_uppercase + digits):
        return ''.join(choice(chars) for _ in range(size))

    def send_message(webhook_url):
        username = id_generator()
        message = f"@everyone {id_generator(1900)}"
        avatar = "https://picsum.photos/id/{}/200".format(randint(1, 500))


        webhook = DiscordWebhook(url=webhook_url, content=message, username=username, avatar_url=avatar)
        response = webhook.execute()

        if not response.ok:
            print(f"{y}[{b}INFO{y}]{w} Erreur lors de l'envoie des messages !")
            
        else:
            print(f"{y}[{b}LOG{y}]{w} Un message à été envoyé !")
            
    clear()
    wbspammer_banner()
    webhook = input(f"{y}[{b}#{y}]{w}Entre l'url du webhook que tu veux spammer:\n>>>")
    attempt_count = 0
    sent_count = 0
    clear()
    wbspammer_banner()
    print(f"{y}[{b}INFO{y}]{w}Spamming du webhook en cours, appuyez sur CTRL+C pour arreter le spam....")
    sleep(1)

    failed_previous = False

    try:
        while True:
            if (send_message(webhook)):
                sent_count += 1
                failed_previous = False
            else:
                if failed_previous: 
                    sleep(1)
                else:
                    sleep(1)
                failed_previous = True
            attempt_count += 1
    except KeyboardInterrupt:
        pass

