# UNE COSC110 Programming Task 1

Voting in Codetown - programming task 1 for the COSC110 unit in UNE

## Installation

Download the tar gzipped file, and extract it via:

```bash
foo@bar:~$ tar zxvf cosc110-prog-task-1.tgz
```

## Usage

```bash
foo@bar:~$ ./vote.py
```

To test the program, run:

```bash
foo@bar:~$ ./test.sh
```

Use the --unittest parameter to run the unit tests, and --interactiontest
to run the interaction tests.

## Problem statement

It's election year in Codetown, and for the first time ever, the local
council is trialling an electronic voting system.

The current mayor, Oliver Seton, has asked you to develop a program to
collect and count votes from citizens using this new system.

The voting process is as follows:

1. Voter ID Entry
    
    Each voter has been assigned a unique voter ID, which is a seven-digit
    integer between 1000000 and 9999999 (inclusive).

    Your program should first ask the user to enter their voter ID.

    If the voter ID has already voted in the election, an error message
    should be displayed and a new voter ID should be requested.

    If the voter ID is left blank (i.e., the user presses Enter without
    typing anything), the program should end, and the election results
    should be displayed.
    
2.  Ranking the Candidates
    
    After entering a valid voter ID, the user must score each of the
    three candidates. The candidates are listed in the following order
    (which was randomly selected):

    1. William Gorithm
    2. Meg A. Byte
    3. Oliver Seton

Each candidate must be assigned a score (an integer number between 0 and
9), where 9 indicates the most preferred candidate and 0 indicates the
least preferred candidate.

After submitting their scores, the program should return to ask for the
next voter’s ID. Ideally, the screen should be cleared between voters,
but this is not required for this assessment.

Once voting ends (when a blank voter ID is entered), the program should
determine the winner using the [Score Voting Method](https://en.wikipedia.org/wiki/Score_voting):

> Each candidate earns an integer score between 0 and 9 in each ballot,
> where a more preferred candidate gets a higher score. The candidate
> with the highest average score wins the election.

If there is a tie, the candidate listed first in the above order wins:

* William Gorithm wins whenever no candidate has a higher score than him
  (i.e., even if others have the same score).
* If William Gorithm has a lower score than any other candidate, and the
  other candidates are tied, then Meg A. Byte wins.
* Oliver Seton only wins if he has a higher score than the other candidates.

## Approach to coding

I am a fan of functional programming, which has informed how I write this
Python code. 

My approach to coding is to divide up the program into "pure" functions as
much as possible (i.e. no side effects and it returns a value). As this
program is not overly complex, I have not felt the need to divide up the
main program into further functions, so I have just commented the main
parts of the code. 

One technique that I am a fan of is to define preconditions via assert
statements at the start of functions to ensure any callers pass in the
correct values and if they don't then it gets discovered at runtime.

By keeping the functions pure, this makes it easy for me to write unit tests
to ensure they work correctly. I have used Python's builtin unittest module
for the unit tests.

Whilst figuring out how to code in Python (I'm a relative newbie) I
discovered the joy of generator expressions and list comprehensions. I
have only used a generator expression, as whilst I initially used a
list comprehension as a filter in the function that determines the
winner, I realised that I was overcomplication things so, sadly, I
couldn't show off this feature.
 
## License

[MIT](https://choosealicense.com/licenses/mit/)

