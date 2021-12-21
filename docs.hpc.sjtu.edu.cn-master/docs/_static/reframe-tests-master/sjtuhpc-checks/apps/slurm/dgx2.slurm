#!/bin/bash

#SBATCH --job-name=hello_dgx2
#SBATCH --partition=dgx2
#SBATCH --output=%j.out
#SBATCH --error=%j.err
#SBATCH --mail-type=end
#SBATCH --mail-user=xxxxx@sjtu.edu.cn
#SBATCH -n 1
#SBATCH --gres=gpu:1

hostname
