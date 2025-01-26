

# Allgemein zum Repository:
 Hier ist die zentrale Dokumentationsdatei, die einen Überblick über das Projekt gibt. Hier kann man die Zielsetzung, eingesetzte Methoden und den Ablauf des Projekts verstehen.
![Tree Chart](treechart.png)
# Struktur des Githubs:
Unsere Struktur des Projektes in Github ist folgendermaßen Wir haben 3 Bereiche den code, Daten und den Tool Bereich.
# Code Bereich:
  ## Code-Bereich

Der Code-Bereich wird in zwei Hauptbereiche unterteilt: **Data Cleanup** und **Streamlit**.

### Data Cleanup:
- **get_rid_of_NULL.ipynb:** Identifiziert und entfernt Spalten mit ausschließlich fehlenden Werten.  
- **tables_cleaning.py:** Aggregiert und bereinigt die Daten weiter.  
- Weitere Skripte:  
  - `zusammenfassung_dia.py`: Zusammenfassung der Excel-Dateien zu Diagnosen.  
  - `zusammenfassung_tode.py`: Zusammenfassung der Excel-Dateien zu Todesfällen.  

### Streamlit:
#### Kernmodule:
- **functions.py:** Zentrale Funktionen für die Datenverarbeitung und Analysen.  
- **Info.py:** Spezifische Informationen über die Daten, die für die Benutzeroberfläche benötigt werden.  
- **get_data.py:** Beschafft die Rohdaten und verarbeitet sie für die Analyse.  

#### Assets & Pages:
- **pages:** Drei Streamlit-Seiten:  
  - `Entwicklung.py`: Visualisiert Entwicklungen in den Daten.  
  - `Zusammenhänge.py`: Zeigt Zusammenhänge zwischen verschiedenen Variablen.  
  - `Unterschiede.py`: Analysiert Unterschiede zwischen Datengruppen.  
- **assets:** Zusätzliche Ressourcen wie Bilder oder Stylesheets.  


# Daten-Bereich
Dieser Bereich enthält die Roh- und bereinigten Daten. Die Unterstruktur folgt den verschiedenen Verarbeitungsstufen:

## raw_data
- Die unberührten Originaldaten, unterteilt in **csv** und **excel**.  
  - **preprocessing:** Erste Vorbereitungsarbeiten an den Rohdaten.

## cleaned_data
- Enthält die bereinigten und aggregierten Daten, aufgeteilt in verschiedene Stufen:
  - **pre_cleaning:** Erste bereinigte Version der Daten.  
  - **null_cleaned:** Entfernt oder aufgefüllte Null-Werte.  
  - **final_cleaned:** Die endgültige Version der bereinigten Daten.  
    - Eine zusammengefasste Datei **final_cleaned_insgesamt** bietet eine Gesamtübersicht.

---

# Tools-Bereich
Enthält Skripte und Programme zur Unterstützung der Datenvorbereitung. Der Fokus liegt hier auf der Automatisierung und Vereinfachung des Preprocessing.

---

# TODOS

## Datenaufbereitung
- Die Rohdaten (Patientendiagnosen und Todesfälle) wurden nach Jahren sortiert und in Tabellen gespeichert (**Vor-Corona**, **Corona**, **Nach-Corona**).  
- Diese Tabellen wurden nach Abteilungen und insgesamt aggregiert, um die Übersichtlichkeit zu verbessern.

## Bereinigung fehlender Daten
- Spalten mit ausschließlich fehlenden Daten (z. B. **15-18 Jahre Weiblich**, **28-20 Jahre Weiblich**) wurden entfernt.  
- Spalten mit vereinzelten Lücken wurden durch Durchschnittswerte aufgefüllt.

## Sonderfall 2023
- Eine zusätzliche leere Spalte wurde durch Durchschnittswerte aus früheren Jahren ergänzt.

## Falsche Werte
- In den Patientendiagnosen wurden Daten aus Zeilen (z. B. **Kinderkardiologie**, **Kinderchirurgie**) entfernt, da diese offensichtlich fehlerhaft waren.

## Daten zu Todesfällen
- Die Spalte **75-80 Jahre Weiblich** wurde entfernt, da sie durchweg keine Daten enthielt.
