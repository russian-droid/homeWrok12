'''
Write a function called repeat_str which repeats the given string src exactly count times.
repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"
'''

def repeat_str(repeat, string):
    new_str=''
    for j in range(repeat):
        new_str +=string
    return new_str    
