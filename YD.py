import argparse
from pytube import YouTube
from tqdm import tqdm  # Import tqdm


def download_videos(urls):
    """
    Download videos from the provided URLs.

    Parameters:
    - urls: list of strings, URLs of the videos to download

    Returns:
    None
    """
    for url in tqdm(urls, desc="Downloading Videos"):  # Wrap urls with tqdm for progress visualization
        try:
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()
            print(f"Downloading {yt.title}...")
            video.download()
            print("Download completed.")
        except Exception as e:
            print(f"Error downloading {url}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download YouTube videos from provided URLs.")
    parser.add_argument("--url", action="append",
                        help="URL of the YouTube video to download. Use --url multiple times to add more.")

    args = parser.parse_args()

    if not args.url:
        parser.print_help()
        exit(1)

    download_videos(args.url)
