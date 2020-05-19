"""
Contains implementation of ResponseList ADT and Response class.
"""
import copy


class ResponseList:
    """
    ResponseList ADT implementation based on linked list.
    """
    def __init__(self):
        """
        ResponseList -> NoneType
        Create a new ResponseList.
        """
        self._head = None

    def get_df_for_line(self, year=None):
        """
        ResponseList -> list
        Returns data from ResponseList so that it can easily be turned
        into a pandas data frame to plot line graph.
        """
        age = self.head
        result = []
        while age is not None:
            if year is None:
                result.append((age.value_x, age.value_y * 100))
            else:
                result.append((year, age.value_x, age.value_y * 100))
            age = age.next
        return result

    def __len__(self):
        """
        ResponseList -> int
        Returns number of responses in the ResponseList.
        :return: length of the self.
        """
        node = self._head
        length = 0
        while node is not None:
            length += 1
            node = node.next
        return length

    def __contains__(self, value):
        """
        ResponseList, value -> bool
        Determines if an item is contained in the ResponseList.

        :param value: item to look for.
        :return: True if item is in the list, False otherwise.
        """
        node = self._head
        while node is not None and node.value_x != value:
            node = node.next
        return node is not None

    def __add__(self, new_node):
        """
        ResponseList, Response -> NoneType
        Adds a new item to the list and pastes it so that responses are
        sorted by OX value.

        :param new_node: response to add.
        :return:
        """
        if self._head is None:
            self._head = new_node
        elif len(self) == 1:
            if self._head.value_x < new_node.value_x:
                self._head.next = new_node
            else:
                old = copy.deepcopy(self._head)
                self._head = new_node
                self._head.next = old
        else:
            node = self._head
            while (node.next is not None) and (node.next.value_x < new_node.value_x):
                node = node.next
            new_node.next, node.next = node.next, new_node
        return self

    def __remove__(self, item):
        """
        ResponseList, Response -> NoneType
        Removes an instance of the item from the bag.

        :param item: item to remove.
        :return:
        """
        prev_node = None
        cur_node = self._head
        while cur_node is not None and cur_node.value_x != item.value_x:
            prev_node = cur_node
        cur_node = cur_node.next
        assert cur_node is not None, "The item must be in the response list."
        if cur_node is self._head:
            self._head = cur_node.next
        else:
            prev_node.next = cur_node.next
        return cur_node.item

    def __iter__(self):
        """
        ResponseList -> Iterator
        Returns an iterator for traversing the list of items.
        :return:
        """
        return _ResponseListIterator(self._head)

    @property
    def head(self):
        """
        ResponseList -> Response
        :return: _head value.
        """
        return self._head


class _ResponseListIterator:
    """
    Defines a linked list iterator for the Bag ADT.
    """
    def __init__(self, list_head):
        self._cur_node = list_head

    def __iter__(self):
        return self

    def next(self):
        """
        helper method for Iterator
        :return: next item for iterator of raises Exception
        """
        if self._cur_node is None:
            raise StopIteration
        item = self._cur_node.item
        self._cur_node = self._cur_node.next
        return item


class Response:
    """
    Representation of the Response, which is a pair of numbers.
    The first number is value of x and the second one is value of y,
    so that data is ready to be plotted.
    """
    def __init__(self, x=0, y=0):
        """
        Response, int/str, int/float -> NoneType
        Create a new Response object.

        :param x: value on the OX axis.
        :param y: value on the OY axis.
        """
        self.value_x = x
        self.value_y = y
        self.item = (self.value_x, self.value_y)
        self.next = None

    def get_df_for_pie(self):
        """
        Response -> list
        Returns data from Response so that it can easily be turned
        into a pandas data frame to plot pie diagram.
        """
        return [self.value_y - self.value_x, self.value_y]

    @property
    def value_x(self):
        """
        Response -> int/str
        Returns value of value_x parameter.
        """
        return self.__value_x

    @value_x.setter
    def value_x(self, val_x):
        """
        Setter for __value_x parameter of Response object.
        :param val_x: value to set.
        :return:
        """
        try:
            assert isinstance(val_x, (str, int))
            self.__value_x = val_x
        except AssertionError:
            self.value_x = 0

    @property
    def value_y(self):
        """
        Response -> int/float
        Returns value of value_y parameter.
        """
        return self.__value_y

    @value_y.setter
    def value_y(self, val_y):
        """
        Setter for __value_y parameter of Response object.
        :param val_y: value to set.
        :return:
        """
        try:
            assert isinstance(val_y, (float, int))
            self.__value_y = val_y
        except AssertionError:
            self.value_y = 0
