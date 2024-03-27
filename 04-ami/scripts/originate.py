from asterisk.ami import SimpleAction
import sys

action = SimpleAction(
    'Originate',
    Channel='SIP/2010',
    Exten=f'{}',
    Priority=1,
    Context='from-internal',
    CallerID='python',
)
client.send_action(action)


def main():


if __name__ == "__main__":
    main()
