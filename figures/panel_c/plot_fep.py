import matplotlib.pyplot as plt
import numpy as np



# load the data
nrg_co2_x, nrg_co2_y, nrg_co2_err = np.loadtxt('data/co2_nrg.dat', unpack=True) # load co2 energy from umbrella sampling
min_val_co2 = min(nrg_co2_y)
min_loc_co2 = nrg_co2_x[np.where(nrg_co2_y == min_val_co2)][0]

nrg_h2o_x, nrg_h2o_y,  = np.loadtxt('data/nrg_h2o.dat', unpack=True) # load h2o energy from boltzmann inversion of free MD simulation
min_val_h2o = min(nrg_h2o_y)
min_loc_h2o = nrg_h2o_x[np.where(nrg_h2o_y == min_val_h2o)][0]

print(f'Minimum value for CO2: {min_val_co2} at location {min_loc_co2}')
print(f'Minimum value for H2O: {min_val_h2o} at location {min_loc_h2o}')




# plot of the free energy profile

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


fig,ax=plt.subplots(figsize=(5,2.25))
ax.plot([min_loc_co2, 15], [min_val_co2+0.01, min_val_co2+0.01], color='black', lw=1.8, ls=(0, (1, 1)))
ax.plot([min_loc_h2o, 15], [min_val_h2o+0.01, min_val_h2o+0.01], color='#DC267F', lw=1.8, ls=(0, (1, 1)))

# h2o
ax.plot(nrg_h2o_x, nrg_h2o_y, color='#DC267F', label=r'H$_2$O')
#ax.fill_between(nrg_h2o_x, nrg_h2o_y - np.array(nrg_h2o_err), nrg_h2o_y + np.array(nrg_h2o_err), color='#DC267F', alpha=0.2)

# co2
ax.plot(nrg_co2_x, nrg_co2_y, '-',color='black',label=r'CO$_2$',lw=2.25)
ax.fill_between(nrg_co2_x, nrg_co2_y - nrg_co2_err, nrg_co2_y + nrg_co2_err, color='black', alpha=0.2)

ax.set_xlabel(r'Distance to pore wall ($\mathrm{\AA}$)')
ax.set_ylabel(r'Aq. free energy  ($\mathrm{kcal/mol}$)')
ax.axes.tick_params(axis='both',which='both',direction='in',length=3,
                       width=1.2,labelsize=10)
ax.set_ylim(-0.92,0.75)
ax.set_xlim(0,15)
ax.set_xticks(np.arange(0,16,2))

ax.text(13.91,-0.61,r'$-$0.70',color='black',fontsize=12,ha='center',va='center',rotation=0,)
ax.text(13.94,-0.39,r'$-$0.48',color='#DC267F',fontsize=12,ha='center',va='center',rotation=0,)


ax.grid(ls='--')
ax.legend()
plt.savefig('fep_plot.png', dpi=800, bbox_inches='tight')
plt.show()