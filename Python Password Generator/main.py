import string
from random import *

value = string.ascii_letters + string.punctuation + string.digits

password = "".join(choice(value) for x in range(randint(8, 16)))

print('\n Your New Password is: ', password)