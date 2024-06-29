Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
... 
... def count_words(filename):
...     word_counts = {}
...     with open(filename, 'r', encoding='utf-8') as file:
...         for line in file:
...             for word in line.strip().split():
...                 word = word.lower()
...                 word_counts[word] = word_counts.get(word, 0) + 1
...     return word_counts
... 
... def print_word_counts(word_counts):
...     sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
...     for word, count in sorted_counts:
...         print(f'{word}: {count}')
... 
... def main():
...     if len(sys.argv) != 2:
...         print('Usage: python wdcount_xxxxxxx.py <filename>')
...         sys.exit(1)
...    
...     filename = sys.argv[1]
...     word_counts = count_words(filename)
...     print_word_counts(word_counts)
... 
... if __name__ == '__main__':
