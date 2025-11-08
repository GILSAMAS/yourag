import argparse
from yourag.cli.commands.base import CLI
from yourag.utils.urls import extract_video_id
from dotenv import load_dotenv


def cli():
    load_dotenv()
    cli = CLI()
    cli.run()
