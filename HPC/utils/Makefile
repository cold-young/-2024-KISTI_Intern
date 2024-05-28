CC = mpiicc

INC = -I/apps/common/xccels_lib/mic-knl/superlu_dist/8.1.2/include/
LIB = -L/apps/common/xccels_lib/mic-knl/superlu_dist/8.1.2/lib64 -lsuperlu_dist

# Source files
SRCS  = dreadhb.c dcreate_matrix.c dcreate_matrix_perturbed.c test.c

# Object files
OBJS = $(SRCS:.c=.o)

# Compiler flags
CFLAGS = -O3 

# Target executable
TARGET = test.out

all: $(TARGET) clean_obj

# Rule to build the target executable
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) $(INC) $(SRCS) $(LIB) -o $(TARGET)

# Rule to build object files
%.o: %.c
	$(CC) $(CFLAGS) $(INC) -c $< -o $@

clean_obj:
	rm -f $(OBJS)

# Clean rule
clean: clean_obj
	rm -f $(TARGET)

.PHONY: all clean clean_obj
