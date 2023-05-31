import string

# String Text
text = '''
    +_*/%<><=>=== || && ! 0 (0) 0 =^
    123456789sjikgbjhxv
    +_*/%<><=>=== || && ! 0 (0) 0 = .:^
    19718627367sjikgbjhxv
'''

# Tokens
identifier = list(string.ascii_letters)
operator = ['&&','||','==','<=','>=','+','-','*','/','=','<' ,'>']
symbol = ['_','{', '}', '(', ')','[',']', '.','"', ':', ',']

# Global variables
white_space = ''
lexeme = ''
run = True
num = 0

# Scannning Text
for i, char in enumerate(text):
    if run:
        if (i+1 < len(text)): 
            # Identifier Token [a-Z]
            if text[i+1] in identifier:
                print("IDENTIFIER "+ text[i+1])
            # Operator Token
            if text[i+1] in operator:
                if i+2 < len(text):
                    strc = text[i+1] + text[i+2] 
                    if strc in operator:
                        print("OPERATOR "+ strc)
                        run = False
                        num = i+2
                    else:
                        print("OPERATOR "+ text[i+1])
            # Symbol Token
            if text[i+1] in symbol:
                print("SYMBOL "+ text[i+1])
    else:
        if i > num:
            run = True
