from assets.plugin.common.base import *

def auto_login():
    rpc("Auto Login")
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
    auto_login_banner()
    tk = input(f"{y}[{w}#{y}]{w}Entre le token du compte auquel tu veux te connecter:\n>>>")
    
    opts = webdriver.FirefoxOptions()
    opts.binary = firefox_path
    driver = webdriver.Firefox(options=opts, executable_path=r'geckodriver.exe')
    script="""let token = "tk";
function login(token) {
    setInterval(() => {
      document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
    }, 50);
    setTimeout(() => {
      location.reload();
    }, 2500);
  }
login(token);""".replace("tk", tk)
    
    try:
        headers = {'Authorization': tk}
        response = get('https://discordapp.com/api/v6/users/@me', headers=headers).json()
        usr_name = f"{response['username']}#{response['discriminator']}"
    except:
        clear()
        auto_login_banner()
        input(f"{y}[{w}INFO{y}]{w} Token invalide !")
        auto_login()
    
    driver.get('https://discord.com/login')
    sleep(3)
    driver.execute_script(script)
    clear()
    auto_login_banner()
    input(f"{y}[{w}INFO{y}]{w} Vous etes actuellement connecté(e) au compte: {usr_name} !\n{y}[{w}#{y}]{w}Appuyez sur entrée pour se déconnecter... ")
    driver.close()
    clear()
    auto_login_banner()
    print(f"{y}[{w}INFO{y}]{w} Déconnecté avec succès !")
    sleep(1)

