# перевод в нормальный вид для 10 < с.с. < 17
def translating(lst_a):
    d = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    res = []
    result = ''
    lst_a = normal(lst_a)
    for a in lst_a:
        try:
            res.append(d[a])
        except:
            res.append(a)
    for i in res:
        result += str(i)
    return result

#убрать нули из начала
def normal(lst_a):
    k = 0
    for i in range(len(lst_a)):
        if lst_a[i] != 0:
            break
        else:
            k += 1
    if k == len(lst_a):
        return [0]
    else:
        return lst_a[k:]

#перевод из 10 в C систему счисления
def change_base(a,c):
    res = []
    tmp = a
    while tmp > 0:
        res.insert(0,tmp % c)
        tmp //= c
    return res

# перевод числа в список по разрядам
def listening(a):
    res = []
    while a > 0:
        res.insert(0,a%10)
        a //= 10
    return res

# =    =    =   =   =   =   =   =    =   =  
# n1,n2 ниже это списки с цифрами исходных чисел

# выравнивание двух чисел по разрядам 
def align(n1,n2):
    diff = abs(len(n1) - len(n2))
    if len(n1) > len(n2):
        for i in range(diff):
            n2.insert(0,0)
        return n1,n2
    elif len(n1) < len(n2):
        for i in range(diff):
            n1.insert(0,0)
        return n1,n2
    return n1,n2

# сравнение какое число больше
def compare(n1,n2):
    n1,n2 = align(n1,n2)
    for i in range(len(n1)):
        if n1[i] > n2[i]:
            return n1
        elif n1[i] < n2[i]:
            return n2
        if i == len(n2):
            return n1

# = =   =   =   =   =   =   =   =   =   =
# арифметические действия

# сумма
def add(n1,n2,c):
    n1,n2 = align(n1,n2)
    k = len(n1)
    tmp = [0] * (k+1)
    res = []
    for i in range(k-1,-1,-1):
        if (tmp[i+1] + n1[i] + n2[i]) >= c:
            res.insert(0,(tmp[i+1] + n1[i] + n2[i]) - c)
            tmp[i] += 1
        else:
            res.insert(0,tmp[i+1] + n1[i] + n2[i])
    res.insert(0,tmp[0])
    return res

# разность
def subtr(n1,n2,c):
    n1,n2 = align(n1,n2)
    k = len(n1)
    tmp = [0]*k
    res = []
    for i in range(k-1,-1,-1):
        if (tmp[i] + n1[i] - n2[i]) < 0:
            n1[i-1] -= 1
            tmp[i] += c
            res.insert(0, (tmp[i] + n1[i]-n2[i]))
        else:
            res.insert(0, (tmp[i] + n1[i]-n2[i]))
    return res

# произведение
def mult(n1,n2,c):
    res = []
    n1,n2 = align(n1,n2)
    for i in range(1,len(n1)+1):
        st = []
        tmp = [0] * (len(n1) + 2)
        for j in range(1,len(n2)+1):
            if n1[-i] * n2[-j] + tmp[-j] >= c:
                st.insert(0,(n1[-i] * n2[-j] + tmp[-j]) % c)
                tmp[-j-1] += (n1[-i] * n2[-j] + tmp[-j]) // c
            else:
                st.insert(0,n1[-i] * n2[-j] + tmp[-j])
        for razrad in range(i-1):
            st.append(0)
        st.insert(0, tmp[-len(n2)-1] % c)
        st.insert(0, tmp[-len(n2)-1] // c)
        res = add(st,res,c)
    return res

A = 510382647109285
B = 51923648

a2 = translating(change_base(A,2))    
b2 = translating(change_base(B,2)) 
a3 = translating(change_base(A,2))    
b3 = translating(change_base(B,2))
a8 = translating(change_base(A,8))    
b8 = translating(change_base(B,8)) 
a16 = translating(change_base(A,16))
b16 = translating(change_base(B,16))
print('\nПеревод из 10 в N с.с.:\n','0bA:',a2,'0bB:',b2,'\nA^3:',a3,'B^3:',b3,'\n0oA:',a8,'0oB:',b8,'\n0xA:',a16,'0xB:',b16,'\n')

lst = [2,3,8,16]
for i in lst:
    print(f'сложение в {i} CC:\n',translating(add(change_base(A,i),change_base(B,i),i)))
    print(f'вычитание в {i} CC:\n',translating(subtr(change_base(A,i),change_base(B,i),i)))
    print(f'умножение в {i} CC:\n',translating(mult(change_base(A,i),change_base(B,i),i)))



