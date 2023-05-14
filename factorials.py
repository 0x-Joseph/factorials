import numpy as np


def factorial(F):
    a = 1
    for i in range(1, F+1):
        a *= i
    return a


def permutations(n, k):
    return factorial(n)//factorial(k)


def subsets(n, k):
    return permutations(n, k)//factorial(n-k)


def ask():
    while True:
        try:
            choose = input('Select: \t Permutation \033[1m(P)\033[0m' + ('or').center(10,' ') + 'Subset \033[1m(S)\033[0m \t with the pool size and length, separate with a space \t ----> \t').split(' ')
            choice = str(choose[0])
            N = int(choose[1])
            K = int(choose[2])  
        except:
            print('try again')
        if choice == 's':
            try:
                answer = subsets(N, K)
            except:
                print('OverflowError: integer division result too large for a float')
        elif choice == 'p':
            try:
                answer = permutations(N, K)
            except:
                print('OverflowError: integer division result too large for a float')
        else:
            print('Try again')
        if len(str(answer)) >= 10:
            answer = str(str(answer)[0] + '.' + str(answer)[1:4] + 'e+' + str(len(str(answer)) - 1))
            print('\t'*17 + 'ANSWER\t\t=\t' + answer + '\n')
        else:
            print('\t'*17 + 'ANSWER\t=\t' + str('{:,}'.format(answer)) + '\n')

print('\n\n\n' + ('Welcome to the collections counter!').center(200, "-") + '\n\n')

ask()
