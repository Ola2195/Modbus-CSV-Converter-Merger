import csv
import re
import argparse
import os

def txt_to_csv_modbus(input_file, output_file):
    """
    Funkcja odczytuje plik TXT zawierajacy konfiguracje Modbus slave i zapisuje dane do pliku CSV.
    
    Argumenty:
    input_file (str): Sciezka do pliku wejsciowego (TXT), ktory zawiera dane do konwersji.
    output_file (str): Sciezka do pliku wyjsciowego (CSV), w ktorym zapisane beda dane po konwersji.
    """
        
    # Naglowki dla pliku CSV
    headers = ["Typ_pam", "Nr_rejestru", "Nr_punktu", "Post_wart", "WspA", "WspB", "Ofset_bitu", "Ilosc_bitow"]
    
    # Wzorzec wyrazenia regularnego dla linii danych
    pattern = r"^(M|R)\s+(\d+)\s+(\d+)\s+([SFLUB])\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)$"

    with open(input_file, 'r', encoding='utf-8') as txt_file, open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        
        for line in txt_file:
            line = line.strip() # Usun biale znaki
            match = re.match(pattern, line)

            if match:
                row = match.groups()
                writer.writerow(row)
        
        print(f"Plik CSV {output_file} został zapisany.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Funkcja do konwersji pliku TXT z konfiguracja modbus slave do CSV.")
    parser.add_argument("input_file_path", help="Sciezka do pliku wejsciowego (TXT).")
    parser.add_argument(
        "output_file_path",
        nargs="?",  # Argument jest opcjonalny
        default="output.csv",
        help="Sciezka do pliku wyjsciowego (CSV)."
    )
    args = parser.parse_args()

    # Sprawdzenie, czy plik wejsciowy istnieje
    if not os.path.exists(args.input_file_path):
        print(f"Blad: Plik wejsciowy '{args.input_file_path}' nie istnieje.")
        exit(1)

    # Sprawdzenie, czy rozszerzenie pliku wyjsciowego to .csv
    if not args.output_file_path.lower().endswith('.csv'):
        print(f"Blad: Plik wyjsciowy musi miec rozszerzenie '.csv'.")
        exit(1)
    
    txt_to_csv_modbus(args.input_file_path, args.output_file_path)