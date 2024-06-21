import subprocess
import os 

def install_wechat():

	current_dir = os.getcwd()
        
  
	# Path to the setup.exe file
	print("Wechat installing")

	# Path to the setup.exe file
	setup_file = os.path.join(current_dir,'Source','WeChat','WeChatSetup.exe')

	# Command to run the setup file silently
	command = f'{setup_file} /S /v" /qn'

	# Run the command using subprocess
	subprocess.run(command, shell=True)
	print("WeChat Succsessfully installed")

install_wechat()