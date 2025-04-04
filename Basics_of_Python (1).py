#Display Fibonacci Series up to 10 terms

def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    while len(fib_series) < n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Example usage
print(fibonacci_series(10))
#Display numbers at the odd indices of a list

def numbers_at_odd_indices(lst):
    return [lst[i] for i in range(1, len(lst), 2)]

# Example usage
input_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numbers_at_odd_indices(input_list))

#Count the number of different words in the provided text

def count_unique_words(text):
    words = text.lower().split()
    return len(set(words))

# Example usage
input_string = """
I have provided this text to provide tips on creating interesting paragraphs.
First, start with a clear topic sentence that introduces the main idea.
Then, support the topic sentence with specific details, examples, and evidence.
Vary the sentence length and structure to keep the reader engaged.
Finally, end with a strong concluding sentence that summarizes the main points.
Remember, practice makes perfect!
"""
print(count_unique_words(input_string))

#Write a function count_vowels(word)

def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for letter in word if letter in vowels)

# Example usage
print(count_vowels("education"))
#Iterate through the list of animals and print each one in all caps

def print_animals_in_caps(animals):
    return [animal.upper() for animal in animals]

# Example usage
animals_list = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
print(print_animals_in_caps(animals_list))
#Program that iterates from 1 to 20, printing each number and whether it's odd or even

def odd_or_even():
    result = []
    for i in range(1, 21):
        result.append((i, "Odd" if i % 2 != 0 else "Even"))
    return result

# Example usage
print(odd_or_even())
#Function sum_of_integers(a, b)

def sum_of_integers(a, b):
    return a + b

# Example usage
print(sum_of_integers(5, 7))
