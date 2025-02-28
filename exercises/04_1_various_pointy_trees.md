# Loops exercise:

## 1 

Your goal in this file is to print out various pointy pine trees.

Your first ones will probably be a little slanted!

First, ask the user how tall they want their pine-tree to be:
```
How tall is your tree? 7
```

Use that to draw a slanted pine tree with the asterisk (*) character:
```
*
**
***
****
*****
******
*******
```

### Important Hint
Here's a hint: Python lets you "multiply" a string to make a longer version of that same string:
```python
a_string = "a"
print(a_string * 8)

> aaaaaaaa
```

Start with this:
```python
# Start here with your slanting tree:
tree_height = input("How tall is your tree? ")

print("Drawing a slanted tree:")
# Use what you've learned about loops to draw a tree:
```

## 2

All of our trees are slanted to the left!  This is really upsetting the vibe.
Let's slant some trees to the right, now:

For an input of 7, we expect an output of:
```
      *
     **
    ***
   ****
  *****
 ******
*******
```
### Important Hint
Hm, there needs to be some space between the top of the tree and the beginning of the line.
Try combining " " whitespace with your string "multiplication" trick from last time.
You can stick any number of strings together with `+`. 

## 3

But not every tree can be so slanted.  Maybe it's time to draw a symmetrical tree.

(If you're coming back from session 6, you can use string functions to make this easy.)

But if you're here in session 4, try to do a tiny bit of math and some string concatenation.

Here, from the same "tree_height" above, let's draw a symmetrical tree.

As before, with a height of 7, we draw:

```
      **      
     ****
    ******
   ********
  **********
 ************
**************
```
