
# -------------------------------------
# IPython Basics and Launching in VS Code
# To launch IPython in the VS Code terminal (run this in the command line or terminal)
# python -m IPython

# -------------------------------------
# Accessing Documentation and Source Code

# Accessing documentation using ? (e.g., the `len` function)
len?

# Accessing source code and documentation using ?? (e.g., for a custom function)
def square(x):
    '''Return the square of x.'''
    return x ** 2

square??  # This will display the source code and documentation

# -------------------------------------
# Tab Completion Examples

# Tab completion for object methods
my_list = [1, 2, 3]
# Press Tab after typing 'my_list.' to see list methods

# Tab completion for dunder methods (e.g., special methods like __init__)
# Press Tab after typing 'my_list.__' to see special/dunder methods

# Tab completion while importing modules
from itertools import co  # Press Tab here to auto-complete with `combinations` or `compress`

# -------------------------------------
# Pasting Code with %paste and %cpaste

# Use %paste to paste a code snippet from your clipboard directly
%paste

# For interactive multiline pasting, use %cpaste, and type '--' on a new line to end input
%cpaste
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")
--

# -------------------------------------
# Running External Scripts with %run

# Assuming we have a file `myscript.py` with Python code, we can run it directly in IPython
%run myscript.py

# Any variables, functions, or classes defined in myscript.py will be available in the IPython session

# -------------------------------------
# Timing Code Execution with %timeit

# Timing a single line of code
%timeit [x**2 for x in range(1000)]

# Timing multiple lines with %%timeit (note the double %)
%%timeit
squares = []
for x in range(1000):
    squares.append(x**2)

# -------------------------------------
# Exploring Available Magic Commands with %magic and %lsmagic

# Display the overview of all magic commands with usage examples
%magic

# Display a list of all available magic commands
%lsmagic

# -------------------------------------
# Viewing Command History with %history

# Display all command history with line numbers
%history -n

# Display only the last 5 commands
%history -n -5

# -------------------------------------
# Shell Commands in IPython (Windows Versions)

# On Windows, list files in the current directory
!dir

# Display the current directory path
!cd

# Print a message to the terminal
!echo "Hello from the shell!"

# -------------------------------------
# Shell-like Commands in IPython

# Directory and file operations within IPython
%mkdir test_dir
%ls
%pwd
%rmdir test_dir

# -------------------------------------
# Error Handling and Debugging

# Using %xmode to control exception detail level
%xmode Plain    # Minimal information
%xmode Context  # Default mode with context
%xmode Verbose  # Detailed traceback with variable values

# Example of debugging with %debug
def divide(a, b):
    return a / b

# Cause a ZeroDivisionError
divide(1, 0)  # Run this and then use %debug to investigate the error

# Starting an interactive debugging session after an error occurs
%debug

# Enable automatic debugging mode
%pdb on

# -------------------------------------
# Profiling Code Performance with %prun and %lprun

# Profiling a function with %prun
def compute_squares(n):
    return [i**2 for i in range(n)]

%prun compute_squares(10000)

# Line-by-line profiling with %lprun (requires `line_profiler` extension)
# Note: Use `%load_ext line_profiler` to load the profiler first
%load_ext line_profiler
%lprun -f compute_squares compute_squares(5000)
