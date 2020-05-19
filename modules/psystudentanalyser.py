"""
Contains implementation of Analyser class,
which is inherited from PsyAnalyser class.
It simplifies work with StudentGroup objects.
"""
from studentgroup import StudentGroup
from psyanalyser import PsyAnalyser
from responselist import Response, ResponseList


class PsyStudentAnalyser(PsyAnalyser):
    """
    Student Analyser representation.
    Is Analyser, but with wider options.
    """

    def __init__(self):
        """
        PsyStudentAnalyser -> NoneType
        Create a new PsyStudentAnalyser object.
        """
        super().__init__()

    def add_person(self, person):
        """
        (Analyser, Person) -> NoneType
        Adds person to dictionary by adding their parameters to the
        corresponding dictionary value.
        I such an StudentGroup doesn't exist, creates a new one
        based on the person.

        :param person: Person object to add.
        :return:
        """
        if person.age in self.groups:
            self.groups[person.age].add_person(person)
        else:
            new_group = StudentGroup(age=person.age,
                                     depression=person.depression,
                                     anxiety=person.anxiety,
                                     suicide=person.suicide,
                                     suicidal_thoughts= \
                                         person.suicidal_thoughts,
                                     self_harm=person.self_harm,
                                     dep_diagnosed=person.dep_diagnosed,
                                     behavior=person.behavior,
                                     anx_diagnosed=person.anx_diagnosed,
                                     doctor=person.doctor,
                                     total=1,
                                     list_dep=person.list_dep,
                                     list_anx=person.list_anx)
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
                               self.groups[group].total)
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
                               self.groups[group].total)
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
                               self.groups[group].total)
        return result

    def get_doctor(self):
        """
        PsyAnalyser, bool -> ResponseList
        Returns percents of people who had visited a therapist in each
        age group.
        """
        result = ResponseList()
        for group in self.groups:
            result += Response(x=group, y=self.groups[group].doctor /
                               self.groups[group].total)
        return result

    def get_list_anx(self):
        """
        PsyAnalyser -> ResponseList
        Returns prevalence of each anxiety d/o.
        """
        disorders = dict()
        for group in self.groups:
            for disorder in self.groups[group].list_anx:
                if disorder in disorders:
                    disorders[disorder] += 1
                else:
                    disorders[disorder] = 1
        result = ResponseList()
        disorders.pop("", None)
        all_disorders = sum(disorders.values())
        for disorder in disorders:
            result += Response(x=disorder, y=disorders[disorder]/all_disorders)
        return result

    def get_list_dep(self):
        """
        PsyAnalyser -> ResponseList
        Returns prevalence of each depressive d/o.
        """
        disorders = dict()
        for group in self.groups:
            for disorder in self.groups[group].list_dep:
                if disorder in disorders:
                    disorders[disorder] += 1
                else:
                    disorders[disorder] = 1
        result = ResponseList()
        disorders.pop("", None)
        all_disorders = sum(disorders.values())
        for disorder in disorders:
            result += Response(x=disorder, y=disorders[disorder]/all_disorders)
        return result

    def get_study(self):
        """
        PsyAnalyser, bool -> ResponseList
        Returns percent of people who think studying negatively
        affected their mental health.
        """
        result = Response()
        for group in self.groups:
            result.value_x += self.groups[group].study
            result.value_y += self.groups[group].total
        return result

    def get_suicidal_thoughts(self):
        """
        PsyAnalyser, bool -> ResponseList
        Returns percent of people who had/have suicidal thoughts.
        """
        result = Response()
        for group in self.groups:
            result.value_x += self.groups[group].suicidal_thoughts
            result.value_y += self.groups[group].total
        return result

    def get_self_harm(self):
        """
        PsyAnalyser, bool -> ResponseList
        Returns percent of people who practice(d) self-harm.
        """
        result = Response()
        for group in self.groups:
            result.value_x += self.groups[group].self_harm
            result.value_y += self.groups[group].total
        return result

    def get_dep_diagnosed(self):
        """
        PsyAnalyser, bool -> ResponseList
        Returns percent of people who have been diagnosed with
        depressive d/o.
        """
        result = Response()
        for group in self.groups:
            result.value_x += self.groups[group].dep_diagnosed if \
                              self.groups[group].depression else 0
            result.value_y += self.groups[group].total
        return result

    def get_anx_diagnosed(self):
        """
        PsyAnalyser, bool -> ResponseList
        Returns percent of people who have been diagnosed with
        anxiety d/o.
        """
        result = Response()
        for group in self.groups:
            result.value_x += self.groups[group].anx_diagnosed if \
                              self.groups[group].anxiety else 0
            result.value_y += self.groups[group].total
        return result

    def get_behavior(self):
        """
        PsyAnalyser, bool -> ResponseList
        Returns percent of people who have changed their behavior and/or
        plans because of anxiety.
        """
        result = Response()
        for group in self.groups:
            result.value_x += self.groups[group].behavior
            result.value_y += self.groups[group].total
        return result
