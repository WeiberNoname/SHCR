
import subprocess
import os

def basic_setup():

	subprocess.run(['sudo','apt','update'])
	subprocess.run(['sudo','apt','upgrade'])


basic_setup()
