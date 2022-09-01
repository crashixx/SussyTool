from assets.plugin.common.base import *

def tokeninfo():
    rpc("Token Lookup")
    clear()
    tlookup_banner()
    token = str(input(f"""{y}[{b}#{y}]{w}Entre le token que tu veux scanner ici :\n>>>"""))

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    languages = {
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
    }

    cc_digits = {
        'american express': '3',
        'visa': '4',
        'mastercard': '5'
    }

    res = get('https://discordapp.com/api/v6/users/@me', headers=headers)

    if res.status_code == 200:
        res_json = res.json()
        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
        user_id = res_json['id']
        avatar_id = res_json['avatar']
        avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
        phone_number = res_json['phone']
        email = res_json['email']
        mfa_enabled = res_json['mfa_enabled']
        flags = res_json['flags']
        locale = res_json['locale']
        verified = res_json['verified']
        language = languages.get(locale)
        creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        has_nitro = False
        res = get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
        nitro_data = res.json()
        has_nitro = bool(len(nitro_data) > 0)

        if has_nitro:
            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            days_left = abs((d2 - d1).days)
        billing_info = []


        if has_nitro:
            nitro_info = {days_left}
        else:
            nitro_info = "None"

        clear()
        tlookup_banner()
        print(f"""{y}[{b}#{y}]{w}Informations Générales:
{y}[{b}>{y}]{w}Username: {user_name}
{y}[{b}>{y}]{w}User ID: {user_id}
{y}[{b}>{y}]{w}Date de creation: {creation_date}
{y}[{b}>{y}]{w}URL de l'avatar: {avatar_url if avatar_id else ""}

{y}[{b}#{y}]{w}Informations Nitro:
{y}[{b}>{y}]{w}Statut de nitro: {nitro_info}

{y}[{b}#{y}]{w}Contact:
{y}[{b}>{y}]{w}Numéro de téléphone: {phone_number if phone_number else ""}
{y}[{b}>{y}]{w}Mail: {email if email else ""}""")
    
        for x in get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json():
            payment_count=1
            yy = x['billing_address']
            name = yy['name']
            address_1 = yy['line_1']
            address_2 = yy['line_2']
            city = yy['city']
            postal_code = yy['postal_code']
            state = yy['state']
            country = yy['country']

            if x['type'] == 1:
                cc_brand = x['brand']
                cc_first = cc_digits.get(cc_brand)
                cc_last = x['last_4']
                cc_month = str(x['expires_month'])
                cc_year = str(x['expires_year'])
                
                data = {
                    f'{y}[{b}>{y}]{w}Type de paiement:': 'Carte de crédit',
                    f'{y}[{b}>{y}]{w}Nom du titulaire:': name,
                    f'{y}[{b}>{y}]{w}Marque de la carte:': cc_brand.title(),
                    f'{y}[{b}>{y}]{w}Numéro de carte:': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                    f"{y}[{b}>{y}]{w}Date d'expiration:": ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                    f'{y}[{b}>{y}]{w}Adresse n1:': address_1,
                    f'{y}[{b}>{y}]{w}Adresse n2:': address_2 if address_2 else '',
                    f'{y}[{b}>{y}]{w}Ville:': city,
                    f'{y}[{b}>{y}]{w}Code postal:': postal_code,
                    f'{y}[{b}>{y}]{w}State:': state if state else '',
                    f'{y}[{b}>{y}]{w}Country:': country,
                    f'{y}[{b}>{y}]{w}Methode de payment par defaut:': x['default']
                }

            elif x['type'] == 2:
                data = {
                    f'{y}[{b}>{y}]{w}Type de paiement:': 'PayPal',
                    f'{y}[{b}>{y}]{w}Nom du Paypal:': name,
                    f'{y}[{b}>{y}]{w}Mail du Paypal:': x['email'],
                    f'{y}[{b}>{y}]{w}Adresse n1:': address_1,
                    f'{y}[{b}>{y}]{w}Adresse n2:': address_2 if address_2 else '',
                    f'{y}[{b}>{y}]{w}Ville:': city,
                    f'{y}[{b}>{y}]{w}Code postal:': postal_code,
                    f'{y}[{b}>{y}]{w}Pays:': state if state else '',
                    f'{y}[{b}>{y}]{w}Méthode de paiement par défaut:': x['default']
                }
            billing_info.append(data)

            if len(billing_info) > 0:
                print(f"""
{y}[{b}#{y}]{w}Informations de paiement {payment_count}:\n{billing_info}""")

           

        print(f"""
{y}[{b}#{y}]{w}Sécurité:
{y}[{b}>{y}]{w}A2F: {mfa_enabled}
{y}[{b}>{y}]{w}Flags: {flags}

{y}[{b}#{y}]{w}Autres:
{y}[{b}>{y}]{w}Région: {locale} ({language})
{y}[{b}>{y}]{w}Mail Vérifié: {verified}""")

    elif res.status_code == 401:
        input(f"""{y}[{b}INFO{y}]{w} Token non valide !""")
        
    else:
        print(f"""{y}[{b}INFO{y}]{w} Une erreur est survenue""")


    input(f"""\n{y}[{b}#{y}]{w}Appuyez sur entrée pour continuer...""")


