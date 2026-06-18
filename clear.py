import os

def clear_terminal():
    # 'nt' means Windows, 'posix' covers macOS and Linux
    os.system('cls' if os.name == 'nt' else 'clear')

# Call the function whenever you need to clear the screen
clear_terminal()
