#!/bin/bash

# for dim in 1 2
# do
# for type in 1 2 3 4 5
# do
# for splits in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
# do
	 echo "python general_python_sims.py $splits NNGP dim_${dim}_type_${type} 2 > nngp_${splits}_${dim}_${type}_3.txt"
# 	 echo "python general_python_sims.py $splits DIWP dim_${dim}_type_${type} 2 > diwp_${splits}_${dim}_${type}_3.txt"
# done
# done
# done


for dim in 1 2
do
for type in 1 2 3 4 5
do
for splits in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
do
         # echo "Rscript uci_run_splits.R split0=$splits data_name=\'dim_${dim}_type_${type}\' > stable_${splits}_${dim}_${type}.txt"
	 echo "Rscript run_old_functions.R split0=$splits data_name=\'dim_${dim}_type_${type}\' > old_stable_${splits}_${dim}_${type}.txt"
done
done
done
