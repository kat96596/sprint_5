import random
import string
def generate_random_email():
    first_names = ['john', 'jane', 'alex', 'maria', 'david', 'anna']
    last_names = ['smith', 'johnson', 'williams', 'brown', 'jones']
    
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    random_digits = ''.join(random.choices(string.digits, k=3))
    
    return f"{first_name}_{last_name}_6_{random_digits}@yandex.ru"


def generate_random_password(min_length=6):
    length = random.randint(min_length, min_length + 3)
    all_chars = string.ascii_letters + string.digits
    
    return ''.join(random.choices(all_chars, k=length))


def generate_short_password():
    length = random.randint(3, 5)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
