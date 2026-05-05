import pandas as pd
import matplotlib.pyplot as plt
import os


downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
file_path = os.path.join(downloads_path, "distribution_data.xlsx")

excel_file = pd.ExcelFile(file_path)


fig, axes = plt.subplots(5, 2, figsize=(12, 18))
axes = axes.flatten()


for i, sheet in enumerate(excel_file.sheet_names):
    df = excel_file.parse(sheet)
    axes[i].hist(df["Values"], bins=30)
    axes[i].set_title(sheet)
    axes[i].set_xlabel("Values")
    axes[i].set_ylabel("Frequency")

plt.tight_layout()
plt.show()