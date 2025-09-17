**pandas_module – Simulating the Pandas Module in Python
Problem Statement:**
  Design a user-defined Python module to simulate the pandas module.
**The module should:**
1.	Read a CSV file into a DataFrame-like structure.
2.	Provide features to:
    o	Read a particular row, column, or cell.
    o	Modify a column or a cell.
    o	Create new columns.
    o	Save the updated data back to a CSV file.
    o	Display the data.
    o	Perform simple operations like sum, max, and min on numeric columns.
3.	Handle all errors using exception handling.
4.	Be designed in a modular way so it can be imported and reused in other projects.
 ** How the Code Works:**
  •	The project defines a custom class called DataFrame that behaves like a simplified version of pandas.DataFrame.
  •	Another class called Series represents a single column and allows basic operations such as sum, max, and min.
  •	A helper function is provided to read a CSV file and prepare a DataFrame object.
  •	All operations (reading rows, columns, cells, modifying data, saving, and displaying) are implemented as methods inside these classes.
  •	Proper exception handling is included so invalid operations won’t crash the program.
  In short, the structure is:
     Using This Module in Another File:
      Once you have the pandas_module.py file in your project:
      1.	Import the module in your Python file using:
      2.	import pandas_module as pm
      3.	Read a CSV file into a DataFrame by calling the readfile function.
      4.	Perform operations like accessing rows, columns, modifying values, or saving back to a file.
**Example usage in words:**
  •	Import pandas_module.
  •	Call the function to read your CSV file, which returns a DataFrame object.
  •	Use that object to access rows, columns, or individual cells.
  •	Modify or add columns when needed.
  •	Save the changes back to a new CSV file.
  •	Run aggregation functions (sum, max, min) on any numeric column.
Why This Project is Useful
  •	Helps beginners understand how pandas works internally.
  •	Teaches object-oriented programming by building classes (DataFrame, Series).
  •	Strengthens knowledge of CSV file handling in Python.
  •	Shows how to add exception handling for safer code execution.
Limitations
  •	Works only with CSV files.
  •	Supports only basic row/column/cell operations.
  •	Aggregations are limited to sum, max, and min.
  •	It’s a learning project, not a full replacement for pandas.
The files attached in this git will have the code which helps in getting the things as explained in this documentation. (Files: pandas_module.py, usage.py)
