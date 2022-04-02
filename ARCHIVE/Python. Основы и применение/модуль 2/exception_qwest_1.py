try:
    foo()
    #5 / 0
    #assert 5 == '5'
except (ZeroDivisionError) as e:
    '''
    name = str(type(e))
    name = name[name.find('\'') + 1 : name.rfind('\'')]
    print(name)
    '''
    #print(str(type(e).__name__))
    print('ZeroDivisionError')
except (ArithmeticError) as e:
    #print(str(type(e).__name__))
    print('ArithmeticError')
except (AssertionError) as e:
    #print(str(type(e).__name__))
    print('AssertionError')