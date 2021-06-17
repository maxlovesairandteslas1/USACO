"""
Python
The most intuitive way to do input/output is using the built in input() and print() methods.
The input() method will return the next line, and can be processed using different python methods.
The print() method takes in a string and an optional string end (defaults to '\n'). 
Copied from USACO guide website"""
# read in a string
myStr = input()
# prints the string on its own line
print(myStr)

# take in an integer n on a single line
n = int(input())
# prints integer n with " test" after it
print(n, end=" test")


"""

In older USACO problems, the input and output file names are given and follow the convention problemname.in. After the program is run, output must be printed to a file called problemname.out.

Fence Painting
Bronze - Very Easy
Focus Problem – read through this problem before continuing!

You must rename the .in and .out files depending on the problem. For example, in the above problem you would use paint.in and paint.out.

Python
See here for documentation about file I/O.

The most intuitive way to do file I/O in Python is by redirecting the system input and output to files. After doing this, you can then use the above input() and print() methods as usual.

"""

# When doing past problems, use this.
import sys
# input for older versions
sys.stdin = open("problemname.in", "r")
# output for older versions
sys.stdout = open("problemname.out", "w")


"""
USACO Note - Extra Whitespace
Importantly, USACO will automatically add a newline to the end of your file if it does not end with one.

Warning!    
Occasionally, there is a period of time near the beginning of the contest window where the model outputs do not end in newlines. This renders the problem unsolvable ...

Make sure not to output trailing spaces, or you will get an error such as the following:

bad

Here are some examples of what is allowed and what isn't when the intended output consists of a single integer ans:
"""
ans = "hoi im am max"
print(ans) # OK, newline
print(ans,end='') # OK, no newline
print(str(ans)+'\n') # NOT OK, extra newline



