# String Functions

<div style="font-size: 1rem; color: red">
Note: All string methods return a new string. They do not change the original string.
</div>
```Python
# Variable used
string = "ABCDEFabcdef"
```


## Functions
- ### len(string)
    *gives total number of characters in string*
    > ReturnType : **Integer**
    > ```python
    > len(string) 
    > # 12
    > ```

- ### in/not in
    *checks if string is present in another string*
    > ReturnType : **boolean**
    > ```python
    > print('cd' in string)
    > # True 

- ### Slicing
    *returns a specified set of characters from a string*
    > ReturnType : **string**
    > ```python
    > print(string[4:10])
    > # EFabcd
    >
    > print(string[:8]) # from the start
    > 
    > print(string[2:]) # to the end
    >
    > print(string[-4:-10]) 
    > # negative indices to start from end
    >```

---
## Built-in Methods 
---

- ### string.upper()/string.lower()
    *converts to uppercase*
    > ```python
    > print(string[5].upper())
    > # F
    >
    > print(string[5].lower())
    > # f

- ### string.strip()
    *remove whitespaces from around string*
    > ReturnType : **String**
    >```python
    > string.strip()
    > # ABCDEFabcdef

- ### string.split()
    *returns the list of string elements separated by the separator*
    > ReturnType : **list**
    >```python
    > print(string.split(''))
    > ```

- ### string Concatenation
    *returns a new concatenated string*
    > ReturnType : **String**
    > ```python
    > print('hello ' + 'world')
    > # hello world
    > ```

- ### string.capitalize()
    *capitalize the first letter*
    > ReturnType : **String**
    > ```python
    > print(string.capitalize())
    > # Abcdefabcdef
    > ```

- ### string.casefold()
    *converts the string to lowercase*
    > ReturnType : **string**
    > ```python
    > print(string.casefold())
    > # abcdefabcdef
    > ```

- ### string.center(length, character)
    *centers the specified string within specifid length surrounded by particular character*
    - @param *length* : [Required] length of returned string
    - @param *character* : [Optional] surrounding characters
    > ReturnType : **String**
    > ```python
    > print(string.center(20, '|'))
    > ```

- ### string.count(value, start, end)
    

