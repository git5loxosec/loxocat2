import os
import urllib.parse
import base64
import subprocess
import pyperclip
from colorama import Fore, Style
from file_handler import FileHandler

class ShellGenerator:
    def __init__(self, shells_dir='db', shell_file_path='db/shell.txt'):
        self.shells_dir = shells_dir
        self.shell_file_path = shell_file_path
        self.shell_options = FileHandler.read_file(self.shell_file_path).splitlines() if FileHandler.file_exists(self.shell_file_path) else []

    def read_shell_options(self):
        return self.shell_options

    def show_reverse_shells(self):
        print(Fore.CYAN + "\n 🐚 Reverse Shells 🐚" + Style.RESET_ALL)
        os_choices = ['1', '2', '3', 'back']
        os_files = ['linux.txt', 'windows.txt', 'mac.txt']

        print(Fore.CYAN + "1. 🐧 Linux")
        print(Fore.MAGENTA + "2. 🪟 Windows")
        print(Fore.YELLOW + "3. 🍎 Mac")
        print(Fore.RED + "4. Back 🔙" + Style.RESET_ALL)

        os_choice = input("🔢 Select OS 💽: ")
        if os_choice == '4':
            return

        os_file = os_files[int(os_choice) - 1]
        shells_file = os.path.join(self.shells_dir, os_file)

        with open(shells_file, 'r') as file:
            lines = file.readlines()

        titles = []
        for line in lines:
            if line.strip().startswith("(titulo)"):
                title = line.strip().split(" ", 1)[1]
                titles.append(title)

        for index, title in enumerate(titles, start=1):
            print(f"{Fore.MAGENTA}{index}. {title.strip()}{Style.RESET_ALL}")

        shell_choice = input(" 🔢 Select language 🗣️: ")
        selected_script = lines[lines.index(f"(titulo) {titles[int(shell_choice) - 1]}\n") + 1].strip()

        shell_options = self.read_shell_options()
        for index, shell in enumerate(shell_options, start=1):
            print(f"{Fore.RED}{index}. {shell}{Style.RESET_ALL}")

        shell_choice = input(" 🔢 Select a Shell: ")
        selected_shell = shell_options[int(shell_choice) - 1]

        selected_script = selected_script.replace("(shell)", selected_shell)
        lhost = input(" 🌐 Enter LHOST: ")
        lport = input("🚪 Enter LPORT: ")
        selected_script = selected_script.replace("(lhost)", lhost).replace("(lport)", lport)

        encode_options = ['1', '2', '3', '4']
        print(Fore.BLUE + " 1. None")
        print(Fore.BLUE + " 2. URL encode")
        print(Fore.BLUE + " 3. URL double encode")
        print(Fore.BLUE + " 4. Base64" + Style.RESET_ALL)

        encode_choice = input(" 🔢 Select encoder🔒: ")
        if encode_choice == '2':
            selected_script = urllib.parse.quote(selected_script)
        elif encode_choice == '3':
            selected_script = urllib.parse.quote_plus(selected_script)
        elif encode_choice == '4':
            selected_script = base64.b64encode(selected_script.encode()).decode()

        print(Fore.GREEN + "\n 🐚 Generated Reverse Shell 🚀\n")
        print(selected_script)
        pyperclip.copy(selected_script) 
        print("\n 📋 Your shell script is copied to clipboard." + Style.RESET_ALL)

        listener_choice = input("Do you want to start the pwncat-cs listener 🐈? (y/n): ")
        if listener_choice == 'y':
            listener_info = FileHandler.read_file('con/listener.txt')
            if listener_info:
                listener_command = f"pwncat-cs {listener_info}"
                subprocess.call(listener_command, shell=True)
            else:
                print("Listener information not found. Please configure the listener.")

if __name__ == "__main__":
    shell_generator = ShellGenerator()
    shell_generator.show_reverse_shells()
