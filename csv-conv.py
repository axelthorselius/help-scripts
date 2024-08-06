import csv

def convert_newline_csv_to_comma_separated(input_file, output_file):
    # Read the input file
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Strip any extra whitespace or newline characters from each line
    entries = [line.strip() for line in lines]

    # Write the output file with entries separated by commas
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(entries)

if __name__ == "__main__":
    input_file = 'input.csv'  # replace with your input file name
    output_file = 'output.csv'  # replace with your output file name
    convert_newline_csv_to_comma_separated(input_file, output_file)
