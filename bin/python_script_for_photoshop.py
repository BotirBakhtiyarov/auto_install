import subprocess
import os
from pywinauto import Desktop, findwindows
import time

def install_photoshop():

    current_dir = os.getcwd()

    print("Installing PhotoShop...")

    setup_file = os.path.join(current_dir, 'Source', 'AdobePhotoshop2024', 'Set-up.exe')
    command = f'"{setup_file}" /S /v" /qn'
    
    # Run the command using subprocess
    subprocess.Popen(command, shell=True)
    installation_successful = False
    try:
        # Wait for the installer window to open
        installer_window = Desktop(backend="uia").window(title_re='.*Photoshop*.')
        time.sleep(5)
        if installer_window.wait('visible', timeout=60):
            time.sleep(5)
            # Find and click the "Next" button
            next_button = installer_window.child_window(title="Continue", control_type="Button")
            if next_button.exists():
                next_button.click()
                installation_successful = True
            else:
                continue_button = installer_window.child_window(title="继续", control_type="Button")
                if continue_button.exists():
                    continue_button.click()
                    installation_successful = True
    except (findwindows.WindowNotFoundError, findwindows.ElementNotFoundError):
        pass

    print("PhotoShop successfully installed")

install_photoshop()
