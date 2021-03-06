'''
CodeWars kata from codewars.com

Write a function called repeat_str which repeats the given string src exactly count times.
repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"
'''

def repeat_str(repeat, string):
    #create a variable and keep adding to it, 
    #later we return the variable because we can't return print()
    new_str=''
    for j in range(repeat):
        new_str +=string
    return new_str    

#------another way
def repeat_str(repeat, string):
    new_str=''
    new_str=repeat*string
    return new_str 
'''
BECAUSE
2*'String' -> StringString
4*('string',) -> ('string', 'string', 'string', 'string')
3*('good', 'morning') -> ('good', 'morning', 'good', 'morning', 'good', 'morning)
'''
