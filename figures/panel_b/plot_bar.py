import matplotlib.pyplot as plt
import numpy as np

# data from interaction energy calculations
co2_dat = -(161/1000)*23.0605 
h2o_dat = -(146/1000)*23.0605


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



fig, ax = plt.subplots(figsize=(2, 2.25))

ax.bar(1, h2o_dat, width=0.7, color='#DC267F', label='H2O',alpha=0.7, hatch='//',
        edgecolor='#DC267F', linewidth=3)
ax.bar(2, co2_dat, width=0.7, color='black', label='CO2',alpha=0.7, hatch='//',
        edgecolor='black', linewidth=3)
ax.text(1, h2o_dat-0.1, f'{h2o_dat:.2f}', ha='center', va='bottom', fontsize=11,
        bbox=dict(facecolor='white', edgecolor='#DC267F', boxstyle='round,pad=0.25',
                  linewidth=2))
ax.text(2, co2_dat-0.1, f'{co2_dat:.2f}', ha='center', va='bottom', fontsize=11,
        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.25',
                  linewidth=2))

ax.set_ylabel(r'Gas $E_\mathrm{int}$ (kcal/mol)')
for spine in ['bottom', 'right']:
    ax.spines[spine].set_visible(False)
ax.set_ylim(-4.5,0)
ax.xaxis.set_tick_params(which='both',direction='in',size=0, labelsize=10)
ax.yaxis.set_tick_params(which='both',direction='in',width=1.5,labelsize=10)
ax.set_xticks([0,1,2,3])
ax.set_xlim(0.2, 2.8)
ax.set_xticklabels(['',  r'H$_2$O', r'CO$_2$', ''], fontsize=12)
ax.xaxis.set_ticks_position('top')

plt.savefig('bar_nrg.png', bbox_inches='tight', dpi=600)
plt.show()