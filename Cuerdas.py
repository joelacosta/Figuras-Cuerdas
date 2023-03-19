#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['mathtext.fontset'] = 'cm'
gris='0.7'
estilo='dashed'
ancho=1.5
size=25

#Figura 1

f=plt.figure(figsize=(16,9))
plt.plot([-2,0],[-3,3],color=gris,linestyle=estilo,linewidth=ancho)
plt.plot([-1,1],[-3,3],color=gris,linestyle=estilo,linewidth=ancho)
plt.plot([0,2],[-3,3],color=gris,linestyle=estilo,linewidth=ancho)
plt.plot([1,3],[-3,3],color=gris,linestyle=estilo,linewidth=ancho)
plt.arrow(0,0,0.333*1.09,1.09,zorder=3,width=0.007,length_includes_head=True,color='k')
plt.arrow(0,0,1.1,0.25*1.1,zorder=3,width=0.007,length_includes_head=True,color='k')

plt.plot([-4,4],[-1,1],color=gris,linestyle=estilo,linewidth=ancho)
plt.plot([-4,4],[0,2],color=gris,linestyle=estilo,linewidth=ancho)
plt.plot([-4,4],[1,3],color=gris,linestyle=estilo,linewidth=ancho)
plt.xlim([-0.1,2.1])
plt.ylim([-0.1,2.1])

plt.text(0.29,1.11,r'$z+\omega_2$',fontsize=size)
plt.text(1.28,1.45,r'$z+\omega_1+\omega_2$',fontsize=size)
plt.text(1.01,0.31,r'$z+\omega_1$',fontsize=size)
plt.text(-0.04,0.03,r'$z$',fontsize=size)
plt.axis('off')
plt.savefig('identificacion.png',dpi=200,bbox_inches=None)
plt.show()


#Figura 2

color='blue'
linewidth=1

def circulo(X,Y,radio):
    t=np.linspace(0,np.pi,120)
    x=[X+radio*np.cos(v) for v in t]
    y=[Y+radio*np.sin(v) for v in t]
    return x,y

f=plt.figure(figsize=(16,9))

ax = f.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

for i in [-2,-1,0,1,2]:
    x=-float(i)+0.5
    plt.plot([x,x],[0,3],color=color,linewidth=linewidth)
    plt.plot(circulo(i,0,1)[0],circulo(0,0,1)[1],color=color,linewidth=linewidth)

x=np.linspace(-0.5,0.5,100)
y=[np.sqrt(1-v**2) for v in x]
plt.fill_between(x,y,3,color='0.6')

ax.tick_params(labelsize=15)
plt.xticks([-2,-1,0,1,2])
plt.text(1.5,-0.1,r'$Re\ \tau$',fontsize=size)
plt.text(0.05,1.9,r'$Im\ \tau$',fontsize=size,rotation=90)
plt.text(0.0,1.45,r'$\mathcal{F}$',fontsize=size,)
plt.text(0.9,1.45,r'$\mathcal{F}_T$',fontsize=size,)
plt.text(0.0,0.75,r'$\mathcal{F}_S$',fontsize=size,)
plt.xlim([-2,2])
plt.yticks([1,2])
plt.ylim([0,2.25])

plt.savefig('fundamental.png',dpi=200,bbox_inches=None)
plt.show()

#Figura 3
f=plt.figure(figsize=(16,9))
ax = f.add_subplot(1, 1, 1)

plt.arrow(0,0,0.25,1,zorder=3,width=0.004,length_includes_head=True,color='k',head_length=0.028)
plt.arrow(0.0,0.0,0.4,0,zorder=3,width=0.01,length_includes_head=True,color='k',head_length=0.02)

for i in range(10):
    s=-1+0.4*(i-5)
    plt.plot([0+s,2+s],[-4,4],color=gris,linestyle=estilo,linewidth=ancho)
for i in range(3):
    plt.plot([-1,2],[i,i],color=gris,linestyle=estilo,linewidth=ancho)

plt.plot([0.25,0.25],[0,1],color=gris,linewidth=ancho/2)

plt.text(0.245,-0.07,r'$\tau_1$',fontsize=size)
plt.text(0.25,0.45,r'$\tau_2$',fontsize=size,rotation=90)
plt.text(0.395,-0.07,r'$1$',fontsize=size)
plt.text(0.12,0.57,r'$\tau$',fontsize=size)

plt.xlim([-0.1,1])
plt.ylim([-0.1,2.2])
plt.axis('off')

plt.savefig('toro.png',dpi=200,bbox_inches=None)
plt.show()




