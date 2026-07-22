from ticket import create_ticket
from display import display_ticket


def main():
    ticket = create_ticket()

    display_ticket(*ticket)


if __name__ == "__main__":
    main()