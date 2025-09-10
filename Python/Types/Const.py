class CONSTANTS:
    '''
    Create a class that holds variables with CONSTANT constraints
    Simulates the behaviour of a CONSTANT
    '''
    # create a custom Exception for when trying to overwrite a const value
    class ConstError(TypeError): pass

    def __setattr__(self, name, value):
        '''
        Overwrite the default function that is called when trying
        to assign a value to a variable.

        IF a variable with the name exists, raise and error, aka make it a constant
        ELSE create the variable with the value
        '''
        # if a variable exists with the same name, raise an errorself.
        # this is what makes it act like a constant
        if self.__dict__.has_key(name):
            raise self.ConstError("Can't rebind const {}".format(name))

        # if no variables exists, allow the creation
        self.__dict__[name]=value



if __name__ == '__main__':
    ##### TESTING THE IMPLEMENTATION
    _const = CONSTANTS() # allows creations of constants

    # THIS SHOULD BE ALLOWED
    _const.CONST_NAME = 21
    print("Constant Value is now: {}".format(_const.CONST_NAME))

    # THIS SHOULD RAISE A ConstError
    try:
        _const.CONST_NAME = 33
    except Exception as e:
        print("A {} error was raised, because you tried to rebind/overwrite a constant".format(e))
    finally:
        print("Testing done")
