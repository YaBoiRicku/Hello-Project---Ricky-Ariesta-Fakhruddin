import random
import logging

chara = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'

total = input('How many passwords do you need? - ')
total = int(total)

length = input('The length of the password? - ')
length = int(length)

with open('list.txt', 'w'):
        pass

for i in range(total):
    password = ''
    for x in range(length):
        password += random.choice(chara)
    logging.basicConfig(level=logging.DEBUG, filename="list.txt", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
    logging.info(password)
print("Success, now check the list folder for the password you generate and don't forget to save it")

input('Press ENTER to exit')



