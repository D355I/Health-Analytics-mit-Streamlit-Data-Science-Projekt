import pandas as pd
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename


try:
    
    df = pd.read_excel(askopenfilename())
    print("Datei erfolgreich geladen.")
    
    # Liste 
    print("\nVerfügbare Spalten in der Datei:")
    for idx, col in enumerate(df.columns, start=1):
        print(f"{idx}. {col}")
    
    # BSpalte 
    spalte_anzahl = int(input("\nBitte die Nummer der gewünschten Spalte eingeben: ")) - 1
    
    #  Spalte abrufen
    if 0 <= spalte_anzahl < len(df.columns):
        column_name = df.columns[spalte_anzahl]
        print(f"Gewählte Spalte: {column_name}")
        
        
        # Zeilen entfernen (insgesamt)
        if 'Todesursache' in df.columns:
            df_filtered = df[~df['Todesursache'].str.contains('insgesamt', case=False, na=False)]
            print(f"{len(df) - len(df_filtered)} Zeilen mit 'insgesamt' wurden entfernt.")
        else:
            df_filtered = df
        
        # NaN-Werte entfernen
        spalte_reinigt = pd.to_numeric(df_filtered[column_name], errors='coerce').dropna()
        print(spalte_reinigt.describe())
        
        # Berechnung 
        q1 = spalte_reinigt.quantile(0.25)  # 25%-Quantil
        q3 = spalte_reinigt.quantile(0.75)  # 75%-Quantil
        iqr = q3 - q1  # Interquartilsabstand (IQR)
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        # Dynamische Achsenbegrenzung setzen
        x_min = max(0, lower_bound - 0.1 * (upper_bound - lower_bound))
        x_max = upper_bound + 0.1 * (upper_bound - lower_bound)

        # Boxplot erstellen
        plt.figure(figsize=(10, 6))
        plt.boxplot(
            spalte_reinigt,
            vert=False,  # Horizontaler Boxplot
            patch_artist=True,  # Ermöglicht die Färbung der Box
            boxprops={'facecolor': 'lightblue', 'color': 'teal'},  # Box-Farbe
            whiskerprops={'color': 'teal'},  # Whisker-Farbe
            capprops={'color': 'teal'},  # Endkappen-Farbe
            flierprops={'marker': '.', 'color': 'red', 'markersize': 5},  # Kleine Punkte für Ausreißer
            medianprops={'color': 'black', 'linewidth': 2}  # Median-Linie
        )

        # Datenpunkte innerhalb des Boxplots 
        plt.scatter(
            spalte_reinigt,
            [1] * len(spalte_reinigt),  # Alle Punkte auf der Höhe des Boxplots
            color='blue',  # Farbe der Punkte
            alpha=0.7,  # Transparenz der Punkte
            s=20  # Größe der Punkte
        )

        # Titel und Achsenbeschriftungen
        plt.title(f'Boxplot für {column_name} (ohne "insgesamt")', fontsize=14)
        plt.xlabel('Werte', fontsize=12)
        plt.xlim(x_min, x_max)

        # Plot anzeigen
        plt.show()
    else:
        print("Ungültige Auswahl. Bitte erneut versuchen.")
except FileNotFoundError:
    print("Die angegebene Datei wurde nicht gefunden. Bitte den Pfad überprüfen.")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
