#!/bin/bash -l
#SBATCH -A standby
#SBATCH -n 15
#SBATCH -t 240
#SBATCH -c 1
#SBATCH --mem-per-cpu=16000


parallel -j 15 << HERE
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 1 > out_2_1.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 2 > out_2_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 3 > out_2_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 4 > out_2_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 5 > out_2_5.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 6 > out_2_6.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 7 > out_2_7.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 8 > out_2_8.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 9 > out_2_9.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 10 > out_2_10.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 11 > out_2_11.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 12 > out_2_12.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 13 > out_2_13.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 14 > out_2_14.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 15 > out_2_15.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 16 > out_2_16.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 17 > out_2_17.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 18 > out_2_18.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 19 > out_2_19.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 20 > out_2_20.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 21 > out_2_21.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 22 > out_2_22.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 23 > out_2_23.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 24 > out_2_24.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 25 > out_2_25.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 26 > out_2_26.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 27 > out_2_27.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 28 > out_2_28.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 29 > out_2_29.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 30 > out_2_30.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 31 > out_2_31.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 32 > out_2_32.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 33 > out_2_33.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 34 > out_2_34.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 35 > out_2_35.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 36 > out_2_36.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 37 > out_2_37.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 38 > out_2_38.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 39 > out_2_39.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 40 > out_2_40.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 41 > out_2_41.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 42 > out_2_42.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 43 > out_2_43.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 44 > out_2_44.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 45 > out_2_45.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 46 > out_2_46.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 47 > out_2_47.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 48 > out_2_48.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 49 > out_2_49.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 2 50 > out_2_50.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 3 1 > out_3_1.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 3 2 > out_3_2.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 3 3 > out_3_3.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 3 4 > out_3_4.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 3 5 > out_3_5.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 3 6 > out_3_6.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 3 7 > out_3_7.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 3 8 > out_3_8.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 3 9 > out_3_9.txt
srun --exact -N1 -n1 -c1 --mem-per-cpu=16000 python QPDS_50_noise2.py 3 10 > out_3_10.txt
HERE
