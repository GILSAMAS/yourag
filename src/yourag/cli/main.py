import argparse

def cli():
    parser = argparse.ArgumentParser(description="YourAG CLI")
    subparsers = parser.add_subparsers(dest="command")

    ingest_parser = subparsers.add_parser("ingest", help="Ingest a YouTube video")
    ingest_parser.add_argument("-v", "--video_id", type=str, help="The ID of the YouTube video to ingest")

    args = parser.parse_args()

    if args.command == "ingest":
        from yourag.cli.commands.ingest import ingest_video
        ingest_video(args.video_id)