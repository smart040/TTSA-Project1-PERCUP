#!/bin/bash -l
#SBATCH -A standby
#SBATCH -n 15
#SBATCH -t 240
#SBATCH -c 1
#SBATCH --mem-per-cpu=16000


parallel -j 15 << HERE
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_12.py 2 1 > out_2_1.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_12.py 2 2 > out_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_12.py 2 3 > out_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_12.py 2 4 > out_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_12.py 2 5 > out_2_5.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_12.py 2 6 > out_2_6.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_12.py 2 7 > out_2_7.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_12.py 2 8 > out_2_8.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_12.py 2 9 > out_2_9.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_12.py 2 10 > out_2_10.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_12.py 2 11 > out_2_11.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_12.py 2 12 > out_2_12.txt
HERE
