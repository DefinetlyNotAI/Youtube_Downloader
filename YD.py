import argparse
from pytube import YouTube


def download_video(url, output_path):
    """
    Downloads a YouTube video from the given URL and saves it to the specified output path.
    """
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download(output_path)


def parse_arguments():
    """
    Parses command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Download YouTube videos.")
    # Removed the explicit '-h' option since argparse adds it automatically
    parser.add_argument('--yt', nargs='+', required=False,
                        help='URL of the YouTube video to download. Use --yt multiple times to add more.')
    parser.add_argument('--to', default='./',
                        help='Directory path where the downloaded videos should be saved. Creates the directory if it doesn\'t exist. Defaults to current working directory.')

    # Parsing the text file option
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--txt', type=argparse.FileType('r'),
                       help='Path to a text file containing YouTube video URLs, one URL per line.')

    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.txt:
        urls = [line.strip() for line in args.txt.readlines()]
    else:
        urls = args.yt

    for url in urls:
        try:
            download_video(url, args.to)
            print(f"Downloaded {url} successfully.")
        except Exception as e:
            print(f"Failed to download {url}: {e}")


if __name__ == "__main__":
    main()
