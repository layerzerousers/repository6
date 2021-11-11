import datetime


def is_odd():
    a = '2021-09-01'
    a = a.split('-')
    aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
    bb = datetime.date.today()
    cc = aa-bb
    dd = str(cc)
    result = int(dd.split()[0])*-1

    result = result//7 + 1
    if result % 2 == 0:
        return False
    elif result % 2 != 0:
        return True


print(is_odd())