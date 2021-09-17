def print_formatted(n):
    # your code goes here
    # w=len(bin(st)[2:])
            # This line of code responses to this requirement: "Each value should be                 space-padded to match the width of the binary value of n."
        #   when we use bin() method, it returns binary value but it starts with 0b. For            example : bin(1) = 0b1, so to remove '0b' from the beginning we use string              slicing.

    # for i in range(1,st+1):

    #     print (str(i).rjust(w,' '),str(oct(i)[1:]).rjust(w,' '),str(hex(i)[2:].upper()).rjust(w,' '),str(bin(i)[2:]).rjust(w,' '),sep=' ')
    results = []

    for i in range(1, n+1):
        decimal = str(i)
        octal = str(oct(i)[2:])
        hex_ = str(hex(i)[2:]).upper()
        binary = str(bin(i)[2:])

        results.append([decimal, octal, hex_, binary])

    width = len(results[-1][3])  # largest binary number

    for i in results:
        print(*(rep.rjust(width) for rep in i))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)