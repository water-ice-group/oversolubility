import matplotlib.pyplot as plt
import numpy as np

######################################################################
####################### LOAD THE DATA ################################
######################################################################
# unpack and normalize the data

# single layer
s_co2_x, s_co2_y = np.loadtxt('data/co2/01/c_dens.dat', unpack=True)
s_co2_y = s_co2_y / np.max(s_co2_y)  
s_h2o_x, s_h2o_y = np.loadtxt('data/co2/01/ow_dens.dat', unpack=True)
s_h2o_y = s_h2o_y / np.max(s_h2o_y)  
s_graph_x, s_graph_y = np.loadtxt('data/co2/01/gra_dens.dat', unpack=True)
s_graph_y = s_graph_y / np.max(s_graph_y)
s_BiC_x, s_BiC_y = np.loadtxt('data/BiC/01/c_dens.dat', unpack=True)
s_BiC_y = s_BiC_y / np.max(s_BiC_y)
s_BiC_graph_x, s_BiC_graph_y = np.loadtxt('data/BiC/01/gra_dens.dat', unpack=True)
s_BiC_graph_y = s_BiC_graph_y / np.max(s_BiC_graph_y)

# triple layer
t_co2_x,t_co2_y = np.loadtxt('data/co2/02/c_dens.dat', unpack=True)
t_co2_y = t_co2_y / np.max(t_co2_y) 
t_h2o_x,t_h2o_y = np.loadtxt('data/co2/02/ow_dens.dat', unpack=True)
t_h2o_y = t_h2o_y / np.max(t_h2o_y) 
t_graph_x,t_graph_y = np.loadtxt('data/co2/02/gra_dens.dat', unpack=True)
t_graph_y = t_graph_y / np.max(t_graph_y)
t_BiC_x, t_BiC_y = np.loadtxt('data/BiC/02/c_dens.dat', unpack=True)
t_BiC_y = t_BiC_y * 0.9 / np.max(t_BiC_y)
t_BiC_graph_x, t_BiC_graph_y = np.loadtxt('data/BiC/02/gra_dens.dat', unpack=True)
t_BiC_graph_y = t_BiC_graph_y / np.max(t_BiC_graph_y)

# quadruple layer
q_co2_x, q_co2_y = np.loadtxt('data/co2/03/c_dens.dat', unpack=True)
q_co2_y = q_co2_y / np.max(q_co2_y) 
q_h2o_x, q_h2o_y = np.loadtxt('data/co2/03/ow_dens.dat', unpack=True)
q_h2o_y = q_h2o_y / np.max(q_h2o_y)
q_graph_x, q_graph_y = np.loadtxt('data/co2/03/gra_dens.dat', unpack=True)
q_graph_y = q_graph_y / np.max(q_graph_y)
q_BiC_x, q_BiC_y = np.loadtxt('data/BiC/03/c_dens.dat', unpack=True)
q_BiC_y = q_BiC_y * 0.9 / np.max(q_BiC_y)
q_BiC_graph_x, q_BiC_graph_y = np.loadtxt('data/BiC/03/gra_dens.dat', unpack=True)
q_BiC_graph_y = q_BiC_graph_y / np.max(q_BiC_graph_y)












######################################################################
####################### PLOT THE DATA ################################
######################################################################
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





fig,ax=plt.subplots(4,3,figsize=(8,4),gridspec_kw={'width_ratios': [1,1.71,2.14],'height_ratios': [3,1.5,1.5,1.5]}, constrained_layout=False)
# single layer
########################################################################################
single_xticks = [-2,0,2]
maxs = 3.3
mins = -3.3
ax[0,0].set_xticks([])
ax[0,0].set_yticks([])
ax[0,0].spines['bottom'].set_visible(False)
ax[0,0].set_xticks(single_xticks)
ax[0,0].axes.xaxis.set_tick_params(size=0,width=0,labelsize=0)
ax[0,0].set_xlim(mins,maxs)
ax[0,0].grid(ls='--',lw=1.0)
# -----------------------------------------------------------------------------------
ax[1,0].plot(s_h2o_x,s_h2o_y,label=r'$\rho \: \mathrm{(H_2O)}$',color='#DC267F')
zeros = [0]*len(s_h2o_x)
ax[1,0].fill_between(s_h2o_x,zeros,s_h2o_y,color='#DC267F',alpha=0.2)
ax[1,0].plot(s_graph_x,s_graph_y,label=r'$\rho \:}$(Graph)',color='#61b3b4')
zeros = [0]*len(s_graph_x)
ax[1,0].fill_between(s_graph_x,zeros,s_graph_y,color='#61b3b4',alpha=0.2)
ax[1,0].set_xlim(mins,maxs)
ax[1,0].set_ylim(0,1.2)
ax[1,0].set_yticks([])
ax[1,0].set_xticks(single_xticks)
ax[1,0].axes.xaxis.set_tick_params(size=0,width=0,labelsize=0)
ax[1,0].spines['top'].set_visible(False)
ax[1,0].spines['bottom'].set_visible(False)
ax[1,0].grid(ls='--',lw=1.0)
# -----------------------------------------------------------------------------------
ax[2,0].plot(s_co2_x,s_co2_y,label=r'$\rho \: \mathrm{(CO_2)}$',color='#000000')
zeros = [0]*len(s_co2_x)
ax[2,0].fill_between(s_co2_x,zeros,s_co2_y,color='#000000',alpha=0.4)
ax[2,0].plot(s_graph_x,s_graph_y,label=r'$\rho \:}$(Graph)',color='#61b3b4')
zeros = [0]*len(s_graph_x)
ax[2,0].fill_between(s_graph_x,zeros,s_graph_y,color='#61b3b4',alpha=0.2)
ax[2,0].set_xlim(mins,maxs)
ax[2,0].set_ylim(0,1.2)
ax[2,0].set_yticks([])
ax[2,0].set_xticks(single_xticks)
ax[2,0].axes.xaxis.set_tick_params(size=0,width=0,labelsize=0)
ax[2,0].spines['top'].set_visible(False)
ax[2,0].grid(ls='--',lw=1.0)
ax[2,0].spines['bottom'].set_visible(False)
ax[2,0].set_ylabel('Density',size=12,color='black',labelpad=10)
# -----------------------------------------------------------------------------------
ax[3,0].plot(s_BiC_x,s_BiC_y,label=r'$\rho \: \mathrm{(HCO_3^-)}$',color='#785EF0')
zeros = [0]*len(s_BiC_x)
ax[3,0].fill_between(s_BiC_x,zeros,s_BiC_y,color='#785EF0',alpha=0.4)
ax[3,0].plot(s_BiC_graph_x,s_BiC_graph_y,label=r'$\rho \:}$(Graph)',color='#61b3b4') 
zeros = [0]*len(s_BiC_graph_x)
ax[3,0].fill_between(s_BiC_graph_x,zeros,s_BiC_graph_y,color='#61b3b4',alpha=0.2)
ax[3,0].set_xlim(mins,maxs)
ax[3,0].set_ylim(0,1.2)
ax[3,0].set_yticks([])
ax[3,0].set_xticks(single_xticks)
ax[3,0].spines['top'].set_visible(False)
ax[3,0].grid(ls='--',lw=1.0)
ax[3,0].spines['bottom'].set_visible(True)
ax[3,0].tick_params(axis='x', which='major', 
                    length=4, width=1.5,
                    direction='in', color='black',
                    labelsize=10)

########################################################################################



# triple layer
########################################################################################
triple_xticks = [-4,-2,0,2,4]
maxt = 6
mint = -6
ax[0,1].set_xticks([])
ax[0,1].set_yticks([])
ax[0,1].set_xticks(triple_xticks)
ax[0,1].axes.xaxis.set_tick_params(size=0,width=0,labelsize=0)
ax[0,1].set_xlim(mint,maxt)
ax[0,1].spines['bottom'].set_visible(False)
ax[0,1].grid(ls='--',lw=1.0)
# -----------------------------------------------------------------------------------
ax[1,1].plot(t_h2o_x,t_h2o_y,label=r'$\rho \: \mathrm{(H_2O)}$',color='#DC267F')
zeros = [0]*len(t_h2o_x)
ax[1,1].fill_between(t_h2o_x,zeros,t_h2o_y,color='#DC267F',alpha=0.2)
ax[1,1].plot(t_graph_x,t_graph_y,label=r'$\rho \:}$(Graph)',color='#61b3b4')
zeros = [0]*len(t_graph_x)
ax[1,1].fill_between(t_graph_x,zeros,t_graph_y,color='#61b3b4',alpha=0.2)
ax[1,1].set_xlim(mint,maxt)
ax[1,1].set_ylim(0,1.2)
ax[1,1].set_yticks([])
ax[1,1].set_xticks(triple_xticks)
ax[1,1].axes.xaxis.set_tick_params(size=0,width=0,labelsize=0)
ax[1,1].spines['top'].set_visible(False)
ax[1,1].spines['bottom'].set_visible(False)
ax[1,1].grid(ls='--',lw=1.0)
# -----------------------------------------------------------------------------------
ax[2,1].plot(t_co2_x,t_co2_y,label=r'$\rho \: \mathrm{(CO_2)}$',color='#000000')
zeros = [0]*len(t_co2_x)
ax[2,1].fill_between(t_co2_x,zeros,t_co2_y,color='#000000',alpha=0.4)
ax[2,1].plot(t_graph_x,t_graph_y,label=r'$\rho \:}$(Graph)',color='#61b3b4')
zeros = [0]*len(t_graph_x)
ax[2,1].fill_between(t_graph_x,zeros,t_graph_y,color='#61b3b4',alpha=0.2)
ax[2,1].set_xlim(mint,maxt)
ax[2,1].set_ylim(0,1.2)
ax[2,1].set_yticks([])
ax[2,1].set_xticks(triple_xticks)
ax[2,1].axes.xaxis.set_tick_params(size=0,width=0,labelsize=0)
ax[2,1].spines['top'].set_visible(False)
ax[2,1].grid(ls='--',lw=1.0)
ax[2,1].spines['bottom'].set_visible(False)
# -----------------------------------------------------------------------------------
ax[3,1].plot(t_BiC_x,t_BiC_y,label=r'$\rho \: \mathrm{(HCO_3^-)}$',color='#785EF0')
zeros = [0]*len(t_BiC_x)
ax[3,1].fill_between(t_BiC_x,zeros,t_BiC_y,color='#785EF0',alpha=0.4)
zeros = [0]*len(t_BiC_graph_x)
ax[3,1].plot(t_BiC_graph_x,t_BiC_graph_y,label=r'$\rho \:}$(Graph)',color='#61b3b4')
zeros = [0]*len(t_BiC_graph_x)
ax[3,1].fill_between(t_BiC_graph_x,zeros,t_BiC_graph_y,color='#61b3b4',alpha=0.2)
ax[3,1].set_xlim(mint,maxt)
ax[3,1].set_ylim(0,1.2)
ax[3,1].set_yticks([])
ax[3,1].set_xticks(triple_xticks)
ax[3,1].spines['top'].set_visible(False)
ax[3,1].grid(ls='--',lw=1.0)
ax[3,1].spines['bottom'].set_visible(True)
ax[3,1].tick_params(axis='x', which='major', 
                    length=4, width=1.5,
                    direction='in', color='black',labelsize=10)

########################################################################################




# quadruple layer
########################################################################################
multi_xticks = [-6,-4,-2,0,2,4,6]
maxm = 7.6
minm = -7.6
ax[0,2].set_xticks([])
ax[0,2].set_yticks([])
ax[0,2].set_xticks(multi_xticks)
ax[0,2].axes.xaxis.set_tick_params(size=0,width=0,labelsize=0)
ax[0,2].set_xlim(minm,maxm)
ax[0,2].spines['bottom'].set_visible(False)
ax[0,2].grid(ls='--',lw=1.0)
# -----------------------------------------------------------------------------------
ax[1,2].plot(q_h2o_x,q_h2o_y,label=r'$\rho \: \mathrm{(H_2O)}$',color='#DC267F')
zeros = [0]*len(q_h2o_x)
ax[1,2].fill_between(q_h2o_x,zeros,q_h2o_y,color='#DC267F',alpha=0.2)
ax[1,2].plot(q_graph_x,q_graph_y,label=r'$\rho \:}$(Graph)',color='#61b3b4')
zeros = [0]*len(q_graph_x)
ax[1,2].fill_between(q_graph_x,zeros,q_graph_y,color='#61b3b4',alpha=0.2)
ax[1,2].set_xlim(minm,maxm)
ax[1,2].set_ylim(0,1.2)
ax[1,2].set_yticks([])
ax[1,2].set_xticks(multi_xticks)
ax[1,2].axes.xaxis.set_tick_params(size=0,width=0,labelsize=0)
ax[1,2].spines['top'].set_visible(False)
ax[1,2].spines['bottom'].set_visible(False)
ax[1,2].grid(ls='--',lw=1.0)
ax[1,2].text(8.5,0.5, r'H$\mathbf{_2}$O', size=12,
             color='#DC267F', rotation=270,
             ha='center', va='center',
             weight='bold')
# -----------------------------------------------------------------------------------
ax[2,2].plot(q_co2_x,q_co2_y,label=r'$\rho \: \mathrm{(CO_2)}$',color='#000000')
zeros = [0]*len(q_co2_x)
ax[2,2].fill_between(q_co2_x,zeros,q_co2_y,color='#000000',alpha=0.4)
ax[2,2].plot(q_graph_x,q_graph_y,label=r'$\rho \:}$(Graph)',color='#61b3b4')
zeros = [0]*len(q_graph_x)
ax[2,2].fill_between(q_graph_x,zeros,q_graph_y,color='#61b3b4',alpha=0.2)
ax[2,2].set_xlim(minm,maxm)
ax[2,2].set_ylim(0,1.2)
ax[2,2].set_yticks([])
ax[2,2].set_xticks(multi_xticks)
ax[2,2].axes.xaxis.set_tick_params(size=0,width=0,labelsize=0)
ax[2,2].spines['top'].set_visible(False)
ax[2,2].grid(ls='--',lw=1.0)
ax[2,2].text(8.5,0.6, r'CO$\mathbf{_2}$', size=12,
                color='#000000', rotation=270,
                ha='center', va='center',
                weight='bold')
# -----------------------------------------------------------------------------------
ax[3,2].plot(q_BiC_x,q_BiC_y,label=r'$\rho \: \mathrm{(HCO_3^-)}$',color='#785EF0')
zeros = [0]*len(q_BiC_x)
ax[3,2].fill_between(q_BiC_x,zeros,q_BiC_y,color='#785EF0',alpha=0.4)
zeros = [0]*len(q_BiC_graph_x)
ax[3,2].plot(q_BiC_graph_x,q_BiC_graph_y,label=r'$\rho \:}$(Graph)',color='#61b3b4')
zeros = [0]*len(q_BiC_graph_x)
ax[3,2].fill_between(q_BiC_graph_x,zeros,q_BiC_graph_y,color='#61b3b4',alpha=0.2)
ax[3,2].set_xlim(minm,maxm)
ax[3,2].set_ylim(0,1.2)
ax[3,2].set_yticks([])
ax[3,2].set_xticks(multi_xticks)
ax[3,2].spines['top'].set_visible(False)
ax[3,2].spines['bottom'].set_visible(True)
ax[3,2].grid(ls='--',lw=1.0)
ax[3,2].text(8.5,0.6, r'HCO$\mathbf{_3^-}$', size=12,
             color='#785EF0', rotation=270,
             ha='center', va='center',
             weight='bold')

ax[3,2].tick_params(axis='x', which='major', 
                    length=4, width=1.5,
                    direction='in', color='black',
                    labelsize=10)

########################################################################################





# label centre bottom of figure
ax[3,1].text(0,-0.7,r'z coordinate  ($\mathrm{\AA}$)',size=12,color='black')

plt.subplots_adjust(wspace=0.0,hspace=0)
plt.savefig(f'./density_profile.png',dpi=800,
            bbox_inches='tight',
            edgecolor='none',transparent=True)
plt.show()
