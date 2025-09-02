#!/bin/bash
home=$(pwd)

CV_start_val=15.0
CV_end_val=2.2
division=50

range=$(echo "$CV_end_val-$CV_start_val" |bc -l )
step=$(echo "$range/$division" |bc -l )


# assemble the directories
# --------------------------------------------------------------------------- 
counter=1

CV=$CV_start_val

while (( $(echo "$CV >= $CV_end_val" |bc -l) ))
do
    dir=CV_$(printf "%03d" $counter)

    if [[ ! -e  $dir ]]; then
        mkdir $dir
    fi

    cd $dir
    mkdir prod_v1
    cd prod_v1

    ln -s ../../init.lmpdat .
    ln -s ../../lammps.inp .
    cp ../../plumed.dat .

    sed -i "s/XXX_CV_XXX/$(printf "%.3f" "$CV")/g" plumed.dat

    counter=$(($counter+1))
    CV=$(echo "$CV + $step" |bc -l )

    echo $counter $CV 
    cd $home
done



# construct and submit slurm jobs
# --------------------------------------------------------------------------- 

slurm_jobs=5
#partition=$(echo "$division/$slurm_jobs" |bc -l)
#partition_val=$(printf "%.0f" $partition)

slurm_counter=1
division_int=$(printf "%.0f" "$division")
partition_size=$((division_int / slurm_jobs))

for ((i=0; i<division_int; i+=partition_size)); do
    start_val=$((i+1))
    end_val=$((i + partition_size))
    [[ $end_val -gt $division_int ]] && end_val=$division_int

    sed "s/XXXSTARTXXX/$start_val/" run.slurm \
        | sed "s/XXXENDXXX/$end_val/" \
        | sed "s/XXXNAMEXXX/$slurm_counter/" > run_${slurm_counter}.slurm

    # UNCOMMENT ON RUN
    # sbatch run_${slurm_counter}.slurm
    slurm_counter=$((slurm_counter + 1))
done
