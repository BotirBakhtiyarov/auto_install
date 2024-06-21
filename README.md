# 工一云电脑 Software Installer

工一云电脑 Software Installer is a Python-based application designed to automate the installation of various software programs on Windows operating systems. This documentation provides comprehensive information on installation, usage, architecture, customization, and contribution guidelines.

## Table of Contents

1. **Introduction**
2. **Features**
3. **System Requirements**
4. **Installation**
5. **Usage**
6. **Project Structure**
7. **Scripts Overview**
8. **Customization**
9. **Contribution Guidelines**
10. **Advanced Topics**
    - Handling Dependencies
    - Silent Installation Techniques
    - GUI Customization with CustomTkinter
11. **Known Issues**
12. **Future Enhancements**
13. **License**
14. **Credits**
15. **Contact**

## 1. Introduction

工一云电脑 Software Installer simplifies the process of installing multiple applications on Windows machines through a user-friendly GUI. It leverages Python's subprocess module for silent installations and Pywinauto for automating interactions with installer windows.

## 2. Features

- **GUI Interface**: Allows users to select applications for installation via checkboxes.
- **Silent Installation**: Executes installation scripts silently using subprocess.Popen.
- **Automated Interactions**: Utilizes Pywinauto for automating GUI interactions during installation processes.
- **Post-Installation Tasks**: Copies necessary files to designated directories after installation completion.
- **Custom Styling**: GUI designed using CustomTkinter for enhanced visual appeal and usability.

## 3. System Requirements

- **Python**: Version 3.x
- **Dependencies**:
  - `pywinauto` library (`pip install pywinauto`)
  - `customtkinter` library (if applicable, provide installation instructions)

## 4. Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/BotirBakhtiyarov/auto_install.git
   cd auto_install
   ```

2. **Install dependencies**:
   ```bash
   pip install customtkinter
   pip install pywinauto
   ```

## 5. Usage

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Select Applications**:
   - Check the checkboxes next to the applications you want to install.

3. **Initiate Installation**:
   - Click the "Install" button to start the installation process for selected applications.

4. **Follow GUI Prompts**:
   - During installation, follow any prompts shown in the GUI.

## 6. Project Structure

- **bin/**: Contains Python scripts for each application installation.
- **customtkinter/**: (If applicable) Custom library for enhanced GUI styling and functionality.
- **main.py**: Entry point for launching the GUI and initiating installations.
- **README.md**: Project overview and usage instructions.

## 7. Scripts Overview

### AutoCAD 2024 Installation Script

- **bin/python_script_for_auto_cad_2024.py**:
  - Installs AutoCAD 2024 silently (`/S` switch) using `subprocess.Popen`.
  - Uses `pywinauto` for automating GUI interactions during installation.
  - Copies necessary files to the installation directory post-installation.

### CustomTkinter

- **customtkinter/**: (Assumed as a custom library)
  - Provides enhanced styling and functionality for Tkinter GUIs.
  - Integrated to improve the visual appearance and usability of the installer interface.

## 8. Customization

工一云电脑 Software Installer allows customization through several aspects:

- **Adding New Applications**: Create new Python scripts in `bin/` following the existing structure for additional applications.
- **GUI Customization**: Modify the GUI layout, colors, and fonts using CustomTkinter as per your requirements.
- **Installer Behavior**: Adjust the installation scripts (`bin/*.py`) to include additional steps or handle specific use cases.

## 9. Contribution Guidelines

1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature/improvement`).
3. **Implement your changes** and ensure adherence to coding standards.
4. **Test thoroughly** to validate functionality.
5. **Commit** your changes (`git commit -am 'Add feature/improvement'`).
6. **Push** to the branch (`git push origin feature/improvement`).
7. **Submit a pull request** with a detailed description of your changes and improvements.

## 10. Advanced Topics

### Handling Dependencies

工一云电脑 Software Installer relies on Python and specific libraries (`pywinauto`, `customtkinter`). Ensure these dependencies are installed correctly on the target system.

### Silent Installation Techniques

Use `subprocess.Popen` with appropriate arguments (`/S`, `/v" /qn"`) for silent installations to avoid user prompts during the installation process.

### GUI Customization with CustomTkinter

CustomTkinter offers flexibility in GUI design. Modify `customtkinter/` to enhance the visual appearance and user experience of the installer interface.

## 11. Known Issues

- Installer may fail if system prerequisites are not met (e.g., missing dependencies).
- GUI interactions may not handle unexpected user actions gracefully.

## 12. Future Enhancements

- Expand application support by adding more installation scripts (`bin/*.py`).
- Enhance error handling and logging capabilities for better troubleshooting.
- Implement automated testing to ensure robustness across different environments.

## 13. License

工一云电脑 Software Installer is licensed under the [MIT License](LICENSE). See LICENSE file for details.

## 14. Credits

- **Contributors**: List of individuals who have contributed to the project.
- **Libraries**: Acknowledgment of third-party libraries used in the project.

## 15. Contact

For questions or support, please contact [Botir Bakhtiyarov](mailto:botirabkhtiyarob@gmail.com).

---
