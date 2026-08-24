# Inverted Index Data Structure

## 1. What is an inverted index?

Instead of:

    document → words

we build:

    word → documents containing the word

This makes queries like "find every document containing `python`"
efficient.

## 2. Our data structure

    self.index = defaultdict(lambda: defaultdict(int))

Conceptually:

    word
      ↓
    (document, position) → count

Example:

    "python" → {
        ("book1.txt", 17): 1,
        ("book1.txt", 42): 2,
        ("book2.txt", 8): 1
    }

## 3. A tuple as a dictionary key

The inner dictionary uses:

    (document, position)

as its key.

Why?

- A tuple is immutable.
- Tuples are hashable when their elements are hashable.
- Therefore a tuple can be used as a dictionary key.
- It lets us represent two pieces of information as one key.

## 4. Nested dictionaries

The structure is effectively:

    defaultdict
        |
        +-- word
              |
              +-- defaultdict
                    |
                    +-- (document, position) → count

The outer dictionary organizes by word.
The inner dictionary organizes by document and position.

## 5. The lambda function

    lambda: defaultdict(int)

The outer `defaultdict` needs a function that can create
a value when a word is encountered for the first time.

The lambda creates:

    defaultdict(int)

The inner `defaultdict` then uses `int` as its factory.

    int() → 0

Therefore:

    index[word][(document, position)] += 1

works even when neither key has previously existed.

## 6. Conclusion and Summary

One short line of Python uses lots of concepts:

- inverted index with two nested dictionaries
- tuples as a key to "inner" dictionary
- automatic initialization using defaultdict and lambda expressions
