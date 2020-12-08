# recursion-in-python
As a newbie in programming, I recently found that's quite hard to solve a task using recursion algorithm. Especially if you feel like you already master the `if... else...` and `for` loop iteration, you started to feel you can solve anything, until the interviewer ask you to do something using recursive algorithm. This kind of situation happened to me a few days ago (I made this repo on `8-Dec-2020`). It took several minutes for me to figured out how the recursive algorithms work, becaouse my mentor told that recursive algorithms are not recommended when we want to process large ammount of data and that makes me rarely use recursion in my programming exercises.

## Recursive Algorithm Simplified
After that day, I decided to dive deeper on the recursive algorithm then found it's actually quite... strange. Yeah at least for me who do not come from computing background. After several hours of learning, reading, and contemplating, I found there are three main steps that everyone should go through to make a solid recursive algorithm:
  1. Identify the recursive case
  2. Identify the stopping criterion
  3. Identify the unintentional case
  
 ### Case Study: Factorial
Factorial is one of the common mathematical operation that symbolized with exclamation mark (`!`), that calculates the product of all positive integer less than or equal to `n`. So, `n! = n x (n-1) x (n-2) x (n-3) ... x 1`. Start from this point, you might seen the pattern of this operation so we can start to construct the code using the **recursive case**:
 ```
 def factorial(n):
  return n * factorial(n-1) # recursive case (1)
 ```
 If you run that code, you would find that the function run repeatedly until your system run out of memory. This happens because you have not identify the **stopping criterion**. In the factorial case, we want the recursion stop when `n == 1`, and for `n == 0` the mathematicians agreed that `0! = 1`. Indeed that's quite strange, but we don't try to be smart. Let's just do what they said :)
 ```
 def factorial(n):
  if n in [0,1]: # stopping criterion (2)
    return 1 
  else:
    return n * factorial(n-1) # recursive case (1)
 ```
That code should perfectly work! But what if the input is negative or float? That's when we need to add a bit of finishing touch to our code. If we insert the negative or float value, the system would return an error notification `The number must be positive or integer only!`,
```
 def factorial(n):
  assert n >= 0 and int(n) == n, 'The number must be positive or integer only!' # unintentional case (3)
  if n in [0,1]: # stopping criterion (2)
    return 1 
  else:
    return n * factorial(n-1) # recursive case (1)
```
For more detailed explanation and other examples, please open `recursive.py` file on this repo.

Cheers!
