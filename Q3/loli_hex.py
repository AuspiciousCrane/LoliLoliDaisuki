class HexError(Exception): pass
class NotIntegerError(HexError): pass
class InvalidArgument(HexError): pass

hex_dict = {
    10 : "A",
    11 : "B",
    12 : "C",
    13 : "D",
    14 : "E",
    15 : "F"
}

def toHex(n):
    global hex_dict
    hex_list = []
    if not isinstance(n, int):
        raise NotIntegerError("Input must be of type integer")

    if n < 0:
        raise InvalidArgument("Input must be a positive integer")

    new_num = n
    if new_num == 0:
        return "0"

    while(new_num != 0):
        num = new_num % 16
        if num < 10:
            hex_list.append(str(num))
        elif num < 16:
            hex_list.append(hex_dict[num])

        new_num = new_num // 16

    return "".join(reversed(hex_list))


if __name__ == "__main__":
    print(toHex(14))
    print(toHex(171))
