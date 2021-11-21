from client import client
from query import get_person_list, add_person

def view():
    person_list = client.execute(get_person_list)
    person_list = dict(person_list)['person']

    for person in person_list :
        print(person['id'])
        print(person['name'])
        print(person['house']['address'])
        print()

def add():
    print('name:',end=' ')
    name = input()
    print('age:', end=' ')
    age = int(input())
    print('address:', end=' ')
    address = input()

    result = client.execute(add_person, variable_values={
        'name':name,
        'age':age,
        'address':address
    })

    print(result)
    print()

def main():
    while(1):
        print("1 : view, 2 : add, others : quit")
        flag = int(input())
        if flag == 1 :
            view()
        elif flag == 2 :
            add()
        else:
            break;



if __name__ == '__main__':
    main()
