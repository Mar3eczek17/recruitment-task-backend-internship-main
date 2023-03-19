import json


class Make_aReservation:
    print('$ Make a reservation ')
    name = input("What's your Name?\n")
    book = input("When would you like to book? {DD.MM.YYYY HH:MM}\n")

    def __init__(self):
        self.filename = '23.03-30.03.json'

    def file_to_text(self):
        with open(self.filename, "r") as file_opened:
            text = json.load(file_opened)
            return text

    def reservation(self):
        if self.book[:5] in self.file_to_text():
            while True:
                exists = 0
                for data in self.file_to_text()[self.book[:5]]:
                    if data['start_time'] <= self.book[11:16] < data['end_time']:
                        exists += 1
                if exists <= 0:
                    print('Aviabel')
                else:
                    for data in self.file_to_text()[self.book[:5]]:
                        if data['start_time'] <= self.book[11:16] < data['end_time']:
                            print(f'The time you chose is unavailable, would you like to make a reservation for '
                                  f'{data["end_time"]} instead? (yes/no)')
                kepp_going = input()
                print(f'$ {kepp_going}')
                break


make_aReservation = Make_aReservation()
make_aReservation.reservation()
