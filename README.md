# Pairwise Ranking System

This is a simple Python program that helps you rank a list of items based on your preferences using a pairwise comparison approach. The program asks you a series of "this or that" questions, comparing two items at a time, and uses your answers to generate a ranked list of items.

This method is useful when you want to determine your preference order but aren't sure how to rank items directly! Just answer the questions, and It will give you your own ranking!

---

## 🚀 How to Run

Ensure you have Python 3 installed on your system and then run the script! Open a terminal or command prompt, navigate to the directory where `ranker.py` is saved, and run:

```
python ranker.py
```

---

## Input Items:

When prompted, enter the items you want to rank, separated by commas:

```
Enter the items to rank, separated by commas: Pizza, Sushi, Burgers, Pasta
```

---

The program will ask you which of two items you prefer until a complete ranking is determined.

---

## 📦 Sample Output

```
Welcome to the ranking system!
Enter the items to rank, separated by commas: Style, I Did Something Bad, August, Tolerate It

Let's start the ranking process.

Which do you prefer?
1: I Did Something Bad
2: Tolerate It
Enter 1 or 2: 1

Which do you prefer?
1: Style
2: I Did Something Bad
Enter 1 or 2: 2

Which do you prefer?
1: Style
2: Tolerate It
Enter 1 or 2: 1

Which do you prefer?
1: August
2: I Did Something Bad
Enter 1 or 2: 2

Which do you prefer?
1: August
2: Style
Enter 1 or 2: 2

Which do you prefer?
1: August
2: Tolerate It
Enter 1 or 2: 2

Your ranked items are:
1. I Did Something Bad
2. Style
3. Tolerate It
4. August
```

---

Happy Ranking! 🎉
