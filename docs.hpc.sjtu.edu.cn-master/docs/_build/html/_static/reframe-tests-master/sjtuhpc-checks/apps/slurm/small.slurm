#!/bin/bash

#SBATCH --job-name=hello
#SBATCH --partition=small
#SBATCH --output=%j.out
#SBATCH --error=%j.err
#SBATCH --mail-type=end
#SBATCH --mail-user=xxxxx@sjtu.edu.cn
#SBATCH -n 4
#SBATCH --ntasks-per-node=4

hostname

