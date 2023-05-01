import os
import re

def getDate(filename):
    date_regex = r'\d{2}_\d{2}_\d{2}'

    date_match = re.search(date_regex, filename)

    if date_match:
        date = date_match.group()
        print(date)


def sizeOfFile(filename):
    if os.path.isfile(filename):
        size_bytes = os.path.getsize(filename)
        size_kilobytes = size_bytes / 1024  
        size_megabytes = size_kilobytes / 1024  

        print(f"The size of '{filename}' is {size_bytes} bytes ({size_kilobytes:.2f} KB or {size_megabytes:.2f} MB).")
    else:
        print(f"'{filename}' is not a valid file.")


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(50))
