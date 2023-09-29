import numpy as np
import os.path
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import AutoMinorLocator
import math

def PiePerc(lab):
	redarray = np.unique(lab)
	if len(redarray) == 2:
		a = stats.mode(lab)
		#print(redarray,a[0][0])
		if redarray[0] == a[0][0]:
			percarray=[200/3,100/3]
		else:
			percarray=[100/3,200/3]
	if len(redarray) == 3:
		if redarray[2] == 6:
			percarray = [100/2,100/2]
			redarray = [redarray[0],redarray[1]]
		else:
			percarray = [100/3,100/3,100/3]
	return percarray,redarray

plt.figure()
A,B,C,D,E,F = np.loadtxt("BaryonsList.txt",unpack=True,dtype=str,delimiter=",")
fig, ax = plt.subplots(nrows=2,ncols=5,figsize=(15,10))
fig.suptitle("Quark composition of charmed hadrons",fontsize='40')
hl = int(len(A)/2)
Radii = np.sqrt(E.astype(np.float64))
SF = 0.3/np.min(Radii)
MaxRadii = np.max(Radii)
patch_handles=[]
labelslist = ['u','d','c','s','b','t']
colorslist = ['red','green','blue','orange','magenta','yellow']
for i in range(len(A)):
	print(A[i])
	inputlabels = [int(B[i]),int(C[i]),int(D[i])]
	sizes,quarklabels = PiePerc(inputlabels)
	print(inputlabels)
	#title = A[i]
	if i < hl:
		patches, texts, autotexts = ax[0,i].pie(sizes, colors=[colorslist[k] for k in quarklabels],shadow=False,autopct='%1.1f%%',textprops={'fontsize': 14,'weight':'bold','color':'white'},radius=SF*Radii[i],startangle=90)
		plt.setp(autotexts,weight='bold')
		for autotext in autotexts:
			#autotext.set_horizontalalignment('center')
			autotext.set_color('white')
		if Radii[i]**2 < 1:
			plt.setp(autotexts,size='x-small')
		else:
			plt.setp(autotexts,size='small')
		ax[0,i].set_title(A[i],fontsize=25,y=1.2)
	else:
		patches, texts, autotexts = ax[1,i-hl].pie(sizes, colors=[colorslist[k] for k in quarklabels],shadow=False,autopct='%1.1f%%',textprops={'fontsize': 14,'weight':'bold','color':'white'},radius=SF*Radii[i],startangle=90)
		plt.setp(autotexts,weight='bold')
		for autotext in autotexts:
			#autotext.set_horizontalalignment('center')
			autotext.set_color('white')
		if Radii[i]**2 < 1:
			plt.setp(autotexts,**{'fontsize':5})
		else:
			plt.setp(autotexts,size='small')
		ax[1,i-hl].set_title(A[i],fontsize=25,y=1.2)
#ax[1,4].pie([100/6,100/6,100/6,100/6,100/6,100/6],labels=['u','d','c','s','b','t'],colors=['red','green','blue','orange','magenta','yellow'],textprops={'color':'white'},radius=0)
#plt.legend(handles=['red','green','blue','orange','magenta','yellow'],labels=['u','d','c','s','b','t'],loc='lower right', bbox_to_anchor=(0.0,0.0,1.5,0.5),title='Quarks')
for hand in range(len(colorslist)):
	patch_handles.append(mpatches.Patch(color=colorslist[hand],label = labelslist[hand]))
plt.legend(handles = patch_handles, loc='lower right', bbox_to_anchor=(0.0,0.0,1.5,0.5),title='Quarks')
plt.savefig("Hadrons.pdf")
