#!/bin/python 
import argparse
import sys 


parser = argparse.ArgumentParser(description="IPv4 subnet tool")

parser.add_argument("address",nargs='?',help ="IPV4/CIDR 192.168.x.x/x") 
parser.add_argument('-p','--power-of', type=int,help="prints 2 ** x")

args= parser.parse_args()



def to_binary(ip:int) -> list[int]:
    binary_list = []
    ip_split = ip.split('.')
    for item in ip_split:
        binary_list.append(format(int(item),'08b')) 
    return binary_list




def ip_string(ip_address:str) -> list[str] : 
    ip,cidr = ip_address.split('/') 
    return ip,cidr



def validate_ip_address(ip:str,cidr:str) -> bool: 
    cidr_valid = None
    ip_valid = None 
    ip_split = ip.split('.') 
    
    if len(ip_split) >= 1 or len(ip_split) == 4: 
        
        ip_valid = True
    else: 
        print("Ip Length Error")
        ip_valid = False

    if int(cidr) <= 32 and int(cidr) >= 1:
        cidr_valid = True 
    else: 
        print("CIDR Value Error")
        cidr_valid = False
    if cidr_valid and ip_valid: 
        return True 
    else: 
        return False





def cidr_to_binary(cidr: int) -> list[str]: 
    chunck = []
    mask = '1' * int(cidr) + '0' * (32 - int(cidr))
    for i in range(0,32,8): 
        chunck.append(mask[i:i+8]) 
    return chunck 

#Slicing was a great suggestion, I should study that more. 



def get_total_networks(binary_data:list[str],CLASS_DEFAULTS,default_prefix) -> int:
    if default_prefix in CLASS_DEFAULTS: 
        list_index = CLASS_DEFAULTS[default_prefix] / 8
        borrowed_bits = int(''.join(binary_data).count('1')) - CLASS_DEFAULTS[default_prefix]
        if borrowed_bits < 0: 
            return 1
        return (2 ** borrowed_bits)
    else: 
        print("tough")



def ip_parse(cidr_list:list,cidr:int) -> str: 
    binString = ''.join(cidr_list) 
    network_bits = binString[:cidr]
    host_bits = binString[cidr:]
    return network_bits,host_bits





def find_subnetMask(cidr_list,ip): 
    subnet_mask = []
    for item in cidr_list:
        resolved_ip = int(item,2)
        subnet_mask.append(str(resolved_ip))
    return '.'.join(subnet_mask)





def get_ip_class(ip_address:str) -> str: 
    ip_range = ip_address.split('.')
    ip_range = int(ip_range[0]) 
    
    if ip_range >=1 and ip_range <= 126:
        ip_class= "Class A" 
    elif ip_range >= 128 and ip_range <= 191:
        ip_class = "Class B" 
    elif ip_range >= 192 and ip_range <= 223:
        ip_class = "Class C"
    return ip_class





def get_network_id(subnet,ip):
        subnet = subnet.split('.')
        ip = ip.split('.') 
        network_id = []
        for mask_octet,octet in zip(subnet,ip): 
            if mask_octet == '255': 
                network_id.append(octet)
            elif mask_octet == '0': 
                network_id.append('0')
            else: 
                magic_number = 256 - int(mask_octet)
                network_id.append(str(int(octet) // magic_number*magic_number))
        return '.'.join(network_id)





    


if args.power_of is not None: 
    print(f"2 ** {args.power_of}\t{2**args.power_of}")
    sys.exit(0)






if args.address:  
    try :
        ip_address = args.address
        ip,cidr = ip_string(ip_address)
        
        if not validate_ip_address(ip,cidr):
            print("Invalid IP Address or CIDR")
            sys.exit(1)
        
    except ValueError: 
        print("Entry must be in Ipv4/CIDR notation")
        sys.exit(1)  


else:
    while True: 
        ip_address = input("Enter Ipv4 Address with CIDR notation: ")
        try :
            ip,cidr = ip_string(ip_address)
            if validate_ip_address(ip,cidr):
                break
            else: 
                continue
        except ValueError: 
            print("Entry must be in Ipv4/CIDR notation")
      

cidr= int(cidr)


network_bits,host_bits = ip_parse(cidr_to_binary(cidr),cidr)
my_ip = {}
CLASS_Defaults ={"Class A": 8,"Class B": 16,"Class C": 24}  

my_ip['ip_address'] = ip
my_ip['cidr'] = cidr
my_ip['ip_class'] = get_ip_class(ip)
my_ip["default-prefix"] = CLASS_Defaults[my_ip['ip_class']]
my_ip['binary_output'] = '.'.join(to_binary(ip))
my_ip['binary_mask'] = '.'.join(cidr_to_binary(cidr)) 
my_ip['subnetMask'] = find_subnetMask(cidr_to_binary(cidr),ip)
my_ip['network_bits'] = len(network_bits)
my_ip['host_bits'] = len(host_bits)
my_ip['total_networks'] = get_total_networks(cidr_to_binary(cidr),CLASS_Defaults,my_ip['ip_class'])
my_ip['total_hosts'] = (2 ** len(host_bits)) - 2 
my_ip['Network ID'] =get_network_id(my_ip['subnetMask'],my_ip['ip_address'])


for key,value in my_ip.items():
    print(f"{key}\t{value}")









