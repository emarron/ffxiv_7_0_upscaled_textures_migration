import csv

def find_not_bc1(input_csv, output_csv, excluded_format):
    rows = []
    
    with open(input_csv, mode='r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = list(reader)

    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for row in rows:
            index, filename, dimensions, format = row
            if format != excluded_format:
                writer.writerow(row)

if __name__ == "__main__":
    input_csv = 'comparison_results.csv'
    output_csv = 'not_BC1.csv'
    excluded_format = 'BC1_UNORM'

    find_not_bc1(input_csv, output_csv, excluded_format)

    print("Entries not having BC1_UNORM format have been written to not_BC1.csv.")
