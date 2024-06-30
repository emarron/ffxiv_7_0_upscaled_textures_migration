def read_file_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    return set(lines)

def compare_files(reusable_file, all_bgcommon_file, differs_file):
    reusable_lines = read_file_lines(reusable_file)
    all_bgcommon_lines = read_file_lines(all_bgcommon_file)

    differs_lines = all_bgcommon_lines - reusable_lines

    with open(differs_file, 'w') as file:
        for line in sorted(differs_lines):
            file.write(line + '\n')

if __name__ == "__main__":
    reusable_file = 'reusable.txt'
    all_bgcommon_file = 'all_bgcommon_of_7-0_not_pd.txt'
    differs_file = 'differs.txt'

    compare_files(reusable_file, all_bgcommon_file, differs_file)

    print("Comparison completed successfully.")
