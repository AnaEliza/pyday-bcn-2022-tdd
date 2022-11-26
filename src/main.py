# import

# {}

mapping = {"D":"3",
           "O":"666",
           "J":"5",
           "P":"7",
           "Y":"999",
           "T": "8",
           "E": "33",
           "S": "7777",
           "C": "222",
           "U": "88",
           "Z": "9999",
           "L": "555",
           " ": "0",
           "I": "444",
           "K": "55",
           "H": "44",
           "N": "66",
           "A": "2",
           "R": "777",
           "G": "4",
           "M": "6",
}

def encode(msg: str) -> str:
    output = ""
    for letter in msg:
        code = mapping[letter]
        if output and output[-1] == code[0]:
            output += "_"
        output += code

    return output

    return output
