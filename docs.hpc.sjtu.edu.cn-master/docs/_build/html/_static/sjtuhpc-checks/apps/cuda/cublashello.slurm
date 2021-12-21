#!/bin/bash

#SBATCH --job-name=cublas
#SBATCH --partition=dgx2
#SBATCH --output=%j.out
#SBATCH --error=%j.err
#SBATCH -n 1
#SBATCH --gres=gpu:1

ulimit -s unlimited
ulimit -l unlimited

source /usr/share/Modules/init/bash
module purge
module load gcc/8.3.0-gcc-4.8.5 cuda/10.1.243-gcc-8.3.0

./cublashello
