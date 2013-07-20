import math
# 1
F= 143 #None
d=0.45 #m
h= 0.18 #m
m= 9.0 #kg
g= 9.8


#2
y_comp= h
print('Q2:', y_comp)

# 3 In N, what is the y-component of the net force acting 
# on the point particle system during this process?
Fup= F
Fdown= m*g
Fnet= Fup - Fdown
print('Q3:', Fnet)

# 4 In m, what is the distance in m through which the 
# net force acts on the point particle system?
# Fnet= mgh
h_fnet= h
print('Q4: ', h_fnet)

# 5 In J, how much work is done on the point particle system 
# during this process?
Wdone=  Fnet * h_fnet
print('Q5: ', Wdone)

# 6 Box speed
# Wdone= 0.5*m*v^2
vbox= math.sqrt(2*Wdone/m)
print('Q6: ', vbox)

#9 KEtrans
KEtrans= 0.5*m*vbox**2
print('Q9: ', KEtrans)

# 10 In m, what is the distance through which the 
# gravitational force acts on the real system?
# KEtransf= mgh
h10= KEtrans/(m*g)
print('Q10: ', h10)

#11 In J, how much work is done on the system by the gravitational force?
#Wg=mgh10
Wg11= -m*g*h
print('Q11: ', Wg11)

#12 In m, what is the distance through which your hand moves?
y_hand= d + h
print('Q12: ', y_hand)

#13 In J, how much work do you do on the real system?
Wyou= F*(d+h) 
print('Q13: ', Wyou)

#14 KEtot
KEtot = Wyou - (m*g*h)
print("Q14: ", KEtot)

# 15 KErot
# KErot= Wyou - KEtot -KEtrans
KErot= F*d
print("Q15: ", KErot)

#16 -17
Fpull= 6
x_cm= 0.12
d= 0.31
m= 2.5
R= 0.11

#16 At this instant: in m/s, what is the speed of the center of mass 
# of the disk?
Epull= Fpull*x_cm
vcm= math.sqrt(2*Epull/m)
print('Q16: ', vcm)

#17 Erot
Krot= Fpull*(d-x_cm) 
print('Q17: ', Krot)

#18 
m=7.0
F= 66
L= 0.8
d= 3.0

KEtrans= F*(d-(L/2)) 
v18=math.sqrt(2*KEtrans/m)
print('Q18: ', v18)

Etot= F*d
print('Q19: ', Etot)

#20
Etherm= Etot - KEtrans
print('Q20: ', Etherm)

