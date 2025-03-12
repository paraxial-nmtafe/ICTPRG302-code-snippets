"""
    Implement "Green Glass Door" in Python.

    Rules:
    1. The player does not know "the rule"
    2. The player must name objects that they can take through the green glass door
        2a. These objects must not have a space in them. "Fish" is okay, "Tank of fish"
            is not.
    3. The game says whether or not this object is allowed
    4. The game continues until the player gives up by making a blank guess.
    
    For you, the implementer, "the rule" is that the player may take anything 
    through the green glass door so long as its name has a consecutive double 
    letter in it.

    Eg, A 'kettle' (2 Ts) may be taken, but a 'teapot' (also 2 Ts, but not next to each other) 
    may not be.

    Extension:
    Your very efficient friend wants to guess as fast as possible.  Read in the inputs from
    11_revision_inputs/taken_objects and output a file with the object name and "yes" or "no" 
    next to it.
    eg:
    book: yes
    paper: no
"""

