import sys
from data_analysis import DataAnalysis

def main(file_name):
    data = DataAnalysis()
    print(f"Reading data from {file_name}")
    data.read_data(file_name)
    
    TOP_ELEMENTS = 10

    if data.lang_counter:
        print("Languages:")
        print_output(data.top_n_lang_freqs(TOP_ELEMENTS))
    else:
        print("No language data found.")

    if data.tld_counter:
        print("Top level country domains:")
        print_output(data.top_n_country_tlds_freqs(TOP_ELEMENTS))
    else:
        print("No TLD data found.")

ROUND_TO = 3

def print_output(collection):
    for item in collection:
        print(f"{item[0]}: \t {round(item[1], ROUND_TO)}")

# Temporarily hardcode the path to the CSV for diagnostics
# csv_file_path = '/Users/asuiro/Desktop/cs5001/lab08/user_data_starter/users.csv'
# main(csv_file_path)
main(sys.argv[1])
