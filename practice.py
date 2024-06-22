def categorize_age(age):
    #match age:
        case _ if age <= 9:
            return 'Gen Alpha'
        case _ if age <= 27:
            return 'Gen Z'
        case _ if age <= 38:
            return 'Millennial'
        case _ if age <= 73:
            return 'Baby Boomer'
        case _:
            return 'Silent Generation'
 
 
def main():
    try:
        age = int(input('Enter your age: '))
        generation = categorize_age(age)
        print(f'You belong to: {generation}')
    except ValueError:
        print('Please enter a valid age')
 
if __name__ == '__main__':
    main()