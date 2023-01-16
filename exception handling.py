try:
    a = int(input('masukkan nilai a '))
    b = int(input('masukkan nilai b '))
    print('hasil a/b adalah',a/b)
except ZeroDivisionError:
    print('masukkan angka selain 0')
except ValueError:
    print('silahkan masukkan angka')