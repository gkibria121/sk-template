from sk_calculator import Calculator



calculator = Calculator()
scripts = '''
def c1(x):

    return x+1'''

calculator.set_scripts(scripts)

result = calculator.evaluate('c1(1+2+3)')
print(result)