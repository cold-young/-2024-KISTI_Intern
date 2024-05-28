#!/bin/bash
for file_name in 4 8 16 32 64 128 256 512 1024; do 
    for np_value in 4 8 16 32; do
        if [[ $np_value -eq 4 ]]; then
            r_values=(2)
            c_values=(2)
        elif [[ $np_value -eq 8 ]]; then
            r_values=(2 4)
            c_values=(4 2)
        elif [[ $np_value -eq 16 ]]; then
            r_values=(2 4 8)
            c_values=(8 4 2)
        elif [[ $np_value -eq 32 ]]; then
            r_values=(2 4 8 16)
            c_values=(16 8 4 2)
        fi

        length=${#r_values[@]}

        for (( i=0; i<$length; i++ )); do
            r_value=${r_values[$i]}
            c_value=${c_values[$i]}
            echo "Running mpirun -np $np_value ./test.out -r $r_value -c $c_value ./ex_matrix/tdm$file_name\_0527.rua"
            mpirun -np $np_value ./test.out -r $r_value -c $c_value ./ex_matrix/tdm$file_name\_0527.rua
            wait
        done
    done
done