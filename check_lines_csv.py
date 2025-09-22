import csv
import argparse

def count_lines_in_csv(file_path):
    with open (file_path, 'r') as file:
        reader = csv.reader(file)
        line_count = sum(1 for row in reader)
    return line_count

def main():
    # set up argument parser
    parser = argparse.ArgumentParser(description="COunt the numebr of lines ina  csv file")
    parser.add_argument('file_path', type=str, help="path to the csv file")

    # parse the arguments
    args = parser.parse_args()
    file_path = args.file_path

    # count lines in a csv file
    try:
        line_count = count_lines_in_csv(file_path)
        print(f"Number of line in  csv file: {line_count}")
    except FileNotFoundError:
        print(f"Error: File Not found at '{file_path}'")
    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    main()

