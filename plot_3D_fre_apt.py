from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors, ticker, cm
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec
import csv

om_dr = []
freq = []
apt = []

for line in open("om_dr.txt"):
    om_dr.append(float(line))

with open('fre_apt_3.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
    	try:
    		freq.append(float(row[0]))
    		apt.append(float(row[1]))
    	except Exception as e :
    		print(e)



m = len(om_dr)
n = int(len(freq)/m)


print (len(freq), len(om_dr), len(apt) )

dimension = (m, n)
print(dimension)
#rearrange the apt array
om_dr = np.array(om_dr)
om_dr = 1000 * om_dr
freq = np.array(freq).reshape(dimension)
#print(freq[0])

apt = np.array(apt).reshape(dimension)
#print(apt[0])

fre_min = np.amin(freq)
fre_max = np.amax(freq)

# grid the plot area

Freq , Om_dr= np.meshgrid(freq[0], om_dr)

print (Om_dr.shape, Freq.shape, apt.shape)

fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1, 1, 1, projection='3d')
#plt.contourf(Om_dr, Freq,  apt, locator=ticker.LogLocator(), cmap=cm.Blues_r)
surf = ax.plot_surface(Om_dr, Freq,apt, rstride=1, cstride=1, cmap=cm.afmhot,
                       linewidth=0, antialiased= True)
ax.set_ylim(3.272, 3.284)
fig.colorbar(surf, shrink=0.5, aspect=10)

#ax.set_zlim(0,10)

ax.set_title('FAST_CARS_II')
ax.set_xlabel('Drving beam Rabi $10^{11}$')
ax.set_ylabel('Signal Frequency $10^{14}$')
ax.view_init(elev=80, azim=50)


plt.show()
