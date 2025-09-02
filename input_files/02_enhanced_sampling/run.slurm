#!/bin/bash
#SBATCH --job-name=US_XXXNAMEXXX
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=48:00:00
#SBATCH --partition=MAIN
#SBATCH --gpus=1


module add gcc/7.5.0 icc mkl anaconda/python3 mpi/openmpi/gnu7
module unload cuda/10.2
module load cuda/11.7
conda activate mace

home=$(pwd)
EXEC=/path/to/lammps/executable

start_val=XXXSTARTXXX
end_val=XXXENDXXX

for x in $(seq $start_val 1 $end_val)
do
    dir=CV_$(printf "%03d" $x)
    cd $dir/prod_v1

    # UNCOMMENT ON ACTUAL RUN 
    ${EXEC} -k on g 1 -sf kk < lammps.inp

    cd $home
done

exit 0

