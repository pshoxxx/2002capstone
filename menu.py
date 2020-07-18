#!/usr/bin/env python3
import webbrowser

def tool_google():
    webbrowser.open("http://www.google.com")
    webbrowser.open_new_tab("https://cdn-cybersecurity.att.com/blog-content/GoogleHackingCheatSheet.pdf")
    exit()

def tool_netcraft():
    webbrowser.open("https://www.netcraft.com")
    exit()

def tool_shodan():
    webbrowser.open("https://www.shodan.io")
    exit()

def web_tools_menu():
    print("-" * 60)
    print("Web tools")
    print("-" * 60)
    print("1. Google Dorking")
    print("2. Netcraft")
    print("3. Shodan")
    web_selection = input("Please select an option. ")
    if web_selection == "1":
        tool_google()
    elif web_selection == "2":
        tool_netcraft()
    elif web_selection == "3":
        tool_shodan()
    else:
        print("Invalid option.")
        exit()

def main_menu():
    print("-" * 60)
    print("Welcome to Fancy Advanced Recon Tool")
    print("-" * 60)
    print("1. Port Scan")
    print("2. Web Tools")
    selection = input("Please select an option. ")

    if selection == 1:
        port_scan()
    else:
        web_tools_menu()
main_menu()

