import argparse


def analyser_commande():
    parser = argparse.ArgumentParser(
        description="Retourne l'idul du joueur et l'attribut parties"
        parser.add_argument(
            '-m', '--mode',
            metavar='IDUL', dest='idul',
            help="usage: main.py [-h] [-p] idul\n\nQuoridor\n\npositional arguments:\n  idul          IDUL du joueur\n\noptions:\n  -h, --help    show this help message and exit\n  -p, --parties  Lister les parties existantes"
        )
        parser.add_argument(
            '-p',
            metavar='PARTIES', dest='parties',
            choices=[True, False],
            help="usage: main.py [-h] [-p] idul\n\nQuoridor\n\npositional arguments:\n  idul          IDUL du joueur\n\noptions:\n  -h, --help    show this help message and exit\n  -p, --parties  Lister les parties existantes"
        )
    )

    return parser.parse_args()