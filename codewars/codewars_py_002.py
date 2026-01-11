def dec2hex(decimal):
    remainder = 1
    hexadecimal = []
    while decimal != 0:
        remainder = decimal % 16
        hexadecimal.append(f"{remainder}")
        decimal = decimal // 16
    
    hex_dict = {"10":"A", "11":"B", "12":"C", "13":"D", "14":"E", "15":"F"}
    for i in range(len(hexadecimal)):
        if hexadecimal[i] in hex_dict:
            hexadecimal[i] = hex_dict[hexadecimal[i]]
    return "".join(hexadecimal)

def rgb(r, g, b):
    r_hex = dec2hex(r)
    g_hex = dec2hex(g)
    b_hex = dec2hex(b)
    return "".join([r_hex, g_hex, b_hex])

print(rgb(0,0,0))

    