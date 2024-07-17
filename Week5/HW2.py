def validate_password(password):
    lowerLetters = False
    capitalLetters = False
    digits = False
    specialChars = False
    for c in password:
        if c.islower(): lowerLetters+=True
        if c.isupper(): capitalLetters+=True
        if c.isdigit(): digits+=True
        if c in "$#@": specialChars+=True
    return lowerLetters and capitalLetters and digits and specialChars and len(password)>=6 and len(password)<=12

def validate_passwords(passwords):
    passwords = passwords.split(",")
    valid_passwords = ""
    for password in passwords:
        if validate_password(password):
            valid_passwords += password + ", "
    return valid_passwords[:-3]

print(validate_passwords("ABd1234@1,a F1#,2w3E*,2We3345,fffF3d4##")=="ABd1234@1, fffF3d4#")