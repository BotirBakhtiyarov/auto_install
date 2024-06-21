import os
import subprocess
import customtkinter as ctk

# Function to install an application
def install_app(app_name):
    app_scripts = {
        "Auto Revit 2024": "python_script_for_auto_revit_2024.py",
        "Auto CAD 2024": "python_script_for_auto_cad_2024.py",
        "BIMPOP": "python_script_for_bimpop.py",
        "WeChat": "python_script_for_wechat.py",
        "BaiduNetDisk": "python_script_for_baidunetdisk.py",
        "Office": "python_script_for_office.py",
        "AllPlan": "python_script_for_allplan.py",
        "PhotoShop": "python_script_for_photoshop.py",
        "THBIM": "python_script_for_bim.py"
    }

    script_path = os.path.join("bin", app_scripts[app_name])
    subprocess.Popen(["python", script_path])

# Function to handle installation button click
def install_clicked():
    selected_apps = [app for app in apps if app_choice[app].get()]
    for app in selected_apps:
        install_app(app)
        print(app)
    clear_checkbuttons()

def clear_checkbuttons():
    for app in apps:
        app_choice[app].set(False)

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# CustomTkinter setup
root = ctk.CTk()
root.title("工一云电脑 Software Installer")
root.geometry('450x300')
root.configure(bg="#0057A7")
root.resizable(0,0)
icon_path = "Source/img/myicon.ico"  # Replace with the path to your icon file
root.iconbitmap(icon_path)

# Create a Frame to contain the checkboxes
frame = ctk.CTkFrame(root)  # Frame with the same background color as root
frame.pack(padx=10, pady=10)

# Create checkboxes within the frame
apps = ["Auto Revit 2024", "Auto CAD 2024", "BIMPOP", "WeChat", "BaiduNetDisk", "Office", "AllPlan", "PhotoShop", "THBIM"]
app_choice = {app: ctk.BooleanVar() for app in apps}

num_columns = 3
for i, app in enumerate(apps):
    row = i // num_columns
    column = i % num_columns
    checkbutton = ctk.CTkCheckBox(frame, variable=app_choice[app], text=app)
    checkbutton.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

# Adjust column weights for the frame to ensure even distribution
for col in range(num_columns):
    frame.grid_columnconfigure(col, weight=1)

# Create install button outside the frame
install_button = ctk.CTkButton(root, text="Install", command=install_clicked)
install_button.pack(pady=10)

root.mainloop()
