import re


class TextCleaner:
    def __init__(self):
        self.processed_context = []

    def process(self, context):
        self.context = context.lower()

        # Replace common abbreviations
        self.context = self.context.replace('mr.', 'mr').replace('dr.', 'dr')

        # Replace commas with a token
        self.context = self.context.replace(',', ' COMMA')

        # Remove all other punctuation (excluding apostrophes)
        self.context = re.sub(r'[!"#$%&\()*+,-./:;<=>?@\[\\\]^_`{|}~]', '',
                              self.context)
        # r意味着转移字符失效(no escape codes)

        # Split into sentences based on periods
        self.sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s',
                                  self.context)

        self.tokenized_sentences = [self.sentence.split() for self.sentence in
                                    self.sentences]

        return self.tokenized_sentences
