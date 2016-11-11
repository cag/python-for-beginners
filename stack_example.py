

class GruesAttackingError(Exception):
    pass

def method_3():
    try:
        method_2()
        method_2()
    except GruesAttackingError as e:
        print('Dispatching grue with great prejudice...')

def method_1():
    """This method does foo to bar. In the case of grues attacking, it returns 1"""
    try:
        import requests
    except ImportError:
        print('no requests :(')
    print('method 1 executing')
    raise GruesAttackingError('Grues are attacking!')

def method_2():
    method_1()
    method_1()

method_3()
