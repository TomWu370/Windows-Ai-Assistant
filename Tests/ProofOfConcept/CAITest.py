import asyncio

from characterai import PyCAI, PyAsyncCAI
async def main():
    api = 'token'

    char = "charid"

    client = PyAsyncCAI(api)

    chat =  await client.chat2.get_chat(char)
    print(chat)

    author = {"author_id": chat["chats"][0]["creator_id"]}
    user =  await client.user.info()
    chat_id = chat["chats"][0]["chat_id"]

    msg1 = "Hello."
    async with client.connect() as chat2:
        # new chat simply creates a new chat, it doesn't clear the current chat
        # therefore a hack to clear the chat is to create a new chat with a unique name, ie unix time/date
        await chat2.new_chat(char, 'CHAT_ID1', author['author_id'])

    #await client.chat.new_chat(char)

asyncio.run(main())