# 🐍 05: String Functions

---

## Instructions:
Write code to solve each of these problems.

Keep PEP8 in mind and make your code easy to read with meaningful variable names.

> Remember: code that you haven't run or tested is not trustworthy!

---

## String Method Usage

### 1. Length of a String
Ask the user for a word and print its length using `len()`.

### 2. Capitalize a Sentence
Ask the user for a sentence and print it with the first character capitalized using `capitalize()`.

#### 2b: Usability question:
In what situations is this a bad idea? Consider the sentence "Old MacDonald had a farm".

### 3. Convert to Uppercase
Ask the user for a sentence and print it in all uppercase letters using `upper()`.

### 4. Convert to Lowercase
Ask the user for a sentence and print it in all lowercase letters using `lower()`.

### 5. Replace a Word
Write a script that starts with the phrase "JavaScript is simple to code with".
Then change out "JavaScript" with "Python" using `replace()`.

### 6. Find a Substring
Ask the user for a sentence and find the position of the word "code" using `find()`.
If you cannot find the word "code", print out the message "I guess you had other things to talk about"

### 7. Strip Whitespace
Ask the user for a sentence with leading and trailing spaces and print it stripped using `strip()`.

### 8. Check if a Word is in a Sentence
Ask the user for a sentence and a word, then check if the word is in the sentence using `in`.

### 9. Combine Two Strings
Write a function which takes two strings and combines them with a space in-between.  The function should *return* the combined string.

### 10. Print Each Character in Uppercase
Ask the user for a word and print each character individually in uppercase using a loop.

### 11. Replace All Vowels with "*"
Ask the user for a sentence and replace all vowels with "*".

### 12. Find All Occurrences of a Letter
Ask the user for a sentence and a letter, then print all positions where the letter appears.

### 13. Count Words in a Sentence
Ask the user for a sentence and count how many words it contains using `split()` and `len()`.

### 14. Strip and Capitalize Each Word
Ask the user for a sentence and strip and capitalize each word using a loop.
Use the `split()` method.

### 15. Reverse a Sentence
Ask the user for a sentence and print it in reverse using slicing. `[:]`

> [!Note]
> Slicing has "steps", just like `range`. You can work backwards by adding a second colon, and a step value. 
> ```python
> print("abcdef"[::2])
> >>> ace 
> ```

---

## Extensions
These problems are a little harder, and require you to think a bit about *how* you are going to figure something out.

### 16. Check Palindrome
Write a function `is_palindrome(word)` that returns `True` if the word is a palindrome (and `False` if it is not).

### 17. Remove All Digits from a String
Ask the user for a string and remove all digits using a loop and `isdigit()`.
