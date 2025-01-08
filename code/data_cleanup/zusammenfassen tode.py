import pandas as pd
from tkinter.filedialog import askopenfilename, asksaveasfilename
import re

def kategorisiere_spalte(spaltenname):
    """Kategorisiert eine Spalte basierend auf ihrem Namen."""
    match = re.search(r'(\d+)-?(\d+)?', str(spaltenname))  # Sicherstellen, dass der Spaltenname ein String ist
    if match:
        unteres_alter = int(match.group(1))
        oberes_alter = int(match.group(2)) if match.group(2) else None

        if oberes_alter is not None:
            if oberes_alter < 13:
                return "Kind"
            elif oberes_alter <= 18:
                return "Jugendlich"
            elif oberes_alter <= 65:
                return "Erwachsener"
            else:
                return "Senior"
        else:
            if unteres_alter < 13:
                return "Kind"
            elif unteres_alter <= 18:
                return "Jugendlich"
            elif unteres_alter <= 65:
                return "Erwachsener"
            else:
                return "Senior"
    return None

def verarbeite_datei():
    """Verarbeitet die eingegebene Excel-Datei, kategorisiert Spalten und speichert die aktualisierten Daten."""
    dateipfad = askopenfilename(title="Wähle eine Excel-Datei aus", filetypes=[("Excel Dateien", "*.xlsx")])
    if not dateipfad:
        print("Keine Datei ausgewählt. Verarbeitung abgebrochen.")
        return

    df = pd.read_excel(dateipfad)
    print("Datei erfolgreich geladen.")
   

   
    ausgeschlossene_spalten = ["Jahr", "Todesursache"]

    kategorisierte_daten = {}
    for spalte in df.columns:
        if spalte in ausgeschlossene_spalten:
            kategorisierte_daten[spalte] = df[spalte]  # Diese Spalten werden direkt übernommen
            continue

        kategorie = kategorisiere_spalte(spalte)  # Verarbeite den Spaltennamen
        if kategorie:
            # Geschlecht unterscheiden
            if "weiblich" in spalte.lower():
                kategorie += " Weiblich"
            elif "männlich" in spalte.lower():
                kategorie += " Männlich"
            elif "Insgesamt" in spalte.lower():
                kategorie += " Insgesamt"

            if kategorie not in kategorisierte_daten:
                # Nur numerische Werte berücksichtigen
                kategorisierte_daten[kategorie] = pd.to_numeric(df[spalte], errors='coerce').fillna(0)
            else:
                kategorisierte_daten[kategorie] += pd.to_numeric(df[spalte], errors='coerce').fillna(0)

    kategorisiertes_df = pd.DataFrame(kategorisierte_daten)

    ausgabe_dateipfad = asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Dateien", "*.xlsx")], title="Speicherort auswählen")
    if not ausgabe_dateipfad:
        print("Kein Speicherort Verarbeitung abgebrochen.")
        return

    kategorisiertes_df.to_excel(ausgabe_dateipfad, index=False)
    print(f"Datei erfolgreich gespeichert {ausgabe_dateipfad}")

verarbeite_datei()
