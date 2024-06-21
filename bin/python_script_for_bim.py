from subprocess import Popen
import os
import time
from pywinauto import Desktop

def install_bim():

	current_dir = os.getcwd()
	# Path to the setup.exe file
	print("BIM installing")

	# Path to the setup.exe file
	setup_file = os.path.join(current_dir,'Source','BIM安装程序','公路工程设计BIM系统V1.6安装包_22.0620.exe')

	# Command to run the setup file silently
	command = f'{setup_file} /S /v" /qn'

	# Run the command using subprocess
	Popen(command, shell=True)
	installer_window = Desktop(backend="uia").window(title_re="安装 - 公路工程设计BIM系统V1.6_22.0620")
	if installer_window.wait('visible', timeout=30):
		time.sleep(5)
		print("started")
		# installer_window.print_control_identifiers()
		checkbox = installer_window.child_window(title='我同意此协议(A)', control_type='RadioButton')
        
		if checkbox.exists():
			checkbox.click_input(double=True)
		else:
			pass
		time.sleep(1)
		next_button = installer_window.child_window(title="下一步(N)", control_type="Button")
		if next_button.exists():
			next_button.click()
		else:
			pass

		time.sleep(1)
		next_button = installer_window.child_window(title="下一步(N)", control_type="Button")
		if next_button.exists():
			next_button.click()
		else:
			pass
		time.sleep(1)
		next_button = installer_window.child_window(title="下一步(N)", control_type="Button")
		if next_button.exists():
			next_button.click()
		else:
			pass
		time.sleep(1)
		next_button = installer_window.child_window(title="安装(I)", control_type="Button")
		if next_button.exists():
			next_button.click()
		else:
			pass
		time.sleep(90)

		# Path to the setup.exe file
	setup_file = os.path.join(current_dir,'Source','BIM安装程序','HighWayBIM_V1.6UpDate_23.0815.exe')

	# Command to run the setup file silently
	command = f'{setup_file} /S /v" /qn'

	# Run the command using subprocess
	Popen(command, shell=True)
	installer_window = Desktop(backend="uia").window(title_re="安装 - 补丁_V1.6公路BIM_23.0815")
	if installer_window.wait('visible', timeout=60):
		time.sleep(1)
		next_button = installer_window.child_window(title="下一步(N)", control_type="Button")
		if next_button.exists():
			next_button.click()
		else:
			pass
		time.sleep(1)
		next_button = installer_window.child_window(title="下一步(N)", control_type="Button")
		if next_button.exists():
			next_button.click()
		else:
			pass
		time.sleep(1)
		next_button = installer_window.child_window(title="安装(I)", control_type="Button")
		if next_button.exists():
			next_button.click()
		else:
			pass
		time.sleep(30)

	# Path to the setup.exe file
	setup_file = os.path.join(current_dir,'Source','BIM安装程序','finalpart.exe')

	# Command to run the setup file silently
	command = f'{setup_file} /S /v" /qn'

	# Run the command using subprocess
	Popen(command, shell=True)
	installer_window = Desktop(backend="uia").window(title_re="微软常用运行库合集*.")
	if installer_window.wait('visible', timeout=60):
		print('found')
		next_button = installer_window.child_window(title="下一步(N) >", control_type="Button")
		if next_button.exists():
			next_button.click()
		else:
			pass
		time.sleep(1)
		next_button = installer_window.child_window(title="下一步(N) >", control_type="Button")
		if next_button.exists():
			next_button.click()
		else:
			pass
		time.sleep(1)
		print("BIM installed")

install_bim()
