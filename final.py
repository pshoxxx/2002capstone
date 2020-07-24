#!/usr/bin/env python3
# seed the pseudorandom number generator
from random import seed
from random import randint
import socket
import subprocess
import sys
import ipaddress
import webbrowser
from datetime import datetime

# Clear up the screen
subprocess.call('clear', shell=True)

# seed random number generator
seed()
# generate some random numbers
randomnumber = randint(1,4)
if randomnumber == 1:

    print(r'''
   __   _
 _(  )_( )_
(_   _    _)
  (_) (__)

            ''')

if randomnumber == 2:
    print(r'''
                                                                                         
FFFFFFFFFFFFFFFFFFFFFF      AAA               RRRRRRRRRRRRRRRRR   TTTTTTTTTTTTTTTTTTTTTTT
F::::::::::::::::::::F     A:::A              R::::::::::::::::R  T:::::::::::::::::::::T
F::::::::::::::::::::F    A:::::A             R::::::RRRRRR:::::R T:::::::::::::::::::::T
FF::::::FFFFFFFFF::::F   A:::::::A            RR:::::R     R:::::RT:::::TT:::::::TT:::::T
  F:::::F       FFFFFF  A:::::::::A             R::::R     R:::::RTTTTTT  T:::::T  TTTTTT
  F:::::F              A:::::A:::::A            R::::R     R:::::R        T:::::T        
  F::::::FFFFFFFFFF   A:::::A A:::::A           R::::RRRRRR:::::R         T:::::T        
  F:::::::::::::::F  A:::::A   A:::::A          R:::::::::::::RR          T:::::T        
  F:::::::::::::::F A:::::A     A:::::A         R::::RRRRRR:::::R         T:::::T        
  F::::::FFFFFFFFFFA:::::AAAAAAAAA:::::A        R::::R     R:::::R        T:::::T        
  F:::::F         A:::::::::::::::::::::A       R::::R     R:::::R        T:::::T        
  F:::::F        A:::::AAAAAAAAAAAAA:::::A      R::::R     R:::::R        T:::::T        
FF:::::::FF     A:::::A             A:::::A   RR:::::R     R:::::R      TT:::::::TT      
F::::::::FF    A:::::A               A:::::A  R::::::R     R:::::R      T:::::::::T      
F::::::::FF   A:::::A                 A:::::A R::::::R     R:::::R      T:::::::::T      
FFFFFFFFFFF  AAAAAAA                   AAAAAAARRRRRRRR     RRRRRRR      TTTTTTTTTTT      
                                                  
    ''')

if randomnumber == 3:
        print(r'''
                        
______                        ___      _                               _  ______                       _____           _ 
|  ___|                      / _ \    | |                             | | | ___ \                     |_   _|         | |
| |_ __ _ _ __   ___ _   _  / /_\ \ __| |_   ____ _ _ __   ___ ___  __| | | |_/ /___  ___ ___  _ __     | | ___   ___ | |
|  _/ _` | '_ \ / __| | | | |  _  |/ _` \ \ / / _` | '_ \ / __/ _ \/ _` | |    // _ \/ __/ _ \| '_ \    | |/ _ \ / _ \| |
| || (_| | | | | (__| |_| | | | | | (_| |\ V / (_| | | | | (_|  __/ (_| | | |\ \  __/ (_| (_) | | | |   | | (_) | (_) | |
\_| \__,_|_| |_|\___|\__, | \_| |_/\__,_| \_/ \__,_|_| |_|\___\___|\__,_| \_| \_\___|\___\___/|_| |_|   \_/\___/ \___/|_|
                      __/ |                                                                                              
                     |___/                                                                                               
        
        ''')

if randomnumber == 4:
    print(r'''
 _________________
|# :           : #|
|  :           :  |
|  :           :  |
|  :           :  |
|  :___________:  |
|     _________   |
|    | __      |  |
|    ||  |     |  |
\____||__|_____|__|
    
    
    ''')


def common_port_scanner():
    # Ask for input
    remoteServer    = input("Enter a remote host to scan: ")
    remoteServerIP  = socket.gethostbyname(remoteServer)

    # Print a nice banner with information on which host we are about to scan
    print("-" * 60)
    print("Please wait, scanning remote host", remoteServerIP)
    print("-" * 60)

    # Check what time the scan started
    t1 = datetime.now()

    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)

    # We also put in some error handling for catching errors

    try:
        for port in range(1,1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}: 	 Open".format(port))
            sock.close()

    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total =  t2 - t1

    # Printing the information to screen
    print('Scanning Completed in: ', total)

# common_scanner()

# Function to scan ranges of ports
def custom__port_scanner():

# Add two variables to specify ranges of ports to scan
port_a = input("Please enter a number: ")
port_b = input("Please enter a number: ")
# Ask for input
    remoteServer    = input("Enter a remote host to scan: ")
    remoteServerIP  = socket.gethostbyname(remoteServer)

    # Print a nice banner with information on which host we are about to scan
    print("-" * 60)
    print("Please wait, scanning remote host", remoteServerIP)
    print("-" * 60)

    # Check what time the scan started
    t1 = datetime.now()

    # Using the range function to specify ports (Use range of two variables)

    # We also put in some error handling for catching errors

    try:
        for port in range(port_a, port_b + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}: 	 Open".format(port))
            sock.close()

    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total =  t2 - t1

    # Printing the information to screen
    print('Scanning Completed in: ', total)

def custom_ip_scan():
    # Ask for input of range of ips to scan in cidr notation

    remoteServer = input("Enter remote host to scan in CIDR notation: ")
    
    
    iplst = [str(ip) for ip in ipaddress.IPv4Network(remoteServer)]

       
    for ip in iplst:
         # Ask for input
        remoteServer    = ip
        remoteServerIP  = socket.gethostbyname(remoteServer)

     # Print a nice banner with information on which host we are about to scan
        print("-" * 60)
        print("Please wait, scanning remote host", remoteServerIP)
        print("-" * 60)

    # Check what time the scan started
        t1 = datetime.now()

    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)

    # We also put in some error handling for catching errors

        try:
            for port in range(1,1025):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remoteServerIP, port))
                if result == 0:
                    print("Port {}: 	 Open".format(port))
                sock.close()

        except KeyboardInterrupt:
            print("You pressed Ctrl+C")
            sys.exit()

        except socket.gaierror:
            print('Hostname could not be resolved. Exiting')
            sys.exit()

        except socket.error:
            print("Couldn't connect to server")
            sys.exit()

    # Checking the time again
        t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
        total =  t2 - t1

    # Printing the information to screen
        print('Scanning Completed in: ', total)

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