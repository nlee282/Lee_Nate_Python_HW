def count_chars(s):
    digits = 0
    letters = 0

    for c in s:
        if c.isdigit():
            digits+=1
        if c.isalpha():
            letters+=1
    print("LETTERS: " + str(letters))
    print("DIGITS: " + str(digits))

count_chars("Hello world! 123")
count_chars("Abcdjfoidsjaofds 239478329423! 123")
count_chars("'.';.;',';.'@#$#$#@$@$][[][]].'.;.'.'abc")
count_chars("            e.            ")
count_chars("")