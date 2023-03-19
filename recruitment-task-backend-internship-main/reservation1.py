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
                    print('Spot time is available')
                else:
                    for data in self.file_to_text()[book[:5]]:
                        if data['start_time'] <= book[11:16] < data['end_time']:
                            print(f"The time you chose is unavailable, would you like to make a reservation for "
                                  f"{data['end_time']} instead?")
                kepp_going = input('yes/no\n')
                print(f'$ {kepp_going}')
                if kepp_going[0].lower() == 'y':
                    works = True
                else:
                    break

        # prompt user for duration of reservation
        while True:
            try:
                duration = int(input("How long would you like to book court? (in minutes, up to 90 minutes) "))
                print(duration)
            except ValueError:
                print("Invalid duration.")


# user full name
print('$ Make a reservation ')
full_name = input("What's your Name?\n")
print(f'$ {full_name}')

# make reservation
make_aReservation = Make_aReservation()
make_aReservation.make_reservation(full_name)
