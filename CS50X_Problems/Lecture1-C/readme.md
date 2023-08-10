# Lecture 1 -  c

## Practice problems

1. Debug
2. Half
3. Prime 

## Lab 1

1. Population growth
   
## Problem set 1

1. Hello
2. Mario (less)
3. Mario (more)
4. Cash
5. Credit

To compile the C programs you can use the `gcc` compiler or `make` using the follow structure in your command line (note: it is for linux operative systems - e.g., Ubuntu):

~~~
// Install the gcc compiler
sudo apt install gcc -y

// Compile the source code written on the C language (the default executable name is a.out)
gcc <source_name>.c 

// To run the executable
./a.out

// Compile the source code written on the C language and give a name to the executable file
gcc <source_name>.c -o <executable_name>

// To run the executable
./<executable_name>
~~~

Or

~~~
// Making the c program (the <executable_name> should correspond to the source code file name)
make <executable_name>

// To run the executable
./<executable_name>
~~~

For more information about the problems' instructions see [here](https://cs50.harvard.edu/c/2023/weeks/1)