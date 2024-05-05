class AirTicket:

    def __init__(self, passenger_name, _from, to, date_time, flight,\
                 seat, _class, gate):

        self.passenger_name = passenger_name
        self._from = _from
        self.to = to
        self.date_time = date_time
        self.flight = flight
        self.seat = seat
        self._class = _class
        self.gate = gate
    
    def __str__(self):

        space_passenger_name = ' ' * (16 - len(self.passenger_name))
        space_from = ' ' * (4 - len(self._from))
        space_to = ' ' * (3 - len(self.to))
        space_date_time = ' ' * (16 - len(self.date_time))
        space_flight = ' ' * (20 - len(self.flight))
        space_seat = ' ' * (4 - len(self.seat))
        space_class = ' ' * (3 - len(self._class))
        space_gate = ' ' * (4 - len(self.gate))

        return f'|{self.passenger_name}{space_passenger_name}|{self._from}{space_from}|\
{self.to}{space_to}|{self.date_time}{space_date_time}|{self.flight}{space_flight}|\
{self.seat}{space_seat}|{self._class}{space_class}|{self.gate}{space_gate}|'

class Load:

    data = []

    @staticmethod
    def write(text):

        with open(text, 'r', encoding="utf8") as f:
            attr = f.readline().split(';')[:-1]

            for line in f:
                values = line.split(';')[:-1]

                items = {}
                for i in range(len(attr)):
                    items[attr[i]] = values[i]

                Load.data.append(AirTicket(items['passenger_name'], items['from'],\
                                            items['to'], items['date_time'], items['flight'],\
                                            items['seat'], items['class'], items['gate']))
