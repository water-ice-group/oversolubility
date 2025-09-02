import numpy as np
import sys

filename = sys.argv[1]
ref_cv   = sys.argv[2]
f_const  = sys.argv[3] # needs to be in kj
dir_num  = int(sys.argv[4])

def load_data(file):
    fin = np.loadtxt(file)
    time = fin[:,0]
    cv   = fin[:,1] # make sure correct variable is being loaded here
    
    avg = np.average(cv)
    std = np.std(cv)

    return (time,cv,avg,std)

start = 200
time,cv,avg,std = load_data(filename)
r_cv_list = [float(ref_cv)]*len(time[start:])
f_const_list = [float(f_const)]*len(time[start:])

output = np.array([time[start:],cv[start:],r_cv_list,f_const_list])
output = output.transpose()

np.savetxt(f'data.{dir_num}',output)
