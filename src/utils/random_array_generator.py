from numpy.random import seed, randint


def generate_random_array(text_size, text_min_value, text_max_value, default_size, default_min, default_max,  is_seed_active=False, seed_value=1):
    # Default size is 15.
    if text_size != '' and int(text_size) > 0:
        size = int(text_size)
    else:
        size = default_size

    if is_seed_active:
        seed(seed_value)

    # Default min value is 1, and max value is 50.
    if text_min_value != '' and text_max_value != '' and int(text_max_value) > int(text_min_value):
        min_value = int(text_min_value)
        max_value = int(text_max_value)
    elif text_max_value != '' and int(text_max_value) > default_min:
        min_value = default_min
        max_value = int(text_max_value)
    elif text_min_value != '':
        min_value = int(text_min_value)
        max_value = default_max + int(text_min_value)
    else:
        min_value = default_min
        max_value = default_max

    return randint(min_value, max_value, size).tolist()
