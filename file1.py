from fractions import Fraction
#
# for letter in 'Python':  # 第一个实例
#     print('当前字母 :', letter)
#
# fruits = ['banana', 'apple', 'mango']
# for fruit in fruits:  # 第二个实例
#     print('当前水果 :', fruit)
#
# print("Good bye!")

x=Fraction(3,5)
print(x*2)

print(3 in {1,2,2})
print(3 in [1,2,3])

# for i in range(1,10):
#     for j in range(1,10):
#         if j<=i:
#             print(i,'*',j,'=',i*j,end="        ")
#     print("")

for k in range(0,10):
        print(k,end="     ")
print()

qw=['q','w','e']
print(qw.pop())
qw.append('asqwdadw')
print(qw.pop())

def f():
        a,b=1,1
        while True:
                yield a
                a,b=b,a+b
a=f()
for i in range(10):
        print(a.__next__(),end='    ')
