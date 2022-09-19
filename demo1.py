def abc(ele):
    def xyz():
        print("..........")
        ele()
        print("..........")
        b = 10 * 10
        print(b)
    return xyz
@abc
def add ():
    a = 10 + 10
    print(a)
add()

