"""
Contains implementation of StudentGroup class.
StudentGroup class is inherited from AgeGroup.
"""
from agegroup import AgeGroup, test_input


class StudentGroup(AgeGroup):
    """
    Representation of StudentGroup, which is AgeGroup,
    but has additional parameters.
    """

    def __init__(self, age, depression=0, anxiety=0, suicide=0, study=0,
                 suicidal_thoughts=0, self_harm=0, dep_diagnosed=0,
                 behavior=0, anx_diagnosed=0, doctor=0, total=0, list_dep=[],
                 list_anx=[]):
        """
        (StudentGroup, int) -> NoneType
        Create a new StudentGroup object.

        :param age: age of StudentGroup.
        """
        super().__init__(age=age, depression_resp=total,
                         anxiety_resp=total,
                         suicide_resp=total, depression=depression,
                         anxiety=anxiety, suicide=suicide)
        self.doctor = doctor
        self.study = study
        self.suicidal_thoughts = suicidal_thoughts
        self.self_harm = self_harm
        self.dep_diagnosed = dep_diagnosed
        self.behavior = behavior
        self.anx_diagnosed = anx_diagnosed
        self.list_dep = list_dep
        self.list_anx = list_anx
        self.total = total

    def merge(self, other):
        """
        StudentGroup, StudentGroup -> NoneType
        Merges two AgeGroup objects by summarizing parameters' values to
        self.
        :param other: AgeGroup to merge with.
        :return:
        """
        super().merge(other)
        if self.age == other.age:
            self.doctor += other.doctor
            self.study += other.study
            self.suicidal_thoughts += other.suicidal_thoughts
            self.self_harm += other.self_harm
            self.dep_diagnosed += other.dep_diagnosed
            self.behavior += other.behavior
            self.anx_diagnosed += other.anx_diagnosed
            self.list_dep.extend(other.list_dep)
            self.list_anx.extend(other.list_anx)
            self.total += other.total

    def add_person(self, person):
        """
        (StudentGroup, Person) -> NoneType
        :return:
        """
        if self.age == person.age:
            self.anxiety += person.anxiety
            self.anxiety_resp += 1
            self.depression += person.depression
            self.depression_resp += 1
            self.suicide += person.suicide
            self.suicide_resp += 1
            self.total += 1
            self.doctor += person.doctor
            self.study += person.study
            self.suicidal_thoughts += person.suicidal_thoughts
            self.self_harm += person.self_harm
            self.dep_diagnosed += person.dep_diagnosed
            self.behavior += person.behavior
            self.anx_diagnosed += person.anx_diagnosed
            self.list_dep.extend(person.list_dep)
            self.list_anx.extend(person.list_anx)

    @property
    def doctor(self):
        """
        (StudentGroup) -> int
        Returns number of students who have visited a doctor.

        :return: __doctor parameter.
        """
        return self.__doctor

    @doctor.setter
    def doctor(self, doctor):
        """
        (StudentGroup, int) -> NoneType
        Setter for __doctor parameter

        :param doctor:
        :return:
        """
        self.__doctor = test_input(doctor)

    @property
    def study(self):
        """
        (StudentGroup) -> int
        Returns number of students who assume that study decreased level
        of their mental health.

        :return: __study parameter.
        """
        return self.__study

    @study.setter
    def study(self, study):
        """
        (StudentGroup, int) -> NoneType
        Setter for __study parameter.

        :param study: number of students who assume that study decrease
        level of their mental health.
        :return:
        """
        self.__study = test_input(study)

    @property
    def suicidal_thoughts(self):
        """
        (StudentGroup) -> int
        Returns number of students who had suicidal_thoughts.

        :return: __suicidal_thoughts parameter.
        """
        return self.__suicidal_thoughts

    @suicidal_thoughts.setter
    def suicidal_thoughts(self, suicidal_thoughts):
        """
        (StudentGroup, int) -> NoneType
        Setter for __suicidal_thoughts parameter.

        :param suicidal_thoughts: number of students who had
        suicidal_thoughts.
        :return:
        """
        self.__suicidal_thoughts = test_input(suicidal_thoughts)

    @property
    def self_harm(self):
        """
        (StudentGroup) -> int
        Returns number of students who practiced self-harm.

        :return: __self_harm parameter.
        """
        return self.__self_harm

    @self_harm.setter
    def self_harm(self, self_harm):
        """
        (StudentGroup, int) -> NoneType
        Setter for __self_harm parameter.

        :param self_harm: number of students who practiced self-harm.
        :return:
        """
        self.__self_harm = test_input(self_harm)

    @property
    def suicide(self):
        """
        (StudentGroup) -> int
        Returns number of students who had suicide attempts.

        :return: __suicide parameter.
        """
        return self.__suicide

    @suicide.setter
    def suicide(self, suicide):
        """
        (StudentGroup, int) -> NoneType
        Setter for __suicide parameter.

        :param suicide: number of students who had suicide
        attempts.
        :return:
        """
        self.__suicide = test_input(suicide)

    @property
    def dep_diagnosed(self):
        """
        (StudentGroup) -> int
        Returns number of students who have diagnosed depressive
        disorder.

        :return: __dep_diagnosed parameter.
        """
        return self.__dep_diagnosed

    @dep_diagnosed.setter
    def dep_diagnosed(self, dep_diagnosed):
        """
        (StudentGroup, int) -> NoneType
        Setter for __dep_diagnosed parameter.

        :param dep_diagnosed: number of students who have diagnosed
        depressive disorder.
        :return:
        """
        self.__dep_diagnosed = test_input(dep_diagnosed)

    @property
    def behavior(self):
        """
        (StudentGroup) -> int
        Returns number of students who have changed their plans or (and)
        behavior because of anxiety.

        :return: __behavior parameter.
        """
        return self.__behavior

    @behavior.setter
    def behavior(self, behavior):
        """
        (StudentGroup, int) -> NoneType
        Setter for __behavior parameter.

        :param behavior: number of students who have changed their plans
        or (and) behavior because of anxiety.
        :return:
        """
        self.__behavior = test_input(behavior)

    @property
    def anx_diagnosed(self):
        """
        (StudentGroup) -> int
        Returns number of students who have diagnosed anxiety disorder.

        :return: __anx_diagnosed parameter.
        """
        return self.__anx_diagnosed

    @anx_diagnosed.setter
    def anx_diagnosed(self, anx_diagnosed):
        """
        (StudentGroup, int) -> NoneType
        Setter for __anx_diagnosed parameter.

        :param anx_diagnosed: number of students who have diagnosed
        anxiety disorder.
        :return:
        """
        self.__anx_diagnosed = test_input(anx_diagnosed)

    @property
    def total(self):
        """
        (StudentGroup) -> int
        Returns total number of students.

        :return: __total parameter.
        """
        return self.__total

    @total.setter
    def total(self, total):
        """
        (StudentGroup, int) -> NoneType
        Setter for __total parameter.

        :param total: total number of students.
        :return:
        """
        self.__total = test_input(total)
