'''
A basic python function with everybody's favourite developer greeting.
'''

def usual_greeting(greeting):
    '''This function returns an appropriate greeting depending on the argumeny
    
    Args:
        greeting (str): a string representing a greeting.
    Returns:
        A string that matches the argument.
    Raises:
        N/A
    '''
    if greeting == 'hi':
        return 'Hello World'
    elif greeting == 'bye':
       return 'Goodbye Earth'
    return 'Try Again'