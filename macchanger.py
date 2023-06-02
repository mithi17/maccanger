import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's mac address")
    parse.add_option("-m", "--mac", dest="new_mac", help="new mac address")
    (options, arguments) = parser.prase_args()
    if not options.interface:
        parser.error("[-] please specify a interface, use --help for more options")
    elif not options.new_mac:
        parser.error("[-] please specify a new mac address, use --help for more options")
    return options

def change_mac(interface,new_mac ):
    print("[+]changing mac address for" + interface + "to" + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", + new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)
