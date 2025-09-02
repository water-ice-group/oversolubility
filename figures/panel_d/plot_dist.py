import matplotlib.pyplot as plt
import numpy as np

# load the data
h2o_dat_x,h2o_dat_y = np.loadtxt('data/h2o_ori.dat', unpack=True)
co2_dat_x,co2_dat_y = np.loadtxt('data/co2_ori.dat', unpack=True)


# plot the data
plt.rcParams['lines.linewidth']                 = 2.7                      
plt.rcParams['axes.linewidth']                  = 1.5                   
plt.rcParams['font.family']                     = 'sans-serif'
plt.rcParams['font.sans-serif']                 = ['Arial']
plt.rcParams['mathtext.fontset']                = 'dejavusans'          
plt.rcParams['savefig.dpi']                     = 300                    
plt.rcParams['savefig.format']                  = 'pdf'                  
plt.rcParams['legend.labelspacing']             = 0.15                   
plt.rcParams['legend.handletextpad']            = 0.3                    
plt.rcParams['axes.xmargin']                    = 0.0                   
plt.rcParams['axes.ymargin']                    = 0.0                   
plt.rcParams['legend.frameon']                  = True  


fig, ax = plt.subplots(figsize=(3,1.5))
ax.plot(h2o_dat_x, h2o_dat_y, color='#DC267F', lw=3, label=r'H$_2$O')
ax.plot(co2_dat_x, co2_dat_y, color='black', lw=3, label=r'CO$_2$')

ax.set_ylim(0,0.03)
ax.set_xticks(np.arange(0, 180, 30))
ax.axes.tick_params(axis='both',direction='in',
                    length=3,width=1.2,
                    which='major',labelsize=10)
ax.set_xlabel(r'$\theta_\mathrm{z}$ ($^{\circ}$)',size=12)
ax.set_ylabel(r'Norm. Prob. Dist.',size=10)
ax.set_yticklabels([])

ax.legend()
ax.grid(ls='--')
plt.savefig('contact_layer.png', bbox_inches='tight',dpi=800)
plt.show()
