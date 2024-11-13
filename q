# https://aftershock.news/?q=node/386307&full
def filter_sps(lst, filters, key):
    final = []
    for elem in lst:
        if filters(elem[key]):
            final += [elem]
    return final

def devie_3(value):
    return value % 3 == 0



def calc(oper, x, y):
    return oper(x,y)

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x, y):
    return x * y

def div(x,y):
    return x / y

def reduce_lst(lst, reducing_func, initial):
    for elem in lst:
        initial = reducing_func(initial, elem)
    return initial


def reduce_fnc(lst_func, elem):
    final = elem
    for func in lst_func:
        final = func(final, elem)
    return final
print(reduce_fnc([mul, mul, mul], 5))
