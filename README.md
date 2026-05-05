# JARILLA_ModelSim_Prefi_PT2
Families prob Distribution

# Distribution Visualizer (Python)

This project reads an Excel file containing datasets of different probability distributions and visualizes them using histograms in Python.

## Description

The script loads an Excel file named `distribution_data.xlsx` from the Downloads folder. Each sheet in the file represents a different distribution. The program then plots all distributions in a grid layout using matplotlib.

## Requirements

Install the required libraries before running the script:

pip install pandas matplotlib openpyxl

## How to Run

1. Make sure the file `distribution_data.xlsx` is located in your Downloads folder.
2. Run the Python script:

python visualizer.py

3. A window will open showing all the distribution graphs.

## Notes

* Each sheet in the Excel file must contain a column named "Values".
* The script automatically reads all sheets and generates histograms.
* The output displays 10 graphs arranged in a 5 by 2 grid.

## Author

Angelo Jarilla

Video demo: https://drive.google.com/file/d/1dU0nViXaITGgJhPTnx3QVokEI-6KKtjG/view?usp=drive_link
