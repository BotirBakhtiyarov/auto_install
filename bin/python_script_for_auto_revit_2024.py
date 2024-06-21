from subprocess import Popen
import subprocess
import os
import zipfile
from pywinauto import Desktop
import time

def install_auto_revit_2024():
    current_dir = os.getcwd()
    # Path to the setup.exe file
    print("Auto Revit 2024 installing")

    # Path to the setup.exe file
    setup_file = os.path.join(current_dir,'Source','AutoRevit2024','Setup','Setup.exe')

    # Command to run the setup file silently
    command = f'{setup_file} /S'

    # Run the command using subprocess
    Popen(command, shell=True)
    # windows = Desktop(backend='uia').windows()
    # for window in windows:
    #     print(window.window_text())
    installer_window = Desktop(backend="uia").window(title_re=".*Revit 2024*.")
    if installer_window.wait('visible', timeout=10000):
        print("started")
        # installer_window.print_control_identifiers()
        time.sleep(2)
        checkbox = installer_window.child_window(title='I agree to the Terms of Use', control_type='CheckBox')
        
        if checkbox.exists():
            checkbox.toggle()
            print("Checkbox 'I agree to the Terms of Use' checked.")
        else:
            print("Checkbox 'I agree to the Terms of Use' not found.")
        time.sleep(1)
        next_button = installer_window.child_window(title="Next", control_type="Button")
        if next_button.exists():
            next_button.click()
            print("Clicked the 'Next' button")
        else:
            print("Button 'Next' not found")
        time.sleep(2)
        next_button = installer_window.child_window(title="Install", control_type="Button")
        if next_button.exists():
            next_button.click()
            print("Clicked the 'Install' button")
        else:
            print("Button 'Next' Install found")

        while True:            
            try:
                installer_window.wait_not('visible')
                print("Succsessfully installed")

                print("Start cracking")
                def unzip_folder(zip_file, destination_folder):
                    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                        zip_ref.extractall(destination_folder)

                # specify the path to the zip file and the destination folder where you want to extract the contents
                zip_file = os.path.join(current_dir,'Source','AutoRevit2024','Crack.zip')
                destination_folder = os.path.join(current_dir ,'Source','AutoRevit2024')

                # call the unzip_folder function with the specified parameters
                unzip_folder(zip_file, destination_folder)
                print("Please choose Revit 2024")

                crack_file = os.path.join(current_dir, 'Source', 'AutoRevit2024', 'keygen.exe')
                windows = Desktop(backend='uia').windows()
                
                subprocess.run(crack_file, shell=True)

                print("Auto Revit 2024 Succsessfully installed")
                break
            except:
                pass

install_auto_revit_2024()

