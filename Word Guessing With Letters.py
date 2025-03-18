import random
def get_input_list():#ساخت لیست
    list_of_words1=set()#ورودی تکراری ممنوع
    while True:
        first_user=input('Name list ')
        if first_user.isalpha():
            break    
        print('invalid input! please enter only letters')
    first_length=len(first_user)
    list_of_words1.add(first_user.lower())
    while True:
        user=input("enter next name (or 'ex' to exit): ")
        if user=='ex':
            break
        if user.isalpha() and len(user)==first_length:#اگ ورودی دوم برابر با ورودی اول باش اضافه بش ب لیست
            list_of_words1.add(user.lower())
        elif not user.isalpha():
            print('invalid input! please enter only letters')
    print("_"*10)
    return list(list_of_words1)
names=(get_input_list())
selected_name=random.choice(names)
guess_count=len(selected_name)
guessed_list=["_"]* len(selected_name)
current_guess=" ".join(guessed_list)
print(current_guess)
while guess_count> 0:
    print(f'wrong! => remained guesses: {guess_count-1}')
    guessed_char= input('enter a char: ')
    if guessed_char.isalpha():
        if guessed_char in selected_name:
            if guessed_char in guessed_list:
                print('you have guessed before, try new character')
            else:
                for idx, char in enumerate(selected_name):
                    if char==guessed_char:
                        guessed_list[idx]=guessed_char
                current_guess=' '.join(guessed_list)
                print(f'perfect => {current_guess}')
                if not '_' in guessed_list:
                    print("you won!")
                    break
        else:
            guess_count-=1
        if guess_count==0:
            print(f'select Ai {selected_name}')
            print(f'wrong! => remained guesses: {guess_count}')
    else:
        print('please enter a valid character')