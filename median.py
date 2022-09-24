def median(list):
    list.sort()
    length = len(list)
    num = length/2

    if (num %2) == 0:
        ans = ((list[int(num) -1 ] + list[int(num)]) / 2)
        print(ans)

    else:
        solve = num / 2
        id = round(solve)
        print(list[id])

median([-1,-2,-2,3])
median([1,2,3])