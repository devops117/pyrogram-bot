#MIT License
#
#Copyright (c) 2022-2023 DevOps117
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import typing # typing.Optional

import click # click.group, click.option, click.password_option, click.echo, click.STRING, click.INT
import pyrogram # pyrogram.Client


async def client_get_me(client: pyrogram.Client) -> str:
    async with client:
        return await client.get_me()


@click.group()
def create_session() -> None:
    pass


@create_session.command()
@click.option('--session-dir', required=True, type=click.Path(exists=True, writable=True, file_okay=False, dir_okay=True))
@click.option('--name', required=True, prompt=True, type=click.STRING, help='Name of the session')
@click.option(
    '--api-id',
    prompt=True,
    hide_input=True,
    required=True,
    type=click.INT,
    help='API id can be obtained from my.telegram.org',
)
@click.option(
    '--api-hash',
    prompt=True,
    hide_input=True,
    required=True,
    help='API hash can be obtained from my.telegram.org',
)
@click.password_option('--bot-token', required=True, help='Bot token can be obtained from t.me/BotFather')
def create_bot_session(
    session_dir: str,
    name: str,
    api_id: int,
    api_hash: str,
    bot_token: str,
) -> None:
    client = pyrogram.Client(
        name,
        api_id,
        api_hash,
        bot_token=bot_token,
        workdir=session_dir,
    )

    client_info = client.run(client_get_me(client))
    click.echo(client_info)


@create_session.command()
@click.option('--session-dir', required=True, type=click.Path(exists=True, writable=True, file_okay=False, dir_okay=True))
@click.option('--name', required=True, prompt=True, type=click.STRING, help='Name of the session')
@click.option(
    '--api-id',
    prompt=True,
    hide_input=True,
    required=True,
    type=click.INT,
    help='API id can be obtained from my.telegram.org',
)
@click.option(
    '--api-hash',
    prompt=True,
    hide_input=True,
    required=True,
    help='API hash can be obtained from my.telegram.org',
)
@click.password_option('--phone-number', required=True, help='Phone number with country code prefix')
@click.password_option('--password', help='Two-Step Verification password')
def create_user_session(
    session_dir: str,
    name: str,
    api_id: int,
    api_hash: str,
    phone_number: str,
    password: typing.Optional[str],
) -> None:
    client = pyrogram.Client(
        name,
        api_id,
        api_hash,
        phone_number=phone_number,
        password=password,
        workdir=session_dir,
    )

    client_info = client.run(client_get_me(client))
    click.echo(client_info)


if __name__ == "__main__":
    create_session()

__all__ = [""]
