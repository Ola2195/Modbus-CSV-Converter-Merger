# Modbus CSV Converter and Merger

This repository contains three Python scripts that help in processing Modbus configuration and merging CSV files. The scripts perform the following tasks:

1. **`txt_to_csv_modbus.py`**: Converts a TXT file containing Modbus slave configuration into a CSV file.
2. **`txt_to_csv_eps.py`**: Converts a TXT file containing point descriptions into a CSV file.
3. **`merge_csv_files.py`**: Merges two CSV files based on a common column `Nr_punktu`.

## Prerequisites

Before running the scripts, ensure you have Python installed on your system. You will also need the following Python packages:

- `pandas` – for CSV handling and merging
- `re` – for regular expressions (should be included by default with Python)
- `argparse` – for command-line argument parsing (included by default in Python)

## Scripts

### 1. **`txt_to_csv_modbus.py`**: Convert Modbus Configuration TXT to CSV

This script reads a TXT file containing Modbus slave configuration and saves the data into a CSV file.

#### Input File Format (Modbus)

The input TXT file should contain lines with Modbus slave configuration data in the following format:

```
M <Nr_rejestru> <Nr_punktu> <Typ_pam> <Post_wart> <WspA> <WspB> <Ofset_bitu> <Ilosc_bitow>
R <Nr_rejestru> <Nr_punktu> <Typ_pam> <Post_wart> <WspA> <WspB> <Ofset_bitu> <Ilosc_bitow>
```

- `M` or `R`: Type of register.
- `Nr_rejestru`: Register number.
- `Nr_punktu`: Point number.
- `Typ_pam`: Memory type (one of: `S`, `F`, `L`, `U`, `B`).
- `Post_wart`: Post value.
- `WspA`: A parameter.
- `WspB`: Another parameter.
- `Ofset_bitu`: Bit offset.
- `Ilosc_bitow`: Number of bits.

Example of an input file (`modbus_slave_config.txt`):

```
M 100 200 S 1 10 20 5 16
R 101 201 F 2 12 22 7 32
```

#### Usage

```bash
python txt_to_csv_modbus.py <input_file_path> [output_file_path]
```

- **`input_file_path`**: Path to the input TXT file containing Modbus slave configuration data.
- **`output_file_path`** (optional): Path to the output CSV file. The default is `output.csv`.

#### Example

```bash
python txt_to_csv_modbus.py modbus_config.txt modbus_config.csv
```

This will convert the `modbus_config.txt` to `modbus_config.csv`.

### 2. **`txt_to_csv_eps.py`**: Convert Point Descriptions TXT to CSV

This script reads a TXT file containing point descriptions and saves the data into a CSV file.

#### Input File Format (EPS)

The input TXT file should contain lines with point descriptions in the following format:

```
.|<Nr_punktu>|<Nazwa_punktu>|<OtherField1>|<OtherField2>
```

- `Nr_punktu`: Point number.
- `Nazwa_punktu`: Point name.
- `<OtherField1>`, `<OtherField2>`: Other fields, which are not used in this script.

Example of an input file (`eps_opisy_punktow.txt`):

```
.|100|Temperature|Field1|Field2
.|101|Pressure|Field1|Field2
```

#### Usage

```bash
python txt_to_csv_eps.py <input_file_path> [output_file_path]
```

- **`input_file_path`**: Path to the input TXT file containing point descriptions.
- **`output_file_path`** (optional): Path to the output CSV file. The default is `output.csv`.

#### Example

```bash
python txt_to_csv_eps.py points_list.txt points_list.csv
```

This will convert `points_list.txt` to `points_list.csv`.

### 3. **`merge_csv_files.py`**: Merge Two CSV Files Based on `Nr_punktu`

This script merges two CSV files based on the common column `Nr_punktu`.

#### Usage

```bash
python merge_csv_files.py <input_file1> <input_file2> [output_file]
```

- **`input_file1`**: Path to the first CSV file.
- **`input_file2`**: Path to the second CSV file.
- **`output_file`** (optional): Path to the output CSV file. The default is `output.csv`.

#### Example

```bash
python merge_csv_files.py file1.csv file2.csv merged_output.csv
```

This will merge `file1.csv` and `file2.csv` into `merged_output.csv`.

## Error Handling

The scripts include basic error handling for the following scenarios:

- File not found (if the specified input file does not exist).
- Invalid file extensions (ensuring the files are in `.csv` format).
- Incorrect arguments passed to the scripts.

---

### Notes

- **Regular Expressions**: The scripts use regular expressions to parse data from TXT files. Ensure the input files are correctly formatted according to the specified patterns for each script.
  
- **File Encoding**: The `txt_to_csv_eps.py` script assumes the input file is encoded in `ISO-8859-2`. If your file uses a different encoding, adjust the `encoding` argument in the `open` function accordingly.
