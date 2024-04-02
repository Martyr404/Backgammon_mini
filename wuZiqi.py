import random


rowLabel="0  1  2  3  4  5  6  7  8  9 ";
colLabel=[str(num)+'  +  +  +  +  +  +  +  +  +' for num in range(1,10)]
userActionHistory=[]
occupiedPos=[]


def printQipan():
    print(rowLabel)
    print('\n'.join(colLabel))
    print("注：▲代表玩家，■代表电脑\n")


def userWin():
    flag=False
    for r in range(0,9):#每行检查
        for c in range(3,16,3):
            if(colLabel[r][c]==colLabel[r][c+3]==colLabel[r][c+6]==colLabel[r][c+9]==colLabel[r][c+12]=='▲'):
                flag=True
    for c in range(3,28,3):#每列检查
        for r in range(0,5):
            if(colLabel[r][c]==colLabel[r+1][c]==colLabel[r+2][c]==colLabel[r+3][c]==colLabel[r+4][c]=='▲'):
                flag=True
    for r in range(0,5):#向右对角线检查
        for c in range(3,16,3):
            if(colLabel[r][c]==colLabel[r+1][c+3]==colLabel[r+2][c+6]==colLabel[r+3][c+9]==colLabel[r+4][c+12]=='▲'):
                flag=True
    for r in range(0,5):#向左对角线检查
        for c in range(15,28,3):
            if(colLabel[r][c]==colLabel[r+1][c-3]==colLabel[r+2][c-6]==colLabel[r+3][c-9]==colLabel[r+4][c-12]=='▲'):
                flag=True
    return flag


def aiWin():
    flag = False
    for r in range(0, 9):  # 每行检查
        for c in range(3, 16, 3):
            if (colLabel[r][c] == colLabel[r][c + 3] == colLabel[r][c + 6] == colLabel[r][c + 9] == colLabel[r][
                c + 12] == '■'):
                flag = True
    for c in range(3, 28, 3):  # 每列检查
        for r in range(0, 5):
            if (colLabel[r][c] == colLabel[r + 1][c] == colLabel[r + 2][c] == colLabel[r + 3][c] == colLabel[r + 4][
                c] == '■'):
                flag = True
    for r in range(0, 5):  # 向右对角线检查
        for c in range(3, 16, 3):
            if (colLabel[r][c] == colLabel[r + 1][c + 3] == colLabel[r + 2][c + 6] == colLabel[r + 3][c + 9] ==
                    colLabel[r + 4][c + 12] == '■'):
                flag = True
    for r in range(0, 5):  # 向左对角线检查
        for c in range(15, 28, 3):
            if (colLabel[r][c] == colLabel[r + 1][c - 3] == colLabel[r + 2][c - 6] == colLabel[r + 3][c - 9] ==
                    colLabel[r + 4][c - 12] == '■'):
                flag = True
    return flag


def aiDectUserWin():#检测下一步推荐ai做什么
    flag=False
    defendChoice=[]
    tpe=0
    for r in range(0,9):#每行检查,tpe代号1
        for c in range(3,22,3):
            if(colLabel[r][c]==colLabel[r][c+3]==colLabel[r][c+6]=='▲'):
                flag=True
                tpe=1
                defendChoice.append((10*(r+1)+int(c/3-1)))
                defendChoice.append((10*(r+1)+int(c/3+3)))
    for c in range(3,28,3):#每列检查,tpe代号2
        for r in range(0,7):
            if(colLabel[r][c]==colLabel[r+1][c]==colLabel[r+2][c]=='▲'):
                flag=True
                tpe = 2
                defendChoice.append((10*r+int(c/3)))
                defendChoice.append((10*(r+2)+int(c/3)))
    for r in range(0,7):#向右对角线检查,tpe代号3
        for c in range(3,22,3):
            if(colLabel[r][c]==colLabel[r+1][c+3]==colLabel[r+2][c+6]=='▲'):
                flag=True
                tpe = 3
                defendChoice.append((10*r+int(c / 3-1)))
                defendChoice.append((10*(r+4)+int(c / 3+3)))
    for r in range(0,7):#向左对角线检查,tpe代号4
        for c in range(9,28,3):
            if(colLabel[r][c]==colLabel[r+1][c-3]==colLabel[r+2][c-6]=='▲'):
                flag=True
                tpe = 1
                defendChoice.append((10*r+int(c / 3 + 1)))
                defendChoice.append((10*(r + 4)+int(c / 3 - 3)))
    return flag,defendChoice


def setPos(Num,icon:str):#玩家落子行为
    global occupiedPos
    if (not (10<Num<100)) or (not (Num % 10!=0)) or (Num in occupiedPos):
        while 1:
            print("请输入[11,100)之间的数，个位不能为0,且不能是棋盘非空闲区域")
            Num=int(input("请输入新坐标："))
            if (10<Num<100) and (Num % 10!=0) and (Num not in occupiedPos):
                break
    shiWei = Num // 10
    geWei = Num % 10
    global colLabel
    colLabel[shiWei - 1] = colLabel[shiWei - 1][:3 * geWei] + icon + colLabel[shiWei - 1][3 * geWei + 1:]
    occupiedPos.append(Num)

def userAction(userNum):#玩家行动
    setPos(userNum,'▲')
    global userActionHistory
    userActionHistory.append(userNum)


def aiAttention(rate:float):#随机概率注意到
    flag=aiDectUserWin()
    if flag:
        temp=random.random()
        if temp<=rate:
            return 1
        else:
            return 0
    else:
        return 0


def setPosAi(Num):#ai落子行为
    shiWei = Num // 10
    geWei = Num % 10
    global colLabel
    global occupiedPos
    colLabel[shiWei - 1] = colLabel[shiWei - 1][:3 * geWei] + '■' + colLabel[shiWei - 1][3 * geWei + 1:]
    occupiedPos.append(Num)


def aiAction(defendChoice:list):#新笨蛋电脑行动
    global random
    global occupiedPos
    for i in defendChoice:
        if (i%10==0):
            defendChoice.remove(i)
    if aiAttention(1) and defendChoice and (set(defendChoice).intersection(set(occupiedPos))!=set(defendChoice)):
        #aiAttention百分百注意三点成线情况并且堵截，1代表注意概率
        Num=0
        if (not (10 < Num < 100)) or (not (Num % 10 != 0)) or (Num in occupiedPos):
            while 1:
                index = random.randint(0, len(defendChoice)-1)  # 有威胁defend落子
                Num = defendChoice[index]
                if (10 < Num < 100) and (Num % 10 != 0) and (Num not in occupiedPos):
                    break
        setPosAi(Num)
        occupiedPos.append(Num)
    else:#没有威胁落子
        Num=0
        if (not (10 < Num < 100)) or (not (Num % 10 != 0)) or (Num in occupiedPos):
            while 1:
                Num = random.randint(11, 100)
                if (10 < Num < 100) and (Num % 10 != 0) and (Num not in occupiedPos):
                    break
        setPosAi(Num)
        occupiedPos.append(Num)


while 1:
    printQipan()
    usernum=int(input("请输入落点坐标如：86 的两位数(代表第8行第6列)："))
    userAction(usernum)
    flag,defendChoice=aiDectUserWin()
    aiAction(defendChoice)
    printQipan()
    if(userWin()):
        print("玩家胜")
        print("玩家操作记录{}".format(userActionHistory))
        break
    if(aiWin()):
        print("电脑胜")
        print("玩家操作记录{}".format(userActionHistory))
        break

