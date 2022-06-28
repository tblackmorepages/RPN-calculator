# Reverse Polish Notation Calculator

![python3.7+](https://img.shields.io/badge/Python-3.7+-green.svg)

A command line program that accepts an RPN expression as input and evaluates it.

## Installation

First download requirements.txt and install in terminal using:

```bash
pip install -r requirements.txt
```

Next download the `rpn.py` file. The calculator can then be run in the terminal using:
```bash
python3 rpn.py
```

## Usage

Input expressions should follow the Reverse Polish Notation syntax. Each number or operator should be separated from its neighbors by a single space **unless** it is a number in text format which should be separated by a double space. For example the following expressions are equivalent:

```python
> 523 74 +
> five hundred twenty three  seventy four  +
```

The calculator supports the following operations:
* Addition (`+`)
* Subtraction (`-`) 
* Multiplication (`*`) 
* Integer division (`/`)
* Modulo (`%`)

For help whilst using the calculator enter `help` or `?`. 

To exit the calculator use any of the following: `exit`, `quit`, `close`.

## Example

```python
$ python3 rpn.py
Launching RPN calculator...
> 5 2 /
2
> three  seven  *
21
> two  3 * 11  fourteen  * +
160
```


## Unit Testing

Unit tests can be run by downloading the `tests` folder and using the following command in the terminal:
```bash
python3 -m pytest tests
```