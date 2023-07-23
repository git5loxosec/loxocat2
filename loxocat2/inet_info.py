from colorama import Fore, Style
import subprocess
import re
from file_handler import FileHandler

class InetInfo:
    @staticmethod
    def get_info(listener_file_path):
        def get_ip(info_raw):
            match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', info_raw)
            return match.group() if match else "😴"

        eth0_info_raw = subprocess.getoutput("ifconfig eth0")
        wlan0_info_raw = subprocess.getoutput("ifconfig wlan0")

        eth0_info = get_ip(eth0_info_raw)
        wlan0_info = get_ip(wlan0_info_raw)

        listener_info = FileHandler.read_file(listener_file_path)

        print(Fore.MAGENTA + " Network 📶" + Style.RESET_ALL)
        print(Fore.GREEN + " eth0: " + Style.RESET_ALL, eth0_info)
        print(Fore.YELLOW + " wlan0: " + Style.RESET_ALL, wlan0_info)
        print(Fore.CYAN + " Listener: " + Style.RESET_ALL, listener_info)
