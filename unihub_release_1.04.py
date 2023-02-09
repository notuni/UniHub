total_modules = '5'
import os
print(f'Module 1/{total_modules} loaded - "os"')
try:
    import webbrowser
    print(f'Module 2/{total_modules} loaded - "webbrowser"')
except ModuleNotFoundError: 
    os.system('pip install webbrowser')
    import webbrowser
try:
    import time
    print(f'Module 3/{total_modules} loaded - "time"')
except ModuleNotFoundError: 
    os.system('pip install time')
    import time
try:
    import requests
    print(f'Module 4/{total_modules} loaded - "requests"')
except ModuleNotFoundError: 
    os.system('pip install requests')
    import requests
try:
    import fade
    print(f'Module 5/{total_modules} loaded - "fade"')
except ModuleNotFoundError: 
    os.system('pip install fade')
user = os.getlogin()
version = '1.04'
version_type = f'Public Release - {version}'
unihub_splash = '''test
       █    ██  ███▄    █  ██▓ ██░ ██  █    ██  ▄▄▄▄   
       ██  ▓██▒ ██ ▀█   █ ▓██▒▓██░ ██▒ ██  ▓██▒▓█████▄ 
      ▓██  ▒██░▓██  ▀█ ██▒▒██▒▒██▀▀██░▓██  ▒██░▒██▒ ▄██
      ▓▓█  ░██░▓██▒  ▐▌██▒░██░░▓█ ░██ ▓▓█  ░██░▒██░█▀  
      ▒▒█████▓ ▒██░   ▓██░░██░░▓█▒░██▓▒▒█████▓ ░▓█  ▀█▓
      ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░▓   ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░▒▓███▀▒
      ░░▒░ ░ ░ ░ ░░   ░ ▒░ ▒ ░ ▒ ░▒░ ░░░▒░ ░ ░ ▒░▒   ░ 
       ░░░ ░ ░    ░   ░ ░  ▒ ░ ░  ░░ ░ ░░░ ░ ░  ░    ░ 
         ░  UniHub      ░  ░   ░  ░  ░   ░      ░      
                                                     ░ '''
colored_splash = fade.random(unihub_splash)
description = '''UniHub, the Beam.NG mod manager and the space's biggest leakers in the world!!! Made by the bigget leaker to ever live!'''
s = ''' 
''' # Used to return inbetween prints
def splash():
    print(colored_splash)
def clear(): # Function to clear terminal
    os.system('cls')
def invalid():
    clear()
    print('''Didn't detect a valid input, hit enter to go back''')
    input()
    clear()
    mods()
def open_link(link):
    clear()
    print(colored_splash)
    webbrowser.open(link)
    print('Opened download link in browser. Hit enter to go back.')
    time.sleep(2)
    input()
    mods()
def mods():
    clear()
    print(colored_splash)
    print('''
[1] Bailey_LSX5
[2] CrashHard
[3] Chikken
[4] Dax Maps
[5] DetroitLLC
[6] Domestic Market
[7] Emery1212
[8] xoFroggy

*Hit enter to go back without selection.*''')
    choice = input()
    if choice == '1':
        clear()
        print(colored_splash)
        print('''
[1] Bailey's 2018 GMC 2500 HD
[2] Bailey's 5th Gen Camaro
[3] Bailey's Pickup Parts

*Hit enter to go back without selection.*''')
        choice1 = input()
        clear()
        if choice1 == '1':
            open_link('https://modsfire.com/5k0ET9UXO6T4SMW')
        else:
            if choice == '2':
                open_link('https://www.mediafire.com/file/vikzrhc0yu5mtgq/bailey_5th_gen_camaro_stiv.zip/file')
            else:
                if choice1 == '3':
                    open_link('https://modsfire.com/L9BYE7sDF68STh2')
                else:
                    if choice1 == '':
                        mods()
                    else:
                        invalid()
    else:
        if choice == '':
            menu()
        else:
            if choice == '2':
                clear()
                print(colored_splash)
                print('''
[1] CrashHard Dummy 2.0

*Hit enter to go back without selection.*''')
                choice2 = input()
                if choice2 == '1':
                    open_link('https://modsfire.com/pr94oP9ulidpYn4')
                else:
                    if choice2 == '':
                        menu()
                    else:
                        invalid()
            else:
                if choice == '3':
                    clear()
                    print(colored_splash)
                    print('''
[1] 1977 Dodge Ram Fascia
[2] 1978 Ford F-250 Ranger
[3] 1988 GMC Sierra Fascia
[4] 1991-1996 Chevy Caprice Classic (And Impala)
[5] 1996 Dodge Intrepid
[6] 1997 Dodge Ram
[7] 1999 Chevy Tahoe
[8] 1999 Ford F-350 Crew Cab
[9] 2005 Nissan Altima
[10] 2006 Ford F350
[11] 2010-2012 Nissan Altima.zip
[12] 2015 6.7L Ford F-250 Single Cab
[13] 2016 Nissan Titan Crew Cab Short Bed
[14] Chrysler/Dodge Conquest/ Mitsubishi Starion
[15] D-Series Bed Rack
[16] GMT800 Chevy-GMC Tahoe-Suburban
[17] Artis Forged 22x9.5 Rim Pack

*Hit enter to go back without selection.*''')
                    choice3 = input()
                    if choice3 == '1':
                        open_link('https://cdn.discordapp.com/attachments/906773022659190814/928856667997745162/77ramfascia.zip')
                    else:
                        if choice3 == '2':
                            open_link('https://drive.google.com/file/d/1Vj3l9_K-rzkwOzc4QiCNeFjQrsGfwVoP/view?usp=sharing')
                        else:
                            if choice3 == '3':
                                open_link('https://drive.google.com/file/d/1O2fVH4BUbnD_D3DoUVKX4YWiF7cghX20/view?usp=sharing')
                            else:
                                if choice3 == '4':
                                    open_link('https://kemono.party/data/47/ea/47eacd604f1161482c4cc0fc34c315544a30f298d76faebd7aeeb2317c7e92c5.zip?f=cockcaprice%5B1%5D.zip')
                                else:
                                    if choice3 == '5':
                                        open_link('https://kemono.party/data/6b/51/6b51a5e3a084ec88bc2afe047c4e921ff3fecf718ee1a199a7264ed98d75679e.zip?f=dingusintrepidrelease1%5B1%5D.zip')
                                    else:
                                        if choice3 == '6':
                                            open_link('https://kemono.party/data/bc/f6/bcf6c32ef5f81a48eceb2bba06a47c6bb0a6b69276940c36bf8d9d45a48080a5.zip?f=97ram-111422.zip')
                                        else:
                                            if choice3 == '7':
                                                open_link('https://kemono.party/data/97/10/9710d202f6156b7fc64df73b454105a25295acc28c1caddc5eba9a284e57cab9.zip?f=chikkennnnnnnnnnnnnnsshitty19999tahoebeta1.zip')
                                            else:
                                                if choice3 == '8':
                                                    open_link('https://drive.google.com/file/d/1FBgV-6nLFSjI9XMwJ2eaL-mcIL0Cz2q-/view?usp=sharing')
                                                else:
                                                    if choice3 == '9':
                                                        open_link('https://kemono.party/data/5d/f2/5df286cc36831b900c7a2f0b6c33f15fc12e28727237deac4c8f0b61e69a540d.zip?f=ballsack05%5B1%5D.zip')
                                                    else:
                                                        if choice3 == '10':
                                                            open_link('https://drive.google.com/file/d/1RrXrEm16lARR6Ci75f_0mv6leUAlnqiF/view?usp=sharing')
                                                        else:
                                                            if choice3 == '11':
                                                                open_link('https://drive.google.com/file/d/1OUq2Cnmc10H0k_i2ycBX6Iuy2cLLau8b/view?usp=sharing')
                                                            else:
                                                                if choice3 == '12':
                                                                    open_link('https://drive.google.com/file/d/17LXpFBMY5fwdSnYXLH62Brrg9SKbPTwF/view?usp=sharing')
                                                                else:
                                                                    if choice3 == '13':
                                                                        open_link('https://kemono.party/data/cc/cf/cccf195a6dccebffdc7b229e18785561c278c2add39089ae27f6ed953cf501a8.zip?f=nissantitty%5B1%5D.zip')
                                                                    else:
                                                                        if choice3 == '14':
                                                                            open_link('https://kemono.party/data/e2/8c/e28cea30a44ebccc8b90e6eefe11c82bfffc4eacda58e92e366393e676c6c0e2.zip?f=cockquestidkmaybe%5B1%5D.zip')
                                                                        else:
                                                                            if choice3 == '15':
                                                                                open_link('https://cdn.discordapp.com/attachments/906773022659190814/988183225832710154/dingusbedrakc.zip')
                                                                            else:
                                                                                if choice3 == '16':
                                                                                    open_link('https://drive.google.com/file/d/1l37RLGtm-vTLybSzcwMEDji8QECYcMkI/view')
                                                                                else:
                                                                                    if choice3 == '17':
                                                                                        open_link('https://kemono.party/data/dd/eb/ddeb5b0b8f97030a27a793fb30a78646b9e8d90f7d350ccd411706c440cd535a.zip?f=idk_car_rims_22x9_artis_only_ni%5B1%5D.zip')
                                                                                    else:
                                                                                        if choice3 == '':
                                                                                            mods()
                                                                                        else:
                                                                                            invalid()
                else:
                    if choice == '4':
                        clear()
                        print(colored_splash)
                        print('''
[1] Freedom Overload

*Hit enter to go back without selection.*''')
                        choice4 = input()
                        if choice4 == '1':
                            open_link('https://modsfire.com/KA76C3CDfQEDL74')
                        else:
                            if choice4 == '':
                                menu()
                            else:
                                invalid()
                    else:
                        if choice == '5':
                            clear()
                            print(colored_splash)
                            print('''
[1] 1988 Malibu
[2] Promod Camaro Early Access Beta 0.01

*Hit enter to go back without selection.*''')
                            choice5 = input()
                            if choice5 == '1':
                                open_link('https://modsfire.com/41UnuapCQ8Oqo6t')
                            else:
                                if choice5 == '2':
                                    open_link('https://drive.google.com/file/d/1e0TcVBxgHWcJbv5P646vNWkrR4J845Ik/view')
                                else:
                                    if choice5 =='':
                                        menu()
                                    else:
                                        invalid()
                        else:
                            if choice == '6':
                                clear()
                                print(colored_splash)
                                print('''
[1] Chevy Duramax
[2] 2006 Chevy Cateye
[3] 2011 Chevy Silverado

*Hit enter to go back without selection.*''')
                                choice6 = input()
                                if choice6 == '1':
                                    open_link('https://kemono.party/data/6e/d5/6ed54a27651644e6eb3bb66ca81be70580a237be01d256919e789f6e38f43920.zip?f=tyysduramax.zip')
                                else:
                                    if choice6 == '2':
                                        open_link('https://kemono.party/data/6e/f5/6ef582cf84a798155838acfdac82d220001dc545211a33e01c8a470d8c2ab2e1.zip?f=chevy_cat.zip')
                                    else:
                                        if choice6 == '3':
                                            open_link('https://kemono.party/data/09/b1/09b191dbd6a21bb13e01316777520a219901a318949250ddffe61c7d956b17a7.zip?f=08to11silvtyy.zip')
                                        else:
                                            if choice6 == '':
                                                menu()
                                            else:
                                                invalid()
                            else:
                                if choice =='7':
                                    clear()
                                    print(colored_splash)
                                    print('''
[1] Axle Valley''')
                                    choice7 = input()
                                    if choice7 == '1':
                                        open_link('https://www.mediafire.com/file/f8m2834ifgaef0o/axle_valley.zip/file')
                                    else:
                                        if choice7 == '':
                                            menu()
                                        else:
                                            invalid()
                                else:
                                    if choice == '8':
                                        clear()
                                        print(colored_splash)
                                        print('''
[1] Frog's 1968 Chevy C10 V1.2
[2] Frog's 1976 Stepside GMC/Chevy V1.0
[3] Frog's 1977 Dodge W200 V2.4
[4] Frog's 1986 Bullnose Ford V1.0
[5] Frog's 2003 Ford Lightning V1.4
[6] Frog's 2003 Ford Excursion V1.5
[7] Frog's 2006 Chevy Trailblazer V1.1
[8] Frog's 2006 Ford F150 V1.1
[9] Frog's 2016 Ford F350 Superduty V1.6
[10] Frog's 2017 Ford Excursion WIP V1.0.1
[11] Frog's 2020 Toyota Tundra V0.0.1
[12] Frog's 2021 Ford Raptor V1.0
[13] Frog's 2021 Nissan Titan SL V0.1
[14] Frog's Lift WIP V1.0
[15] Frog's Mazda B Series V1.1
[16] Frog's Chevy Silverado/GMC Sierra V1.8.1
[17] Frog's Wheel/Tire Pack V2.2.2
[18] Frog's Truck Nuts V1.0
[19] Frog's Nissan 240SX V1.2

*Hit enter to go back without selection.*''')
                                        choice8 = input()
                                        if choice8 == '1':
                                            open_link('https://kemono.party/data/c8/19/c8190c9481d29781b8fc4eee3638b24ee779b49a11b61114d55880964cf8fd1f.zip?f=frogc10_BeamNG.zip')
                                        else:
                                            if choice8 == '2':
                                                open_link('https://kemono.party/data/11/bd/11bd2ad454f25e9debb78055f39940f5e871a04ea0193a1c8852685c61fd1726.zip?f=froggmcstep.zip')
                                            else:
                                                if choice8 == '3':
                                                    open_link('https://kemono.party/data/33/04/3304fefdac2922b7bb455fe4e26ccfdbffa5dfdc6e6f0f51d30c62acc889503b.zip?f=frogw200_BeamNG.zip')
                                                else:
                                                    if choice8 == '4':
                                                        open_link('https://kemono.party/data/f5/d3/f5d3ce684d7d29901f6af3b0d974e2ffa4778d6fc7b1351c9fea1f270e090385.zip?f=frog86.zip')
                                                    else:
                                                        if choice8 == '5':
                                                            open_link('https://kemono.party/data/f9/ae/f9aea48083e805c782d0f0e97ea1fa222e1d698ad9e5a737928227167557510f.zip?f=froglightning_BeamNG.zip')
                                                        else:
                                                            if choice8 == '6':
                                                                open_link('https://kemono.party/data/b1/e2/b1e21eb1926a2774e7d5e27fb05834b396a7a3694b9b62a6a748a860da9d5dec.zip?f=frogexcursion_BeamNG.zip')
                                                            else:
                                                                if choice8 == '7':
                                                                    open_link('https://kemono.party/data/1f/0d/1f0d3b5b10aced4f70bd30ae8e67cd09a18556e93c650df9dbab0457d252d4ba.zip?f=frogtrailblazer_BeamNGV1.1.zip')
                                                                else:
                                                                    if choice8 == '8':
                                                                        open_link('https://kemono.party/data/81/e7/81e7f3a7d44b5dc040cb43e80f216e6414048ecb229512e51ede9ae8c8d4fbd0.zip?f=frog06150_BeamNG.zip')
                                                                    else:
                                                                        if choice8 == '9':
                                                                            open_link('https://kemono.party/data/61/47/61473434c36aae97ae8617811eca9c01c68daadcfb8884721da7014410346c7e.zip?f=frog350_BEAMNG.zip')
                                                                        else:
                                                                            if choice8 == '10':
                                                                                open_link('https://kemono.party/data/60/4e/604e7e6237333e08a9d9c65fff26b49fe6913f975fd3d830b0742d176d5a3287.zip?f=frogexcursion17_BeamNG.zip')
                                                                            else:
                                                                                if choice8 == '11':
                                                                                    open_link('https://kemono.party/data/73/50/7350c2df74e9ba182f4baa32a6da6e554e9a15b30b9bf73664da5e009418985f.zip?f=frogtundra_BeamNG.zip')
                                                                                else:
                                                                                    if choice8 == '12':
                                                                                        open_link('https://kemono.party/data/70/8c/708c60a3a9ef990ee36d93d76b25ea7f730ac381e582a1688bb2516fba96a268.zip?f=frograptor_BeamNG.zip')
                                                                                    else:
                                                                                        if choice8 == '13':
                                                                                            open_link('https://kemono.party/data/c4/fd/c4fd0cbe2409b9a831c5b502a8300181e641e9e40398d77d9a8456f95a5b4dd5.zip?f=frogtitan20_BETA.zip')
                                                                                        else:
                                                                                            if choice8 == '14':
                                                                                                open_link('https://kemono.party/data/22/04/2204470a2d19c59d18ae0ff2a120539acb8dcab58c5c2f76810fa35060266b8f.zip?f=froglift_V1.0.zip')
                                                                                            else:
                                                                                                if choice8 == '15':
                                                                                                    open_link('https://kemono.party/data/be/35/be357aad8cf6d2d875c777f0ced8196b74c123817012d63a67f676a8c3b48c85.zip?f=frogbseries_BeamNGV1.1.zip')
                                                                                                else:
                                                                                                    if choice8 == '16':
                                                                                                        open_link('https://kemono.party/data/aa/79/aa791e85163049953ba915d49f54e396f7fed70e164046a7bd802b29a37d93a3.zip?f=frogsilveradoV1.8.1.zip')
                                                                                                    else:
                                                                                                        if choice8 == '17':
                                                                                                            open_link('https://kemono.party/data/33/aa/33aa261a58fff90d7082713c495a8156313c5970eefbc09c3d21eceefb324ef5.zip?f=frogs_wheel_pack_V2.2.2.zip')
                                                                                                        else:
                                                                                                            if choice8 == '18':
                                                                                                                open_link('https://kemono.party/data/c9/b6/c9b622c505ecc56c32b538f5f336891a025e812227367f4f09347a766dfbc1c4.zip?f=frognuts.zip')
                                                                                                            else:
                                                                                                                if choice8 == '19':
                                                                                                                    open_link('https://kemono.party/data/45/2b/452be0db6d39c684877da5c6628c62c56ed46e325e131975d59f6b6c7b1cf7c7.zip?f=frog240_BeamNG.zip')
                                                                                                                else:
                                                                                                                    if choice8 == '':
                                                                                                                        menu()
                                                                                                                    else:
                                                                                                                        invalid()
                                    else:
                                        if choice == '':
                                            menu()
                                        else:
                                            invalid()

def menu(): # Function so we can return
    clear()
    print('''Uni#1606 (Banned), NotUni#8585 (Banned), AlsoNotUni#1631 (Locked), AlsoAlsoNotUni#5300 (Current)''')
    print(colored_splash, s, description, s, version_type)
    options = '''
    [1] - Mod List
    [2] - News
    [3] - Current Disord
    [4] - Changelog
    [5] - Version Info'''
    print(options,s)
    inpu1 = input()
    if inpu1 == '1':
        clear()
        mods()
    else:
        if inpu1 == '2':
            clear()
            print('All news will be displayed here, hit enter to go back.')
            input()
            menu()
        else:
            if inpu1 == '3':
                discord()
            else:
                if inpu1 == '4':
                    clear()
                    print('Changelog will be here when completed. Hit enter to return.')
                    input()
                    menu()
                else:
                    if inpu1 == '5':
                        clear()
                        print(f'''
You are using {version_type}, released on 2/09/2023 (M/DD/YYYY), it using {total_modules} modules to operate. To find an updated version type "discord" and enter. Otherwise hit enter to go back.''')
                        inpu2 = input()
                        if inpu2 == 'discord':
                            discord()
                        else:
                            menu()
                    else:
                        menu()

def discord():
    clear()
    webbrowser.open('https://discord.gg/mCtsUYUJ6t')
    print('''Opening Discord link in browser. Didn't work? Enter it manually https://discord.gg/mCtsUYUJ6t hit enter to return to the menu.''')
    input()
    menu()
menu()