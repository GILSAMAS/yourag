import argparse

def cli():
    parser = argparse.ArgumentParser(description="YourAG CLI")
    subparsers = parser.add_subparsers(dest="command")

    ingest_parser = subparsers.add_parser("ingest", help="Ingest a YouTube video")
    ingest_parser.add_argument("-v", "--video_id", required=True, type=str, help="The ID of the YouTube video to ingest")

    query_parser = subparsers.add_parser("query", help="Query a YouTube video")
    query_parser.add_argument("-v", "--video_id", required=True, type=str, help="The ID of the YouTube video to query")
    query_parser.add_argument("-q", "--query_text", required=True, type=str, help="The text query to search within the video content")

    args = parser.parse_args()

    if args.command == "ingest":
        from yourag.cli.commands.ingest import ingest_video
        ingest_video(args.video_id)

    elif args.command == "query":
        from yourag.cli.commands.query import query_video
        query_video(args.video_id, args.query_text)