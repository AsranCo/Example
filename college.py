###############################################################
# words = [['s', 'a', 'l', 'a', 'm'], ['k', 'h', 'o', 'o', 'b', 'i', '?']]
#
# # for word in words:
# for char in words:
#     print(char, end='')
# print()

###############################################################
# def Zarb(n):
#     m = 1
#     while n >= m:
#         for i in range(1, n + 1):
#             print(i * m, end=' ')
#         print()
#         m = m + 1
#
#
# Zarb(int(input()))

###############################################################
# def Mazrab():
#     p, d = map(int, input().split())
#     while True:
#         if 0 <= d % p <= p / 2:
#             print(d)
#             break
#         else:
#             d += d
#             continue
#
#
# Mazrab()

###############################################################


# s = list()
# while (s2 := input()) != "test":
#     s.append(s2)
#     print(s)

# import math
#
# n = 9
# k = 4
# result = math.comb(n, k)
# print('comb(n, k) :', result)
###############################################################
# import math
# x = int(input())
# y = math.ceil(math.pow(x, 5/3) + math.tan(math.radians(x)))
# z = math.floor(math.pow(math.pi, (2 + math.atan(math.pow(math.sin(math.radians(x)), 2)))))
# print(math.gcd(y, z))

###############################################################

# from datetime import date, datetime
#
#
# def day_calculator(n):
#     sajjad_bdate = date(1999, 1, 14)
#     birthday = n.split("-")
#     bi = date(int(birthday[0]), int(birthday[1]), int(birthday[2]))
#     age = (bi - sajjad_bdate).days
#     if int(age) > 0:
#         return (age)
#     else:
#         return ("Not yet born")
###############################################################
# def karim(n):
#     x = []
#     l = []
#     for f in range(n):
#         x.append(str(input()))
#     for i in range(n):
#         l.append(len(set(x[i])))
#     l.sort()
#     print(l[-1])
#
#
# karim(int(input()))


###############################################################
# rang = int(input())
# ramz = input()
#
# li = []
# c = 0
# for f in range(rang):
#     li.append(str(input()))
# for i in range(len(ramz)):
#     if li[i].find(ramz[i]) > 4:
#         print(9 - li[i].find(ramz[i]))
#         c = c + (9 - li[i].find(ramz[i]))
#     else:
#         print( li[i].find(ramz[i]))
#         c = c + li[i].find(ramz[i])
# print(c)
#
###############################################################
# print(str("{:b}".format(int(input()))).count("1"))
###############################################################

# import re
#
#
# def validate_email(email):
#     regex = r'\b[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Za-z]{3}\b'
#     if (re.fullmatch(regex, email)):
#         return True
#     else:
#         return False
#
#
# def validate_phone(number):
#     regex = r'^(?:09|\+989|00989)?(\d{9})$'
#     if (re.fullmatch(regex, number)):
#         return True
#     else:
#         return False
###############################################################!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import math
# import re
#
#
# def solve(arr):
#     list = []
#     list = (arr.replace('=', "").replace('+', "")).split("  ")
#     h = list[2]
#     a = list[0]
#     b = list[1]

# solve("10# + 50 = 10052")
###############################################################

def type(x):
    result = []
    for f in x:
        if f.startswith('=') and len(result) != 0:
            result.pop()
        else:
            result.append(f)
    print(''.join(result))


type(str(input()))