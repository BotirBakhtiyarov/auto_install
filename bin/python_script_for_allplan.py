import subprocess
import os 

def install_allplan():
	current_dir = os.getcwd()
	# Path to the setup.exe file
	print("AllPlan installing")

	# Path to the setup.exe file
	setup_file = os.path.join(current_dir, 'Source', 'Allplan2023_1_2', 'Allplan_2023_1_2_Installer.exe')

	# Command to run the setup file silently
	command = f'{setup_file} /S /v" /qn'

	# Run the command using subprocess
	subprocess.run(command, shell=True)
	print("Allplan Succsessfully installed")

install_allplan()