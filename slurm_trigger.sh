#!/bin/bash
#SBATCH --job-name=neglag_fit
#SBATCH --output=./logs/neglag_fit_%A_%a.out
#SBATCH --error=./logs/neglag_fit_%A_%a.err
#SBATCH --array=0-8
#SBATCH --time=4:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --partition=smp

# Load modules or activate Conda/venv if needed
module load anaconda3/2022.10
eval "$(conda shell.bash hook)"
conda activate litmus01

# 2️⃣  Pass the array index as the argparse argument `i`
python AS_mock_run.py "${SLURM_ARRAY_TASK_ID}"
