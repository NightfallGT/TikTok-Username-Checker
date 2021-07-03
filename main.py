import asyncio
from os import system
from typing import List

import aiohttp


def write_file(arg: str) -> None:
    with open('hits.txt', 'a', encoding='UTF-8') as f:
        f.write(f'{arg}\n')


class Checker:
    def __init__(self, usernames: List[str]):
        self.to_check = usernames

    async def _check(self, session: aiohttp.ClientSession, username: str) -> None:
        async with session.head(f'https://www.tiktok.com/@{username}') as response:
            if response.status == 200 and len(username) > 2:
                print(
                    '%s[UNAVAILABLE] https://www.tiktok.com/@%s%s'
                    % ('\u001b[31;1m', username, '\u001b[0m')
                )
            else:
                print(
                    '%s[AVAILABLE] https://www.tiktok.com/@%s%s'
                    % ('\u001b[32;1m', username, '\u001b[0m')
                )
                write_file(username)

    async def start(self):
        print('Loading.. This may take awhile.')
        async with aiohttp.ClientSession() as sess:
            return await asyncio.gather(*[self._check(sess, u) for u in self.to_check])


if __name__ == '__main__':
    system('cls && title TikTok Username Checker by NightfallGT and github.com/sql69')

    with open('usernames.txt', encoding='UTF-8') as f:
        username_list = [line.strip() for line in f]

    checker = Checker(username_list)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(checker.start())
