import os
import pyperclip

class UserInteractions:
    def __init__(self):
        self.generated_script = None
        self.cache_directory = "__pycache__"
        self.cache_file_path = os.path.join(self.cache_directory, "last_generated_script.txt")

        if not os.path.exists(self.cache_directory):
            os.makedirs(self.cache_directory)

    def generate_last_reverse_shell(self):
        if self.generated_script is None:
            print("No reverse shell has been generated yet.")
            return

        with open(self.cache_file_path, "w") as file:
            file.write(self.generated_script)

        print("Last generated reverse shell saved in cache.")

    def edit_and_generate_last_shell(self):
        if not os.path.exists(self.cache_file_path):
            print("No last generated reverse shell found in cache.")
            return

        with open(self.cache_file_path, "r") as file:
            last_generated_script = file.read()

        lhost = input("Enter LHOST: ")
        lport = input("Enter LPORT: ")
        edited_script = last_generated_script.replace("(lhost)", lhost).replace("(lport)", lport)

        pyperclip.copy(edited_script)
        print("=== Edited and Generated Last Shell ===")
        print(edited_script)
        print("\nYour edited shell script is copied to clipboard.")

