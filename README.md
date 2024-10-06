Data Structures and Algorithms Assignment: Sparse Matrix Implementation
Hello Everyone,

I hope this README finds you in great spirits and ready to dive into our second Data Structures and Algorithms assignment! This project will guide you through implementing and manipulating Sparse Matrices—a common structure used in technical interviews and real-world applications, like search engines and machine learning algorithms.

Assignment Overview
In this assignment, you'll be working with sparse matrices, which are matrices where most of the elements are zero. Efficient storage and manipulation of such matrices are crucial when dealing with large datasets. The code provided reads matrix data from a file, performs various operations (addition, subtraction, multiplication), and outputs the results.

Project Features:
Load Sparse Matrix from a File: Reads sparse matrix data from a file and stores only the non-zero elements for efficient memory usage.
Matrix Operations:
Addition: Add two sparse matrices.
Subtraction: Subtract one sparse matrix from another.
Multiplication: Multiply two sparse matrices, ensuring that the matrix dimensions are compatible.
Error Handling: Proper error messages are displayed when files are not found or when operations are mathematically invalid.
Getting Started
Prerequisites
Before running the code, ensure you have:

Python 3.x installed on your system
A working knowledge of basic Python and file handling
A code editor like VS Code for writing and running the program
File Structure
Sparse_matrix.py: This is the Python file where all your matrix operations are defined.
Input Files: You will need at least two input files for matrix data (e.g., easy_sample_04_1.txt and easy_sample_04_2.txt).
Make sure your input files follow the format described in the code:

text
Copy code
numRows=3
numCols=3
(0,0,5)
(1,1,3)
(2,2,2)
How to Run the Code
Clone the Repository: First, clone or download the repository from GitHub to your local machine.

Input Files: Place your matrix data files in the same directory as the Sparse_matrix.py file.

Run the Program: You can execute the program using the following command:

bash
Copy code
python Sparse_matrix.py
The program will prompt you to select an operation (1. Add, 2. Subtract, 3. Multiply). It will then load the matrices from the input files and print the result.

Example Input and Output
Example Input (easy_sample_04_1.txt):
text
Copy code
numRows=3
numCols=3
(0,0,5)
(1,1,3)
(2,2,2)
Example Output (Addition):
text
Copy code
(0,0,10)
(1,1,6)
(2,2,4)
