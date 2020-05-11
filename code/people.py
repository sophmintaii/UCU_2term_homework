"""
Contains implementation of Person, Student and Student classes.
Student is inherited from Person,
"""


def test_input(value):
    """
    int -> int
    Returns value if it is correct and 0 otherwise.
    :param value: value to check.
    :param value:
    :return:
    """
    try:
        assert value in [0, 1]
        return value
    except (AssertionError, ValueError):
        return 1


class Person:
    """
    Representation of the Person.
    The class is needed to work with AgeGroup class.
    """
    def __init__(self, age, depression=0, suicide=0, anxiety=0, doctor=0):
        """
        (Person, int, int, int, int, int) -> NoneType
        Create a new Person object.
        Their age, whether person is/was suffering from depression or
        anxiety and whether they have suicide attempts, whether person
        has visited doctor can be specified.

        depression, suicide, anxiety and doctor parameters are 0 (False)
        or 1(True).
        """
        self.age = age
        self.depression = depression
        self.anxiety = anxiety
        self.suicide = suicide
        self.doctor = doctor

    @property
    def age(self):
        """
        (Person) -> int
        Returns age of the person.

        :return: __age parameter.
        """
        return self.__age

    @age.setter
    def age(self, age):
        """
        (Person, int) -> NoneType
        Setter for __age parameter.

        :param age: age of the person.
        :return:
        """
        try:
            assert age >= 0
            self.__age = age
        except (AssertionError, ValueError):
            self.__age = 0

    @property
    def suicide(self):
        """
        (Person) -> bool
        Returns 1 if person had suicide attempts and 0 otherwise.

        :return: __suicide parameter.
        """
        return self.__suicide

    @suicide.setter
    def suicide(self, suicide):
        """
        (Person, int) -> NoneType
        Setter for __suicide parameter of Person object.
        :param suicide: does person have suicide attempts.
        :return:
        """
        self.__suicide = test_input(suicide)

    @property
    def depression(self):
        """
        (AgeGroup) -> int
        Returns 1 id person have depressive disorders and 0 otherwise.
        :return: __depression parameter.
        """
        return self.__depression

    @depression.setter
    def depression(self, depression):
        """
        (Person, int) -> NoneType
        Setter for __depression parameter of Person object.
        :param depression: does person have depressive disorders.
        :return:
        """
        self.__depression = test_input(depression)

    @property
    def anxiety(self):
        """
        (Person) -> bool
        Returns 1 if person have anxiety disorders and 0 otherwise.
        :return: __anxiety parameter.
        """
        return self.__anxiety

    @anxiety.setter
    def anxiety(self, anxiety):
        """
        (Person, int) -> NoneType
        Setter for __anxiety parameter of Person object.
        :param anxiety: does person have anxiety disorder.
        :return:
        """
        self.__anxiety = test_input(anxiety)

    @property
    def doctor(self):
        """
        (Person) -> int
        Returns 1 if Person visited a doctor and 0 otherwise.

        :return: __doctor parameter.
        """
        return self.__doctor

    @doctor.setter
    def doctor(self, doctor):
        """
        (Person, int) -> NoneType
        Setter for __doctor parameter of Person object.
        :param doctor: have person visited a doctor.
        :return:
        """
        self.__doctor = test_input(doctor)


class Student(Person):
    """
    Representation of the Student, who is Person,
    but has additional parameters.
    """
    def __init__(self, age, depression=0, anxiety=0, suicide=0, doctor=0,
                 study=0, suicidal_thoughts=0, self_harm=0, dep_diagnosed=0,
                 behavior=0, anx_diagnosed=0, list_dep=[], list_anx=[]):
        """
        (Student, int) -> NoneType
        Create a new Student object.

        :param age: age of the student.
        :param depression: does student have depressive d/o.
        :param anxiety: does student have anxiety d/o.
        :param suicide: have student had suicide attempts.
        :param doctor: have student visited a therapist.
        :param study: does student think that study decreased level of
        their mental health.
        :param suicidal_thoughts: have student had suicidal thoughts.
        :param self_harm: have student practiced self-harm.
        :param dep_diagnosed: have student been diagnosed with
        depressive d/o.
        :param behavior: have student changed their plans and behavior
        because of anxiety.
        :param anx_diagnosed: have student been diagnosed with
        anxiety d/o.
        :param list_dep: list of depressive d/o's.
        :param list_anx: list of anxiety d/o's.
        """
        super().__init__(age=age, depression=depression,
                         suicide=suicide, anxiety=anxiety, doctor=doctor)
        self.study = study
        self.suicidal_thoughts = suicidal_thoughts
        self.self_harm = self_harm
        self.dep_diagnosed = dep_diagnosed
        self.behavior = behavior
        self.anx_diagnosed = anx_diagnosed
        self.list_dep = list_dep
        self.list_anx = list_anx

    @property
    def study(self):
        """
        (Student) -> int
        Returns True if student assume that study decreased level of
        their mental health and False otherwise.

        :return: __study parameter.
        """
        return self.__study

    @study.setter
    def study(self, study):
        """
        (Student, int) -> NoneType
        Setter for __study parameter.

        :param study: does student assume that study decrease level of
        their mental health.
        :return:
        """
        self.__study = test_input(study)

    @property
    def suicidal_thoughts(self):
        """
        (Student) -> int
        Returns 1 if student had suicidal thoughts and 0
        otherwise.

        :return: __suicidal_thoughts parameter.
        """
        return self.__suicidal_thoughts

    @suicidal_thoughts.setter
    def suicidal_thoughts(self, suicidal_thoughts):
        """
        (Student, int) -> NoneType
        Setter for __suicidal_thoughts parameter.

        :param suicidal_thoughts: have student had suicidal thoughts.
        :return:
        """
        self.__suicidal_thoughts = test_input(suicidal_thoughts)

    @property
    def self_harm(self):
        """
        (Student) -> int
        Returns True if student practiced self-harm and False otherwise.

        :return: __self_harm parameter.
        """
        return self.__self_harm

    @self_harm.setter
    def self_harm(self, self_harm):
        """
        (Student, int) -> NoneType
        Setter for __self_harm parameter.

        :param self_harm: have student practiced self-harm.
        :return:
        """
        self.__self_harm = test_input(self_harm)

    @property
    def suicide(self):
        """
        (Student) -> int
        Returns True if student had suicide attempts and False
        otherwise.

        :return: __suicide parameter.
        """
        return self.__suicide

    @suicide.setter
    def suicide(self, suicide):
        """
        (Student, int) -> NoneType
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
        Returns True if student have diagnosed depressive disorder and
        False otherwise.

        :return: __dep_diagnosed parameter.
        """
        return self.__dep_diagnosed

    @dep_diagnosed.setter
    def dep_diagnosed(self, dep_diagnosed):
        """
        (Student, int) -> NoneType
        Setter for __dep_diagnosed parameter.

        :param dep_diagnosed: Does student have diagnosed depressive
        disorder.
        :return:
        """
        self.__dep_diagnosed = test_input(dep_diagnosed)

    @property
    def behavior(self):
        """
        (Student) -> int
        Returns True if student have changed their plans or (and)
        behavior because of anxiety and False otherwise.

        :return: __behavior parameter.
        """
        return self.__behavior

    @behavior.setter
    def behavior(self, behavior):
        """
        (Student, int) -> NoneType
        Setter for __behavior parameter.

        :param behavior: have student changed their plans or (and)
        behavior because of anxiety.
        :return:
        """
        self.__behavior = test_input(behavior)

    @property
    def anx_diagnosed(self):
        """
        (Student) -> int
        Returns True if student have diagnosed anxiety disorder and
        False otherwise.

        :return: __anx_diagnosed parameter.
        """
        return self.__anx_diagnosed

    @anx_diagnosed.setter
    def anx_diagnosed(self, anx_diagnosed):
        """
        (Student, int) -> NoneType
        Setter for __anx_diagnosed parameter.

        :param anx_diagnosed: does student have diagnosed
        anxiety disorder.
        :return:
        """
        self.__anx_diagnosed = test_input(anx_diagnosed)
