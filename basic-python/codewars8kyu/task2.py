n=[123]
def validate_code(code):
    for i in range(1):  # runs only once, i = 0
        if i == 1:
            return("True")
        elif i == 2:
            return("True")
        elif i == 3:
            return("True")
        else:
            return ("False")  # i = 0, so this runs
i=validate_code(n)
print(i)