#global scope
x = 'global x'

def function():
    #local scope
    x = 'local x'

function()
print(x)

####################################

#global
name = 'Berf'

def changeName(new_name):
    #local
    global name
    name = new_name
    print(name)

changeName('Güler')
print(name)

######################################

name = 'global string'

def greeting():
    name = 'berf'
    def hello():
        name = 'güler'
        print('hello ' + name)

    hello()
greeting()

########################################

x = 50

def test():
    global x
    print(f'x : {x}')

    x = 100
    print(f'changed x to {x}' )

test()

print(x)