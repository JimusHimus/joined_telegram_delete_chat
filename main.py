import os
from telethon.sync import TelegramClient
from telethon.tl.types import MessageActionContactSignUp

# setup your environment first
session = 'joined_telegram_delete_chat'
api_id = int(os.getenv('TG_API_ID'))
api_hash = os.getenv('TG_API_HASH')

client = TelegramClient(session, api_id, api_hash)


def connect():
    client.start()


def clear_useless_chats():
    connect()
    dialogs = client.get_dialogs()
    deleted_count = 0
    for dialog in dialogs:
        # if last message (in case of signup also the first message) is a signup action message
        if dialog.message.action == MessageActionContactSignUp():
            name = dialog.name
            print(f'Found useless chat with {name}')
            dialog.delete()
            deleted_count += 1
    print(f'{deleted_count} chats deleted')


if __name__ == '__main__':
    clear_useless_chats()
