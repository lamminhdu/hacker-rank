
import math

def compareTriplets(a, b):
    a_win = 0
    b_win = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            a_win += 1
        elif a[i] < b[i]:
            b_win += 1
    return [a_win, b_win]



def diagonalDifference(arr):
    lef_to_right = 0
    right_to_left = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                lef_to_right += arr[i][j]
            if (i + j) == (len(arr) - 1):
                right_to_left += arr[i][j]
    diff = abs(lef_to_right - right_to_left)
    return diff



def plusMinus(arr):
    n = len(arr)
    pos = 0
    neg = 0
    zer = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zer += 1
    print(f"{(pos / n):.6f}")
    print(f"{(neg / n):.6f}")
    print(f"{(zer / n):.6f}")



def staircase(n):
    stairs = [['#' for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i):
            stairs[i][j] = ' '
    stairs.reverse()
    for i in stairs:
        for j in i:
            print(j,end="")
        print("")



def sum_arr(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_arr(arr[1:])

def miniMaxSum(arr):
    sum_of_4 = []
    for i in arr:
        sub_arr = arr[:]
        sub_arr.remove(i)
        sum_of_4.append(sum_arr(sub_arr))
    print(min(sum_of_4), max(sum_of_4))



def birthdayCakeCandles(candles):
    tallest = max(candles)
    num_tallest = 0
    for i in candles:
        if i == tallest:
            num_tallest += 1
    return num_tallest



def timeConversion(s):
    split_arr = s.split(':')
    sec = ''
    for letter in split_arr[2]:
        if letter == 'A' and split_arr[0] == '12':
            split_arr[0] = '00'
        elif letter ==  'P' and split_arr[0] != '12':
            split_arr[0] = int(split_arr[0]) + 12
        elif letter == 'A' or letter == 'P' or letter == 'M':
            pass
        else:
            sec += letter
    split_arr[2] = sec
    s_format = f"{split_arr[0]}:{split_arr[1]}:{split_arr[2]}"
    return s_format


def split_time(s):
    split_arr = s.split(':')
    sec = ''
    amp = ''
    for letter in split_arr[2]:
        if letter == "P" or letter == "A" or letter == 'M':
            amp += letter
        else:
            sec += letter
    split_arr[2] = sec
    split_arr.append(amp)
    return split_arr

def timeConversion2(s):
    split_arr = split_time(s)
    if split_arr[3] == 'AM' and split_arr[0] == 12:
        split_arr[0] = '00'
    elif split_arr[3] == 'PM' and split_arr[0] != 12:
        split_arr[0] = int(split_arr[0]) + 12
    s_format = f"{split_arr[0]}:{split_arr[1]}:{split_arr[2]}"
    return s_format



def convert_fruit(position, distances):
    location = []
    for distance in distances:
        actual = distance + position
        location.append(actual)
    return location

def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apples = 0
    count_oranges = 0
    apples_location = convert_fruit(a, apples)
    oranges_location = convert_fruit(b, oranges)
    for apple in apples_location:
        if apple in range(s,t+1):
            count_apples += 1
    for orange in oranges_location:
        if orange in range(s,t+1):
            count_oranges += 1
    print(count_apples)
    print(count_oranges)

def kangaroo(x1, v1, x2, v2):
    "x1 < x2"
    meet = 'NO'
    if v1 <= v2:
        return meet
    else:
        s1 = x1
        s2 = x2
        while s1 < s2:
            s1 += v1
            s2 += v2
        if s1 == s2:
            meet = 'YES'
        return meet



def find_lcm(num1, num2):
    mul = num1 * num2
    gcd = math.gcd(num1, num2)
    lcm = mul / gcd
    return lcm

def find_lcm_arr(a):
    lcm = a[0]
    for i in a[1:]:
        lcm = find_lcm(lcm, i)
    return lcm

def lcm_mul(lcm):
    mul = 1
    i = 1
    arr_lcm = []
    while mul < 100:
        mul = lcm * i
        i += 1
        arr_lcm.append(mul)
    return arr_lcm

def gcd_division(gcd):
    arr_gcd = []
    for i in range(1, gcd+1):
        if gcd % i == 0:
            arr_gcd.append(i)
    return arr_gcd

def getTotalX(a, b):
    lcm = find_lcm_arr(a)
    gcd = math.gcd(*b)
    arr_lcm = lcm_mul(lcm)
    arr_gcd = gcd_division(gcd)
    between = 0
    for gcd in arr_gcd:
        if gcd in arr_lcm:
            between += 1
    return between



def breakingRecords(scores):
    highest = scores[0]
    lowest = scores[0]
    break_highest = 0
    break_lowest = 0
    for score in scores:
        if score > highest:
            break_highest += 1
            highest = score
        if score < lowest:
            break_lowest += 1
            lowest = score
    return [break_highest,break_lowest]



def birthday(s, d, m):
    n = len(s)
    ways = 0
    for i in range(n-m+1):
        sum_segment = 0
        for j in range(m):
            sum_segment += s[i+j]
            #print(f"i={i}, j={j}, sum={sum_segment}"
        if sum_segment == d:
            ways += 1
    return ways




def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n-1):
        for j in range(i+1,n):
            sum_num = ar[i] + ar[j]
            print(f"i={i}, j={j}, sum={sum_num}")
            if sum_num % k == 0:
                count += 1
    return count


def divisibleSumPairs2(n, k, ar):
    count = 0
    br = ar[:]
    for i in ar:
        br.remove(i)
        for j in br:
            sum_num = i + j
            #print(f"i={i}, j={j}, sum={sum_num}")
            if sum_num % k == 0:
                count += 1
    return count



def count_bird_type(arr,num):
    count = 0
    for i in arr:
        if i == num:
            count += 1
    return count

def migratoryBirds(arr):
    frequent = [0] * 5
    print(frequent)
    for i in range(5):
        count = count_bird_type(arr, i+1)
        frequent[i] = count
    #print(frequent)
    id = frequent.index(max(frequent)) + 1
    return id


def migratoryBirds2(arr):
    birds = [0]*5
    for i in arr:
        birds[i-1] += 1
    #print(birds)
    return birds.index(max(birds)) + 1



def dayOfProgrammer(year):
    return 1



def bonAppetit(bill, k, b):
    sub_bill = bill[:]
    anna_eat = bill[k]
    sub_bill.remove(anna_eat)
    b_except = sum(sub_bill) / 2
    if b_except < b:
        print(b - b_except)
    if b_except == b:
        print("Bon Appentit")



def count_color(color, ar):
    count = 0
    for i in ar:
        if i == color:
            count += 1
    return count

def sockMerchant(n, ar):
    colors = list(set(ar))
    dict_type = {}
    pairs = 0
    for color in colors:
        dict_type[color] = count_color(color, ar)
    print(dict_type)
    for color in dict_type.keys():
        pair_color = dict_type[color] // 2
        pairs += pair_color
    return pairs



def pageCount(n, p):
    """n: book pages, p: page to find, return min left_to_right, right_to_left turn

Test case 1:
print(pageCount(5, 3))
return: int
1

Test case 2:
print(pageCount(6, 2))
return: int
1

Test case 3:
print(pageCount(5, 4))
return: int
0
    """
    odd_page = []
    even_page = []
    for i in range(n+1):
        if i % 2 == 0:
            even_page.append(i)
        else:
            odd_page.append(i)
    turn = max(len(odd_page),len(even_page))
    if p % 2 == 0:
        left_to_right = even_page.index(p)
        right_to_left = turn - 1 - left_to_right
    else:
        left_to_right = odd_page.index(p)
        right_to_left = turn - 1 - left_to_right
    return min(left_to_right, right_to_left)



def countingValleys(steps, path): #take lot of time
    valley = 0
    sea_level = 0
    path_arr = list(path)
    sea_level_path = []
    for i in range(steps):
        if path_arr[i] == 'U':
            sea_level += 1
        elif path_arr[i] == 'D':
            sea_level -= 1
        if sea_level == -1 and path_arr[i+1] == 'U':
            valley += 1
        #sea_level_path.append(sea_level)
        #print(sea_level_path)
    return valley


def countingValleys2(steps, path):
    valley = 0
    sea_level = 0
    sea_level_path = []
    for i in path:
        if i == 'U':
            sea_level += 1
        else:
            sea_level -= 1
        if sea_level == 0 and i == 'U':
            valley += 1
        sea_level_path.append(sea_level)
    print(sea_level_path)
    return valley



def icecreamParlor(m, arr):
    for i in range(len(arr)-1):
        for j in range(i+1, n):
            sum = arr[i] + arr[j]
            if sum == m:
                return [i+1, j +1]



def balancedSums(arr):#time limit exceeded 100 000 element
    balance = "NO"
    for i in range(len(arr)):
        left = [j for j in arr[:i]]
        right = [j for j in arr[(i+1):]]
        if sum(left) == sum(right):
            balance = "YES"
    return balance


def balancedSums2(arr):#time limit exceeded 100 000 element
    n = len(arr)
    s = 'NO'
    for i in range(n):
        sum_left = sum_right = 0
        for l in range(i):
            sum_left += arr[l]
            #print(f"i={i}, l={l}, sum_left={sum_left}")
        for r in range((i+1),n):
            sum_right += arr[r]
            #print(f"i={i}, r={r}, sum_right={sum_right}")
        if sum_left == sum_right:
            s = 'YES'
    return s


def balancedSums3(arr):#time limit exceeded 100 000 element
    n = len(arr)
    s = 'NO'
    sum_arr = sum(arr)
    for i in range(n):
        sum_left = 0
        for l in range(i):
            sum_left += arr[l]
        sum_right = sum_arr - sum_left - arr[i]
        #print(f"i={i}, sum={sum_arr}, sum_left={sum_left}, sum_right={sum_right}")
        if sum_left == sum_right:
            s = 'YES'
    return s

def balancedSums_final(arr): #code runing ok for all test !!!
    sum_arr = sum(arr)
    s = 'NO'
    sum_left = 0
    sum_right = 0
    n = len(arr)
    for i in range(n):
        if i == 0:
            sum_left = 0
        elif i == (n - 1):
            sum_left = sum_arr
        else:
            sum_left += arr[i-1]
        sum_right = sum_arr - sum_left - arr[i]
        print(sum_left,i,sum_right)
        if sum_left == sum_right:
            s = 'YES'
    return s

def balancedSums_best_code(arr):
    x  = 0
    sum_arr = sum(arr)
    for y in arr:
        if (2 * x == sum_arr - y):
            return 'YES'
        else:
            x += y
    return 'NO'


def getMoneySpent(keyboards, drives, b):
    total_price = []
    for key in keyboards:
        for drive in drives:
            sum = key + drive
            if sum <= b:
                total_price.append(sum)
    if not total_price:
        return -1
    else:
        return max(total_price)



def catAndMouse(x, y, z):
    cat_A_dis = abs(z - x)
    cat_B_dis = abs(z - y)
    print(cat_A_dis,cat_B_dis)
    if cat_A_dis == cat_B_dis:
        case = 'Mouse C'
    elif cat_A_dis > cat_B_dis:
        case = 'Cat B'
    else:
        case = 'Cat A'
    return case



def pickingNumbers(a):
    nums = set(a)
    max_lens = []
    print(nums)
    for i in nums:
        smaller = [j for j in a if (j - i == -1) or (j - i == 0)]
        greater = [j for j in a if j - i == 1]
        max_len = max(len(smaller),len(greater))
        max_lens.append(max_len)
        #print(i,smaller,greater,max_len)
    return max(max_lens)



def hurdleRace(k, height):
    max_height = max(height)
    dose = max_height - k
    if dose > 0:
        return dose
    else:
        return 0



def designerPdfViewer(h, word):
    # Write your code here
    alpha_index = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5,
                   'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
                   'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17,
                   's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23,
                   'y': 24, 'z': 25
                   }
    word_height = []
    for letter in word:
        index = alpha_index[letter]
        word_height.append(h[index])

    tallest = max(word_height)
    word_len = len(word)
    return tallest * word_len


def utopianTree(n):
    # Write your code here
    h = 1
    for i in range(n):
        if i % 2 == 0:
            h *= 2
        else:
            h += 1
    return h


def two_sum2(arr, target):
    pre_map = {}  # val : index
    for i, v in enumerate(arr):  # index and value
        diff = target - v
        if diff in pre_map:
            print(pre_map[diff], i)
        else:
            pre_map[v] = i

def viralAdvertising(n):
    # Write your code here
    shared = 5
    sum_like = 0
    sum_people = 0
    for i in range(1,n+1):
        like = math.floor(shared / 2)
        sum_people += shared
        shared = like * 3
        sum_like += like
        print(i,like,shared,sum_like,sum_people)
    return sum_like



def saveThePrisoner(n, m, s):
    # Write your code here
    remain = m % n
    if (remain + s) > n:
        result = s + remain - n - 1
    else:
        result = s + remain - 1
    if result == 0:
        return n
    else:
        return result

def saveThePrisoner1(n, m, s): # time out
    # Write your code here
    arr = list(range(1,n+1))
    remain = m % n
    index = arr.index(s) + remain - 1
    if index > n-1:
        index -= n
    print(arr,remain, index)
    return arr[index]

def circularArrayRotation(a, k, queries):
    for i in range(k):
        last = a.pop()
        a.insert(0,last)
    result = []
    for i in queries:
        result.append(a[i])
    return result


def permutationEquation(p):
    # Write your code here
    y_arr = []
    for i in range(1,len(p)+1):
        y = p.index(p.index(i) + 1) + 1
        y_arr.append(y)
    return y_arr

def jumpingOnClouds(c, k):
    e = 100
    n = len(c)
    for i in range(1,n+1):
        if i == n:
            i = 0
        if i % k == 0:
            e -= 1
            if c[i] == 1:
                e -= 2
            print(i,e)
    return e

def jumpingOnClouds1(c, k):
    e = 100
    n = len(c)
    for i in range(n):
        if i % k == 0:
            e -= 1
            if c[i] == 1:
                e -= 2
    return e

def jumpingOnClouds2(c, k):
    e = 100
    n = len(c)
    i = k % n
    e -= c[i]*2 + 1
    while i != 0:
        i = (i+k) % n
        e -= c[i]*2 + 1
        print(i,e)
    return e

def findDigits(n):
    # Write your code here
    d = 0
    num = n
    while num != 0:
        split = num % 10
        num = int(num / 10)
        if split != 0:
            if n % split == 0:
                d += 1
    return d

def appendAndDelete(s, t, k):
    if s == t:
        return 'Yes'
    else:
        append = 0
        delete = 0
        s_sub = s
        t_sub = t
        i = 0
        if len(s) > len(t):
            t_sub += (len(s)-len(t))*" "
        elif len(s) < len(t):
            s_sub += (len(t)-len(s))*" "
        while s_sub[i] == t_sub[i]:
            i += 1
        for x in range(i,len(s)):
            delete += 1
        for y in range(i,len(t)):
            append += 1
        total = delete + append
        print(append,delete,total)
        if total == k:
            return 'Yes'
        else:
            return 'No'

def squares(a, b):
    return 1

def libraryFine(d1, m1, y1, d2, m2, y2):
    d_diff = d1 - d2
    m_diff = m1 - m2
    y_diff = y1 - y2
    print(d_diff,m_diff,y_diff)
    if y_diff < 0 or (y_diff == 0 and m_diff < 0) or (y_diff == 0 and m_diff == 0 and d_diff < 0):
        fine = 0
    elif y_diff == 0 and m_diff == 0:
        fine = 15 * d_diff
    elif y_diff == 0 and m_diff > 0:
        fine = 500 * m_diff
    elif y_diff > 0:
        fine = 10000
    return fine



def min_except_zero(arr): #constraints arr < 1000
    min_arr = 1000
    for i in arr:
        if i <= min_arr and i != 0:
            min_arr = i
    return min_arr

def cutTheSticks(arr):
    # Write your code here
    res = []
    for i in range(len(arr)):
        if max(arr) == 0:
            break
        else:
            min_arr = min_except_zero(arr)
            cut = 0
            for j in range(len(arr)):
                if arr[j] != 0:
                    arr[j] -= min_arr
                    cut += 1
            res.append(cut)
            print(arr,min_arr,cut)
    return res



def jumpingOnClouds(c):
    # Write your code here
    path_count = 0
    path = []
    for i in range(len(c)):
        if c[i] != 1:
            break
    path.append(i)
    while i < (len(c)-2):
        if c[i+2] == 1:
            i += 1
        else:
            i += 2
        path_count += 1
        path.append(i)
    if path[-1] != len(c)-1:
        path.append(len(c)-1)
        path_count += 1
    return path_count


def jumpingOnClouds1(c):
    # Write your code here
    path_count = 0
    path = []
    n = len(c)
    for i in range(n):
        if c[i] != 1:
            print(i)
            path.append(i)
            while path[-1] != n-1:
                if i < n-2:
                    if c[i+2] == 1:
                        i += 1
                    else:
                        i += 2
                else:
                    i += 1
                path.append(i)
                path_count += 1
            break
    print(path)
    return path_count



def acmTeam(topic):#runtime error
    # Write your code here
    n = len(topic)
    m = len(topic[0])
    team = {}
    for i in range(n-1):
        for j in range(i+1,n):
            subject = []
            for k in range(m):
                know = int(topic[i][k]) + int(topic[j][k])
                if know > 0:
                    subject.append(k+1)
            team[str(i+1)+str(j+1)] = subject
    print(team)

    max_sub = 0
    for value in team.values():
        if len(value) > max_sub:
            max_sub = len(value)

    max_count = 0
    for value in team.values():
        if len(value) == max_sub:
            max_count += 1
    return [max_sub, max_count]


def acmTeam1(topic):#RUNTIME
    # Write your code here
    n = len(topic)
    m = len(topic[0])
    subject = []
    for i in range(n-1):
        for j in range(i+1,n):
            know_count = 0
            for k in range(m):
                know = int(topic[i][k]) + int(topic[j][k])
                if know > 0:
                    know_count += 1
            subject.append(know_count)
    print(subject)

    count = 0
    for t in subject:
        if t == max(subject):
            count +=1
    return [max(subject), count]



def taumBday(b, w, bc, wc, z):
    # Write your code here
    check = abs(bc-wc)
    if check > z:
        cost = (b+w)*min(bc,wc)
        if bc > wc:
            cost += b*z
        else:
            cost += w*z
    else:
        cost = b*bc + w*wc
    return cost


def kaprekarNumbers(p, q):
    # Write your code here
    step = 0
    for i in range(p,q+1):
        square = i*i
        digit = len(str(i))
        right = square % 10**digit
        left = int(square/10**digit)
        if left + right == i:
            print(i, end=" ")
            step += 1
    if step == 0:
        print("INVALID RANGE")

def minimumDistances(a):#two sum ?
    # Write your code here
    dis_record = []
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i] == a[j]:
                dis = j - i
                dis_record.append(dis)
    return -1 if len(dis_record) == 0 else min(dis_record)



def howManyGames(p, d, m, s):#fail
    # Return the number of games you can buy
    buy = 0
    total_price = p
    while total_price <= s:
        if p > m:
            p -= d
        else:
            p -= 0
        buy += 1
        total_price += p
    return buy

def howManyGames1(p, d, m, s):#fail
    # Return the number of games you can buy
    if s < p:
        return 0
    elif s == p:
        return 1
    else:
        buy = 1 + int((p-m)/d)
        total = buy*(p-m)
        print(buy,total)
        while total + m < s:
            total += m
            buy += 1
            print(buy,total)
        return buy

def howManyGames2(p,d,m,s):#OK
    buy = 0
    total = 0
    while total + p <= s:
        total += p
        p -= d
        buy += 1
        if p <= m:
            p = m
    return buy



def chocolateFeast(n, c, m):
    chocolate = int(n/c)
    wrap = chocolate
    while wrap >= m:
        new_chocolate = int(wrap/m)
        chocolate += new_chocolate
        wrap = new_chocolate + wrap % m
    return chocolate



def serviceLane(width, cases):
    # Write your code here
    res = []
    for i in range(len(cases)):
        min_width = width[cases[i][0]]
        for j in range(cases[i][0],cases[i][1]):
            if width[j] < min_width:
                min_width = width[j]
        res.append(min_width)
    return res



def workbook(n, k, arr):
    # Write your code here
    special = 0
    pages = []
    for i in range(n):
        page = []
        j = 1
        while j <= arr[i]:
            if len(page) < k:
                page.append(j)
            if len(page) == k:
                pages.append(page)
                page = []
            j += 1
        if page:
            pages.append(page)

    print(pages)
    print(len(pages))

    for x in range(len(pages)):
        for y in pages[x]:
            if x + 1 == y:
                special += 1
    return special

def flatlandSpaceStations(n, c): #time out
    m = len(c)
    c.sort()
    if n == m:
        return 0
    elif n-m == 1:
        return 1
    else:
        dis = []
        for i in range(n):
            dis_i = []
            for j in c:
                if i == j:
                    dis_j = 0
                elif abs(i - j) == 1:
                    dis_j = 1
                else:
                    dis_j = abs(i-j)
                dis_i.append(dis_j)
            dis.append(min(dis_i))
        print(dis)
        return max(dis)

def flatlandSpaceStations1(n, c):
    c.sort()
    #maxd = max(c[0], n-1 - c[-1])
    print(maxd)
    for i in range(len(c)-1):
        maxd = max((c[i+1]-c[i])//2, maxd)
        print(i,maxd)
    return maxd

def flatlandSpaceStations2(n,c):
    c.sort()
    answer = 0
    for i in range(1,len(c)):
        print(f"i={i}, answer = {answer}, ")
        answer = max(answer, (c[i] - c[i-1]) // 2)
        print(answer)
    answer = max(answer,c[0], n-1 - c[-1])
    return answer


