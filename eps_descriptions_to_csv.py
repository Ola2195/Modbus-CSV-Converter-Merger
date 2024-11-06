import csv
import re
import argparse
import os

def txt_to_csv_eps(input_file, output_file):
    """
    Funkcja odczytuje plik TXT z opisami punktów i zapisuje dane do pliku CSV.
    
    Argumenty:
    input_file (str): Ścieżka do pliku wejściowego (TXT), który zawiera dane do konwersji.
    output_file (str): Ścieżka do pliku wyjściowego (CSV), w którym zapisane będą dane po konwersji.
    """

    # Nagłówki dla pliku CSV
    headers = ['Nr_punktu', 'Nazwa_punktu']

    # Wzorzec wyrażenia regularnego dla linii danych
    pattern = re.compile(r"^\.\|(\d+)\|([^\|]+)\|([^\|]+)\|([^\|]+)")

    with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file, open(input_file, mode='r', encoding='ISO-8859-2') as file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)

        for line in file:
            match = re.match(pattern, line)
            if match:
                punkt = match.group(1)
                nazwa = match.group(4).strip()
                writer.writerow([punkt, nazwa])

    print(f"Plik CSV został zapisany jako {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Funkcja do konwersji pliku TXT z lista punktow do CSV, ktory zawiera numer punktu i nazwe.")
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
    
    txt_to_csv_eps(args.input_file_path, args.output_file_path)