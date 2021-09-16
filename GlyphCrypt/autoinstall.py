#valtyr
import subprocess

def autoinstall():
    pip=[
        "python3",
        "-m",
        "pip",
        "install",
        "--upgrade",
        "--user",
        "pip"
    ]

    try:
        subprocess.run(['python3','-m','pip','--version'])
    except:
        print('ATTENTION: pip is required to run the autoinstaller.')
        exit()
    choice=input('Upgrade pip? Y/N: ')
    if(choice.lower()=='y'):
        print("Upgrading...")
        subprocess.run(pip)
    try:
        subprocess.run(["python3","-m","pip","install",'-r','data/requirements.txt'])
        print('Autoinstaller completed!')
    except:
        print("ERR: Autoinstaller failed!")

if __name__=='__main__':
    autoinstall()