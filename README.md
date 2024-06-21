# 工一云电脑 Software Installer

工一云电脑 Software Installer is a Python-based application designed for automating the installation of various software programs on Windows systems. It provides a user-friendly graphical interface (GUI) to select and install multiple applications simultaneously, streamlining the installation process.

## Features

- **GUI Interface**: Allows users to select applications for installation using checkboxes.
- **Silent Installation**: Utilizes `subprocess` for running installer scripts silently (`/S` switch).
- **Automation**: Uses `pywinauto` for automating GUI interactions during installations.
- **Post-Installation Tasks**: Copies required files to designated directories after installation completion.
- **Custom Styling**: GUI designed using CustomTkinter for a visually appealing user interface.

## Requirements

- **Python**: Version 3.x
- **Dependencies**:
  - `pywinauto` library (`pip install pywinauto`)
  - `customtkinter` library (if applicable, provide installation instructions)

## Installation

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

   Ensure you have Python 3.x installed and accessible from your command line environment.

## Usage

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

## Project Structure

- **bin/**: Contains Python scripts for each application installation.
- **customtkinter/**: (If applicable) Custom library for enhanced GUI styling and functionality.
- **main.py**: Entry point for launching the GUI and initiating installations.
- **README.md**: Project overview and usage instructions.

## Scripts Overview

### AutoCAD 2024 Installation Script

- **bin/python_script_for_auto_cad_2024.py**:
  - Installs AutoCAD 2024 silently (`/S` switch) using `subprocess.Popen`.
  - Uses `pywinauto` for automating GUI interactions during installation.
  - Copies necessary files to the installation directory post-installation.

### CustomTkinter

- **customtkinter/**: (Assumed as a custom library)
  - Provides enhanced styling and functionality for Tkinter GUIs.
  - Integrated to improve the visual appearance of the installer interface.

## Contribution Guidelines

1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature/improvement`).
3. **Make your changes** and ensure code quality (`flake8`, `black`).
4. **Commit** your changes (`git commit -am 'Add new feature'`).
5. **Push** to the branch (`git push origin feature/improvement`).
6. **Submit a pull request** with a detailed description of your changes.

## Known Issues

- Installer may fail if system prerequisites are not met (e.g., missing dependencies).
- GUI interactions may not handle unexpected user actions gracefully.

## Future Enhancements

- Support for additional applications and corresponding installation scripts.
- Enhanced error handling and logging during installation processes.
- Integration of automated tests for ensuring robustness.

## Credits

- **Contributors**: List of individuals who have contributed to the project.
- **Libraries**: Acknowledgment of third-party libraries used in the project.

## Contact

For questions or support, please contact [Botir Bakhtiyarov](mailto:botirabkhtiyarob@gmail.com).
