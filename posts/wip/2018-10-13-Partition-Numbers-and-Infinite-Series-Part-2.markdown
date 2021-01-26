---
layout: post
title:  "Partition Numbers and Infinite Series - Part 2"
date:   2018-10-10 00:16:07 +0100
categories: jekyll update
---

<p>
In the last post, we looked at partition numbers, and found a load of interesting patterns, some of which we could check up to about 100. But we never managed to prove that any of these patterns always worked - and without doing that, our results aren't anything more substantial than just a few interesting observations and guesses. In this post, we'll look at a very powerful method which can actually prove (sort of) one of the interesting things we discovered from last time; that \(d(n)\) (the number of distinct ways of partitioning n) was always equal to \(o(n)\), the number of ways of partitioning n with only odd numbers. 
</p>
#### Sequences and Series
You probably remember what sequences are from GCSE; they're lists of numbers that go on forever. Here are a few examples:

<ul>
  <li> \(1, 2, 3, 4, 5, 6, 7, ...\) The natural numbers </li>
  <li> \(1, 3, 5, 7, 9, 11, 13, ...\) The odd numbers   </li>
  <li> \(1, 4, 9, 16, 25, 36, ...\)    The square numbers </li>
  <li> \(2, 3, 5, 7, 11, 13, ...\)       The prime numbers </li>
  <li> \(5, 1, 5, 2, 5, 6, 7, ...\)      Just a random sequence I've come up with that doesn't have a logical pattern </li>
</ul>
<p>
In GCSE, you sometimes had to come up with a formula for the nth term of a sequence, for example for the odd numbers, the nth term is given by  \(a_n = 2n - 1\), and for the square numbers  \(a_n = n^2\). Right now, we're interested in various kinds of partition numbers, which means we should probably care about their sequences:
</p>

<ul>
  <li>\(\) Normal partition numbers</li>
  <li>\(\) Odd partitions</li>
  <li>\(\)Distinct partitions</li>
  <li>\(\)Sums of 2 squares</li>
  <li>\(\)Sums of 3 triangle numbers</li>
</ul>

You probably also know a little bit about summation series, but if not then here's a reminder.

#### Sigma Notation
<p> The symbol \( \Sigma \) (capital sigma) is a Greek letter, which in maths is used to represent a sum. Rather than writing \(1 + 2 + 3 + 4 + 5 + 6\), we'd write this: </p>

$$ \sum_{i = 1}^6 {i} $$

<p>
Each part of this means something. The Greek capital sigma means we are adding the terms together. The letter i is what's called a dummy variable or dummy index. It's a variable because it changes. It's a dummy variable because it's not really important what letter we used, we could have called it j or k or x or this emoji 🐱, and it wouldn't have made any difference. The lower 1 means that i starts at 1, and goes all the way up until 6 (since that's the number at the top) and all of those are added together. 
</p>
Here's another one:

$$ 25 + 16 + 9 + 4 + 1 + 0 + 1 + 4 + 9 + 16 + 25 = \sum_{x =-5}^5 {x^2} $$

<p>
If you can understand this one then you've basically clocked onto sigma notation. The \(x\) is a dummy index, which starts at -5, goes up to 5, and the \(x^2\) tells us that we add the squares of \(x\) together. 
</p>

As a quick exercise, how would you write these three sums in Sigma notation?

<ol>
  <li> \(1 - 1 + 1 - 1 + 1 - 1 + 1\) </li>
  <li> \(1 - 2 + 3 - 4 + 5 - 6 + 7 - 8 + 9 - 10\) </li>
  <li> \(1 + (1/2) + (1/4) + (1/8) + (1/16) + (1/32) + (1/64) + (1/128) + ... \) forever </li>
  <li> \(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 \) </li>
</ol>


First you need to find a formula for the general term of the sequence of summands (a summand is just a thing you're adding up). Then it's just a case of getting the notation correct. The answers are below. 

<button onClick="doSomething(content1, 'showHide1')"> SHOW </button>


<p id="showHide1">
<ol>
  <li> \(\sum_{n = 1}^7 {(-1)^{n - 1}}\)</li>
  <li> \(\sum_{n = 1}^{10} {n \times (-1)^{n - 1}}\)</li>
  <li> \(\sum_{n = 1}^\infty {(1/2)^{n-1}}\)</li>
  <li> \(\sum_{n = 1}^8 {n}\)</li>
</ol>
</p>


The third one is a bit more difficult. The infinity means that you keep adding terms forever and never stop. Surely this can never produce an answer?! Actually, these infinite sums can make sense and are extremely useful, though they are a bit tricky. Mathematicians spent a decent amount of time between the 16th and 18th centuary worrying about how to make sense of these infinite sums, and even today there are plenty of problems that are not totally understood, to do with infinite sums similar to these ones. 
There are basically two ways to deal with an infinite sum like this. The first is to worry really hard about it, spend a lot of time reading some extremely difficult textbooks, and rigorously prove that dealing with infinity isn't really so bad in 99% of cases, and is a complete nightmare the other 1% of the time. The second way is to assume that infinite sums always produce an answer, figure out what that answer is, and worry about the consequences afterwards. Let's go with the second way; BUT keep of track of what assumptions we're making.  Then, if we run into some sort of crazyness, like finding out that 0 = 1 or something, we can look at our assumptions and decide where it probably went wrong. 

#### Dealing with Infinity
Let's start off with a bunch of case studies in infinity:

1. 

$$ \sum_{p = 1} ^\infty 1 $$


First, expand out the sigma notation to see what it's really saying...
start with a dummy index of p at 1, and add 1, then change p to 2, but still add 1, then change p to 3, and add 1 again... so it's just this:

$$1 + 1 + 1 + 1 + 1 + ...$$

You can probably guess right now that something is going to go wrong, because for sure this sum shouldn't produce a finite answer. But let's try anyway. ASSUME that the sum above comes to a finite answer. We can then give that answer a name - call it S. So:

$$ S = \sum_{i=1}^\infty {1} = 1 + 1 + 1 + 1 + 1 + ...$$

Adding 1 to both sides:

$$ S + 1 = 1 + \sum_{i=1}^\infty {1} = 1 + (1 + 1 + 1 + 1 + ...)

= 1 + 1 + 1 + 1 + ... = S$$

<p>Now subtract S from both sides and we get that \(0 = 1\). This is obviously wrong, and so somewhere we've made an incorrect assumption. Where did we assume anything? There were two places - firstly we assumed that the sum S existed, and came to a finite answer. The second assumption, which is more subtle, was when we added 1 to both sides of the equation, and then removed the brackets. Removing the brackets is something you can always do normally (for example, \(1 + (4 + 5) = (1 + 4) + 5 = 1 + 4 + 5\)); but it might not be ok for infinite sums. However, you'll just have to trust me that given an infinite sum, rearranging and ignoring the brackets (a property called <em>associativity</em>) is fine - the error was assuming that the sum existed in the first place. You can kind of tell that anyway - obviously \(1 + 1 + 1 + 1 + ...\) just does not exist. 
</p>

2. For any fixed value of x, consider:

$$ \sum_{p = 1} ^\infty x^p $$

<h4> An aside - people also care about multiplication </h4>

<button onClick="doSomething(content2, 'showHide2')"> SHOW </button>

<p>
Now that you know how to add together infinitely many numbers, using a compact notation, let's have a quick look at how to multiply together infinitely many numbers. Just as Greek capital sigma is a sum, Greek capital pi is a product (multiplication), and it looks like this: \( \Pi \). (Pi has nothing to do with the number 3.141592... in this case.) So \((1/1) \times (1/3) \times (1/5) \times (1/7)\) is \(\prod_{q = 1}^4 (\frac{1}{2q - 1}) = 1/105\). I'm pretty sure you get it already but here are a bunch of exercises just to check you understand what's going on:
</p>



<p id="showHide2">
  When \(a \ne 0\), there are two solutions to \(ax^2 + bx + c = 0\) and they are
  $$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$
</p>


#### Back to Partition Numbers
All this stuff with infinite series might be slightly interesting, but it doesn't really seem to have much to do with partition numbers, which was the original point. However, here's a neat trick which links the two things together really nicely. Given a sequence, we can turn it into an infinite sum:

$$ A(z) = \sum_{n=1}^\infty a_nz^n = a_1 + a_1z + a_2z^2 + a_3z^3 + ...$$

(This is called the generating function, or z-transform, of the sequence - and it's used a lot, including in the real world! The z-tranform is used in my job to relate discrete digital signals to continuous idealisations, where it's possible to do useful maths like calculus to come up with differential equations.)

The next thing to do is absolutely bat shit crazy and there's no way anyone other than a genuis would have come up with this idea - 

$$ D(x) =  \prod_{n=1}^\infty (1 + x^n) = (1 + x)(1 + x^2)(1 + x^3)(1 + x^4)... = 1 + d_1x^1 + d_2x^2 + d_3x^3 + ...$$

$$ O(x) =  \prod_{n=1}^\infty (\frac{1}{1 - x^{2n-1}}) = (\frac{1}{1 - x})(\frac{1}{1 - x^{3}})(\frac{1}{1 - x^{5}})(\frac{1}{1 - x^{7}})... = 1 + do_1x^1 + o_2x^2 + o_3x^3 + ...$$

Why are these things true? For the first one - you have to imagine multiplying out the terms - the coefficient of x^n will come to exactly the number of ways there are of making n from distinct numbers. Here's a little demonstration just for the coefficient of x^5; but hopefully the general idea is clear. 
For the second one - we need to use all the other stuff we learnt so far. 


All this has been interesting - but now this is the super smart bit. get rid of x, x2, x4, x8 leaving 1/(1-x); then get rid of 2^no to leave 1/(1-x^o). 

#### Summary
Well done if you made it this far! Even if you didn't understand everything. Here are the key points again:

- partition numbers are 


#### Appendix
All good questions in maths lead to more follow on questions. We have briefly investigated the generating functions for two of the partition sequences. It makes sense to ask questions about the others. 

$$P(z) = \prod_{n=1}^\infty (\frac{1}{1 - x^n})$$

<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>

<script>
  let content1 = document.getElementById("showHide1").innerHTML;
  console.log(content1);
  let content2 = document.getElementById("showHide2").innerHTML;
  console.log(content2);

  function doSomething(data, id) {
    console.log("started f");
    console.log(id);
    if (document.getElementById(id).innerHTML) {
        document.getElementById(id).innerHTML = "";
        console.log("emptying the thing");
    }
    else {
        document.getElementById(id).innerHTML = data;
        console.log(data);
        MathJax.Hub.Typeset();
    }
  }
</script>