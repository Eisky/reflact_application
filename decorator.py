def outer(fun):
    def wrapper(arg):
        print 'verification code'
        print 'failed'
        result = fun(arg)
        return result

    return wrapper


@outer
def fun1(arg):
    print arg
    return 'Have you got another chance'


@outer
def fun2(arg):
    print arg
    return 'Have you got another chance'


@outer
def fun3(arg):
    print arg
    return 'Have you got another chance'


print fun1('good luck')
print fun2('good luck')
print fun3('good luck')
