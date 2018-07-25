def shout(wrapped):
    def inner(*args, **kwargs):
        print('BEFORE!')
        ret = wrapped(*args, **kwargs)
	print type(ret)
        print('AFTER!')
        return ret
    return inner

@shout
def doge():
    print('such wow!')
    return 1

doge()


def decorator2():
    print "print decorator"

@decorator2()
def dekorowana():
    print "print dekorowanej"

print dekorowana

