

class GruesAttackingError(Exception):
    pass

class MeanGruesAttackingError(GruesAttackingError):
    pass

class NiceGruesAttackingError(GruesAttackingError):
    pass

class OutOfMoneyError(Exception):
    pass

def method_3():
    try:
        method_2()
        method_2()
    except GruesAttackingError as e:
        print('Dispatching grue with great prejudice...')
    print('continuing...')

def method_2():
    try:
        method_1()
        method_1()
    except OutOfMoneyError as e:
        print('Pulling funds from Switzerland')
    except GruesAttackingError as e:
        print('Doing the error-resolving dance with grue')
    except:
        print('Doing a normal error-resolving dance')
    else:
        print('Yay, nothing bad happened!')
    finally:
        print('No matter what')

def method_1():
    """This method does foo to bar. In the case of grues attacking, it returns 1"""
    try:
        import requests
    except ImportError:
        print('no requests :(')
    print('method 1 executing')
    # raise MeanGruesAttackingError

method_2()
