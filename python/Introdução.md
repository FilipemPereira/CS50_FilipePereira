# Introduction to programming with Python
## CS50

Index

1. Variables and Function
1. Conditionals
1. Loops
1. Exceptions (catch and handle)
1. Libraries
1. Unit Tests 
1. File I/O
1. Regular Expressions
1. Object-Oriented Programming


Variables and Function
---

hello.py

-> side effects <-

Bugs:   eg, syntax error

return values

= : assignment signal

1. str : data type String 

.strip() -> Remove the whitespace from str

.capitalize() -> Capitalize str

.title() -> Capitalize str

.split(" ) -> split str

.len() -> return the length of a string or a data structure

Arithmetic Operators
--
1.  \+
2.  \-
3.  \/
4.  %
5.  \*
6.  ** -> power of

2. int : data type integer

int(x) -> convert a string in a equivalent integer number

3. float : real number data type

float(x) -> convert a string in a equivalent real number
.round(number \[,ndigits\]) -> round to the next integer number; round to nDigits digits (parameter nDigits is optional)

4. bool : boolean data type

- True
- False

5. list : list data type

list[-1] <- indices negativos iteram a lista do último para o primeiro elemento

To index: L[i]

6. dict : dictionary data type (ky-value pair)

nota: podemos combinar funções .strip().title()

7. Tuple : non-mutable list

k, v = function()

8. Set



To index: t[i]

Conditionals 
---

Logic Operators

1. \>
2. <
3. <=
4. \>=
5. ==
6. !=

Boolean expressions

match (switch em linguagens derivadas de C)

Loops
---

Exceptions
---
try:


except <>:


else:

pass

Libraries
---
modules

import 

from
1. random

.choice(seq)

.randint(a, b)

.shuffle(x) <- x is a list
1. statistics

.mean

1. sys
.argv() <- vetor de argumentos

´´´
python name.py "Filipe Pereira"

´´´
nota: na lista existem dois elementos

.exit()

Packages
---- 

Third party libraries

PyPi

API's

pip - package manager

1. cowsay
2. requests

Unit Tests
---

assert

pytest

File IO
---

.open()
with open() as file

Module csv
.reader()
.write()
.DictWrite()

Regular Expressions
---

- .  - any character except a newline
- \* - 0 or more repetitions
- \+ - 1 or more repetitions
- ? - 0 or 1 repetition
- {m} - m repetitions
- {m, n} - m-n repetitions
- ^ - start of a string
- $ - ends of a string
- [] - set of characters
- [^..] - complementing the set (everything except ..)
- \d - decimal digit
- \D - not a decimal digit
- \s - whitespace characters
- \S - not a whitespace
- \w - word character -- a well as numbers and the underscore
- \W - not a word character
- (.. | __) - pipe
- (...) - group
- (?:...) - non-capturing version
  
Flags:
- re.IGNORECASE
- re.MULTILINE
- re.DOTALL

.sub()
.search()
.findall()
.split()

OOP
---

Operator Overloading

Et Cetera
---

mypy : type hint

Definir tipo de retorno de uma função

~~~
python name.py --help
~~~

Unpacking

List comprehension

Dictionary comprehension


[Python's documentation](https://docs.python.org)
[Python's libraries](https://docs.python.org/3/libraries)
