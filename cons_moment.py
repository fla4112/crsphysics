# Conservation of Momentum: Collisions
'''
Question 1
Consider the following for questions 1-6.
A bullet of mass 0.096 kg traveling horizontally at a speed of 200 m/s embeds itself in a block
of mass 2.5 kg that is sitting at rest on a nearly frictionless surface.
'''

import math

m1= 0.096
m1vxi= 200 
mblock= 2.5 #kg
mbvxi= 0

#mbvx final?
# P1xf + P2xf= P1xi + P2xi
vxf= (m1*m1vxi + mblock*mbvxi)/(m1+mblock)
print("Q1: vx_f:", vxf)

#Q2 Total KE before collision
KEtot_i= 0.5*m1*m1vxi**2 + 0.5*mblock*mbvxi**2
print("Q2: KEtot_initial: ", KEtot_i)

#Q3 Total KE final
KEtot_f= 0.5*(m1+mblock)*vxf**2
print("Q3: KEtot final: ", KEtot_f)

#Q4 Collision?
print("Q4: Inelastic Collision, both objects embed and move ")

#Q5 Raise in thermal energy
Etherm= KEtot_i -KEtot_f
print("Q5: Etherm: ", Etherm)

#Q6 Transfer of energy Q from surrounding into the block-bullet system.
print("Q6 No transfer: ", 0)

#Q7 
mA= 9
PA_i= [15,-7,0]
mB= 12
PB_i= [3,5,0]

#Q7 X-Dir
Ptotx_i= PA_i[0]+PB_i[0]
print("Q7: ", Ptotx_i)

#Q8 Y-dir
Ptoty_i= PA_i[1]+PB_i[1]
print("Q8: ", Ptoty_i)

#Q9 Z-dir
Ptotz_i= PA_i[2]+PB_i[2]
print("Q9: ", Ptotz_i)

#Q10 -12
print("Q10 -12: ", 0)

#Q13 Total Px final
Px_f= PA_i[0]+PB_i[0]
print("Q13: ", Px_f)

#Q14 Total Py final
Py_f= PA_i[1]+PB_i[1]
print("Q14: ", Py_f)

#Q15 Total Pz final
Pz_f= PA_i[2]+PB_i[2]
print("Q15: ", Pz_f)

#Q16 Object A-final PA,f=[12, 4, 0], what is PBx, f?
PA_f=[12,4,0]
PBx_f=Px_f - PA_f[0]
print("Q16: ", PBx_f)

#Q17 Object A-final PA,f=[12, 4, 0], what is PBx, f?
PA_f=[12,4,0]
PBy_f=Py_f - PA_f[1]
print("Q17: ", PBy_f)

#Q18 Object A-final PA,f=[12, 4, 0], what is PBx, f?
PA_f=[12,4,0]
PBz_f=Pz_f - PA_f[2]
print("Q18: ", PBz_f)

#Q19 PAi magnitude
PAi_mag= math.sqrt(PA_i[0]**2 + PA_i[1]**2 + PA_i[2]**2)
print("Q19: ", PAi_mag)

#T=KE= p**2/(2*m)
#Q20 TA initial
TA_i= PAi_mag**2/(2*mA)
print("Q20: ", TA_i)

#Q21 PBi magnitude
PBi_mag= math.sqrt(PB_i[0]**2 + PB_i[1]**2 + PB_i[2]**2)
print("Q21: ", PBi_mag)

#Q22 Kinetic energy TB initial
TB_i= PBi_mag**2/(2*mB)
print("Q22: ", TB_i)

#Q23 PAf_mag
PA_f=[12,4,0]
PAf_mag= math.sqrt(PA_f[0]**2 + PA_f[1]**2 + PA_f[2]**2)
print("Q23: ", PAf_mag)

#Q24 TA after
TA_f= PAf_mag**2/(2*mA)
print("Q24: ", TA_f)


