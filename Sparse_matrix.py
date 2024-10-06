class UniqueSparseMatrix:
    def __init__(self, inputFilePath=None):
        self.numRows = 0
        self.numCols = 0
        self.elements = {}

        if inputFilePath:
            self.load_matrix_from_file(inputFilePath)
            
    def load_matrix_from_file(self, filePath):
        try:
            with open(filePath, 'r') as file:
                lines = file.readlines()
                self.numRows = int(lines[0].strip().split('=')[1])
                self.numCols = int(lines[1].strip().split('=')[1])

                for line in lines[2:]:
                    line = line.strip()
                    if line:
                        if line.startswith('(') and line.endswith(')'):
                            try:
                                content = line[1:-1].strip().split(',')
                                row, col, value = int(content[0]), int(content[1]), int(content[2])
                                self.set_element(row, col, value)
                            except (ValueError, IndexError):
                                raise ValueError("Input file has wrong format")
                        else:
                            raise ValueError("Input file has wrong format")
        except FileNotFoundError:
            print(f"Error: File {filePath} not found.")
        except Exception as e:
            print(f"Error: {e}")

    def get_element(self, currRow, currCol):
        return self.elements.get((currRow, currCol), 0)

    def set_element(self, currRow, currCol, value):
        if value != 0:
            self.elements[(currRow, currCol)] = value
        elif (currRow, currCol) in self.elements:
            del self.elements[(currRow, currCol)]

    def add(self, other):
        result = UniqueSparseMatrix()
        result.numRows = self.numRows
        result.numCols = self.numCols
        for (row, col), value in self.elements.items():
            result.set_element(row, col, value + other.get_element(row, col))
        return result

    def subtract(self, other):
        result = UniqueSparseMatrix()
        result.numRows = self.numRows
        result.numCols = self.numCols
        for (row, col), value in self.elements.items():
            result.set_element(row, col, value - other.get_element(row, col))
        return result

    def multiply(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Matrix multiplication not possible: Columns of first matrix must equal rows of second matrix.")

        result = UniqueSparseMatrix()
        result.numRows = self.numRows
        result.numCols = other.numCols
        for (rowA, colA), valueA in self.elements.items():
            for colB in range(other.numCols):
                valueB = other.get_element(colA, colB)
                if valueB != 0:
                    resultValue = result.get_element(rowA, colB) + valueA * valueB
                    result.set_element(rowA, colB, resultValue)
        return result


def main():
    # User input to select operation
    print("Select operation: 1. Add 2. Subtract 3. Multiply")
    choice = input()

    # Load matrices from the file
    matrixOne = UniqueSparseMatrix(inputFilePath='easy_sample_04_1.txt')
    matrixTwo = UniqueSparseMatrix(inputFilePath='easy_sample_04_2.txt')

    # Perform the selected operation
    if choice == '1':
        result = matrixOne.add(matrixTwo)
    elif choice == '2':
        result = matrixOne.subtract(matrixTwo)
    elif choice == '3':
        result = matrixOne.multiply(matrixTwo)
    else:
        print("Invalid choice")
        return

    # Print the result
    for (row, col), value in result.elements.items():
        print(f"({row}, {col}, {value})")


if __name__ == "__main__":
    main()
