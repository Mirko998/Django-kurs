#def ime_funkcije(*args):
#        print(args)


#ime_funkcije(1,2,23,432,4,324,23,'Mirko')


dict_1 = {
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5
}

#print(dict_1)

#for key, value in dict_1.items():
#    print(key, value)


def ime_funkcije(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

ime_funkcije(name='Mirko', age=22)