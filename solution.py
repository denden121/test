import os
import json
from car import Car



def print_menu():
    '''Print menu'''
    print('Enter 1 - Print car\'s information\n'
          + 'Enter 2 - Add a new car\n'
            + 'Enter 3 - Delete a car\n'
            + 'Enter 4 - edit  car\'s information\n'
            + 'Enter 5 - Print all the cars\n'
            + 'Enter 6 - Exit')


def print_information_about_car(list_cars):
    '''Print information about car'''
    print("Enter car's id")
    while True:
        id_car = input()
        if id_car in list_cars and id_car != 'exit':
            print(id_car,str(list_cars[id_car]))
            break
        elif id_car == 'exit':
            return
        else:
            print('Couldn\'t find the car.Re-enter car\'s id or type \'exit\' for exiting to main menu')


def add_new_car(list_cars):
    '''Add information about new car'''
    print("Enter car's id (id must be unique)")
    id_car = input()
    while True:
        if not id_car in list_cars:
            break
        print("Car's id must be unique, re-enter")
        id_car = input()
    manufacturer = check_text_value('manufacturer')
    model = check_text_value('model')
    body = check_text_value('body')
    year = check_year()
    list_cars[id_car] = Car(manufacturer, model, body, year)
    save_data(list_cars)
    print('New car added')

def remove_car(list_cars):
    '''Delete cars'''
    while True:
        id_car = input("Enter car's id\n")
        if id_car in list_cars:
            del list_cars[id_car]
            save_data(list_cars)
            print('Car removed')
        elif id_car =='exit':
            return 
        else:
            print("Couldn't find the car.re-enter or ")


def save_data(list_cars):
    '''Save dates about cars in file'''
    with open('list_car.txt', 'w') as f:
        for i in list_cars:
            f.write(f'{i} {str(list_cars[i])}\n')
    print('Data saved')


def check_text_value(name):
    while True:
        thing = input(f'Enter {name} ')
        if  thing != '':
            return  thing
        else:
            print(f"{name} isn't correct, re-enter ")
        
def check_year():
    while True:
        year = input('Enter year ')
        if year.isdigit() and int(year) > 1900:
            return year
        print("Year isn't correct, re-enter ")

def edit_information_about_car(list_cars):
    '''Edit date about cars'''
    print("Enter car's which need to edit")
    while True:
        id_car = input()
        if  id_car in list_cars:
            break
        print("id car's couldn't find, re-enter")
    print('Enter what do you want to change(model, manufacturer, bode, year)')
    temp_car = list_cars[id_car]
    while True:
        thing = input()
        if thing == 'model':
            temp_car.model = check_text_value('model')
            print('To change something else just enter the field name. to exit to the main menu enter exit')   
        elif thing == 'manufacturer':
            temp_car.manufacturer = check_text_value('manufacturer')
            print('To change something else just enter the field name. to exit to the main menu enter exit') 
        elif thing == 'body':
            temp_car.body = check_text_value('body')
            print('To change something else just enter the field name. to exit to the main menu enter exit') 
        elif thing == 'year':
            temp_car.year= check_year()
            print('To change something else just enter the field name. to exit to the main menu enter exit') 
        elif thing == 'exit':
            break
        else:
            print('Incorrect. Re-enter')    
    list_cars[id_car] = temp_car
    save_data(list_cars)


def show_car(list_cars):
    '''Print all the cars'''
    for i in list_cars:
        temp = list_cars[i] 
        print(i , str(temp))


def add_start_date():
    '''Add start cars'''
    list_cars = {}
    if not os.path.exists("list_cars.txt"):
        with open('list_car.txt', 'w') as f:
            temp = Car('toyota', 'mark2', 'cidan', '2000')
            temp1 = Car('toyota', 'chaser', 'cidan', '2000')
            temp2 = Car('bmw', 'm5', 'jeep', '2018')
            list_cars['0'] =temp
            f.write(f'0 {str(temp)}\n')
            list_cars['1'] =temp1
            f.write(f'1 {str(temp1)}\n3')
            list_cars['2'] = temp2
            f.write(f'2 {str(temp2)}\n')
            print("It's first start. Created 3 cars")
    else:
        try:
            with open('list_car.txt') as f:
                temp_list = f.read().split('\n')
                for i in temp_list.split(' '):
                    list_cars[i[0]] = Car(i[1],i[2],i[3],[4])
        except Exception:
            print('File isn\'t corret')
    return list_cars

def main():
    list_cars = add_start_date()
    print('Hi, what do you want to do:\n')
    while True:
        print_menu()
        command = input()
        if command == '1':
            print_information_about_car(list_cars)
        elif command == '2':
            add_new_car(list_cars)
        elif command == '3':
            remove_car(list_cars)
        elif command == '4':
            edit_information_about_car(list_cars)
        elif command == '5':
            show_car(list_cars)
        elif command == '6':
            print("Bye")
            save_data(list_cars)
            break
        else:
            print("Date isn't correct. Re-enter")



if __name__ == "__main__":
    main()