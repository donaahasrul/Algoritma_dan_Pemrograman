# mengginakan packet math untuk akar(math.sqrt)
import math

S1 = float(input('Masukkan Nilai S1 : '))
S2 = float(input('Masukkan Nilai S2 : '))
S3 = float(input('Masukkan Nilai s2 : '))

T = (S1+S2+S3)/2
luas = math.sqrt(T*(T-S1)*(T-S2)*(T-S3))

# round => membulatkan angka di belakang koma(,)
print(round(luas, 2))