def validate(name, pwd):
    if name == 'sunki' and pwd == '123':
        return True
    else:
        return False


try:
    res = validate('sunki', '129')
    if res:
        print 'success'
    else:
        raise Exception('failed')
except Exception as e:
    print 'record to rizhi'
    print e