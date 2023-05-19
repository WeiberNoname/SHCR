
import subprocess

def update_linux():
	#apt update command and upgrade
	subprocess.run(['sudo','apt','update'])

	print("\nsimulate|||||||||||||||||||||||||||||||||||||||||||||||||||\n")
	
	#simulate
	subprocess.run(['sudo','apt-get','upgrade','-s'])

	TF1 = input("Are you sure to keep upgrading?(y/n)")

	if TF1 == "y":
		print("\nupgrade|||||||||||||||||||||||||||||||||||||||||||||||||||\n")
		subprocess.run(['sudo','apt-get','upgrade'])
	elif TF1 == "n":
		print("\nupgradable|||||||||||||||||||||||||||||||||||||||||||||||||||\n")
		#check for package that needs upgrade
		subprocess.run(['apt','list','upgradable'])	
update_linux()
