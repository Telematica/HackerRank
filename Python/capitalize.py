''' 2019-09-05 12:13:00 '''
''' https://www.hackerrank.com/challenges/capitalize/problem '''
import re

def upper_repl(match):
    return match.group(1).upper()
     
def solve(s):
    val = str(s)
    if val.isdigit() or not (0 < len(val) < 1000):
        return False

    return (re.sub(r'(\b\w)', upper_repl, val))

print(
    solve('2sssasasa dsds ')
)