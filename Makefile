CXX := g++
CXXFLAGS := -std=c++17 -Wall -Wextra -I include -I. -fopenmp 

# Directories
SRC_DIR := src
INC_DIR := include
OBJ_DIR := obj
BENCH_DIR := benchmark

# Find all cpp files in src directory
SRCS := $(wildcard $(SRC_DIR)/*.cpp)
# Generate object file names
OBJS := $(SRCS:$(SRC_DIR)/%.cpp=$(OBJ_DIR)/%.o)

# Benchmark program
BENCH_SRC := $(BENCH_DIR)/genetic_benchmark.cpp
BENCH_BIN := genetic_benchmark

# Default target
all: directories $(BENCH_BIN) 

# Create necessary directories
directories:
	@mkdir -p $(OBJ_DIR)
	@mkdir -p $(BENCH_DIR)

# Compile source files to object files
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	@echo "Compiling $<..."
	@$(CXX) $(CXXFLAGS) -c $< -o $@

# build benchmark lib 
$(BENCH_BIN): $(BENCH_SRC) $(OBJS)
	@echo "Building benchmark program..."
	@$(CXX) $(CXXFLAGS) $< $(OBJS) -o $@ 

# Clean build files
clean:
	@echo "Cleaning build files..."
	@rm -rf $(OBJ_DIR) $(BENCH_BIN)

# Clean and rebuild
rebuild: clean all

test:
	make -j
	./genetic_benchmark diabetes

time:
	make -j
	sudo perf record -g ./genetic_benchmark cancer
	
flame:
	sudo perf script | ./FlameGraph-master/stackcollapse-perf.pl > out.perf-folded
	sudo ./FlameGraph-master/flamegraph.pl out.perf-folded > perf.svg
	sudo firefox perf.svgsudo perf script | ./FlameGraph-master/stackcollapse-perf.pl > out.perf-folded

.PHONY: all clean rebuild directories 
