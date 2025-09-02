#!/bin/bash

# force constant in kcal - need to convert to kj 
frc_const=41.84
CV_start_val=15.0
CV_end_val=2.2
division=50

range=$(echo "$CV_end_val-$CV_start_val" |bc -l )
step=$(echo "$range/$division" |bc -l )


# create output directory

home=$(pwd)

if [ -d "frames" ]; then rm -Rf frames; fi
mkdir -p frames/umbrella

# go into directories
counter=1
CV=$CV_start_val

while (( $(echo "$CV >= $CV_end_val" |bc -l) ))
do
    dir=CV_$(printf "%03d" $counter)
    cd ${dir}/prod_v4

    python ${home}/collate.py UMBRELLA $CV $frc_const $counter

    cp data.${counter} ${home}/frames/umbrella/${dir}

    CV=$(echo "$CV + $step" |bc -l )
    counter=$(($counter+1))

    cd $home

done

cd frames
cat umbrella/* > "output.dat"

integrator=/sharedscratch/sghb2/air-water/model_04/production/umbrella_sampling/umb_integ/umbrella_integration.py
python2.7 $integrator -i output.dat -o final_profile.dat -n 100 -t 300 -m $CV_start_val $CV_end_val -r left

cd ../
