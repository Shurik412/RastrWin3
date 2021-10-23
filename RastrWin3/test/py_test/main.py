from mod_test import decor

n = 1


@decor
def pt(n):
    print(str(n))

