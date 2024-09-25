Independently made in a day for fun

You input a max/min count (how many times it can count, referred to as tries, before the attempt is a fail)
- eg, min count 5 means if it took 3 counts to get the number, it is a fail
- max count 5 means if it takes 6+ counts to get the number, it is a fail

with this, it will continue trying again and again until it gets the number within the count boundary
then it calculates the chance of getting the value within that count, out of the upper bound and the amount of lines it took to do it
it then puts this in results.txt (can be viewed in the code and as a file itself)
