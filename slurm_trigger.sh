#!/bin/bash
#SBATCH --job-name=neglag_fit              # Job name shown in squeue
#SBATCH --output=logs/neglag_fit_%A_%a.out       # Std-out (A=array ID, a=task ID)
#SBATCH --error=logs/neglag_fit_%A_%a.err        # Std-err
#SBATCH --array=0-8                      # <-- 0,1,2,3,4,5,6,7,8
#SBATCH --time=12:00:00                  # Wall-clock limit
#SBATCH --cpus-per-task=4                # Cores per task
#SBATCH --mem=16G                         # Memory per task
# (Uncomment/adjust the next line if your cluster needs a partition)
# #SBATCH --partition=short

# Load modules or activate Conda/venv if needed
module load anaconda3/5.2.0
eval "$(conda shell.bash hook)"
conda activate litmus01

# 2️⃣  Pass the array index as the argparse argument `i`
python AS_mock_run.py "${SLURM_ARRAY_TASK_ID}"