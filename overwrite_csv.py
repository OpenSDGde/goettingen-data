import os
import sys

# Standardinhalt, der in jede CSV-Datei geschrieben werden soll
STANDARD_CONTENT = """Year,Value
2019,1
2020,2
"""

def overwrite_csv_files(directory):
    # Überprüfen, ob der angegebene Pfad ein Verzeichnis ist
    if not os.path.isdir(directory):
        print(f"Der Pfad '{directory}' ist kein gültiges Verzeichnis.")
        return

    # Durchlaufen aller Dateien im Verzeichnis
    for filename in os.listdir(directory):
        if filename.lower().endswith('.csv'):
            file_path = os.path.join(directory, filename)
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(STANDARD_CONTENT)
                print(f"Überschrieben: {file_path}")
            except Exception as e:
                print(f"Fehler beim Überschreiben von {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Verwendung: python overwrite_csv.py ./data")
        sys.exit(1)

    target_directory = sys.argv[1]
    overwrite_csv_files(target_directory)
