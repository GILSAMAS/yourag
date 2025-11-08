import argparse


def cli():
    parser = argparse.ArgumentParser(description="YourAG CLI")
    subparsers = parser.add_subparsers(dest="command")

    ingest_parser = subparsers.add_parser("ingest", help="Ingest a YouTube video")
    ingest_parser.add_argument(
        "-v",
        "--video-id",
        required=True,
        type=str,
        help="The ID of the YouTube video to ingest",
    )
    ingest_parser.add_argument(
        "-n",
        "--name",
        required=False,
        type=str,
        help="The name to assign to the video collection",
        default=ingest_parser.get_default("video-id"),
    )

    query_parser = subparsers.add_parser("query", help="Query a YouTube video")
    query_parser.add_argument(
        "-v",
        "--video-id",
        required=True,
        type=str,
        help="The ID of the YouTube video to query",
    )
    query_parser.add_argument(
        "-q",
        "--query-text",
        required=True,
        type=str,
        help="The text query to search within the video content",
    )

    store_parser = subparsers.add_parser("store", help="Manage the vector store")
    # Additional subcommands for store can be added here
    store_parser.add_argument(
        "-ls",
        "--list",
        action="store_true",
        required=True,
        help="List all collections in the vector store",
    )

    args = parser.parse_args()

    if args.command == "ingest":
        from yourag.cli.commands.ingest import ingest_video

        ingest_video(args.video_id, args.name)

    elif args.command == "query":
        from yourag.cli.commands.query import query_video

        query_video(args.video_id, args.query_text)

    elif args.command == "store":
        from yourag.cli.commands.store import list_collections

        list_collections()
