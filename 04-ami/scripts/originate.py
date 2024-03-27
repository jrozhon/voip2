import click
from asterisk.ami import AMIClient, SimpleAction

ASTERISK_IP = "localhost"
ASTERISK_PORT = 5038
AMI_USERNAME = "amiuser"
AMI_PASSWORD = "amipass"


class AmiContextManager:
    def __enter__(self):
        self.client = AMIClient(address=ASTERISK_IP, port=ASTERISK_PORT)
        self.client.login(username=AMI_USERNAME, secret=AMI_PASSWORD)
        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.logoff()


@click.command()
@click.option(
    "-f",
    "--from_ext",
    default="10",
    help="Extension that originates a call (can only be internal)",
)
@click.option(
    "-t",
    "--to_ext",
    default="11",
    help="Extension that receives the call (can be internal or external)",
)
def make_call(from_ext, to_ext):
    with AmiContextManager() as client:
        action = SimpleAction(
            "Originate",
            Channel=f"Local/{from_ext}@from-ami",
            Exten=f"{to_ext}",
            Priority=1,
            Context="from-internal",
            CallerID=f"{to_ext}",
        )
        client.send_action(action)


def main():
    make_call()


if __name__ == "__main__":
    main()
