#!/bin/bash -l
#SBATCH -A standby
#SBATCH -n 15
#SBATCH -t 240
#SBATCH -c 1
#SBATCH --mem-per-cpu=16000


parallel -j 15 << HERE
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 1 > out_2_1.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 2 > out_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 3 > out_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 4 > out_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 5 > out_2_5.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 6 > out_2_6.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 7 > out_2_7.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 8 > out_2_8.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 9 > out_2_9.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 10 > out_2_10.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 11 > out_2_11.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 12 > out_2_12.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 13 > out_2_13.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 14 > out_2_14.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 15 > out_2_15.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 16 > out_2_16.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 17 > out_2_17.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 18 > out_2_18.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 19 > out_2_19.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 20 > out_2_20.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 21 > out_2_21.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 22 > out_2_22.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 23 > out_2_23.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 24 > out_2_24.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 2 25 > out_2_25.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 1 > out_3_1.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 2 > out_3_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 3 > out_3_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 4 > out_3_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 5 > out_3_5.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 6 > out_3_6.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 7 > out_3_7.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 8 > out_3_8.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 9 > out_3_9.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 10 > out_3_10.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 11 > out_3_11.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 12 > out_3_12.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 13 > out_3_13.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 14 > out_3_14.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 15 > out_3_15.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 16 > out_3_16.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 17 > out_3_17.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 18 > out_3_18.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 19 > out_3_19.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 20 > out_3_20.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 21 > out_3_21.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 22 > out_3_22.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 23 > out_3_23.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 24 > out_3_24.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_25.py 3 25 > out_3_25.txt
HERE
