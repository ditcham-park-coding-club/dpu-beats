# Writing Scores

First, add a score file to the scores folder. The score file name must end in `.py`.

A score is a Python script that tells the program what to play.

The simplest thing you can do is one _beat_, using the function `beat()` which is available in the `beats` package. So, the smallest possible score looks like this:

```Python
from beats import beat

beat()
```

Beats in the score play one after the other. So,

```python
beat()
beat()
```
plays two beats.

Normally, `beat()` will play a snare drum for a duration of one beat. To play a longer or shorter beat, add a decimal number in the brackets (a _"parameter"_ or _"argument"_). For example, try:

```python
beat(2)
beat(1)
beat(0.5)
beat()
```

You can also select a different drum from the drum kit. A list of all the drums can be found in the [kit](/kit) folder. To play a different drum, use the `play` function, which takes the drum name as a _string_ (in quotes, without the `.py`). So, here are some different drum beats:

```python
from beats import play

play('Kick-01')
play('Crash-03', 0.5)  # You can add a duration to play as well
play('Tom-01')
```

`rest` is like `beat` but plays nothing.

Finally, there are some functions you can import to make longer and more interesting compositions. To use these, you will have to define _your own_ functions to represent parts of your composition. Functions are just code blocks that give a small part of a program a name, so you can run them many times. They are created using the _keyword_ `def`, followed by the function name, a pair of brackets, a colon, and then your composition, indented. Let's create a bar of drum sounds:

```python
from beats import beat, repeat

def bar():  # The function name is "bar"
  beat(0.5)  # These lines are indented
  beat(1)
  beat(0.5)
  beat(1)
  beat(1)
```
`repeat` takes a function and repeats it a number of times. Let's add a line to repeat the bar four times:
```python
repeat(bar, 4)
```

`together` takes any number of functions and plays them all at the same time. Have a look at the [example score](/scores/example.py) to see this being used.
