import re
from collections import Counter


class DataAnalysis:

    
    def __init__(self):
        self.lang_counter = Counter()
        self.tld_counter = Counter()
        

    def read_data(self, file_name):
        try:
            with open(file_name, 'r') as file:
                print(f"File {file_name} opened successfully.")
                next(file) # Skip header line
                for line in file:
                    print(f"Processing line: {line.strip()}")  # Add this line for diagnostics
                    fields = line.strip().split(',') 
                    if fields:
                        language = fields[-1]
                        self.lang_counter[language] += 1

                        # Extract tld(top-level domain) and increment count
                        # if it's a country code(2 characters)
                        email = fields[3]
                        tld_match = re.search(r'\.([a-z]{2})$', email.split('@')[-1])
                        if tld_match:
                            tld = tld_match.group(1)
                            self.tld_counter[tld] += 1
                        else:
                            tld_match = re.search(r'\.([a-z]{2,3})(\.([a-z]{2}))?$', email.split('@')[-1])
                            tld = tld_match.group(1)
                            self.tld_counter[tld] += 1
                        # else:
                        #     print(f"No TLD match found for email: {email}")
                    else:
                        print("No data in line.")
        except FileNotFoundError:
            print(f"File {file_name} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def top_n_lang_freqs(self, N):
        total_langs = sum(self.lang_counter.values())
        # Sort the languages by frequency using sorted() and lambda
        sorted_langs = sorted(self.lang_counter.items(), key=lambda x: x[1], reverse=True)
        return [(lang, count / total_langs) for lang, count in sorted_langs[:N]]

    def top_n_country_tlds_freqs(self, N):
        total_tlds = sum(self.tld_counter.values())
        # Sort the TLDs by frequency using sorted() and lambda
        sorted_tlds = sorted(self.tld_counter.items(), key=lambda x: x[1], reverse=True)
        return [(tld, count / total_tlds) for tld, count in sorted_tlds[:N]]


#Alternative way of doing it:
    # def top_n_lang_freqs(self, N):
    #     total_langs = sum(self.lang_counter.values())
    #     return [(lang, count / total_langs) for lang, count in self.lang_counter.most_common(N)]
    

    # def top_n_country_tlds_freqs(self, N):
    #     total_tlds = sum(self.tld_counter.values())
    #     return [(tld, count / total_tlds) for tld, count in self.tld_counter.most_common(N)]


data_analysis = DataAnalysis()
data_analysis.read_data('/Users/asuiro/Desktop/cs5001/lab08/user_data_starter/users.csv')


    # TODO:
    # Implement top_n_lang_freqs()
    # Should take a number N as an argument and return
    # an N-length list of tuples representing languages
    # and their frequencies in the data, ordered from
    # highest frequency to lowest.

    # TODO:
    # Implement top_n_country_tlds_freqs()
    # Should take a number N as an argument and return
    # an N-length list of tuples representing country (2-letter)
    # top-level domain identifiers (e.g. 'jp', 'uk', 'cn', 'ca')
    # and their frequencies as email domains the data, ordered 
    # from highest frequency to lowest.

    # TODO:
    # Implement any other necessary/helpful methods to support
    # the ones above.
