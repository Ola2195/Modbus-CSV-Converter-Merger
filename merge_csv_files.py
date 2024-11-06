import pandas as pd
import argparse
import os

def merge_csv_files(input_file1, input_file2, output_file):
    """
    Funkcja do laczenia dwoch plikow CSV na podstawie wspolnej kolumny 'Nr_punktu'.
    
    Parametry:
    input_file1 (str): Sciezka do pierwszego pliku CSV.
    input_file2 (str): Sciezka do drugiego pliku CSV.
    output_file (str): Sciezka do pliku wyjsciowego CSV, ktory bedzie zapisany z polaczonymi danymi.
    """
        
    file1 = pd.read_csv(input_file1)
    file2 = pd.read_csv(input_file2)

    # Laczenie plikow na podstawie kolumny "Nr_punktu"
    polaczony = pd.merge(file1, file2, on="Nr_punktu", how="left")

    polaczony.to_csv(output_file, index=False)

    print(f"Nowy plik {output_file} zostal utworzony.")

if __name__ == "__main__":
    # Inicjalizacja parsera argumentow
    parser = argparse.ArgumentParser(description="Skrypt do laczenia dwoch plikow CSV na podstawie kolumny 'Nr_punktu'.")
    
    # Definicja argumentow
    parser.add_argument("input_file1", help="Sciezka do pierwszego pliku CSV.")
    parser.add_argument("input_file2", help="Sciezka do drugiego pliku CSV.")
    parser.add_argument(
        "output_file",
        nargs="?",  # Argument jest opcjonalny
        default="output.csv",
        help="Sciezka do pliku wyjSciowego CSV."
    )
    
    # Parsowanie argumentow
    args = parser.parse_args()

    # Sprawdzenie, czy pliki wejSciowe istnieja
    if not os.path.exists(args.input_file1):
        print(f"Blad: Plik '{args.input_file1}' nie istnieje.")
        exit(1)
    
    if not os.path.exists(args.input_file2):
        print(f"Blad: Plik '{args.input_file2}' nie istnieje.")
        exit(1)
    
    # Sprawdzenie, czy rozszerzenia plikow wejsciowych to .csv
    if not args.input_file1.lower().endswith('.csv') or not args.input_file2.lower().endswith('.csv'):
        print(f"Blad: Pliki wejsciowe musza miec rozszerzenia '.csv'.")
        exit(1)
    
    # Sprawdzenie, czy rozszerzenia pliku wyjsciowych to .csv
    if not args.output_file.lower().endswith('.csv'):
        print(f"Blad: Plik wyjSciowy musi miec rozszerzenie '.csv'.")
        exit(1)
    
    # Wywolanie funkcji laczenia plikow
    merge_csv_files(args.input_file1, args.input_file2, args.output_file)