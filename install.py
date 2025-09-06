#!/usr/bin/env python3
import os
import sys
import subprocess
from time import sleep

# Color Codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Tool Version
VERSION = "EMREZ V2.1"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_banner():
    clear_screen()
    print(f"""{PURPLE}
    ▓█████▄  ▄▄▄       ███▄ ▄███▓ ██▓ ██▓    
    ▒██▀ ██▌▒████▄    ▓██▒▀█▀ ██▒▓██▒▓██▒    
    ░██   █▌▒██  ▀█▄  ▓██    ▓██░▒██▒▒██░    
    ░▓█▄   ▌░██▄▄▄▄██ ▒██    ▒██ ░██░▒██░    
    ░▒████▓  ▓█   ▓██▒▒██▒   ░██▒░██░░██████▒
     ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░▓  ░ ▒░▓  ░
     ░ ▒  ▒   ▒   ▒▒ ░░  ░      ░ ▒ ░░ ░ ▒  ░
     ░ ░  ░   ░   ▒   ░      ░    ▒ ░  ░ ░   
       ░          ░  ░       ░    ░      ░  ░
     ░                                         
    {RESET}{CYAN}~ {VERSION} Penetration Testing Framework ~{RESET}
    {RED}** AUTHORIZED USE ONLY **{RESET}
    {YELLOW}>> https://github.com/yourusername/EMREZ-V2{RESET}
    """)

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        return (True, result.stdout)
    except subprocess.CalledProcessError as e:
        return (False, e.stderr)

def install_tool(tool_name, check_cmd, install_cmd):
    print(f"\n{YELLOW}[*] Checking {tool_name}...{RESET}")
    success, _ = run_command(check_cmd)
    
    if success:
        print(f"{GREEN}[+] {tool_name} already installed{RESET}")
        return True
    
    print(f"{BLUE}[~] Installing {tool_name}...{RESET}")
    success, output = run_command(install_cmd)
    
    if success:
        print(f"{GREEN}[+] {tool_name} installed successfully{RESET}")
        return True
    else:
        print(f"{RED}[!] Failed to install {tool_name}{RESET}")
        print(f"{RED}[ERROR] {output}{RESET}")
        return False

def tools_installation_menu():
    while True:
        show_banner()
        print(f"""
    {BLUE}[1]{RESET} Install Nmap
    {BLUE}[2]{RESET} Install SQLmap
    {BLUE}[3]{RESET} Install Aircrack-ng
    {BLUE}[4]{RESET} Install Hydra
    {BLUE}[5]{RESET} Install Metasploit Framework
    {BLUE}[6]{RESET} Install All Tools
    {BLUE}[0]{RESET} Return to Main Menu
        """)
        
        choice = input(f"{YELLOW}[?] Select option: {RESET}").strip()
        
        if choice == "1":
            install_tool("Nmap", "nmap --version", "sudo apt install nmap -y")
        elif choice == "2":
            install_tool("SQLmap", "sqlmap --version", "sudo apt install sqlmap -y")
        elif choice == "3":
            install_tool("Aircrack-ng", "aircrack-ng --version", "sudo apt install aircrack-ng -y")
        elif choice == "4":
            install_tool("Hydra", "hydra -h", "sudo apt install hydra -y")
        elif choice == "5":
            install_tool("Metasploit", "msfconsole --version", 
                        "curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod +x msfinstall && ./msfinstall")
        elif choice == "6":
            for tool in [(1, "Nmap"), (2, "SQLmap"), (3, "Aircrack-ng"), (4, "Hydra"), (5, "Metasploit")]:
                tools_installation_menu(str(tool[0]))
        elif choice == "0":
            return
        else:
            print(f"{RED}[!] Invalid option{RESET}")
        
        input(f"{YELLOW}[?] Press Enter to continue...{RESET}")

def nmap_scanner():
    show_banner()
    print(f"{CYAN}=== Nmap Scanner ==={RESET}")
    target = input(f"{YELLOW}[?] Enter target IP/hostname: {RESET}")
    scan_type = input(f"{YELLOW}[?] Scan type (1=Quick, 2=Full, 3=UDP): {RESET}")
    
    if scan_type == "1":
        cmd = f"nmap -sV -T4 {target}"
    elif scan_type == "2":
        cmd = f"nmap -A -T4 {target}"
    elif scan_type == "3":
        cmd = f"nmap -sU -T4 {target}"
    else:
        cmd = f"nmap {target}"
    
    print(f"\n{GREEN}[*] Running: {cmd}{RESET}")
    success, output = run_command(cmd)
    
    if success:
        print(f"\n{GREEN}[+] Scan results:{RESET}")
        print(output)
    else:
        print(f"{RED}[!] Scan failed{RESET}")
        print(output)
    
    input(f"{YELLOW}[?] Press Enter to continue...{RESET}")

def sql_injection_test():
    show_banner()
    print(f"{CYAN}=== SQL Injection Tester ==={RESET}")
    url = input(f"{YELLOW}[?] Enter vulnerable URL (e.g., http://test.com?id=1): {RESET}")
    level = input(f"{YELLOW}[?] Test level (1=Basic, 2=Advanced): {RESET}")
    
    if level == "1":
        cmd = f"sqlmap -u {url} --batch --crawl=2"
    else:
        cmd = f"sqlmap -u {url} --batch --crawl=2 --level=3 --risk=3"
    
    print(f"\n{GREEN}[*] Running: {cmd}{RESET}")
    success, output = run_command(cmd)
    
    if success:
        print(f"\n{GREEN}[+] SQLmap results:{RESET}")
        print(output)
    else:
        print(f"{RED}[!] Test failed{RESET}")
        print(output)
    
    input(f"{YELLOW}[?] Press Enter to continue...{RESET}")

def main_menu():
    while True:
        show_banner()
        print(f"""
    {BLUE}[1]{RESET} Tools Installation Menu
    {BLUE}[2]{RESET} Nmap Scanner
    {BLUE}[3]{RESET} SQL Injection Test
    {BLUE}[4]{RESET} WiFi Tools (Requires Aircrack-ng)
    {BLUE}[5]{RESET} Password Attacks (Requires Hydra)
    {BLUE}[0]{RESET} Exit
        """)
        
        choice = input(f"{YELLOW}[?] Select option: {RESET}").strip()
        
        if choice == "1":
            tools_installation_menu()
        elif choice == "2":
            nmap_scanner()
        elif choice == "3":
            sql_injection_test()
        elif choice == "4":
            print(f"{RED}[!] First install Aircrack-ng from Installation Menu{RESET}")
            sleep(2)
        elif choice == "5":
            print(f"{RED}[!] First install Hydra from Installation Menu{RESET}")
            sleep(2)
        elif choice == "0":
            print(f"{RED}[!] Exiting EMREZ V2...{RESET}")
            sys.exit()
        else:
            print(f"{RED}[!] Invalid option{RESET}")
            sleep(1)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Process stopped by user{RESET}")
        sys.exit()
