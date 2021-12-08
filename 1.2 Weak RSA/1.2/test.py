from decimal import Decimal, getcontext


def extendedGCD(a, b):
    # a*xi + b*yi = ri
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = extendedGCD(b, a % b)
        # q = gcd(a, b) = gcd(b, a%b)
        x, y = y, (x - (a // b) * y)
        return x, y, q


def computeD(fn, e):
    (x, y, r) = extendedGCD(fn, e)
    # y maybe < 0, so convert it
    if y < 0:
        return fn + y
    return y


def fastExpMod(b, e, c):
    result = 1
    while e != 0:
        if (e & 1) == 1:
            result = (result * b) % c
        e >>= 1
        b = (b * b) % c
    return result




if __name__ == '__main__':

    fn = Decimal(11847876695566808647134954951870590393117193296131251542200692595639321022401123346441157131014295655762725022967825490633303186145944627520136638868945418812747627610604032584586874348016314795284876845435984906591009541435035137757927045930120166091052532007135448012720378872553595874998892222830448159229216)
    e = Decimal(65537)

    getcontext().prec = 1000

    d = computeD(fn, e)
    print(d)



