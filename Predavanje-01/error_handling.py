try:
    a = 0/0 
except ZeroDivisionError as ZeroDivisionError:
    a = 0
finally:
    print('Ishendlovao sam ovo.',a)