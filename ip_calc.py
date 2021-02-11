import doctest

from numbers import Number


def get_binary(number: Number) -> str:
    """
    Additional function to get binary number without "0b" at the beginning with 8 bit length
    """
    return bin(number)[2:].rjust(8, '0')


def get_binary_ip(ip: str) -> str:
    """
    Function returns binary view of IP
    """
    ip_lst = ip.split(".")
    binary_lst = [get_binary(int(num)) for num in ip_lst]
    return "".join(binary_lst)


def valid_input_check(raw_address):
    """
    Function check if raw_address is valid
    """
    if not isinstance(raw_address, str):
        return "Error"
    if len(raw_address.split("/")) != 2:
        return "Missing prefix"

    return None


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

    if valid_input_check(raw_address) != None:
        return valid_input_check(raw_address)

    ip = get_ip_from_raw_address(raw_address)
    mask = raw_address.split('/')[1]

    binary_ip = get_binary_ip(ip)

    binary_mask = ""
    binary_mask = binary_mask.rjust(int(mask), '1').ljust(32, '0')

    network_address_binary = "".join(
        [str(int(c1) & int(c2)) for c1, c2 in zip(binary_ip, binary_mask)])

    network_address_str = f'{int(network_address_binary[:8], 2)}.{int(network_address_binary[8:16], 2)}.{int(network_address_binary[16:24], 2)}.{int(network_address_binary[24:], 2)}'

    return network_address_str


def get_broadcast_address_from_raw_address(raw_address: str) -> str:
    """
    Function return Broadcast Address from raw address

    >>> get_broadcast_address_from_raw_address("91.124.230.205/30")
    '91.124.230.207'
    """
    if valid_input_check(raw_address) != None:
        return valid_input_check(raw_address)

    ip = get_ip_from_raw_address(raw_address)
    mask = raw_address.split('/')[1]

    binary_ip = get_binary_ip(ip)

    binary_mask = ""
    binary_mask = binary_mask.rjust(int(mask), '1').ljust(32, '0')

    reversed_mask = "".join([str((int(m) + 1 - int(m) * 2))
                             for m in binary_mask])

    broadcast_address = "".join([str(int(c1) | int(c2))
                                 for c1, c2 in zip(binary_ip, reversed_mask)])

    broadcast_address_str = f'{int(broadcast_address[:8], 2)}.{int(broadcast_address[8:16], 2)}.{int(broadcast_address[16:24], 2)}.{int(broadcast_address[24:], 2)}'

    return broadcast_address_str


def get_binary_mask_from_raw_address(raw_address: str) -> str:
    """
    Function return Binary Mask from raw address

    >>> get_binary_mask_from_raw_address("91.124.230.205/30")
    '11111111.11111111.11111111.11111100'
    """
    if valid_input_check(raw_address) != None:
        return valid_input_check(raw_address)

    mask = raw_address.split('/')[1]
    binary_mask = ""
    binary_mask = binary_mask.rjust(int(mask), '1').ljust(32, '0')

    binary_mask_str = f'{binary_mask[:8]}.{binary_mask[8:16]}.{binary_mask[16:24]}.{binary_mask[24:]}'

    return binary_mask_str


def get_ip_class_from_raw_address(raw_address: str) -> str:
    """
    Function return IP Class from raw address

    >>> get_ip_class_from_raw_address("91.124.230.205/30")
    'A'
    """
    if valid_input_check(raw_address) != None:
        return valid_input_check(raw_address)

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


def get_first_usable_ip_address_from_raw_address(raw_address: str) -> str:
    """
    Function return Usable IP Address from raw address

    >>> get_first_usable_ip_address_from_raw_address("91.124.230.205/30")
    '91.124.230.205'
    """
    if valid_input_check(raw_address) != None:
        return valid_input_check(raw_address)

    network_address = get_network_address_from_raw_address(raw_address)
    network_address_lst = network_address.split(".")

    network_address_lst[-1] = str(int(network_address_lst[-1]) + 1)

    return ".".join(network_address_lst)


def get_penultimate_usable_ip_address_from_raw_address(raw_address: str) -> str:
    """
    Function return Penultimate Usable IP Address from raw address

    >>> get_penultimate_usable_ip_address_from_raw_address("91.124.230.205/30")
    '91.124.230.205'
    """
    if valid_input_check(raw_address) != None:
        return valid_input_check(raw_address)

    broadcast_address = get_broadcast_address_from_raw_address(raw_address)
    broadcast_address_lst = broadcast_address.split(".")

    broadcast_address_lst[-1] = str(int(broadcast_address_lst[-1]) - 2)

    return ".".join(broadcast_address_lst)


def get_number_of_usable_hosts_from_raw_address(raw_address: str) -> Number:
    """
    Function return Number of Usable Hosts from raw address

    >>> get_number_of_usable_hosts_from_raw_address("91.124.230.205/30")
    2
    """
    if valid_input_check(raw_address) != None:
        return valid_input_check(raw_address)

    N = int(raw_address.split("/")[-1])
    return pow(2, 32-N) - 2


def check_private_ip_address_from_raw_address(raw_address: str) -> bool:
    """
    Function return Number of Usable Hosts from raw address

    >>> check_private_ip_address_from_raw_address("91.124.230.205/30")
    False
    """
    if valid_input_check(raw_address) != None:
        return valid_input_check(raw_address)

    ip_main_part = raw_address.split("/")[0]
    if int(ip_main_part[0]) == 10 or int(ip_main_part.split(".")[0]) == 192 and int(ip_main_part.split(".")[1]) == 168 or \
            int(ip_main_part[0]) == 172 and (16 <= int(ip_main_part[1]) <= 32):
        return True
    return False


doctest.testmod()
