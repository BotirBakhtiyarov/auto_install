import subprocess
import os

def install_baidunetdisk():

	current_dir = os.getcwd()
	# Path to the setup.exe file
	print("BaiduNetDisk installing")

	# Path to the setup.exe file
	setup_file = os.path.join(current_dir,'Source','BaiduNetDisk','BaiduNetdisk_7.39.1.1.exe')

	# Command to run the setup file silently
	command = f'{setup_file} /S /v" /qn'

	# Run the command using subprocess
	subprocess.run(command, shell=True)
	print("BaiduNetDisk Succsessfully installed")

install_baidunetdisk()