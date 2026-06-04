# Alpha e Beta
beta = 100
alpha = beta / (beta + 1)

# Capacitores
capacitor = 0.000000220 #220 micro

# Frequencias
frequencia = 1000 # 1k hz

# VCC
vcc = 12

# Correntes
iE = 0.003 # 4 mA
iC = alpha * iE
iB = iE - iC

# Constantes
vT = 0.025 # 25 mV

# Resistencias
rC = 500 # dois de 1k em //
rE = 1000 # 1k
rB1 = 100000 # 100k
rB2 = 47000 # 50k
rTH = (rB1 * rB2) / (rB1 + rB2)
rPI = vT / iB
rSig = 50

# Tensões
vi = 0.001 # 10 mV
vC = vcc - rC * iC
vE = rE * iE
vB = vE + 0.7
vTH = (rB2 * vcc) / (rB1 + rB2)
vbe_aux = (rPI * rTH) / (rPI + rTH)
vbe = (vbe_aux * vi) / (vbe_aux + rSig)

# gm
gm = iC / vT

# IE thevenim
iEThev = (vTH - 0.7) / (rE + (rTH / beta + 1))

# Potencias (P = V*I)
pB = vB * iB
pC = vC * iC
pE = vE * iE

# Ganhos
ganho = -gm * (vbe_aux / (vbe_aux + rSig)) * rC

# Outputs
print("Resultados e valores: ")

print("\nResistencias: ")
print("Rc: " + str(rC))
print("Re: " + str(rE))
print("Rb1: " + str(rB1))
print("Rb2: " + str(rB2))

print("\nTensões: ")
print("Vc: " + str(vC))
print("Ve: " + str(vE))
print("Vb: " + str(vB))
print("Vce: " + str(vC - vE))
print("Vth: " + str(vTH))
print("Rth: " + str(rTH))

print("\nCorrentes:")
print("Ie thevenim: " + str(iEThev))
print("Ie: " + str(iE))
print("Ic: " + str(iC))
print("Ib: " + str(iB * 100))

print("\nPotencias:")
print("Pe: " + str(pE))
print("Pb: " + str(pB))
print("Pc: " + str(pC))

print("\nGanho:")
print("Ganho: " + str(ganho))
