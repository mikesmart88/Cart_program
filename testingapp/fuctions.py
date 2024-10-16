# create yr fuction here

import random,string

def rand_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
     """
     used to generate random  string with a given lenght.
     """
     return ''.join(random.choice(chars) for _ in range(size))

