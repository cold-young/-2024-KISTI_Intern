# NURION Tutorial - Submit job / Interactive job (KOR.)
**Date**: 2024.05.21 (Tue) <br>
**Writer**: Chanyoung Ahn ([cold-young](https://github.com/cold-young))

- KOR version 작성 후, ENG version 작성 예정.
- Reference: [Nurion-guide](https://docs-ksc.gitbook.io/nurion-user-guide-eng)

## Submit Job 

### Common shell commands
```shell
motd # See basic notice and help
pbs_status # watch all nodes status 
pbs_queue_check # watch available nodes

qstat -u #view my jobs
qstat -i -w -T -u [USER_ID]
```
- `qstat -u support`error! why cannot see my jobs?

### Write job script 
```shell
cd 
cd job_examples

mpiifort hello.f90 -o hello.x
vim mpi.sh
```

- *mpi.sh*
```shell
#!/bin/sh
#PBS -V
#PBS -N mpi_job
#PBS -q debug
#PBS -A etc
#PBS -l select=2:ncpus=32:mpiprocs=64
#PBS -l walltime=04:00:00

cd $PBS_O_WORKDIR

module purge
module load craype-mic-knl intel/18.0.3 impi/18.0.3

mpirun ./hello.x
```


## Send/Download files 

```shell
sftp [USER_ID]@nurion-dm.ksc.ke.kr # Nurion
sftp [USER_ID]@neuron-dm.ksc.ke.kr # neuron

# OTP PW: application
# PW: USER_ID PW
```

```shell
# In ftp directory
cd; ls; mkdir 

# In local directory
lcd; lls; lmkdir 

# Send local > nurion
put [LOCAL_FILE]
# mput [] [] ..

# Download from nurion
get [NURION_FILE]
#mget [] [] .. 
```
