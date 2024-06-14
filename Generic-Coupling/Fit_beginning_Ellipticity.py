import pylab
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.gridspec as gridspec
import os

beta, mass, err_mass, dy = np.loadtxt("/home/dario/Documents/UNI/Tesi/Programs/Other Couplings/Data/Stability/ExpoFIT/ExpoElliptic.txt", unpack=True)


# Funzione di fit
def f(x,a,b):
    return a+b*x**(-1)

# Valori iniziali
init = [0, 0.25]

x=beta
y=mass
# dy=err_mass[1:]
#dy=np.ones(len(x))*pow(10,-4)

#outliers
# outliers=[0]
# x=np.delete(x,outliers)
# y=np.delete(y,outliers)
# dy=np.delete(dy,outliers)

# Ciclo per minimizzare il ci quadro
popt, pcov=curve_fit(f, x, y, init, sigma=dy)

print('\n\n\n')
print('FIT DELLA MASSA threshold')
ndof=len(x)-len(init)
chi2=(((y-f(x, *popt))/dy)**2).sum()
print('popt:', popt)
print('dpopt:', np.sqrt(pcov.diagonal()))
print('chi2=%f, \nndof=%f' %(chi2, ndof))

## Grafico dell'energia potenziale bootstrappata in funzione del valore di eta

# Dummy array per disegnare la funzione di plot
xx = np.linspace(1.165625, max(x), 1000)

beta_crit=1.165625
# Figura
plt.figure(1,figsize=(10,5))
gs = gridspec.GridSpec(2, 1, height_ratios=[2, 1]) 

ax1 = plt.subplot(gs[0])
ax1.set_ylabel(r'$\hat{M}_{thr}$',fontsize=25,rotation=1)

ax1.plot( xx, f(xx, *popt), color='red')
ax1.errorbar(beta, mass, err_mass,marker ='.', linestyle = '')
# Draw a vertical line at x=beta_critico
ax1.axvline(x=beta_crit, color='g', linestyle='--')
ax1.minorticks_on()

# Residui normalizzati
ax2 = plt.subplot(gs[1])
r = (y-f(x,*popt))/dy
ax2.errorbar( x,r, linestyle='', marker='o')
ax2.set_xlabel(r'$\beta$', fontsize=25)
ax2.set_ylabel('Residuals',fontsize=20)
ax2.axvline(x=beta_crit, color='g', linestyle='--')


# ########################################################################################################################################################################################################################################
beta, mass_qmax, err_mass_qmax = np.loadtxt("/home/dario/Documents/UNI/Tesi/Programs/Other Couplings/Data/Branches/Exponential/Analisi/MassMaxQvsβ.txt", unpack=True)

def g(x,a,b,c):
    return a+b*x**(-c)

# Valori iniziali
init = (1,1,1)

x=beta
y=mass_qmax
dy=err_mass_qmax


# Ciclo per minimizzare il ci quadro
popt, pcov=curve_fit(g, x, y, init, sigma=dy)

print('\n\n\n')
print('FIT DELLA MASSA AL MASSIMO Q')
ndof=len(x)-len(init)
chi2=(((y-g(x, *popt))/dy)**2).sum()
print('popt:', popt)
print('dpopt:', np.sqrt(pcov.diagonal()))
print('chi2=%f, \nndof=%f' %(chi2, ndof))

## Grafico dell'energia potenziale bootstrappata in funzione del valore di eta

# Dummy array per disegnare la funzione di plot
xx = np.linspace(1.165625, max(x), 1000)


# Figura
fig, (ax1, ax2)= plt.subplots(1, 2, figsize=(10, 5))

ax1.set_ylabel(r'$\hat{M}_{peak}$')
ax1.set_xlabel(r'$\beta$')
ax1.plot( xx, g(xx, *popt), color='red')
ax1.errorbar(x, y, dy, marker ='o', linestyle = '')
ax1.minorticks_on()

###################################################################
beta, qmax, err_qmax = np.loadtxt("/home/dario/Documents/UNI/Tesi/Programs/Other Couplings/Data/Branches/Exponential/Analisi/MaxQvsβ.txt", unpack=True)


# Valori iniziali
init = (0,1,0.5)

x=beta
y=qmax
dy=err_qmax


# Ciclo per minimizzare il ci quadro
popt, pcov=curve_fit(g, x, y, init, sigma=dy)

print('\n\n\n')
print('FIT del MASSIMO Q')
ndof=len(x)-len(init)
chi2=(((y-g(x, *popt))/dy)**2).sum()
print('popt:', popt)
print('dpopt:', np.sqrt(pcov.diagonal()))
print('chi2=%f, \nndof=%f' %(chi2, ndof))

## Grafico dell'energia potenziale bootstrappata in funzione del valore di eta

# Dummy array per disegnare la funzione di plot
xx = np.linspace(1.165625, max(x), 1000)


# Figura

ax2.set_ylabel(r'$\hat{Q}_{peak}$')
ax2.set_xlabel(r'$\beta$')
ax2.plot( xx, g(xx, *popt), color='red')
ax2.errorbar(x, y, dy, marker ='o', linestyle = '')
ax2.minorticks_on()

plt.show()
