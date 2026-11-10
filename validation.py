def get_positive_num(message: str) -> int:
    while True:
        try:
            num = int(input(message))
            if num > 0:
                return num
            print('Enter positive number only!')
            
        except ValueError:
            print('Enter numbers only!')
            
def get_valid_str(message: str) -> str:
    while True:
        the_str = input(message).strip().title()
        if the_str:
            return the_str
        print('Enter a valid name!')