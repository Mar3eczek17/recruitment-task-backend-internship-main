import csv
import json
import datetime
import time


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

    def make_reservation(self, full_name):
        works = True
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
                else:
                    for data in self.file_to_text()[book[:5]]:
                        if data['start_time'] <= book[11:16] < data['end_time']:
                            print(f"The time you chose is unavailable, would you like to make a reservation for "
                                  f"{data['end_time']} instead?")
                kepp_going = input('yes/no\n')
                print(f'$ {kepp_going}')
                if kepp_going[0].lower() == 'n':
                    works = True
                elif kepp_going[0].lower() == 'y':
                    break

        # prompt user for duration of reservation
        while True:
            duration = int(input("How long would you like to book court?\n"))
            duration = datetime.timedelta(minutes=duration)
            duration_str = str(duration)
            duration_str = duration_str[-(8 if len(duration_str) == 7 else 7):]
            # print(duration_str)
            print(self.file_to_text_csv())
            book_day = []
            for data in self.file_to_text_csv()[1:]:
                for items in data:
                    # print(items)
                    if book[:5] == items[1:6]:
                        book_day.append(items)
            print(book_day)
            for i in range(len(book_day) - 1):
                diff = datetime.datetime.strptime(book_day[i + 2], ' %d.%m.%Y %H:%M') - datetime.datetime.strptime(
                    book_day[i+1], ' %d.%m.%Y %H:%M')
                print(diff)
                # print(duration_str)
                # print(type(duration_str))
                if diff == datetime.timedelta(hours=1, minutes=30):
                    print("1) 30 Minutes\n2) 60 Minutes\n3) 90 Minutes")
                    break
                elif diff == datetime.timedelta(hours=1):
                    print("1) 30 Minutes\n2) 60 Minutes\n")
                    break
                elif diff == datetime.timedelta(minutes=30):
                    print("1) 30 Minutes\n")
                    break



                # if duration not in [30, 60, 90]:
            #     raise ValueError
            # if duration == 90 and date_time.hour >= 17:
            #     print("Sorry, the court is only available for 90 minutes until 17:00.")
            #     continue
            # break
            # except ValueError:
            #     print("Invalid duration.")


# user full name
print('$ Make a reservation ')
full_name = input("What's your Name?\n")
print(f'$ {full_name}')

# make reservation
make_aReservation = Make_aReservation()
make_aReservation.make_reservation(full_name)
