# Cookie Jar walkthrough #

Implement a cookie jar in which to store cookies using a class with the following methods:

__init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar. If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
__str__ should return a str with
🍪, where is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.
withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
capacity should return the cookie jar’s capacity.
size should return the number of cookies actually in the cookie jar, initially 0.

## Test ##

### Scenarios ###

1. Deposit n cookies in a full jar.

2. Deposit jar with n cookies where n + size > capacity.

3. Print jar with n cookies.

4. Withdraw more cookies than there are in the jar.

5. Withdraw n cookies where n < size . Size been number of cookies already in jar.

6. Deposit  n cookies and get the size i.e initial size + n.

7. Withdraw and get size i.e initial size - n.
