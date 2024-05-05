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
    
    def to_timestamp(self):
        
        count = 0
        start_year = 1970
        start_mnth = 1
        start_day = 1
        day_31 = [1, 3, 5, 7, 8, 10, 12]
        day_30 = [4, 6, 9, 11]

        d = self.__date.split('.')

        while start_year != int(d[2]):
            if Date.leap_year(start_year):
                count += 366 * 24 * 60 * 60
            else:
                count += 365 * 24 * 60 * 60
            
            start_year += 1

        while start_mnth != int(d[1]):
            
            if start_mnth == 2:
                if Date.leap_year(start_year):
                    count += 29 * 24 * 60 * 60
                else:
                    count += 28 * 24 * 60 * 60
                    
            elif start_mnth in day_31:
                count += 31 * 24 * 60 * 60

            elif start_mnth in day_30:
                count += 30 * 24 * 60 * 60

            start_mnth += 1
        
        while start_day != int(d[0]):
            count += 24 * 60 * 60
            start_day += 1

        return count

    def __eq__(self, other):

        if self.__date == other.__date:
            return True
        return False
    
    def __ne__(self, other):

        if self.__date != other.__date:
            return True
        return False
    
    def __lt__(self, other):
        d_1 = self.__date.split('.')
        d_2 = other.__date.split('.')

        if int(d_1[2]) > int(d_2[2]):
            return False
        elif int(d_1[2]) < int(d_2[2]):
            return True
        else:
            if int(d_1[1]) > int(d_2[1]):
                return False
            elif int(d_1[1]) < int(d_2[1]):
                return True
            else:
                if int(d_1[0]) > int(d_2[0]):
                    return False
                elif int(d_1[0]) < int(d_2[0]):
                    return True
                else:
                    return False
                
    def __le__(self, other):
        d_1 = self.__date.split('.')
        d_2 = other.__date.split('.')

        if int(d_1[2]) > int(d_2[2]):
            return False
        elif int(d_1[2]) < int(d_2[2]):
            return True
        else:
            if int(d_1[1]) > int(d_2[1]):
                return False
            elif int(d_1[1]) < int(d_2[1]):
                return True
            else:
                if int(d_1[0]) > int(d_2[0]):
                    return False
                elif int(d_1[0]) < int(d_2[0]):
                    return True
                else:
                    return True
    
    def __gt__(self, other):
        d_2 = self.__date.split('.')
        d_1 = other.__date.split('.')

        if int(d_1[2]) > int(d_2[2]):
            return False
        elif int(d_1[2]) < int(d_2[2]):
            return True
        else:
            if int(d_1[1]) > int(d_2[1]):
                return False
            elif int(d_1[1]) < int(d_2[1]):
                return True
            else:
                if int(d_1[0]) > int(d_2[0]):
                    return False
                elif int(d_1[0]) < int(d_2[0]):
                    return True
                else:
                    return False
    
    def __ge__(self, other):
        d_2 = self.__date.split('.')
        d_1 = other.__date.split('.')

        if int(d_1[2]) > int(d_2[2]):
            return False
        elif int(d_1[2]) < int(d_2[2]):
            return True
        else:
            if int(d_1[1]) > int(d_2[1]):
                return False
            elif int(d_1[1]) < int(d_2[1]):
                return True
            else:
                if int(d_1[0]) > int(d_2[0]):
                    return False
                elif int(d_1[0]) < int(d_2[0]):
                    return True
                else:
                    return True
                
    def __str__(self):

        if self.__date is not None:
            d = self.__date.split('.')

            mnth = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 
                    'июл', 'авг','сен', 'окт', 'ноя', 'дек']
            
            return f'{int(d[0])} {mnth[int(d[1]) - 1]} {int(d[2])} г.'
        return str(self.__date)
    
    def __repr__(self):

        return self.__str__()
