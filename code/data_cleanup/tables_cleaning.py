import numpy as np
import pandas as pd
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

file = pd.read_excel(askopenfilename())
rows = file.head(1).to_string()
messagebox.showinfo("File Head", rows)



