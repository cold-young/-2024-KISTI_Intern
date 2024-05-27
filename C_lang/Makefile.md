# C/C++ & Makefile
**Date**: 2024.05.27 (Mon) <br>
**Writer**: Chanyoung Ahn ([cold-young](https://github.com/cold-young))
___

## Build `test.out` file

- *Makefile*
```make
CC = mpiicc

INC = -I/apps/common/xccels_lib/mic-knl/superlu_dist/8.1.2/include/
LIB = -L/apps/common/xccels_lib/mic-knl/superlu_dist/8.1.2/lib64 -lsuperlu_dist

SRCS  = dreadhb.c dcreate_matrix.c dcreate_matrix_perturbed.c test.c
OBJS = $(SRCS:.c=.o)

CFLAGS = -O3 

TARGET = test.out

all: $(TARGET) clean_obj

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) $(INC) $(SRCS) $(LIB) -o $(TARGET)

%.o: %.c
	$(CC) $(CFLAGS) $(INC) -c $< -o $@

clean_obj:
	rm -f $(OBJS)

# Clean rule
clean: clean_obj
	rm -f $(TARGET)

.PHONY: all clean clean_obj

```