import json


class Make_aReservation:
    # print('$ Make a reservation ')
    # name = input("What's your Name?\n")

    def __init__(self):
        self.filename = '23.03-30.03.json'

    def file_to_text(self):
        with open(self.filename, "r") as file_opened:
            text = json.load(file_opened)
            return text

    def reservation(self):
        # print(self.file_to_text())
        game_on = True
        while game_on:
            book = input("When would you like to book? {DD.MM.YYYY HH:MM}\n")
            if book[:5] in self.file_to_text():
                # print(self.file_to_text()[self.book[:5]])
                # print(self.file_to_text()[self.book[:5]])
                exists = 0
                for data in self.file_to_text()[book[:5]]:
                    # print(data['start_time'])
                    # print(data['end_time'])
                    # print(self.book[11:16])
                    if data['start_time'] <= book[11:16] < data['end_time']:
                        exists += 1
                if exists <= 0:
                    print('Aviabel')
                else:
                    # date_time_str = self.book[11:16]
                    # date_time_obj = datetime.datetime.strptime(date_time_str, '%H:%M')
                    # updated_time = date_time_obj + timedelta(minutes=30)
                    # print(f'The time you chose is unavailable, would you like to make a reservation for '
                    #       f'{updated_time.strftime("%H:%M")} instead? '
                    #       '(yes/no)')
                    # [data["end_time"] for data in self.file_to_text()[self.book[:5]]]
                    for data in self.file_to_text()[book[:5]]:
                        if data['start_time'] <= book[11:16] < data['end_time']:
                            print(f'The time you chose is unavailable, would you like to make a reservation for '
                                  f'{data["end_time"]} instead?')
                kepp_going = input('yes/no\n')
                print(f'$ {kepp_going}')
                if kepp_going[0].lower() == 'y':
                    game_on = True
                else:
                    break


make_aReservation = Make_aReservation()
make_aReservation.reservation()
