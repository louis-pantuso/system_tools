#!/bin/python 
import sys 



def to_binary(ip):
    binary_list = []
    ip_split = ip.split('.')
    for item in ip_split:
        binary_list.append(format(int(item),'08b')) 
    return binary_list

def cidr_to_binary(cidr): 
    chunck = []
    mask = '1' * int(cidr) + '0' * (32 - int(cidr))
    for i in range(0,32,8): 
        chunck.append(mask[i:i+8]) 
    return chunck 

#Slicing was a great suggestion, I should study that more. 


def ip_parse(cidr_list,cidr): 
    binString = ''.join(cidr_list) 
    network_bits = binString[:cidr]
    host_bits = binString[cidr:]
    return network_bits,host_bits



if len(sys.argv) >= 2: 
    try :
        ip_address = sys.argv[1]
        ip,cidr = ip_address.split('/')
    except ValueError: 
        print("Entry must be in Ipv4/CIDR notation")
        sys.exit(1)  


else:
    while True: 
        ip_address = input("Enter Ipv4 Address with CIDR notation: ")
        try :
            ip,cidr = ip_address.split('/')
            break
        except ValueError: 
            print("Entry must be in Ipv4/CIDR notation")
      



cidr = int(cidr)
binary_output = '.'.join(to_binary(ip))
subnet_mask = '.'.join(cidr_to_binary(cidr)) 
network_bits,host_bits = ip_parse(cidr_to_binary(cidr),cidr) 
hosts = (2 ** len(host_bits)) - 2 



print(f"Ip Address: {ip}")
print(f"Binary: {binary_output}") 

print(f"CIDR Notation: {cidr}")
print(f"CIDR Mask: {subnet_mask}")
#print(f"CIDR IP: {int(cidr_to_binary(cidr),2)}")
print(f"Network Bits: {len(network_bits)}\tHost Bits: {len(host_bits)}") 
print(f"Total Hosts: {hosts}")
