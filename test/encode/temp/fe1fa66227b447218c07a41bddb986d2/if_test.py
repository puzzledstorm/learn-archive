

flag = None


for i in range(12):
    if flag is None:
        flag = 'init'
        print(flag, i)
    elif flag is not None:
        print(flag, i)
    elif i == 12:
        print('q')