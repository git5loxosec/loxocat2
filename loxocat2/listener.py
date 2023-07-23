import subprocess
from file_handler import FileHandler

class Listener:
    def __init__(self):
        self.listener_file_path = 'con/listener.txt'
        self.listener_info = FileHandler.read_file(self.listener_file_path).splitlines() if FileHandler.file_exists(self.listener_file_path) else None
        self.listener_command = f"pwncat-cs {self.listener_info}" if self.listener_info else None

    def get_listener_info(self):
        return self.listener_info

    def get_listener_command(self):
        return self.listener_command

    def configure_listener_info(self):
        print("Please enter the listener info (separate with comma for multiple info):")
        listener_info = input("> ")
        FileHandler.write_file(self.listener_file_path, listener_info)
        self.listener_info = listener_info
        self.listener_command = f"pwncat-cs {listener_info}"

        print("Listener configured successfully.")

    def start_listener(self):
        if self.listener_info:
            listener_info = FileHandler.read_file(self.listener_file_path)
            listener_command = f"pwncat-cs -l {listener_info}"
            subprocess.call(listener_command, shell=True)
        else:
            print("Listener information not found. Please configure the listener.")
