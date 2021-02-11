import doctest


def get_binary(number):
    """
    Additional function to get binary number without "0b" at the beginning with 8 bit length
    """
    return bin(number)[2:].rjust(8, '0')


def get_binary_ip(ip):
    """
    Function returns binary view of IP
    """
    ip_lst = ip.split(".")
    binary_lst = [get_binary(int(num)) for num in ip_lst]
    return "".join(binary_lst)  



def get_ip_from_raw_address(raw_address: str) -> str:
    """
    Funcntion gets IP from raw address
    
    >>> get_ip_from_raw_address("192.168.1.15/24")
    '192.168.1.15'
    """
    return raw_address.split("/")[0]



def get_network_address_from_raw_address(raw_address: str) -> str:
    """
    Function return Network Address from raw address

    >>> get_network_address_from_raw_address("91.124.230.205/30")
    '91.124.230.204'
    """
    ip = get_ip_from_raw_address(raw_address)
    mask = raw_address.split('/')[1]

    binary_ip = get_binary_ip(ip)

    binary_mask = ""
    binary_mask = binary_mask.rjust(int(mask), '1').ljust(32, '0')

    network_address_binary = "".join([str(int(c1) & int(c2)) for c1, c2 in zip(binary_ip, binary_mask)])

    network_address_str = f'{int(network_address_binary[:8], 2)}.{int(network_address_binary[8:16], 2)}.{int(network_address_binary[16:24], 2)}.{int(network_address_binary[24:], 2)}'

    return network_address_str


def get_broadcast_address_from_raw_address(raw_address):
    """
    Function return Broadcast Address from raw address

    >>> get_broadcast_address_from_raw_address("91.124.230.205/30")
    '91.124.230.207'
    """
    ip = get_ip_from_raw_address(raw_address)
    mask = raw_address.split('/')[1]

    binary_ip = get_binary_ip(ip)

    binary_mask = ""
    binary_mask = binary_mask.rjust(int(mask), '1').ljust(32, '0')

    reversed_mask = "".join([str((int(m) + 1 - int(m) * 2)) for m in binary_mask])

    broadcast_address = "".join([str(int(c1) | int(c2)) for c1, c2 in zip(binary_ip, reversed_mask)])

    broadcast_address_str = f'{int(broadcast_address[:8], 2)}.{int(broadcast_address[8:16], 2)}.{int(broadcast_address[16:24], 2)}.{int(broadcast_address[24:], 2)}'

    return broadcast_address_str


def get_binary_mask_from_raw_address(raw_address):
    """
    Function return Binary Mask from raw address

    >>> get_binary_mask_from_raw_address("91.124.230.205/30")
    '11111111.11111111.11111111.11111100'
    """ 

    mask = raw_address.split('/')[1]
    binary_mask = ""
    binary_mask = binary_mask.rjust(int(mask), '1').ljust(32, '0')

    binary_mask_str = f'{binary_mask[:8]}.{binary_mask[8:16]}.{binary_mask[16:24]}.{binary_mask[24:]}'

    return binary_mask_str

def get_ip_class_from_raw_address(raw_address):
    """
    Function return IP Class from raw address

    >>> get_ip_class_from_raw_address("91.124.230.205/30")
    'A'
    """ 

    ip = get_ip_from_raw_address(raw_address)
    ip_list = ip.split(".")
    ip_class = int(ip_list[0])

    if 0 <= ip_class <= 127:
        return "A"
    elif 128 <= ip_class <= 191:
        return "B"
    elif 192 <= ip_class <= 223:
        return "C"
    elif 224 <= ip_class <= 239:
        return "D"
    elif 240 <= ip_class <= 255:
        return "E"


def get_first_usable_ip_address_from_raw_address(raw_address):
    """
    >>> get_first_usable_ip_address_from_raw_address("91.124.230.205/30")
    """

    network_address = get_network_address_from_raw_address(raw_address)
    network_address_lst = network_address.split(".")

    
doctest.testmod()
