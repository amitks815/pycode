import re
def strongpassword(password):

    if re.match(r'[A-Za-z0-9].{8}',password)  is not None:

        print('strong password')

    else:

        print('weak password')

strongpassword('Abcdqwpe5')

