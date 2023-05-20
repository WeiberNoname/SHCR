
import subprocess

def commandSplit(str):
	str = str.split()
	return str

def commandFilter(result):
	result = commandSplit(result)
	progress = 0
	for word in result:
		progress += 1
		print("Command function "+str(progress))
		if word == "update":
			update_linux()
		elif word == "pyinstaller":
			pyinstaller_install()

def pyinstaller_install():
	print("\npyinstaller|||||||||||||||||||||||||||||||||||||||\n")
	subprocess.run(['sudo','pip','install','pyinstaller'])

def update_linux():
	
	print("\nsimulate|||||||||||||||||||||||||||||||||||||||\n")
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

string = input("Enter Function:")
commandFilter(string)

