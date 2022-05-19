'''
***************Strings vs Bytes******************
'''
#A String in Python3 is a sequence of unicode characters
#While bytes are sequence of raw 8-bit values

def main():
    b = bytes([0x41,0x42,0x43])
    print(b)

    s = 'String'
    print(s)

    #combining both
    #print(s+b) #ERROR :Must be str, not bytes i.e. Cant treat bytes as string
    #TODO : Bytes and string needs to be properly encoded and decoded for working together
    #------>>decode the byte into a string
    s2 = b.decode('utf-8')# decode using utf-8 type is encoding
    print(s2)
    #------>>encode the string into a bytes
    b2 = s.encode('utf-8')#encode using utf-8 --> ASCII char ---> bytes
    print(b+b2)

    #---->string to hexadecimal values
    b3 = s.encode('utf-32')#encode using utf-32 --> Hex char ---> bytes
    print(b3)


if __name__=='__main__':
    main()
