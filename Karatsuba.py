
def multiply(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        a = int(str(x)[:int(round(len(str(x))/2,0))])
        b = int(str(x)[int(round(len(str(x))/2,0)):])
        c = int(str(y)[:int(round(len(str(y))/2,0))])
        d = int(str(y)[int(round(len(str(y))/2,0)):])
        #print(a, b, c, d)
        b_len = int(len(str(x)))-int(round(len(str(x))/2,0))
        d_len = int(len(str(y)))-int(round(len(str(y))/2,0))
        m = (10**(b_len+d_len))*multiply(a, c)
        n = multiply(b, d)
        o = (10**b_len)*multiply(a, d)+(10**d_len)*multiply(c, b)
        return m+n+o

multiply(123, 56783)
