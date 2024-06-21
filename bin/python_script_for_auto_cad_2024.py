import subprocess
from subprocess import Popen
from pywinauto import Desktop
import os
import shutil
import time

def install_auto_cad_2024():
	current_dir = os.getcwd()
	# Path to the setup.exe file
	print("Auto CAD 2024 installing")
	print(current_dir)
	# Path to the setup.exe file
	setup_file = os.path.join(current_dir,'Source', 'Autodesk','AutoCAD_2024_Simplified_Chinese_Win_64bit_dlm','Setup.exe')

	# Command to run the setup file silently
	command = f'{setup_file} /S /v" /qn'

	# Run the command using subprocess
	Popen(command, shell=True)
	time.sleep(10)  # Increase sleep time to 10 seconds
    
	# windows = Desktop(backend='uia').windows()
	# for window in windows:
	# 	print(window.window_text()+",")
    
	installer_window = Desktop(backend="uia").window(title_re='.*AutoCAD*.')
	if installer_window.wait('visible', timeout=10000):  # Increase timeout to 30 seconds
		print("Installer window is visible")
		# installer_window.print_control_identifiers()
		# time.sleep(2)
		checkbox = installer_window.child_window(title='我同意使用条款', control_type='CheckBox')

		if checkbox.exists():
		    checkbox.toggle()
		    print("Checkbox 'I agree to the Terms of Use' checked.")
		else:
		    print("Checkbox 'I agree to the Terms of Use' not found.")
		time.sleep(1)
		next_button = installer_window.child_window(title="下一步", control_type="Button")
		if next_button.exists():
		    next_button.click()
		    print("Clicked the 'Next' button")
		else:
		    print("Button 'Next' not found")
		time.sleep(1)
		next_button = installer_window.child_window(title="安装", control_type="Button")
		if next_button.exists():
		    next_button.click()
		    print("Clicked the '安装' button")
		else:
		    print("Button '安装' not found")


		while True:
			try:
				installer_window.wait_not('visible')
				print("Successfully installed")
				source_file = os.path.join(current_dir,'Source','Autodesk','补丁','acad.exe')

				# Destination folder in Program Files/AutoCAD
				destination_folder = "C:\\Program Files\\Autodesk\\AutoCAD 2024"

				# Check if the destination folder exists
				if not os.path.exists(destination_folder):
				    print("Error: AutoCAD folder does not exist in Program Files.")
				    exit()

				# Check if the source file exists
				if not os.path.exists(source_file):
				    print("Error: Source file not found.")
				    exit()

				# Copy the source file to the destination folder, replacing the existing file
				shutil.copy2(source_file, destination_folder)
				print("Auto CAD 2024 Succsessfully installed")
				break
			except:
				pass
	else:
		print("Installer window is not visible after waiting")

install_auto_cad_2024()