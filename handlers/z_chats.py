# This file is part of Korone (Telegram Bot)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from database import Chats
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(~filters.private & filters.all)
async def on_all_m(c: Client, m: Message):
    if await Chats.filter(id=m.chat.id):
        pass
    else:
        await Chats.create(id=m.chat.id, title=m.chat.title)