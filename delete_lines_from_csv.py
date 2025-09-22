import csv
import argparse

def delete_lines_from_csv(input_file, output_file, num_lines_to_delete):
    """
    Deletes a given number of lines from CSV file and writes the results to a new file

    :param input_file: path to the input CSV file
    :param output_file: path to the ouput file
    :param num_lines_to_delete: Number of lines to delete from the beginning of the file
    """

    try:
        # Open the input for reading
        with open(input_file, 'r', newline='') as infile:
            reader = csv.reader(infile)

            #Read all rows from the input file
            rows = list(reader)

            #skip the specified number of line
            remaining_rows = rows[num_lines_to_delete:]

        # Open the output file for writing
        with open(output_file,'w',newline='') as outfile:
            writer = csv.writer(outfile)

            writer.writerows(remaining_rows)

        print(f"successfully deleted {num_lines_to_delete}lines from {input_file} and saved to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="this script is used to delete lines from very large CSV files"
        "this to avoid opening large csv file to reduce the size of the csv file"
    )
    parser.add_argument(
        "input_dir",
        type=str,
        help="Path to the file that needs lines to be delted"
    )

    parser.add_argument(
        "output_dir",
        type=str,
        help="name of the file after editing"
    )
    parser.add_argument(
        "number_of_lines",
        type=int,
        help="number of lines that needs to be deleted"
    )

    args = parser.parse_args()

    INPUT_DIR = args.inmput_dir
    OUTPUT_DIR= args.output_dir
    NUMBER_OF_LINES = args.number_of_lines

#Example usage
input_csv='path/to/csv/file.csv'
output_csv='path/to/csv/file_1.csv'
lines_to_delete = 200000

delete_lines_from_csv(INPUT_DIR, OUTPUT_DIR, NUMBER_OF_LINES)