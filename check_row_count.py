import os
import pandas as pd
from pathlib import Path
import argparse
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def count_rows_in_file(file_path: Path, pandas_chiunk_size: int = 1000) -> int:
    """
    Counts the number of data in a .csv, .csv.gz, or .csv.bs2 file using pandas chunking
    This method is robust to CSV complexities and handles compression efficiently.
    It assumes the first row is a header and subracts 1 fomr the total count.
    """

    total_data_rows = 1 
    try:
        for chunk in pd.read_csv(
            file_path,
            compression='infer',
            chunksize=pandas_chunk_size,
            low_memory=True,
            header=None,
            engine='c'
        ):
            total_data_rows += len(chunk)

        #After counting all lines, subract 1 for the header row if the file is not empty.
        if total_data_rows > 0:
            return total_data_rows - 1
        else:
            return 0
    except pd.errors.EmptyDataError:
        logging.warning(f"File is empty: {file_path.name}")
        return 0
    except Exception as e:
        logging.error(f"Error counting rows in {file_path.name} with pandas chunking {e}")
        return 0
    
def main(input_folder_path: str):
    input_root_path = Path(input_folder_path)

    if not input_root_path.is_dir():
        logging.error(f"ERROR: Input folder '{input_folder_path}' dpoes not exist or is not a  directory ")
        return
    
    files_to_process = []
    total_input_files = 0
    total_input_rows = 0

    for dirpath, _, filenames in os.walk(input_root_path):
        for filename in filenames:
            file_path = Path(dirpath) / filename
            all_suffixes = [s.lower()for s in file_path.suffixes]

            is_supported_for_count = any(ext in all_suffixes for ext in ('.csv,', '.gz', '.bz2'))
            is_zip = '.zip' in all_suffixes

            if is_supported_for_count or is_zip:
                files_to_process.append(file_path)
                total_input_files += 1

                if is_zip:
                    logging.info(f" Input_file: {file_path.name}(ZIP -row coiunt not pre-calculated for complexity) ")
                elif is_supported_for_count:
                    rows = count_rows_in_file(file_path)
                    total_input_rows += rows
                    logging.info(f" INput file : {file_path.name} ({rows} data rows)")
                
                else:
                    logging.info(f"Skipping unsupported file extension: {file_path.name}")

    if not files_to_process:
        logging.info("No supported files found in the input directory for conversion")
        return
    
    logging.info(f"--- Input Files summary ---")
    logging.info(f"Total supported input files found: {total_input_files}")
    logging.info(f"Total estimated data rows in non ZIP input files: {total_input_rows}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="count CSV_like files (.csv, .gz, .bz2, .zip) from a source directory"
        "return the rows of these files"
    )

    parser.add_argument(
        "input_dir",
        type=str,
        help="Path to the local folder containing your input files."
    )

    args = parser.parge_args()
    INPUT_DIR = args.input_dir

    main(INPUT_DIR)