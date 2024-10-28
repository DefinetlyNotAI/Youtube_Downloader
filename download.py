import argparse
from pytubefix import YouTube
import colorlog
from tqdm import tqdm

# Configure colorlog for logging messages with colors
logger = colorlog.getLogger()
logger.setLevel(colorlog.INFO)  # Set the log level to INFO to capture all relevant logs

handler = colorlog.StreamHandler()
formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "red",
    },
)
handler.setFormatter(formatter)
logger.addHandler(handler)


def download_video(url, output_path):
    """
    Downloads a YouTube video from the given URL and saves it to the specified output path,
    displaying a progress bar and the video title upon completion.
    """
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download(output_path)
    colorlog.info(f"{yt.title} downloaded successfully.")


def parse_arguments():
    """
    Parses command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Download YouTube videos.")
    parser.add_argument('--url', nargs='+', required=True,
                        help='URL of the YouTube video to download. Use --yt multiple times to add more.')
    parser.add_argument('--to', default='./',
                        help='Directory path where the downloaded videos should be saved. Creates the directory if it doesn\'t exist. Defaults to current working directory.')

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--from-txt', type=argparse.FileType('r'),
                       help='Path to a text file containing YouTube video URLs, one URL per line.')

    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.from_txt:
        urls = [line.strip() for line in args.from_txt.readlines()]
    else:
        urls = args.url

    for url in tqdm(urls, desc="Downloading videos"):
        try:
            download_video(url, args.to)
            colorlog.info("Download completed.")
        except Exception as e:
            colorlog.debug(e)
            if str(e) == "get_throttling_function_name: could not find match for multiple":
                colorlog.critical("Video could not be downloaded due to an error with the API of YouTube")
            else:
                colorlog.error(f"Failed to download video: {e}")


if __name__ == "__main__":
    main()
