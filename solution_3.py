class Date:
    
    def __init__(self, date):
        
        if self.is_date(date):
            self.__date = date
        else:
            print('ошибка')
            self.__date = None
    
    def leap_year(year):
            if year % 4 != 0:
                return False

            if year % 100 == 0 and year % 400 != 0:
                return False

            return True

    def is_date(self, date):

        d = date.split('.')

        if len(d[0]) != 2 or len(d[1]) != 2:
            return False
        
        day_31 = [1, 3, 5, 7, 8, 10, 12]
        day_30 = [4, 6, 9, 11]

        if int(d[2]) < 1:
            return False
        
        if int(d[1]) == 2:

            if Date.leap_year(int(d[2])):
                if 0 < int(d[0]) < 30:
                    return True
                return False
                
            else:
                if 0 < int(d[0]) < 29:
                    return True
                return False
        
        if int(d[1]) in day_31:

            if 0 < int(d[0]) < 32:
                return True
            return False
        
        if int(d[1]) in day_30:

            if 0 < int(d[0]) < 31:
                return True
            return False

    date = property()

    @date.setter
    def date(self, value):

        if self.is_date(value):
            self.__date = value
        else:
            print('ошибка')
            self.__date = None

    @date.getter
    def date(self):

        if self.__date is not None:
            d = self.__date.split('.')

            mnth = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 
                    'июл', 'авг','сен', 'окт', 'ноя', 'дек']
            
            return f'{int(d[0])} {mnth[int(d[1]) - 1]} {int(d[2])} г.'
        return str(self.__date)
                
    def __str__(self):

        if self.__date is not None:
            d = self.__date.split('.')

            mnth = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 
                    'июл', 'авг','сен', 'окт', 'ноя', 'дек']
            
            return f'{int(d[0])} {mnth[int(d[1]) - 1]} {int(d[2])} г.'
        return str(self.__date)


class Meeting:

    lst_meeting = []

    def __init__(self, id, date, title):

        self.id = id
        self.date = Date(date)
        self.title = title
        self.employees = []

    def add_person(self, person):
        self.employees.append(person)

    def count(self):
        return len(self.employees)
    
    @staticmethod
    def count_meeting(date):

        count = 0
        for meet in Meeting.lst_meeting:
            
            if meet.date.__str__() == date.__str__():
                count += 1
        
        return count
    
    @staticmethod
    def total():

        count = 0
        for meet in Meeting.lst_meeting:
            count += meet.count()

        return count
    
    def __str__(self):

        strng = f'Рабочая встреча {self.id}\n{self.date} {self.title}\n'

        for pers in self.employees:
            strng += f'{pers}\n'
        
        return strng


    
class User:

    lst_person = []

    def __init__(self, id, nick_name, first_name, \
                 last_name, middle_name, gender):
        
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def __str__(self):

        strng = ''

        if self.id != '':
            strng += f'ID: {self.id} '

        if self.nick_name != '':
            strng += f'LOGIN: {self.nick_name} '

        if self.first_name != '' and self.last_name != ''\
            and self.middle_name != '':

            strng += f'NAME: {self.last_name} {self.first_name} {self.middle_name} '

        elif self.first_name != '' and self.last_name == ''\
            and self.middle_name != '':

            strng += f'NAME: {self.first_name} {self.middle_name} '
        
        elif self.first_name != '' and self.last_name != ''\
            and self.middle_name == '':

            strng += f'NAME: {self.last_name} {self.first_name} '
        
        elif self.first_name == '' and self.last_name != ''\
            and self.middle_name != '':

            strng += f'NAME: {self.last_name} {self.middle_name} '
        
        elif self.first_name != '' and self.last_name == ''\
            and self.middle_name == '':

            strng += f'NAME: {self.first_name} '
        
        elif self.first_name == '' and self.last_name != ''\
            and self.middle_name == '':

            strng += f'NAME: {self.last_name} '
        
        elif self.first_name == '' and self.last_name == ''\
            and self.middle_name != '':

            strng += f'NAME: {self.middle_name} '
        
        if self.gender != '':
            strng += f'GENDER: {self.gender} '
        
        return strng
    
    def __repr__(self):
        return f'{self.id}'
        
class Load:

    @staticmethod
    def write(meet_text, pers_text, pers_meet_text):

        with open(pers_text, 'r', encoding="utf8") as f:
            attr = f.readline().split(';')[:-1]

            for line in f:
                values = line.split(';')[:-1]
                if len(values) == 5:
                    values.append('')

                pers = {}
                for i in range(len(attr)):
                    pers[attr[i]] = values[i]

                User.lst_person.append(User(pers['id'], pers['nick_name'],\
                                            pers['first_name'], pers['last_name'],\
                                            pers['middle_name'], pers['gender']))
        
        with open(meet_text, 'r', encoding="utf8") as f:
            attr = f.readline().split(';')[:-1]

            for line in f:
                values = line.split(';')[:-1]
                if len(values) == 2:
                    values.append('')

                meet = {}
                for i in range(len(attr)):
                    meet[attr[i]] = values[i]

                Meeting.lst_meeting.append(Meeting(meet['id'], meet['date'], meet['title']))
        
        with open(pers_meet_text, 'r', encoding="utf8") as f:

            attr = f.readline().split(';')[:-1]
            values = []

            for line in f:
                values.append(line.split(';')[:-1])

            for meet in Meeting.lst_meeting:
                for vl in values:  
                    for pers in User.lst_person:
                            
                            if meet.id == vl[0] and pers.id == vl[1]:
                                meet.add_person(pers)
