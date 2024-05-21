# Environment Setting for PaScaL_TDMA(KOR.)
**Date**: 2024.05.21 (Tue) <br>
**Writer**: Chanyoung Ahn ([cold-young](https://github.com/cold-young))

- KOR version 작성 후, ENG version 작성 예정.
- Reference: [Nurion-guide](https://docs-ksc.gitbook.io/nurion-user-guide-eng)
___

## Prerequisites

1. My KSC - `Nurion` or `Neuron` / terminal
2. See `module av`, `load` compiler/libraries

```shell
craype-network-opa
craype-mic-knl
intel/oneapi_21.2
impi/oneapi_21.2
xccels_lib/MUMPS_5.6.2
xccels_lib/STARUMPACK_7.1.4
xccels_lib/superlu_dist_8.1.2
```

```shell
# When start
module load craype-network-opa craype-mic-knl \
intel/oneapi_21.2 impi/oneapi_21.2 \
xccels_lib/MUMPS_5.6.2 xccels_lib/STRUMPACK_7.1.4 \
xccels_lib/superlu_dist_8.1.2 

# .. Or Add these commands in .bash_rc
module add craype-mic-knl
module add intel/oneapi_21.2
module add impi/oneapi_21.2

module add xccels_lib/MUMPS_5.6.2
module add xccels_lib/STRUMPACK_7.1.4
module add xccels_lib/superlu_dist_8.1.2

alias interactive='qsub -I -l select=1:ncpus=68:mpiprocs=68:ompthreads=1 -l walltime=4:00:00 -q debug -A etc'
###

# Check 
module list
```

* We should submit any job and `interactive` alias in `scratch/USERID`.
  