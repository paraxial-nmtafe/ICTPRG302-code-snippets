# Collections

This isn't a Python file, it's just a series of questions to ask yourself about collections:

1. What do you expect the value of "alphabet_dictionary" to be if you executed the following:
`alphabet_dictionary = { 'a': 1, 'a':2, 'a':5 }`

2. If you did `max({ 'a':1, 'b': -1 })`, what would you expect?

3. What about `max({ 'a':1, 'b': -1 }.values())`?

4. What about `len({ 'a':1, 'b': -1 })`?

5. Have a think about how, given the list `[1,2,3,4,5]`, you might generate the list `[1,3,5]`

6. Suppose you have the following dictionary:

```python
nested_object = {
    "key": {
        "greeting": "hello"
    }
}
```

How would you get python to return the "hello" value from it?