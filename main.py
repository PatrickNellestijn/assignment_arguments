# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
from types import BuiltinMethodType

#Part 1: Greet Template
def greet(name, greeting_template= 'Hello, <name>!'):
    greeting_template = greeting_template.replace('<name>', 'name')
    return name

#Part 2: Force
#hard de gravity op een decimaal afronden
#body heeft de waarde 
def force(mass, body='earth'):
     planet_gravity = {'sun':274.0, 'jupiter':24.92, 'neptune':11.15, 'saturn':10.44, 'earth':9.798, 'uranus':8.87, 'venus':8.87, 'mars':3.71, 'mercury':3.71, 'moon':1.62, 'pluto':0.58} 
     body_gravity = planet_gravity.get(body) 
     force = round((mass*body_gravity), 1) #geeft foutmelding mbt afronding
     return force

#Part 3: Gravity
#formule kun je van de site overnemen
def pull(m1, m2, d):
    G = 6.674 *((m1*m2)/(d**2))
    return pull
