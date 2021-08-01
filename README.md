# "Joined telegram" chats remover
This is program for removing unnecessary chats where user "joined telegram".

## Requirements
Python 3 with the [telethon](https://docs.telethon.dev/) package installed

## Run
### Setting environment variables
Get and set your TG_API_ID and TG_API_HASH from <https://my.telegram.org>

Example (won't work):

Windows    

    set TG_API_ID=12345
    set TG_API_HASH=0123456789abcdef0123456789abcdef

Linux

    export TG_API_ID=12345
    export TG_API_HASH=0123456789abcdef0123456789abcdef
    

### Usage
    python3 main.py
Follow the telethon's instructions after running program to sign in telegram. The session will be saved in the joined_telegram_delete_chat.session file.