raw_address = "91.124.230.205/30"



def valid_input_check(raw_address):
    if not isinstance(raw_address, str):
        return "Error"
    if len(raw_address.split("/")) != 2:
        return "Missing prefix"
    
    return "OK"


print(valid_input_check(raw_address))
    