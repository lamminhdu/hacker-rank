import math
import string

alphabet = string.ascii_letters


def compareTriplets(arr, brr):
    # given 2 array, compare each element and return score
    if len(arr) != len(brr):
        return None
    else:
        n = len(arr)
        a_point = 0
        b_point = 0
        for i in range(n):
            if arr[i] > brr[i]:
                a_point += 1
            elif arr[i] < brr[i]:
                b_point += 1
    return [a_point, b_point]


def diagonalDifference(arr):

    left_to_right = 0  # "\" diagonal
    right_to_left = 0  # "/" diagonal
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i == j:
                left_to_right += arr[i][j]
            if i + j == n - 1:
                right_to_left += arr[i][j]

    return abs(left_to_right - right_to_left)


def plusMinus(arr):
    pos = 0
    neg = 0
    n = len(arr)

    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1

    pos_res = pos / n
    neg_res = neg / n
    zer_res = 1 - pos_res - neg_res
    print(f"{pos_res:06f}")
    print(f"{neg_res:06f}")
    print(f"{zer_res:06f}")


def staircase(n):
    """
        #
       ##
      ###
     ####
    """
    for i in range(n):
        for j in range(n):
            if i + j >= n-1:
                print('#', end='')
            else:
                print(' ', end='')
        print("")


def staircase_2(n):
    stair = [['#' for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(i):
            stair[i][j] = ' '

    stair.reverse()
    for i in range(n):
        for j in range(n):
            print(stair[i][j], end='')
        print("")


def miniMaxSum(arr):
    # given 5 elements of an array, find min max of an sub-array with 4 elements
    sum_sub = []
    for i in arr:
        brr = arr[:]
        brr.remove(i)
        sum_sub.append(sum(brr))
    return [min(sum_sub), max(sum_sub)]


def birthdayCakeCandles(candles): # time out
    # return the number of tallest candles
    count = 0
    for i in candles:
        if i == max(candles):
            count += 1
    return count


def birthdayCakeCandles_2(candles):
    # return the number of tallest candles
    count = 0
    tallest = max(candles)
    for i in candles:
        if i == tallest:
            count += 1
    return count


def timeConversion(s):
    # convert am/pm format to 24h format
    time = s.split(':')
    if time[2][2] == 'P' and time[0] != '12':
        time[0] = str(int(time[0]) + 12)
    elif time[2][2] == 'A' and time[0] == '12':
        time[0] = '00'
    return time[0] + ':' + time[1] + ':' + time[2][0:2]


def timeConversion_split(s):
    # find a method to split string
    # special = [':', 'A', 'P','M', ' ']
    # num = [str(i) for i in range(10)]
    # time = []
    # n = len(s)
    # i = 0
    #
    # while i < n:
    #     if i != ':':
    #         start = i
    #         while i < n and s[i] not in special:
    #             i += 1
    #         end = i
    #
    #         time.append(s[start:end])
    #     i += 1

    symbol = ['A', 'M', 'P']
    num = ''
    convention = ''
    time = []
    for i in s:
        if i != ':' and i not in symbol:
            num += i
        else:
            if num != '':
                time.append(num)
                num = ''

        if i in symbol:
            convention += i

    time.append(convention)


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # count fruit in s ~ t
    count_apples = 0
    count_oranges = 0
    apples_location = [(i+a) for i in apples]
    oranges_location = [(j+b) for j in oranges]

    for x in apples_location:
        if x in range(s, t+1):
            count_apples += 1

    for y in oranges_location:
        if y in range(s, t+1):
            count_oranges += 1

    print(count_apples)
    print(count_oranges)


def kangaroo(x1, v1, x2, v2):
    # constraint x1 < x2
    # if they meet?
    if v1 <= v2:
        return 'NO'
    else:
        s1 = x1
        s2 = x2
        while s1 < s2:
            s1 += v1
            s2 += v2

        if s1 == s2:
            return 'YES'

        return 'NO'


def lcm_num(a, b):
    # sub program of getTotalX
    return int(a * b / math.gcd(a, b))


def lcm_arr(arr):
    # sub program of getTotalX
    lcm = arr[0]
    for i in arr[1:]:
        lcm = lcm_num(lcm, i)
    return lcm


def getTotalX(arr, brr):
    # count the number between 2 array that satisfy
    # 1: num % lcm(arr) == 0   2: gcd(brr) % num == 0
    count = 0
    lcm_of_arr = lcm_arr(arr)
    gcd_of_brr = math.gcd(*brr)
    mul = lcm_of_arr
    i = 1
    while mul <= gcd_of_brr:
        if gcd_of_brr % mul == 0:
            count += 1
        i += 1
        mul = lcm_of_arr * i
    return count


def breakingRecords(scores):
    # return count of breaking record
    min_record = scores[0]
    max_record = scores[0]
    count_min = 0
    count_max = 0

    for i in scores:
        if i > max_record:
            count_max += 1
            max_record = i
        if i < min_record:
            count_min += 1
            min_record = i

    return [count_max, count_min]


def birthday(s, d, m):
    # determine to many sub array that satisfy len = m, sum = d
    ways = 0

    for i in range(len(s) - m + 1):
        sum_sub = 0
        for j in range(i, i+m):
            print(i,j)
            sum_sub += s[j]
        if sum_sub == d:
            ways += 1

    return ways


def divisibleSumPairs(n, k, arr):
    # how many pairs in arr that sum == k
    pairs = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (arr[i] + arr[j]) % k == 0:
                pairs += 1
    return pairs


def migratoryBirds(arr):
    birds = [0 for i in range(6)]
    for i in arr:
        birds[i] += 1
    print(birds)
    return birds.index(max(birds))


def migratoryBirds_2(arr):
    birds_occurrences = {}
    for i in arr:
        if i not in birds_occurrences:
            birds_occurrences[i] = 1
        else:
            birds_occurrences[i] += 1
    print(birds_occurrences)
    return max(sorted(birds_occurrences), key= lambda x: birds_occurrences[x]) # sorted()


def is_leap_year_gre(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


def is_leap_year_jul(year):
    if year % 4 == 0:
        return True
    return False


def dayOfProgrammer(year):
    # 256 days -> date
    date = ['00', '09', str(year)]
    if year == 1918:
        date[0] = str(13+14)
    elif year < 1918:
        if is_leap_year_jul(year):
            date[0] = '12'
        else:
            date[0] = '13'
    else:
        if is_leap_year_gre(year):
            date[0] = '12'
        else:
            date[0] = '13'
    return '.'.join(date)


def bonAppetit(bill, k, b):
    # check bill, Anna did not eat bill[k]
    bill.pop(k)
    b_actual = sum(bill) / 2
    if b_actual == b:
        print("Bon Appetit")
    else:
        print(int(b - b_actual))


def sockMerchant(n, arr):
    # how many pairs in a bunch of sock
    pairs = 0
    color = {}
    for i in arr:
        if i not in color:
            color[i] = 1
        else:
            color[i] += 1

    for j in color:
        pairs += color[j] // 2
    return pairs


def pageCount(n, p):
    # the minimum turn to page p
    left_side = [i for i in range(n+1) if i % 2 == 0]
    right_side = [i for i in range(n+1) if i % 2 != 0]
    max_page = max(len(left_side), len(right_side))

    if p in left_side:
        first_to_last = left_side.index(p)
        last_to_first = max_page - left_side.index(p) - 1
    else:
        first_to_last = right_side.index(p)
        last_to_first = max_page - right_side.index(p) - 1

    return min(first_to_last, last_to_first)


def pageCount_2(n, p):
    # p // 2: page to flip from front to back
    # n // 2: how many page
    # p // 2 + back to front = n // 2
    return min(p//2, n // 2 - p // 2)


def countingValleys(steps, path):
    # Write your code here
    sea_level = 0
    valleys = 0
    for i in path:
        if i == 'U':
            sea_level += 1
        else:
            sea_level -= 1
        if sea_level == 0 and i == 'U':
            valleys += 1
    return valleys


def getMoneySpent(keyboards, drives, b):
    prices = []
    for keyboard in keyboards:
        for drive in drives:
            price = keyboard + drive
            if keyboard + drive <= b:
                prices.append(price)
    if prices:
        return max(prices)
    return -1


def getMoneySpent_2(keyboards, drives, b):
    # use sort
    n = len(keyboards)
    m = len(drives)
    keyboards.sort(reverse=True)
    drives.sort()
    max_price = -1
    ind = 0
    """
    wrong logical
    for i in range(n):
        for j in range(i, m):
            price = keyboards[i] + drives[j]
            print(i,j)
            if price > b:
                break
            else:
                max_price = max(max_price, price)
    return max_price
    """
    for i in range(n):
        for j in range(m):
            price = keyboards[i] + drives[j]
            if price > b:
                ind += 1  # move to next keyboard when price higher than budget
                break
            else:
                max_price = max(max_price, price)
    return max_price


def catAndMouse(x, y, z):
    # which cat catch the mouse first?
    cat_a = abs(z-x)
    cat_b = abs(z-y)
    if cat_a < cat_b:
        res = 'Cat A'
    elif cat_a > cat_b:
        res = 'Cat B'
    else:
        res = 'Mouse C'
    return res


def pickingNumbers(arr):
    n = len(arr)
    i = 0
    j = 0
    max_element = 0
    while i < n - 1:
        element = 0
        min_element = arr[i]
        j = i + 1
        while j < n:
            if arr[j] < min_element:
                min_element = arr[j]

            if abs(min_element - arr[j]) <= 1:
                element += 1
                j += 1
            else:
                break
        max_element = max(element, max_element)
        i = j
        i += 1
    return max_element

arr = [1,1,2,2,4,5,5,5]
print(pickingNumbers(arr))