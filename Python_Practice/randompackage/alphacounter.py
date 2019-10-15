A = 0
a =0
B = 0
C =0
D =0
e =0

def num(string):
    global A, a, B,C,D, e
    for items in string:
        if items == 'A':
            A = A+1
        elif items == 'a':
            a = a+1
        elif items == 'B':
            B = B+1
        elif items == 'C':
            C = C+1
        elif items == 'D':
            D = D+1
        elif items == 'e':
            e = e+1

num('AAAAaaBCCCDDe')
print('A'+str(A), 'a'+str(a), 'B'+str(B), 'C'+str(C), 'D'+str(D), 'e'+str(e))