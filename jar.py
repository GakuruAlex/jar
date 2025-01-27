class Jar:
    def __init__(self, capacity = 12):
        self._size = 0
        if capacity > 0:
            self._capacity=capacity
        else:
            raise ValueError
    def __str__(self):
        """_str representation of Jar_

        Returns:
            _(str)_: _🍪 * number of cookies in jar_
        """
        return '🍪' * self._size

    def deposit(self, n):
        """_Add a cookie to the cookie jar_

        Args:
            n (_type_): _Number of cookies to add_

        Raises:
            ValueError: _Raise value error if number of cookies in jar after after adding n cookies exceeds jar capacity_
        """
        if self.size + n <= self._capacity:
            self._size = n
        else:
            raise ValueError
    def withdraw(self, n):
        """_Eat a cookie from the cookie jar_

        Args:
            n (_int_): _Number of cookies to eat_

        Raises:
            ValueError: _Raise ValueError if number of cookies to eat are more the number in the jar_
        """
        if self.size - n >= 0:
            self.size = -n
        else:
            raise ValueError
    @property
    def capacity(self):
        """_Get the capacity of the cookie jar_

        Returns:
            (_int_): _Number of cookies jar holds_
        """
        return self._capacity
    @capacity.setter
    def capacity(self, amount: int):
        """_Set capacity of jar_

        Args:
            amount (int): _Number of cookies jar holds_
        """
        self._capacity = amount

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, n: int):
        self._size += n


def main():
    jar = Jar()
    jar.deposit(4)
    print(jar._size)
    print(jar)

if __name__ =="__main__":
    main()