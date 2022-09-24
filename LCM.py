word = "2/4+2/6"
factor = word.split("+")

num_tot = list()
den_tot = list()

for value in factor:
    num = value.split("/")
    # print(num)

    res = [eval(i) for i in num]
    
    if (res[1] % res[0]) == 0:
        num = res[0] / res[0]
        den = res[1] / res[0]

        num_tot.append(num)
        den_tot.append(den)

    else:
        num_tot.append(res[0])
        den_tot.append(res[1])

print(num_tot)
print(den_tot)

den = den_tot[0] * den_tot[1]
num1 = (den / den_tot[0]) + num_tot[0]
num2 = (den / den_tot[1]) + num_tot[1]

num = num1 + num2
print(str(num) +"/"+ str(den))

def try_nums(num, den):
    # for i in list:
    i = 3
    if num % i == 0 and den % i == 0:
        lcm_num = num / i
        lcm_den = den / i
        
        print(lcm_num, lcm_den)


try_nums(num, den)