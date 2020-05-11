"""
Contains implementation of PsyAnalyser class.
It simplifies work with AgeGroup and StudentGroup objects.
"""
from agegroup import AgeGroup
from responselist import Response, ResponseList


class PsyAnalyser:
    """
    Representation of PsyAnalyser.
    """

    def __init__(self, year=None):
        """
        (Analyser) -> NoneType
        Create a new PsyAnalyser object.

        It contains dictionary of AgeGroups, where you can add group or
        person.
        """
        self.year = year
        self.__groups = dict()

    def add_group(self, group):
        """
        (Analyser, AgeGroup) -> NoneType
        Adds group to dictionary of groups, so that its structure is
        age: AgeGroup.
        If group of given age already exists, it changes it.

        :param group: age group to add to the dictionary.
        :return:
        """
        # if there're no group of such an age, create a new one
        if group.age not in self.groups:
            self.groups[group.age] = group
        # if there're a group of the same ahe, merge them
        else:
            self.groups[group.age].merge(group)

    def add_person(self, person):
        """
        (Analyser, Person) -> NoneType
        Adds person to dictionary by adding their parameters to the
        corresponding dictionary value.
        I such an AgeGroup doesn't exist, creates new AgeGroup based on
        the person.

        :param person: Person object to add.
        :return:
        """
        # if there're group of person's age, add person to the group
        if person.age in self.groups:
            self.groups[person.age].add_person(person)
        # if there're no such a group, create a new one
        else:
            # by default, we think that person answered
            # all the questionnaires.
            new_group = AgeGroup(age=person.age, suicide=person.suicide,
                                 suicide_resp=1,
                                 depression=person.depression,
                                 depression_resp=1, anxiety=person.anxiety,
                                 anxiety_resp=1)
            self.groups[person.age] = new_group

    def get_depression(self):
        """
        PsyAnalyser -> ResponseList
        Returns percents of people suffering from depressive d/o in each
        age group.
        """
        result = ResponseList()
        for group in self.groups:
            result += Response(x=group, y=self.groups[group].depression /
                                          self.groups[group].depression_resp)
        return result

    def get_anxiety(self):
        """
        PsyAnalyser -> ResponseList
        Returns percents of people suffering from anxiety d/o in each
        age group.
        """
        result = ResponseList()
        for group in self.groups:
            result += Response(x=group, y=self.groups[group].anxiety /
                                          self.groups[group].anxiety_resp)
        return result

    def get_suicide(self):
        """
        PsyAnalyser -> ResponseList
        Returns percents of people who had suicide attempts in each
        age group.
        """
        result = ResponseList()
        for group in self.groups:
            result += Response(x=group, y=self.groups[group].suicide /
                                          self.groups[group].suicide_resp)
        return result

    @property
    def groups(self):
        """
        (Analyser) -> dict
        Returns groups from the PsyAnalyser object

        :return: value of __groups parameter
        """
        return self.__groups
