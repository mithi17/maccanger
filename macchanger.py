import subprocess
import optparse
import colorama
from colorama import Fore

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify a interface, use --help for more options")
    elif not options.new_mac:
        parser.error("[-] please specify a new mac address, use --help for more options")
    return options

def change_mac(interface, new_mac):
    print(Fore.GREEN + "[+]changing mac address for " + interface + " to " + new_mac)
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    
options = get_arguments()
change_mac(options.interface, options.new_mac)
