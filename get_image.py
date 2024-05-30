import time
import random

image_set = ["macha", "mango", "strawberry", "taro", "thai"]

while True:

    with open('get_image.txt', 'r') as f:
        command = f.read().strip()

    if command == 'get':
        rand_num = random.randint(0,10)
        image_index = rand_num % len(image_set)
        selected_image = image_set[image_index]
        image_path = f'images/{selected_image}.jpg'

        with open('get_image.txt', 'w') as f:
            f.write(str(image_path))
    else:
        time.sleep(1)