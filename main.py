# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'
# Patrick Nellestijn
# Add your code after this line
#Part 1: Greet Template
def greet(name, greeting_template= 'Hello, <name>!'):
    greeting_template = greeting_template.replace('<name>', name)
    return greeting_template
#Part 2: Force
#hard de gravity op een decimaal afronden
#body heeft de waarde 
def force(mass, body='earth'):
     planet_gravity = {'sun':274, 'jupiter':24.9, 'neptune':11.2, 'saturn':10.4, 'earth':9.8, 'uranus':8.9, 'venus':8.9, 'mars':3.7, 'mercury':3.7, 'moon':1.6, 'pluto':0.6} 
     body_gravity=planet_gravity.get(body) 
     calculation_output = mass*body_gravity
     return calculation_output
#Part 3: Gravity
#formule kun je van de site overnemen
def pull(m1, m2, d):
    G=6.674 *(10**-11)
    pull = G *((m1*m2)/(d**2)) 
    return pull 
