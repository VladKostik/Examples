from OOP_example.HW_12.pistol import Pistol

if __name__ == '__main__':
    glock = Pistol('Glock 17', 17, 0, False)
    print(glock.loading)
    glock.loading = 4
    print(glock.loading)
    print(glock.shooting())
    print(glock.shooting())
    print(glock.shooting())
    print(glock.loading)
    print(glock.shooting())
    print(glock.shooting())