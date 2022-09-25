num_tot = list()
den_tot = list()

def fetch_digits(question):
    factor = question.split("+")

    for value in factor:
        num = value.split("/")
        res = [eval(i) for i in num]
        
        # if (res[1] % res[0]) == 0:
        #     num = res[0] / res[0]
        #     den = res[1] / res[0]

        num_tot.append(res[0])
        den_tot.append(res[1])

    return num_tot, den_tot
    
def fetch_LCM(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm

word = input('Enter fraction: ')
fetch_digits(word)

lcm = fetch_LCM(den_tot[0], den_tot[1])
lcm = int(lcm)
num1 = (lcm / den_tot[0]) * num_tot[0]
num2 = (lcm / den_tot[1]) * num_tot[1]

num = num1 + num2
num = int(num)

def reducefract(n, d):
    '''Reduces fractions. n is the numerator and d the denominator.'''
    def gcd(n, d):
        while d != 0:
            t = d
            d = n%d
            n = t
        return n
    assert d!=0, "integer division by zero"
    assert isinstance(d, int), "must be int"
    assert isinstance(n, int), "must be int"
    greatest=gcd(n,d)
    n/=greatest
    d/=greatest
    return int(n), int(d)

def get_whole_number(x, y):
    if x > y:
        rem = x % y
        whole = x // y
        if rem == 0:
            print(f"{int(whole)}/{int(y)}")
        else:
            print(f"{int(whole)} {int(rem)}/{int(y)}")

    else:
        print(str(x) +'/'+ str(y))

rc = reducefract(num, lcm)
get_whole_number(rc[0], rc[1])