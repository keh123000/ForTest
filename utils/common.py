import random
import string
from datetime import datetime


def get_current_time_str(fmt="%Y%m%d%H%M%S%f"):
    return datetime.now().strftime(fmt)


def get_random_str(length=5):
    return ''.join(random.sample(string.ascii_letters + string.digits, length))
