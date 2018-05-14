# Majesty: For The Realm -- Machine Version

To get started in your terminal, type:

```
python -i main.py
```

This will open an interactive REPL session with Python. `main.py` initializes a 4 player Game instance, g, that you can use to interact with the implemented features.

In general, the `Game` instance interacts with its group of `Player` instances. `Player` instances interacts with its group of `Location` instances. `Location` instances contain the scoring algorithm for its particular `Location` type, its side ('A' or 'B'), and the amount of workers currently occupying itself.

`Player` and `Location` instances only return what the -additions- to wealth and meeple counts -would- be. The `Game` object compiles the players wealth and meeple count.
