#!/bin/bash

#SBATCH --job-name=hello
#SBATCH --partition=cpu
#SBATCH --output=%j.out
#SBATCH --error=%j.err
#SBATCH --mail-type=end
#SBATCH --mail-user=xxxxx@sjtu.edu.cn
#SBATCH -N 1
#SBATCH --exclusive

hostname
