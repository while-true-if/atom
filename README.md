# atom
[ [English](./README.md) | [日本語](./docs/README.ja.md) ]

These English text is translated by ChatGPT.  

## Usage  
* Please make sure to distinguish between uppercase and lowercase letters in the element symbols. Otherwise, it may result in an Input Error.
* Usually, the number of atoms is written as a subscript at the lower right, but here you can simply enter the numbers on the right side without using subscripts.  

## Poor example
```
h2
Fes
Tu
HE
```
## Good example
```
H2
FeS
Tl
He
```

## Algorithm
This program is designed to calculate the molecular weight from a given molecular formula. Specifically, when element symbols and their respective counts are provided, it retrieves the atomic weights of each element and multiplies them together to obtain the overall molecular weight.

Here's an overview of the program:

1. The atom list contains element symbols, while the amount list holds the corresponding atomic weights of the elements.
2. It prompts the user to input a molecular formula.
3. The input formula is parsed to extract pairs of element symbols and their counts.
4. For each pair, it searches for the corresponding element symbol and retrieves its atomic weight, which is then multiplied by the count and added to the list z.
5. The program calculates the sum of the values in the z list and displays the molecular weight.　　　　　　　　　　　　　　　　　　　　　　　　　　
* However, please note that this program lacks error handling, and in case of input errors, it only displays an error message without terminating execution. 

## Important points
* In this program, exact values cannot be obtained.
* In this program, if the element symbols are correct, no error message will be displayed. However, it does not guarantee the existence of the molecule.
* This program does not support examples like the following.
```
Ca(OH)2
```
* Therefore, please write it as follows.
```
CaO2H2
```
