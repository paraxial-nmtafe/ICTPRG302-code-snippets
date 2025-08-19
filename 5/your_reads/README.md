# "Your Reads"

This is a worked example that we'll do in class together 🙂

It might be a little complicated, but it puts everything we've learned over the last few weeks together, in a bigger piece of work.

> I'll share whatever code I write at the end of the demo, so try and focus on what I'm doing and why.

(If it looks suspiciously like a CLI clone of GoodReads: no it doesn't, do not ask me any more questions. /joke)

---

Here's the overview: 
You want to store information about books
- ones you've read
- ones you want to read
- ones you gave up on

> If you're not much of a reader, then you could imagine that this is about some other form of media that you consume.  Movies; TV Series; Podcasts...

You want to have the following information available about each book:
- title
- author
- genre
- your_rating
- year_of_publication
- status: (read, want_to_read, gave_up)
- length (pages)

---

1. Let's think of a data structure.  There's really only two acceptable options here. (Both involve dictionaries)
2. I like to start at the interface.  Let's write an input loop and a menu. 
3. Let them escape -- let's have a "quit" function.
4. Let's try "Show".  It's boring, but useful.
5. Now let's try "Add"
6. Subloops and validations...
7. How about "Search"?

(Are you working ahead? Don't get carried away with data entry, because we don't have a way to save data yet! Wait for week 6)