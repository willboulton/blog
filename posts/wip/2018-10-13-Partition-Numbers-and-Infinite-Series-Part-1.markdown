---
layout: post
title:  "Partition Numbers and Infinite Series - Part 1"
date:   2018-10-13 00:16:07 +0100
categories: jekyll update
---
Mathematicians are often stereotyped as people who like to count things; normally this judgement is made by people who are "scared of maths" and gave up as soon as letters started to appear in their equations. Obviously, if you're on this blog, you'll know that mathematics is about quite a lot more than just finding different ways to count various useless things - a pretty tedious task that I would class under accountancy, not mathematics. However, this is just the first post in a series that go slightly beyond A level, so I'm going to stick to the basics and start off with a problem on different ways to count up various patterns. 

#### Ways of counting stuff

> > "I can add up all the change in your purse really really fast" - Kanye West

Here's a pretty dumb question; if I've got 5 identical beads, how many ways can I split them up into different piles? Well, here are some different combinations:

- 5
- 1 + 1 + 1 + 1 + 1
- 2 + 3
- 4 + 1
- some other ways?

After listing a few, we should probably try to approach this problem at least a little bit methodically, so I'm going to start with 1 pile (5) and work my way up to 5 piles (1+1+1+1+1):

- 5
- 4 + 1
- 3 + 2
- 3 + 1 + 1
- 2 + 2 + 1
- 2 + 1 + 1 + 1
- 1 + 1 + 1 + 1 + 1

We've done this systematically, counting down from the largest number, and always using the largest values where possible, so we've definitely not left any possibilities out. So that's the answer; there are 7 ways to split 5 beads into various piles. If you wanted to be fancy and write this using maths and functions, you could summarise this by writing that p(5) = 7, where we are defining p as a function which takes a natural number n as input and returns the number of ways of writing n.

You might reasonably ask "What was the point in working out that?". That's a completely fair question. In maths, it's pretty common to start off with some stupid question, and generalise it, or ask some follow up question, until things become more and more difficult and eventually no-one knows the answer. In this case, there are about a zillion different follow-up questions:

1. This counting process worked for 5, but what about 10, or 200, or a million? Is there a general pattern / a formula? If you graph these, what's the general shape of the graph?
2. Is there a way of speeding up this counting process? Or say someone wants to know the same problem but with 6 instead of 5, do I have to do all of the work again, or does knowing the answer with 5 help?
3. What if the order doesn't matter? So that you're allowed 4 + 1 and 1 + 4 as being different and 2 + 2 + 1 is different to 2 + 1 + 2 which is different to 1 + 2 + 2. Is there a formula then?
4. What if you're only allowed to use different numbers (no repeats)? What if you're only allowed to use odd numbers? Or only allowed to use even numbers? Or square numbers? Or some other restriction?

To use more technical terminology, we want to generalise this question in different ways: using any number (call it n) instead of 5 (Q1), having more (or less) restrictive rules on how to divide up n (Q3 and Q4), and asking for a closed formula (Q1), asymptotic equation (Q1), and an efficient algorithm to compute these numbers, or a recursive algorithm; we'd also like to know the runtime of the algorithm (Q2). (Don't worry if you don't understand every single word here - the point is just that from our initial easy question we've almost immediately produced a barrage of questions, some of which are either active research topics or require a phd in maths to answer fully.) 

Before reading on, you should try to investigate some of these questions for yourself. You could try computing some of these numbers by hand and drawing out a table, or writing a computer program to do it for you, and graphing the results. In particular, you could try Q3, and draw out a table for Q4 using either only even numbers, only odd numbers, or only distinct numbers. 


#### Partitions
Did you try working out any of these questions for yourself? I bet you didn't. Try Q3. I put it in because it's really easy.







Ok, if you're still reading this I'm assuming you either got bored of trying the question yourself, or you did it. Either way, here's how I approached this problem. 
To get started, just work out the first few possibilities. I'll write n for the number we're testing, and r(n) for the number of ways of making n when you're allowed repeats:
---------------------------------------------------------
|  n  | r(n) | Options
---------------------------------------------------------
|  1  |   1  | 1
|  2  |   2  | 2, 1 + 1
|  3  |   4  | 3, 2 + 1, 1 + 2, 1 + 1 + 1
|  4  |   8  | 4, 3 + 1, 2 + 2, 2 + 1 + 1, 1 + 3 ...etc.
---------------------------------------------------------

It looks like the pattern here is powers of two - R(n) = 2 ** (n-1). Great! Are we finished? Unfortunately, no. In maths, just working out the first 4 terms in a sequence, spotting a pattern, and then saying "look I've worked it out, aren't I smart" doesn't really cut it. That kind of logic might get you into an engineering or physics degree, but for a mathematician, there's still plenty of work left to do. If someone woke me up in the middle of the night, and gun to my head asked, "do you know for certain what the value of r(101) is?", I'd probably tell them to get out of my house, but also, I'd have to say that no I don't really know for sure, I think it's probably 2 ** 100, but it'd take way too long for me to calculate that by hand (2 ** 100 is about 30 digits long so there's no way I can list that many possibilities). So to be sure, we need to come up with a foolproof argument for why our guess for this formula of R(n) is right. 

#### An aside - Proof
How are we meant to prove something to be true? What is a proof? How can we ever truly know what is true and what is false?

I'm not the Dalia Lama so I can't answer any deep questions about the true nature of truth. But I can tell you what a mathematical proof is. A proof is a list of mathematical statements, starting from an obvious set of premises, where each statement follows logically from the previous one, until you reach a conclusion. I could write a whole separate post on various different kinds of proof, and why they're important, but for now let's just go with this definition and prove what we reckon is probably true; that R(n) = 2 ** (n-1). 

Premise #1:
    R(1) = 1
    There is only 1 way to write 1 as a sum of positive integers, and that's like this: 1. (Ok, it's not much of a sum, it doesn't have a + sign, but it still counts.) There aren't any other ways. If you think there might be, it's good that you're thinking very rigorously and sceptically about the problem, but on the other hand you probably need psychiatric help because there just aren't any other ways to do it.

Premise #2:
    If you can calculate R(n), then you can calculate R(n+1) = 2 * R(n). I.e., to calculate the next term in the sequence, just take the previous term and double it. 
    This isn't totally obvious, so I'll try to convince you, through ~~song~~ a sub-proof. Say we calculate R(n), listing all 

#### Back to Partitions
Let's define a set of functions:
    Given an input n (the symbol means "is an element of" and the N is the set of natural numbers, so 1, 2, 3, 4, ...etc.) let's define-
    
    - p(n) is the number of partitions of n
    - r(n) is the number of partitions of n where re-orderings are allowed
    - e(n) is the number of partitions of n using only even numbers
    - o(n) is the number of partitions of n using only odd numbers
    - d(n) is the number of partitions of n using only distinct numbers (no repeats allowed)

We've already worked out an exact formula for r(n) - it's 2 ** (n-1). So that's an open and shut case. Are there any other easy things we can think of? Well, e(n) is pretty obviously going to be 0 whenever n is odd (you can't make an odd number by adding together a bunch of even numbers), and when n is even, e(n) is just the same thing as p(n/2) (divide all your piles in half). So we have a complete formula for e(n) too: 

e(n) = { 0 if n is odd; p(n/2) if n is even;

This is another general mathematical principle - reducing one problem to another. I don't have a formula for e(n) but I do know that it's almost the same as p(n/2); so actually the e(n) problem is no harder or easier than working things out for p(n). 

What about these other ones though? I've drawn out a table below. 

How weird. It looks like there are just as many ways of splitting a number up into odd parts as there are for splitting it up into distinct (ie. different) parts. That's pretty crazy. In fact it's so crazy that it's probably worth investigating a bit more. I've written a computer program which does this, and prints the results. The code is in the appendix, but the results are given here below. If you're keen, and know some coding, I'd suggest you write your own code to check this too. 

#### Summary

#### Appendix - Some coding
Being able to code is a pretty useful skill for almost every technical or scientific field. If you know a little bit of coding, I would strongly encourage you to try to write programs that can calculate partition numbers. I've put some code in a github repository which you are free to mess with as much as you like. However, if you don't know any coding, you can still get started a bit. Just make sure you do the following steps:

1. Open a new tab in your browser.
2. Go on the three dots next to the url bar, click it and look for "Developer Tools". In Chrome, it's under "More Tools" > "Developer Tools" and the shortcut is Control + Shift + I. 
3. Click the Console tab. This opens an interactive console where you can type in any valid javascript code and the console will evaluate it for you. 
4. Try typing in some maths operations like 2 + 2, or 6 ** 3 (to run that line of code you need to hit enter). 
5. Type in the command: 

{% highlight javascript %}
fetch().then(response => response.text).then()
{% endhighlight %}

This copies the code from http://sekjsjf directly into the console. You can now use that code even if you don't understand exactly what it does! (This is 99% of programming.)
6. Still in the console, type in Partitions.partition(5) and hit enter. The console should return 7 as the answer. But there are a whole load of other functions that you can try using. There's a handy autocomplete function, and a drop down, showing you a range of available options. Try typing in Partitions.partition.text(), Partitions.odd.text(), Partitions.distinct.text() to get a short description of what each function does. 
7. Try using some other commands. Writing Partitions.odd(5, list=True) will return [1,2,3,4,5]; i.e. rather than just calculating the answer for 5 it will run through all the numbers up to 5 and return the answers for each in an array. 
8. What about if we want to check that d(n) = o(n) for every single number up to 100? We could try writing some code like this:

{% highlight javascript %}
for (let i = 1; i < 100; i = i + 1) {
    if (Partitions.odd(i) === Partitions.distinct(i)) {
        console.log("Same")
    }
    else {
        console.log("These two are different!")
    }
}
{% endhighlight %}

There are loads of good javascript tutorials (here's just one) but as a super crash course:

- A single equals sign assigns a variable a value. i = 1 assigns the variable i a value of 1. 
- triple equals checks for equality. So something like (2 + 2 === 4) evaluates as true. 
- for (let i = 1; i < 100; i++) {do some stuff} looks more intimidating, but it's still pretty simple. We start by creating a new variable called i and giving it the value 1 (let i = 1;). Next we do whatever is in the curly brackets. Once that's done, we add 1 to the value of i (that's the  i = i + 1, which looks weird, but remember that a single equals sign in javascript is an assignment, so really this is saying "I want you to assign the variable i a new value, by taking its current value and adding 1 to it"). Then we evaluate what's in the curly brackets, using the updated value for i. We keep doing this until i reaches 100 ( i < 100;), when we can stop. 
- if (something) {do this} else {do that} is pretty self explanatory. If the condition inside the if (something) is evaluated as true, we do what's inside the first set of brackets. Otherwise, we do whatever the else part says. 
- console.log("whatever") just tells the console to print out that line. 

So in the code here, we assign a new variable called i the value 1. Then we check if Partitions.odd(i) and Partitions.distinct(i) are equal, and if they are we print "Same", otherwise we print "These two are different!". Then we add 1 to the value of i (that's the i = i + 1 part) and do it again. We keep on doing this until i hits 100, when we can stop. One thing to note is that in javascript (and in programming in general) adding 1 to a variable is so common that it has a shorthand - rather than writing i = i + 1, you can write i++, which is more compact but means the same thing. 