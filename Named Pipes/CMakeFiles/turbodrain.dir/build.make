# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/home/alex/Programming/C-C++/Named Pipes/src"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/home/alex/Programming/C-C++/Named Pipes"

# Include any dependencies generated for this target.
include CMakeFiles/turbodrain.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/turbodrain.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/turbodrain.dir/flags.make

CMakeFiles/turbodrain.dir/main.c.o: CMakeFiles/turbodrain.dir/flags.make
CMakeFiles/turbodrain.dir/main.c.o: src/main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/home/alex/Programming/C-C++/Named Pipes/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/turbodrain.dir/main.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/turbodrain.dir/main.c.o   -c "/home/alex/Programming/C-C++/Named Pipes/src/main.c"

CMakeFiles/turbodrain.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/turbodrain.dir/main.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E "/home/alex/Programming/C-C++/Named Pipes/src/main.c" > CMakeFiles/turbodrain.dir/main.c.i

CMakeFiles/turbodrain.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/turbodrain.dir/main.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S "/home/alex/Programming/C-C++/Named Pipes/src/main.c" -o CMakeFiles/turbodrain.dir/main.c.s

# Object files for target turbodrain
turbodrain_OBJECTS = \
"CMakeFiles/turbodrain.dir/main.c.o"

# External object files for target turbodrain
turbodrain_EXTERNAL_OBJECTS =

turbodrain: CMakeFiles/turbodrain.dir/main.c.o
turbodrain: CMakeFiles/turbodrain.dir/build.make
turbodrain: CMakeFiles/turbodrain.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/home/alex/Programming/C-C++/Named Pipes/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable turbodrain"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/turbodrain.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/turbodrain.dir/build: turbodrain

.PHONY : CMakeFiles/turbodrain.dir/build

CMakeFiles/turbodrain.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/turbodrain.dir/cmake_clean.cmake
.PHONY : CMakeFiles/turbodrain.dir/clean

CMakeFiles/turbodrain.dir/depend:
	cd "/home/alex/Programming/C-C++/Named Pipes" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/home/alex/Programming/C-C++/Named Pipes/src" "/home/alex/Programming/C-C++/Named Pipes/src" "/home/alex/Programming/C-C++/Named Pipes" "/home/alex/Programming/C-C++/Named Pipes" "/home/alex/Programming/C-C++/Named Pipes/CMakeFiles/turbodrain.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/turbodrain.dir/depend

