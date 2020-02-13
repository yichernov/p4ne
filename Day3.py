def classify(i):
    if not ( i % 2):
        return "43"
    elif not (i % 3):
        return "45"
    elif not (i % 5):
        return "46"
    else:
        return "42"

i = 1

while i <= 20:
    j = 1
    while j <= 20:
        print (i * j, " ", end = "")
        j += 1
    print ("")
    i += 1