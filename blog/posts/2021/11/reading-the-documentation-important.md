---
title: Why is reading the documentation so important?
date: 2021-11-17T03:31:00.000Z
canonical_url: https://www.abhin.dev/blog/reading-the-documentation-important
description: This post explores why RTFM (Reading the F*cking Manual) might be the best advice you'll get as a developer.
reading_time: 4
slug: reading-the-documentation-important
published: True
tags:
  - Software Development
  - Product
medium: https://javascript.plainenglish.io/reading-the-documentation-important-5cf50bab0c9f
---

Quite often the process of writing code (especially while using a certain library) goes like this: _write code, encounter error, modify code, encounter error, go to StackOverflow, copy code, run code, repeat._

I recently came across the acronym **“RTFM”** which stands for ‘Reading the f\*cking Manual’. I realized as simple as the acronym is, it is equally very true, and a great piece of advice offered to me by a senior developer.

Reading the documentation has been the most missing step in every developer’s journey early on. No online course or module ever explicitly mentions that the course-takers should take time to read the documentation of the technology they are using.

Some often jump into projects without fully understanding how efficiently they can make use of the libraries, frameworks, or packages they’ll use.

While some think one introductory YouTube video will be sufficient to start working with a library. But what they’d experience was spending time debugging code, which may have been solved if only they’d read the documentation, or at least skimmed it.

While watching a YouTube video is not wrong, but perhaps the purpose can be. Not often you will find a YouTube tutorial that covers a library end to end, describing the use of all the functions and features inside it. It may become important at that point to at least visit the guides.

When you avoid reading the documentation, you’re missing out on understanding the deeper mechanical processes of your code, which may lead to you writing less efficient code. You’d end up spending precious hours on websites like StackOverflow or Github Wiki, trying to find why that line of code on line 7 doesn’t work, or suddenly why did the compiler throw an error, and you’ll find a response like this:

> The solution to this problem is making a certain declaration in options while initializing the library. It is given in the documentation under the “ABC” section.

You did find the solution. Unsurprisingly, the solution came from the documentation, but it was not your effort, and you got lucky that some random User3190 had read the documentation. You might encounter problems that others haven’t ever, and so they most likely don’t even exist as questions on Stack-overflow, and you’d spend hours trying to find an answer when you could have just read the documentation, and the solution was given on page 3.

Sometimes the package may have a function that you’re not aware of. To counter that you write another function to accomplish your task, sometimes making use of other functions within the package. Here’s one primitive example from the Python library Pandas:

Code if you didn’t take time to explore:

```python
import pandas as pd
data = pd.read_csv("./data.csv")# Code to remove certain rows
false_rows = [2, 3, 5]
data_new = data.drop(index = false_rows)
```

Code if you did take time to explore:

```python
import pandas as pd
data = pd.read_csv("./data.csv", skiprows = [2, 3, 5])
```

While it does sound like a Herculean task to read the documentation of all the packages or libraries you use regularly, you might attempt to do it in parts or be smart about it.

There’s an abstract concept in programming called the 80–20 rule (or the [Pareto Principle](https://en.wikipedia.org/wiki/Pareto_principle)). It says that for a particular library, framework, or package, you don’t need to learn all of the functions. You only need to learn 20% of the functions, because you’ll use them 80% of the time. You’ll use the rest 80% of the functions only 20% of the time.

Hence, it becomes important to be aware of the functions that you end up writing in almost every project. Something like the `read_csv` function above is one of the most commonly used functions in the Pandas package so it would make sense to know what kind of arguments you could use with that function going forward.

To save time, you should not read the guides for every new package, but maybe just the ones you use every day in your projects.

For example, as a React Developer, you can choose to invest time in reading the guides for React.js, but perhaps not as much time in reading the guides of libraries like Axios, or, helmet, whose function in your app is very limited and you may not be using every time in a project.

In conclusion, reading documentation is perhaps an investment you can make to become a better developer in the long run and know your tools better. So, just **RTFM**. :)
