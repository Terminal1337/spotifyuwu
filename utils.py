import json
import requests
import string
import random
from datetime import datetime
from time import gmtime

def email():
    pass
    mail = res = ''.join(random.choices(string.ascii_uppercase +string.digits, k = 7))
    return mail
def user():
    useru = requests.get("http://apis.kahoot.it/namerator")
    useru = useru.text
    useru = json.loads(useru)
    useru = str(useru['name'])
    return useru
def getyear():
    import random
    number = random.randint(1985,2007)
    return number

