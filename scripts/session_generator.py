import click
import pyrogram


async def client_get_me(client: pyrogram.Client) -> str:
    async with client:
        return await client.get_me()


@click.group()
def create_config() -> None:
    pass


@create_config.command()
@click.option('--name', prompt=True, required=True, type=click.STRING, help='Name of the session')
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
def create_bot_config(
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
    )

    client_info = client.run(client_get_me(client))
    click.echo(client_info)


@create_config.command()
@click.option('--name', prompt=True, required=True, type=click.STRING, help='Name of the session')
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
def create_user_config(
    name: str,
    api_id: int,
    api_hash: str,
    phone_number: str,
    password: str,
) -> None:
    client = pyrogram.Client(
        name,
        api_id,
        api_hash,
        phone_number=phone_number,
        password=password,
    )

    client_info = client.run(client_get_me(client))
    click.echo(client_info)


if __name__ == "__main__":
    create_config()
