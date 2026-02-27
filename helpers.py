import random
import string
# Список доступных доменов для email
EMAIL_DOMAINS = [
    'yandex.ru', 
    'ya.ru', 
    'gmail.com', 
    'mail.ru', 
    'yahoo.com', 
    'outlook.com'
]

def generate_random_email():
    first_names = ['john', 'jane', 'alex', 'maria', 'david', 'anna', 'michael', 'elena', 'robert', 'sarah']
    last_names = ['smith', 'johnson', 'williams', 'brown', 'jones', 'garcia', 'miller', 'davis', 'wilson', 'moore']
    
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    
    cohort_number = 41
    random_digits = ''.join(random.choices(string.digits, k=3))
    
    domain = random.choice(EMAIL_DOMAINS)
    
    email = f"{first_name}_{last_name}_{cohort_number}_{random_digits}@{domain}"
    
    return email.lower()


def generate_random_password(min_length=6):
    length = random.randint(min_length, min_length + 3)
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    all_chars = lowercase + uppercase + digits
    
    password = ''.join(random.choices(all_chars, k=length))
    
    return password


def generate_short_password():
    length = random.randint(3, 5)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
