#!/bin/bash -l
#SBATCH -A standby
#SBATCH -n 15
#SBATCH -t 240
#SBATCH -c 1
#SBATCH --mem-per-cpu=16000


parallel -j 15 << HERE
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=20 data_name=\'dim_2_type_1\' > old_stable_20_2_1.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=1 data_name=\'dim_2_type_2\' > old_stable_1_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=2 data_name=\'dim_2_type_2\' > old_stable_2_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=3 data_name=\'dim_2_type_2\' > old_stable_3_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=4 data_name=\'dim_2_type_2\' > old_stable_4_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=5 data_name=\'dim_2_type_2\' > old_stable_5_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=6 data_name=\'dim_2_type_2\' > old_stable_6_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=7 data_name=\'dim_2_type_2\' > old_stable_7_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=8 data_name=\'dim_2_type_2\' > old_stable_8_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=9 data_name=\'dim_2_type_2\' > old_stable_9_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=10 data_name=\'dim_2_type_2\' > old_stable_10_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=11 data_name=\'dim_2_type_2\' > old_stable_11_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=12 data_name=\'dim_2_type_2\' > old_stable_12_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=13 data_name=\'dim_2_type_2\' > old_stable_13_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=14 data_name=\'dim_2_type_2\' > old_stable_14_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=15 data_name=\'dim_2_type_2\' > old_stable_15_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=16 data_name=\'dim_2_type_2\' > old_stable_16_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=17 data_name=\'dim_2_type_2\' > old_stable_17_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=18 data_name=\'dim_2_type_2\' > old_stable_18_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=19 data_name=\'dim_2_type_2\' > old_stable_19_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=20 data_name=\'dim_2_type_2\' > old_stable_20_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=1 data_name=\'dim_2_type_3\' > old_stable_1_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=2 data_name=\'dim_2_type_3\' > old_stable_2_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=3 data_name=\'dim_2_type_3\' > old_stable_3_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=4 data_name=\'dim_2_type_3\' > old_stable_4_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=5 data_name=\'dim_2_type_3\' > old_stable_5_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=6 data_name=\'dim_2_type_3\' > old_stable_6_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=7 data_name=\'dim_2_type_3\' > old_stable_7_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=8 data_name=\'dim_2_type_3\' > old_stable_8_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=9 data_name=\'dim_2_type_3\' > old_stable_9_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=10 data_name=\'dim_2_type_3\' > old_stable_10_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=11 data_name=\'dim_2_type_3\' > old_stable_11_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=12 data_name=\'dim_2_type_3\' > old_stable_12_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=13 data_name=\'dim_2_type_3\' > old_stable_13_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=14 data_name=\'dim_2_type_3\' > old_stable_14_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=15 data_name=\'dim_2_type_3\' > old_stable_15_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=16 data_name=\'dim_2_type_3\' > old_stable_16_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=17 data_name=\'dim_2_type_3\' > old_stable_17_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=18 data_name=\'dim_2_type_3\' > old_stable_18_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=19 data_name=\'dim_2_type_3\' > old_stable_19_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=20 data_name=\'dim_2_type_3\' > old_stable_20_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=1 data_name=\'dim_2_type_4\' > old_stable_1_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=2 data_name=\'dim_2_type_4\' > old_stable_2_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=3 data_name=\'dim_2_type_4\' > old_stable_3_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=4 data_name=\'dim_2_type_4\' > old_stable_4_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=5 data_name=\'dim_2_type_4\' > old_stable_5_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=6 data_name=\'dim_2_type_4\' > old_stable_6_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=7 data_name=\'dim_2_type_4\' > old_stable_7_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=8 data_name=\'dim_2_type_4\' > old_stable_8_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=9 data_name=\'dim_2_type_4\' > old_stable_9_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=10 data_name=\'dim_2_type_4\' > old_stable_10_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=11 data_name=\'dim_2_type_4\' > old_stable_11_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=12 data_name=\'dim_2_type_4\' > old_stable_12_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=13 data_name=\'dim_2_type_4\' > old_stable_13_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=14 data_name=\'dim_2_type_4\' > old_stable_14_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=15 data_name=\'dim_2_type_4\' > old_stable_15_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=16 data_name=\'dim_2_type_4\' > old_stable_16_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=17 data_name=\'dim_2_type_4\' > old_stable_17_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=18 data_name=\'dim_2_type_4\' > old_stable_18_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 Rscript run_old_functions.R split0=19 data_name=\'dim_2_type_4\' > old_stable_19_2_4.txt
HERE
