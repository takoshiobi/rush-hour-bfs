[![Maintainability](https://api.codeclimate.com/v1/badges/faa6e65de2852bf0e795/maintainability)](https://codeclimate.com/github/akinariobi/rush-hour-bfs/maintainability)
[![Python](https://img.shields.io/badge/python-3.5-blue.svg)](https://www.python.org/downloads/release/python-350/)

### A program for solving the Rush Hour game using BFS

#### Run Code 

**Terminal**

```
$ python3 src/Main.py boards/beginner1.txt
```
*Output*
```
['G', 'G', ' ', ' ', ' ', 'Y']
['V', ' ', ' ', 'B', ' ', 'Y']
['V', 'r', 'r', 'B', ' ', 'Y', '>']
['V', ' ', ' ', 'B', ' ', ' ']
['O', ' ', ' ', ' ', 'H', 'H']
['O', ' ', 'L', 'L', 'L', ' ']
G +1
H -3
Y +3
V -1
O -1
L -2
B +2
r +4
['V', 'G', 'G', ' ', ' ', ' ']
['V', ' ', ' ', ' ', ' ', ' ']
['V', ' ', ' ', ' ', 'r', 'r']
['O', ' ', ' ', 'B', ' ', 'Y']
['O', 'H', 'H', 'B', ' ', 'Y']
['L', 'L', 'L', 'B', ' ', 'Y']
```
**Tkinter**

```
$ python3 src/MainGUI.py boards/beginner1.txt
```
![GUI](https://pp.userapi.com/c841325/v841325491/5bb18/pHbRsFIB9Uc.jpg)
![GUI](https://pp.userapi.com/c841325/v841325491/5bb20/EbJxGP95rVw.jpg)

#### Execution time

*Main.py*
---------
**Level : Beginner**
```
$ python3 -m cProfile src/Main.py boards/beginner1.txt
...
17201733 function calls (14624957 primitive calls) in 7.746 seconds
```
**Level : Expert**
```
$ python3 -m cProfile src/Main.py boards/expert1.txt
...
115822933 function calls (98233315 primitive calls) in 61.892 seconds
```
*MainGUI.py*
------------
**Level : Beginner**
```
$ python3 -m cProfile src/MainGUI.py boards/beginner1.txt
...
17284114 function calls (14695410 primitive calls) in 10.006 seconds
```
**Level : Expert**
```
$ python3 -m cProfile src/MainGUI.py boards/expert1.txt
...
115923180 function calls (98309066 primitive calls) in 68.061 seconds
```

*Maintainability : Codeclimate*
![CODECLIMATE](https://pp.userapi.com/c841325/v841325491/5bb29/V0gcyED745g.jpg)



