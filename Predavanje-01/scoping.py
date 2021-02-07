# NAMESPACE
# 1 - local
# 2 - global
# 3 - built -in


#VAR_1 = 5

#def some_function():
 #   VAR_1 = 6
 #   print(VAR_1)

#some_function()

def ime_funkcije():
    global ime_globalne
    ime_globalne = 52 
    print(ime_globalne)

ime_globalne = 12

ime_funkcije()

print(ime_globalne)