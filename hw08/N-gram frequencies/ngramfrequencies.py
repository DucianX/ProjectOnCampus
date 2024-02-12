class NgramFrequencies:
    def __init__(self, n):
        self.n_gram_dict = {}
        self.n = n
        self.total_count = 0

    def add_item(self, n_gram):
        if n_gram in self.n_gram_dict:
            self.n_gram_dict[n_gram] += 1
        else:
            self.n_gram_dict[n_gram] = 1
        self.total_count += 1

    def top_n_counts(self, n):
        return sorted(self.n_gram_dict.items(), key=lambda x: x[1],
                      reverse=True)[:n]  # [:n] to slice the top n

    def top_n_freqs(self, n):
        new_list = []
        self.n_gram_dict_freq = {}
        for _ in self.n_gram_dict:
            self.n_gram_dict_freq[_] = round((self.n_gram_dict[_] /
                                              self.total_count), 3)
        original_list = sorted(self.n_gram_dict_freq.items(), key=lambda x: x[1], reverse=True)[:n]
        for original_tuple in original_list:
            connected_str = '_'.join(original_tuple[0])
            original_tuple = (connected_str, original_tuple[1])
            new_list.append(original_tuple)
        return new_list
