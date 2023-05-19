import subprocess

def update_linux():

        #apt update command and upgrade
        subprocess.run(['sudo','apt','update'])

        print("\n|||||||||||||||||||||||||||||||||||||||||||||||||||\n")

        subprocess.run(['sudo','apt-get','upgrade'])

        print("\n|||||||||||||||||||||||||||||||||||||||||||||||||||\n")

        #check for package that needs upgrade
        subprocess.run(['apt','list','upgradable'])

        print("\n|||||||||||||||||||||||||||||||||||||||||||||||||||\n")

update_linux()
