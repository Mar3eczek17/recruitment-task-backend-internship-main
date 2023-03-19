import csv
import json
import datetime


class Make_aReservation:
    def __init__(self):
        self.filename = '23.03-30.03.json'
        self.filename_csv = '23.03-30.03.csv'

    def file_to_text(self):
        with open(self.filename, "r") as file_opened:
            text = json.load(file_opened)
            return text

    def file_to_text_csv(self):
        csvFile = []
        with open(self.filename_csv, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                csvFile.append(row)
            return csvFile

    def maximum_number_of_reservation(self, full_name):
        count = 0
        for i in self.file_to_text_csv():
            if i[0] == full_name:
                count += 1
                if count <= 2:
                    continue
                elif count >= 2:
                    print("You have exceeded the maximum number of reservations for this week.")
                    works = False
                    return works

    def make_reservation(self):
        works = True
        while works:
            book = input("When would you like to book? {DD.MM.YYYY HH:MM}\n")
            book_time = datetime.datetime.strptime(book, '%d.%m.%Y %H:%M')
            print(f'$ {book_time}')

            # check if date_time is less than 1 hour from now
            if (book_time - datetime.datetime.now()).total_seconds() < 3600:
                print("Sorry, less than one hour left to book, you can't make a reservation.")
                break

            if book[:5] in self.file_to_text():
                exists = 0
                for data in self.file_to_text()[book[:5]]:
                    if data['start_time'] <= book[11:16] < data['end_time']:
                        exists += 1
                if exists <= 0:
                    print('The spot is available. Do you want to reserve them?')
                for data in self.file_to_text()[book[:5]]:
                    if data['start_time'] <= book[11:16] < data['end_time']:
                        print(f"The time you chose is unavailable, would you like to make a reservation for "
                              f"{data['end_time']} instead?")
                kepp_going = input('yes/no\n')
                print(f'$ {kepp_going}')
                if kepp_going[0].lower() == 'n':
                    works = True
                elif kepp_going[0].lower() == 'y':
                    print(book)
                    break

    def next_number(self):
        works = True
        while works:
            book = input("When would you like to book? {DD.MM.YYYY HH:MM}\n")
            book_time = datetime.datetime.strptime(book, '%d.%m.%Y %H:%M')
            print(f'$ {book_time}')

            # check if date_time is less than 1 hour from now
            if (book_time - datetime.datetime.now()).total_seconds() < 3600:
                print("Sorry, less than one hour left to book, you can't make a reservation.")
                break

            if book[:5] in self.file_to_text():
                exists = 0
                for data in self.file_to_text()[book[:5]]:
                    if data['start_time'] <= book[11:16] < data['end_time']:
                        exists += 1
                if exists <= 0:
                    print('The spot is available. Do you want to reserve them?')
                for data in self.file_to_text()[book[:5]]:
                    if data['start_time'] <= book[11:16] < data['end_time']:
                        print(f"The time you chose is unavailable, would you like to make a reservation for "
                              f"{data['end_time']} instead?")
                        print(data['end_time'])
                kepp_going = input('yes/no\n')
                print(f'$ {kepp_going}')
                if kepp_going[0].lower() == 'n':
                    works = True
                elif kepp_going[0].lower() == 'y':
                    print(book)
                    break

        # prompt user for duration of reservation
        while True:
            # print(self.file_to_text_csv())
            book_day = []
            for data in self.file_to_text_csv()[1:]:
                for items in data:
                    # print(items)
                    if book[:5] == items[1:6]:
                        book_day.append(items)
            book_day = [ts.strip() for ts in book_day]
            # print(book_day)
            if book in book_day:
                # print(book)
                index = book_day.index(book)
                book_day = book_day[index:index + 2]
                print(book_day)
                for i in range(0, len(book_day), 2):
                    time1 = datetime.datetime.strptime(book_day[i], '%d.%m.%Y %H:%M')
                    time2 = datetime.datetime.strptime(book_day[i + 1], '%d.%m.%Y %H:%M')
                    diff = time2 - time1
                    # diff = datetime.datetime.strptime(book_day[i + 2], ' %d.%m.%Y %H:%M') - datetime.datetime.strptime(
                    #     book_day[i+1], ' %d.%m.%Y %H:%M')
                    # print(diff)
                    # print(duration_str)
                    # print(type(duration_str))
                    if diff == datetime.timedelta(hours=1, minutes=30):
                        # duration = int(input("How long would you like to book court?\n"))
                        print(f'How long would you like to book court?\n1) 30 Minutes\n2) 60 Minutes\n3) '
                              f'90 Minutes\n')
                        duration = int(input("Choose value?\n"))
                        print(f'$ {duration}')
                        break
                    elif diff == datetime.timedelta(hours=1):
                        # duration = int(input("How long would you like to book court?\n"))
                        print(f"How long would you like to book court?\n1) 30 Minutes\n2) 60 Minutes\n")
                        duration = int(input("Choose value?\n"))
                        print(f'$ {duration}')
                        break
                    elif diff == datetime.timedelta(minutes=30):
                        # duration = int(input("How long would you like to book court?\n"))
                        print(f"How long would you like to book court?\n1) 30 Minutes\n")
                        duration = int(input("Choose value?\n"))
                        print(f'$ {duration}')
                        break


print('$ Make a reservation ')
full_name = input("What's your Name?\n")
print(f'$ {full_name}')


# make reservation
make_aReservation = Make_aReservation()
make_aReservation.maximum_number_of_reservation(full_name)
make_aReservation.make_reservation()
make_aReservation.next_number()