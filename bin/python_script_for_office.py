import subprocess
import os

def install_office():

	current_dir = os.getcwd()
	# Path to the setup.exe file
	print("Office installing")

	# Path to the setup.exe file
	setup_file = os.path.join(current_dir,'Source','Office2024','YAOCTRI_Installer.cmd')

	# Command to run the setup file silently
	command = f'{setup_file} /S'
	subprocess.run(command, shell=True)
	print("Succsessfully installed")
	print("Start cracking")
	setup_file = os.path.join(current_dir,'Source','Office2024','activator','HEU_KMS_Activator_42.0.0.exe')

	# Command to run the setup file silently
	command = f'{setup_file} /S'
	subprocess.run(command, shell=True)
	print("Office Succsessfully installed")

install_office()