import subprocess
from subprocess import Popen
import os 
from pywinauto import Desktop
from pywinauto.application import Application
import time
def install_bimpop():

	current_dir = os.getcwd()
	# Path to the setup.exe file
	print("BIMPOP installing")

	# Path to the setup.exe file
	setup_file = os.path.join(current_dir,'Source','BIMPOP','V5_SS_Setup_2.5.0.60698','sense_shield_installer_pub_2.5.0.60698.exe')

	# Command to run the setup file silently
	command = f'{setup_file} /S /v" /qn'

	# Run the command using subprocess
	subprocess.run(command, shell=True)
	print("Succsessfully installed")

	print("BIMPOP installing")

	# # Path to the setup.exe file
	setup_file = os.path.join(current_dir,'Source','BIMPOP','BIMPOP_中文正式版20240227.exe')

	# Command to run the setup file silently
	command = f'{setup_file} /S /v /qn'

	# Run the command using subprocess
	subprocess.Popen(command, shell=True)
	time.sleep(5)
	installer_window = Desktop(backend="uia").window(title_re='安装 - BIMPOP 工程预演系统 1.2024.0227')
	if installer_window.wait('visible', timeout=60):
		radio_agree = installer_window.child_window(title="我同意此协议(A)", control_type="RadioButton", found_index=0)
    
	    # Select the radio button if found
		if radio_agree.exists():
		    radio_agree.click_input(double=True)  # You may need to use click_input() or similar method
		    print("Selected the '我同意此协议(A)' radio button")
		else:
		    print("Radio button '我同意此协议(A)' not found")

		time.sleep(1)
		next_button = installer_window.child_window(title="下一步(N) >", control_type="Button")
		if next_button.exists():
			next_button.click()
			print("Clicked the '下一步(N) >' button")
		else:
			print("Button '下一步(N) >' not found")

		time.sleep(1)
		next_button = installer_window.child_window(title="下一步(N) >", control_type="Button")
		if next_button.exists():
			next_button.click()
			print("Clicked the '下一步(N) >' button")
		else:
			print("Button '下一步(N) >' not found")

		time.sleep(1)
		next_button = installer_window.child_window(title="下一步(N) >", control_type="Button")
		if next_button.exists():
			next_button.click()
			print("Clicked the '下一步(N) >' button")
				
		else:
			print("Button '下一步(N) >' not found")
		time.sleep(1)
		next_button = installer_window.child_window(title="安装(I)", control_type="Button")
		if next_button.exists():
			next_button.click()
			print("Clicked the '下一步(N) >' button")
				
		else:
			print("Button '下一步(N) >' not found")
		# installer_window.print_control_identifiers()
install_bimpop()


