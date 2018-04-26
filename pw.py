def minimum(password):
    upper = [ x for x in password if x.isupper()]
    lower = [ x for x in password if x.islower()]
    number = [ x for x in password if x.isdigit()]

    if len(upper) > 0:
        if len(lower) > 0:
            if len(number) > 0:
                return True
    return False

def strength_checker(password):
    strength = 0
    upper = [ x for x in password if x.isupper()]
    lower = [ x for x in password if x.islower()]
    number = [ x for x in password if x.isdigit()]
    alnum = [ x for x in password if not x.isalnum()]


    if len(lower) > 0:
        strength += 1

    if len(upper) > 0:
        strength += 3

    if len(number) > 0:
        strength += 3

    if len(alnum) > 0:
        strength += 3

    
    return strength

print minimum("hello")    
print minimum("Hello")    
print minimum("Hello3")    

print strength_checker("adfwqd")

print strength_checker("QWDasdqw")
print strength_checker("DQwd123")
print strength_checker("e2edw1f##")
print strength_checker("dqwwdqwdE2$")

