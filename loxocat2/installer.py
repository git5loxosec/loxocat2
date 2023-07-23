import os
import subprocess

def create_virtualenv():
    print("Creating 🐘 Loxocat 🐈 virtual environment...")
    subprocess.run(["python3", "-m", "venv", "loxocat"])

def activate_virtualenv():
    print("Activating 🐘 Loxocat 🐈 virtual environment...")
    activate_script = "loxocat/bin/activate" if os.name != "posix" else "loxocat\\Scripts\\activate"
    subprocess.run([activate_script])

def install_pwncat_cs():
    print("Installing pwncat-cs...")
    subprocess.run(["pip", "install", "pwncat-cs"])

def install_dependencies():
    print("Installing project dependencies...")
    subprocess.run(["pip", "install", "-r", "requirements.txt"])

def main():
    create_virtualenv()
    activate_virtualenv()
    install_pwncat_cs()
    install_dependencies()
    print("Installation completed...")
    
if __name__ == "__main__":
    main()
