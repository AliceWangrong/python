from random import randint

def guess(maxValue,maxTimes):
    #随机生成一个整数
    #input(type(maxValue))
    #input(type(maxTimes))
    value=randint(1,maxValue)
    for i in range(maxTimes):
        prompt='Start to Guess:' if i == 0 else 'Guess again:'
        #使用异常处理结构，防止输入不是数字的情况
        try:
            x=int(input(prompt))
        except:
            print('Must input an integer bettween 1 and',maxValue)
        else:
            #猜对了
            if x==value:
                print('Congratulations!')
                break
            elif x>value:
                print('Too big')
            else:
                print('Too little')
    else:
        #次数用完还没有猜对，游戏结束，提示正确答案
        print('Game over.FALL')
        print('The value is',value)
if __name__=='__main__':
    maxValue=eval(input('请输入最大值：'))
    maxTimes=eval(input('您想猜几次：'))
    guess(maxValue,maxTimes)
