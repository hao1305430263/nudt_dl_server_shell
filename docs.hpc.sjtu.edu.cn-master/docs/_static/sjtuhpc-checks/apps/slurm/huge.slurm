#!/bin/bash

#SBATCH --job-name=hello
#SBATCH --partition=huge
#SBATCH --output=%j.out
#SBATCH --error=%j.err
#SBATCH --mail-type=end
#SBATCH --time=2-00:00:00
#SBATCH --mail-user=xxxxx@sjtu.edu.cn
#SBATCH -N 1
#SBATCH --exclusive

hostname

