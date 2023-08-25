from colorama import Fore, Style, init
from rich.console import Console
from rich.table import Table
import os

from user_interactions import UserInteractions
from inet_info import InetInfo
from listener import Listener
from shell_generator import ShellGenerator
from msfvenom_module import MsfvenomModule

init(autoreset=True)
console = Console()

def display_banner_and_info(listener_file_path):
    banner_file_path = 'art/banner.txt'
    with open(banner_file_path, 'r') as file:
        lines = file.readlines()

    half = len(lines) // 2
    for i, line in enumerate(lines):
        if i < half:
            print(Fore.CYAN + line, end="")
        else:
            print(Fore.RED + line, end="")

    InetInfo.get_info(listener_file_path)

def main():
    user_interactions = UserInteractions()
    listener = Listener()
    shell_generator = ShellGenerator()
    msfvenom_module = MsfvenomModule()

    while True:
        display_banner_and_info(listener.listener_file_path)
        print("\n")

        table = Table(show_header=False, collapse_padding=False, show_edge=False, show_lines=False)

        table.add_row(Fore.YELLOW + "1", "Configure Listener 🎧")
        table.add_row(Fore.GREEN + "2", "Generate Reverse Shell 🐚")
        table.add_row(Fore.MAGENTA + "3", "Start Pwncat-cs 🐈 Listener 🎧")
        table.add_row(Fore.BLUE + "4", "Msfvenom payloads 🧪")
        table.add_row(Fore.YELLOW + "5", "Msfconsole 🐮")
        table.add_row(Fore.RED + "e", "Exit 🚪" + Style.RESET_ALL)

        console.print(table)

        choice = input("\nLoxocat toolbox 2.0: ")

        if choice == '1':
            print(Fore.YELLOW + "\nConfiguring Listener 🎧..." + Style.RESET_ALL)
            listener.configure_listener_info()

        elif choice == '2':
            print(Fore.GREEN + "\nStarting Reverse Shell Generator 🐚..." + Style.RESET_ALL)
            shell_generator.show_reverse_shells()

        elif choice == '3':
            print(Fore.MAGENTA + "\nRunning Pwncat-cs 🐈 Listener 🎧..." + Style.RESET_ALL)
            listener.start_listener()

        elif choice == '4':
            print(Fore.BLUE + "\nRunning Msfvenom payloads 🧪..." + Style.RESET_ALL)
            msfvenom_module.run()

        elif choice == '5':
            print(Fore.YELLOW + "\nStarting Msfconsole 🐮..." + Style.RESET_ALL)
            os.system("msfconsole")

        elif choice == 'e':
            print(Fore.RED + "\nExiting..." + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()
