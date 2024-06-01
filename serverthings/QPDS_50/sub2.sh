#!/bin/bash -l
#SBATCH -A standby
#SBATCH -n 15
#SBATCH -t 240
#SBATCH -c 1
#SBATCH --mem-per-cpu=16000


parallel -j 15 << HERE
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 11 > out_3_11.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 12 > out_3_12.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 13 > out_3_13.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 14 > out_3_14.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 15 > out_3_15.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 16 > out_3_16.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 17 > out_3_17.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 18 > out_3_18.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 19 > out_3_19.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 20 > out_3_20.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 21 > out_3_21.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 22 > out_3_22.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 23 > out_3_23.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 24 > out_3_24.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 25 > out_3_25.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 26 > out_3_26.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 27 > out_3_27.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 28 > out_3_28.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 29 > out_3_29.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 30 > out_3_30.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 31 > out_3_31.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 32 > out_3_32.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 33 > out_3_33.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 34 > out_3_34.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 35 > out_3_35.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 36 > out_3_36.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 37 > out_3_37.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 38 > out_3_38.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 39 > out_3_39.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 40 > out_3_40.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 41 > out_3_41.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 42 > out_3_42.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 43 > out_3_43.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 44 > out_3_44.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 45 > out_3_45.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 46 > out_3_46.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 47 > out_3_47.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 48 > out_3_48.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 49 > out_3_49.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50.py 3 50 > out_3_50.txt
HERE
