import sys

def add_everything_up(a, b):
    try:
        try_res = a + b
        return round(try_res, 3)


    except TypeError as exs:
        print(a,b,sep='')

    #sys.exit() #при такой команде сработает только первый вызов функции
             
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
