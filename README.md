# Chapter 5 Exercises: Getting Data into Pandas

This repository contains exercises 5-1 through 5-5 from Chapter 5.

## Prerequisites

Before you do any of the exercises in this book, you need to:
1. Install the **Anaconda** distribution of Python.
2. Install the **JupyterLab** Notebooks for this book.
   - For details, see the appendix for your operating system.

## Instructions

You will need your textbook to get the specific instructions for the exercises from the back of Chapter 5. If you are still waiting for your book to arrive, the specific instruction steps are included below.

---

### Exercise 5-1: Get data from a CSV file
In this exercise, you'll get polling data about the 2016 presidential election in the US. To do that, you'll download a CSV file, save it to your disk, and read that CSV file into a DataFrame.

1. **Open the notebook** named `ex_5-1` in this folder: `/exercises/ch05/ex1`.
   - *Note:* This file includes one cell that imports the Pandas library and another cell that specifies the URL for the CSV file.
2. **Download the CSV file**: With figure 5-3 as a guide, add a cell that downloads the CSV file for the Polling data and saves it to your local disk.
3. **Examine the data**: Find the CSV file on your disk and open it. This is an easy way to examine the data in a dataset.
4. **Read into DataFrame**: Add a cell that uses the `read_csv()` method to read the downloaded CSV file into a DataFrame.

### Exercise 5-2: Get data from an Excel file in a zip file
In this exercise, you'll get data about jobs in the US. To do that, you'll download a zip file that contains an Excel file, save it to your disk, unzip the Excel file, and read it into a DataFrame.

> **Note:** Some students have reported 403 errors when grabbing the zipped file from the URL in the code. Ensure you download the zip file to the same folder as your Jupyter Notebook. **Do not extract it manually**; the program will do it for you.

1. **Open the notebook** named `ex_5-2` in this folder: `/exercises/ch05/ex2`.
2. **Download the zip file**: With figure 5-3 as a guide, add a cell that downloads the zip file. This may take a while as the Excel file contains over 400,000 rows.
3. **Extract the file**: With figure 5-4 as a guide, add another cell to extract the files from the zip file and display the names of those files.
4. **Examine the Excel file**: Note that this file contains two tabs: one for data and one for documentation.
5. **Review documentation**: Determine if the documentation tab is useful.
6. **Read into DataFrame**: Add a cell that reads the data from the Excel file into a DataFrame and displays its first five rows.

### Exercise 5-3: Get data from a database
In this exercise, you'll get data about forest fires in the US. To do that, you'll download a zip file that contains a SQLite database file, unzip the database file, and read selected data into a DataFrame.

#### Setup for `pyreadstat`
If you get a `ModuleNotFoundError` for `pyreadstat`, you can install it within Jupyter Lab:

**Conda:**
```bash
%conda install -c conda-forge pyreadstat
```

**Pip (Google Colab):**
```bash
!pip install pyreadstat
```

1. **Open the notebook** named `ex_5-3` in this folder: `/exercises/ch05/ex3`.
2. **Download the zip file**: With figure 5-3 as a guide, add a cell that downloads the zip file.
3. **Extract and identify files**: With figure 5-4 as a guide, add a cell that extracts the files and prints the filenames. Note the SQLite file and the PDF documentation.
4. **Review documentation**: Open the PDF file and see if it provides useful information.

### Exercise 5-4: Get data from a Stata file
In this exercise, you'll get polling data about social surveys conducted by NORC at the University of Chicago using a Stata file.

1. **Open the notebook** named `ex_5-4` in this folder: `/exercises/ch05/ex4`.
2. **Run the cells**: The ZIP file unzips into three files: release notes (PDF), data file (`.DTA`), and a codebook (PDF).
3. **Review codebook**: Open `GSS_Codebook.pdf`. Page 1 lists column names and descriptions.
4. **Metadata DataFrame**: Add a cell to get the metadata container for the Stata file.
5. **Display metadata**: Use attributes from figure 5-7. Note that this dataset has 6,110 columns!
6. **Build metadata DataFrame**: Use the first procedure in figure 5-8 to build and display a DataFrame for the metadata.
7. **Read into DataFrame**: Use the second procedure in figure 5-8 to read at least five columns into a DataFrame and display results.

### Exercise 5-5: Get data from a JSON file
In this exercise, you'll get data from a JSON file containing shot data for Stephen Curry.

1. **Open the notebook** named `ex_5-5` in this folder: `/exercises/ch05/ex5`.
2. **Download data**: Run the first two cells to download and save `shots.json`.
3. **Inspect JSON**: Open `shots.json` in the file browser and drill down into the data structure.
4. **Process JSON**: With figure 5-11 as a guide, convert the JSON file to a dictionary object, build the DataFrame, and display results.

