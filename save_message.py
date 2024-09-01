from pyrogram import Client, filters
import logging
import asyncio

api_id: int = 12345 <-- replace this
api_hash: str = "abcd" <-- replace this
delete_group: str = "-12345" <-- replace this 
limit: int = 1
app = Client("my_bot", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.private)
async def sender(client, message):
    try:
        # Forward the message to the group
        await app.forward_messages(chat_id=delete_group,
                            from_chat_id=message.chat.id,
                            message_ids=message.id)
        await asyncio.sleep(limit)
    except Exception as e:
        logging.error(f"Error forwarding message: {e}")

if __name__ == "__main__":
    app.run()