#!/usr/bin/env python3
import webbrowser

# Function for port scanner menu
def scanner_menu():
    # Print out options for client to choose (How many hosts they want to scan? One or multiple)
    print("How many hosts will you be scanning?")
    print("1. Single")
    print("2. Custom")
    print("3. Return to previous menu.")
    # Ask for selection input 
    how_many = input("Please enter a selection. ")
        # Redirect to appropriate functions (Common Scan/Custom scan)
    if how_many == "1":
        # Ask how many ports will they be scanning
        print("Which ports will you be scanning?")
        print("1. Common ports (1-1024)")
        print("2. Custom range")
        how_many2 = input("Please enter a selection. ")
        # Redirect to appropriate functions
        if how_many2 == "1":
            common_port_scanner()
        elif how_many2 == "2":
            custom_port_scanner()
    elif how_many == "2":
        # Redirect to appropriate function (custom ip function)
        custom_ip_scan()
    # Return to main menu
    elif how_many == "3":
        main_menu()    
    # Error handling of invalid selections
    else:
        print("Invalid selection.")
        exit()

# Google Dorking Redirect Function
def tool_google():
    webbrowser.open("http://www.google.com")
    webbrowser.open_new_tab("https://cdn-cybersecurity.att.com/blog-content/GoogleHackingCheatSheet.pdf")
    exit()

# Netcraft redirect function
def tool_netcraft():
    webbrowser.open("https://www.netcraft.com")
    exit()

# Shodan redirect function
def tool_shodan():
    webbrowser.open("https://www.shodan.io")
    exit()

# Web tools Menu
def web_tools_menu():
    # Print out menu layout and options
    print("-" * 60)
    print("{:^60}".format("Web tools"))
    print("-" * 60)
    print("1. Google Dorking")
    print("2. Netcraft")
    print("3. Shodan")

    # Ask for selection input 
    web_selection = input("Please select an option. ")

    # Redirect to appropriate option
    if web_selection == "1":
        tool_google()
    elif web_selection == "2":
        tool_netcraft()
    elif web_selection == "3":
        tool_shodan()
    # Error handling
    else:
        print("Invalid option.")
        exit()

# Function for main menu
def main_menu():
    # Print out layout for menu
    print("-" * 60)
    print("{:^60}".format("Welcome to Fancy Advanced Recon Tool"))
    print("-" * 60)
    print("1. Port Scan")
    print("2. Web Tools")
    # Ask for selection input
    selection = input("Please select an option. ")

    # Redirect to appropriate path
    if selection == "1":
        scanner_menu()
    elif selection == "2":
        web_tools_menu()
    else: 
        print("Invalid selection.")
        exit()
main_menu()

