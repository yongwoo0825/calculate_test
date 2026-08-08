
print('구구단')

for i in range(8):
    print('==%s 단==' % (i+2))
    for j in range(9):
        print('%s * %s = %s' % (i+2, j+1, (i+2)*(j+1)))
        