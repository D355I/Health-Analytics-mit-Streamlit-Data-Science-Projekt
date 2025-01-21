import numpy as np
import pandas as pd
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox

file = pd.read_excel(askopenfilename())

# Überprüfen, ob die Spalte "Krankheiten" existiert
if "Krankheiten" in file.columns:
    # Nur die Zeilen beibehalten, die "Ingesamt" enthalten
    cleaned_file = file[file["Krankheiten"].str.contains("Insgesamt", case=False, na=False)]
else:
    messagebox.showerror("Fehler", "Spalte 'Krankheiten' nicht in der Excel-Datei gefunden")
    raise SystemExit

# Bereinigte Datei speichern
try:
    ausgabe_dateipfad = asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Dateien", "*.xlsx")], title="Speicherort auswählen")
    cleaned_file.to_excel(ausgabe_dateipfad, index=False)
    messagebox.showinfo("Erfolg", "Bereinigte Datei wurde gespeichert")
except Exception as e:
    messagebox.showerror("Fehler", f"Fehler beim Speichern der Datei: {e}")