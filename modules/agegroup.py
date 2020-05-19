"""
Contains implementation of AgeGroup class.
"""


def test_input(value):
    """
    int -> int
    Returns value if it is correct and 0 otherwise.
    :param value: value to check.
    """
    try:
        assert value > 0
        return value
    except (AssertionError, ValueError):
        return 0


class AgeGroup:
    """
    Represents age group.
    Every age group contains age (years) and counters for suicides,
    depression and anxiety disorders that people of this age have.
    For every of described parameter there are number of respondents
    that took part in questionnaire, if needed.
    """
    def __init__(self, age=0, suicide=0, suicide_resp=0, depression=0,
                 depression_resp=0, anxiety=0, anxiety_resp=0):
        """
        (AgeGroup, int) -> NoneType
        Create a new age group object.
        """
        self.age = age
        self.suicide = suicide
        self.suicide_resp = suicide_resp
        self.depression = depression
        self.depression_resp = depression_resp
        self.anxiety = anxiety
        self.anxiety_resp = anxiety_resp

    def merge(self, other):
        """
        (AgeGroup, AgeGroup) -> 0
        Merges two AgeGroup objects by summarizing parameters' values to
        self.
        :param other: AgeGroup to merge with.
        :return:
        """
        if self.age == other.age:
            self.suicide += other.suicide
            self.suicide_resp += other.suicide_resp
            self.depression += other.depression
            self.depression_resp += other.depression_resp
            self.anxiety += other.anxiety
            self.anxiety_resp += other.anxiety_resp

    def add_person(self, person):
        """
        (AgeGroup, Person) -> NoneType
        Adds person parameters to parameters of the group.

        :param person: person to add to group.
        :return:
        """
        if self.age == person.age:
            self.anxiety += person.anxiety
            self.depression += person.depression
            self.suicide += person.suicide
            self.anxiety_resp += 1
            self.depression_resp += 1
            self.suicide_resp += 1

    @property
    def age(self):
        """
        (AgeGroup) -> int
        Returns age parameter of the AgeGroup object.
        """
        return self.__age

    @age.setter
    def age(self, age):
        """
        (AgeGroup) -> NoneType
        Setter for __age parameter of AgeGroup object.
        :param age: age (number of years) to set.
        :return:
        """
        self.__age = test_input(age)

    @property
    def suicide(self):
        """
        (AgeGroup) -> int
        Returns number of suicides committed by AgeGroup.
        :return: __suicide parameter.
        """
        return self.__suicide

    @suicide.setter
    def suicide(self, suicide):
        """
        (AgeGroup, int) -> NoneType
        Setter for __suicide parameter of AgeGroup object.
        :param suicide: number of suicides committed by AgeGroup.
        :return:
        """
        self.__suicide = test_input(suicide)

    @property
    def suicide_resp(self):
        """
        (AgeGroup) -> int
        Returns number of total number of respondents to suicide
        questionnaire in AgeGroup.
        :return: __suicide_resp parameter.
        """
        return self.__suicide_resp

    @suicide_resp.setter
    def suicide_resp(self, suicide_resp):
        """
        (AgeGroup, int) -> NoneType
        Setter for __suicide_resp parameter of AgeGroup object.
        :param suicide_resp: total number of respondents to suicide
        questionnaire
        :return:
        """
        self.__suicide_resp = test_input(suicide_resp)

    @property
    def depression(self):
        """
        (AgeGroup) -> int
        Returns number of people in AgeGroup suffering from depression.
        :return: __depression parameter.
        """
        return self.__depression

    @depression.setter
    def depression(self, depression):
        """
        (AgeGroup, int) -> NoneType
        Setter for __depression parameter of AgeGroup object.
        :param depression: number of people in AgeGroup suffering from
        depression.
        :return:
        """
        self.__depression = test_input(depression)

    @property
    def depression_resp(self):
        """
        (AgeGroup) -> int
        Returns number of total number of respondents to depression
        questionnaire in AgeGroup.
        :return: __depression_resp parameter.
        """
        return self.__depression_resp

    @depression_resp.setter
    def depression_resp(self, depression_resp):
        """
        (AgeGroup, int) -> NoneType
        Setter for __depression_resp parameter of AgeGroup object.
        :param depression_resp: total number of respondents to
        depression questionnaire
        :return:
        """
        self.__depression_resp = test_input(depression_resp)

    @property
    def anxiety(self):
        """
        (AgeGroup) -> int
        Returns number of people in AgeGroup suffering from anxiety
        disorders.
        :return: __anxiety parameter.
        """
        return self.__anxiety

    @anxiety.setter
    def anxiety(self, anxiety):
        """
        (AgeGroup, int) -> NoneType
        Setter for __anxiety parameter of AgeGroup object.
        :param anxiety: number of people in AgeGroup suffering from
        anxiety disorders.
        :return:
        """
        self.__anxiety = test_input(anxiety)

    @property
    def anxiety_resp(self):
        """
        (AgeGroup) -> int
        Returns number of total number of respondents to anxiety
        questionnaire in AgeGroup.
        :return: __anxiety_resp parameter.
        """
        return self.__anxiety_resp

    @anxiety_resp.setter
    def anxiety_resp(self, anxiety_resp):
        """
        (AgeGroup, int) -> NoneType
        Setter for __anxiety_resp parameter of AgeGroup object.
        :param anxiety_resp: total number of respondents to anxiety
        questionnaire
        :return:
        """
        self.__anxiety_resp = test_input(anxiety_resp)
