import telepot
import pickle
import random
import time
import os

print('starting bot...')
token = os.environ['HP_TOKEN']
bot = telepot.Bot(token)
received_messages = []
authors = []
offset = 0
for x in bot.getUpdates():
    try:
        check = x['message']
        received_messages.append(x)
        authors.append(x['message']['from']['id'])
    except KeyError:
        pass
messages_num = len(received_messages)
print('Messages received:', messages_num)
previous_message = received_messages[-1]['update_id']
test_group = -307834730
sto_pensando = -18933338
leonardo = 24030913

with open('sto_pensando_archive.pickle', 'rb') as f:
    forwards_list = pickle.load(f)

for message in received_messages:
    print(message)


def interact(message_in):
    write_to = message_in['chat']['id']
    if message_in['text'] == '/pensa' or message_in['text'] == '/pensa@HoPensatoBot':
        dice_roll = random.randint(0, len(forwards_list) - 1)
        for elem in forwards_list[dice_roll]:
            bot.sendMessage(write_to, elem, parse_mode='html')


# main loop
while True:
    loop_cycle = 2  # number of seconds between loops
    time.sleep(loop_cycle)

    # variable that stores most recent messages
    received_messages = []
    authors = []
    for x in bot.getUpdates(offset=offset):
        try:
            check = x['message']
            received_messages.append(x)
            authors.append(x['message']['from']['id'])
        except KeyError:
            pass

    received_message = received_messages[-1]['message']
    # saves the ID of the chat the last message was written in
    chat = received_messages[-1]['message']['chat']['id']
    # saves the ID of the last message
    received_message_id = received_messages[-1]['update_id']

    # checks if HoPensatoBot received a new message
    if received_message != previous_message:

        # saves the time at which last message was received
        last_message_datetime = time.time()

        # prints information on the received message
        x = [print() for _ in range(10)]
        print('\n\n\n\n\n\n\n')
        print('NEW MESSAGE RECEIVED')
        for key in received_messages[-1]['message']:
            print(key)
            print('___________________', received_messages[-1]['message'][key])

        interact(received_message)

        # discards the last message and gets ready to receive a new one
        previous_message = received_message
        offset = received_messages[-1]['update_id'] - 80  # only sees the last 80 messages
        if offset < 0:
            offset = 1
