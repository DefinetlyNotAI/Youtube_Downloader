import argparse
from pytube import YouTube
from tqdm import tqdm


def download_video(url, output_path):
    """
    Downloads a YouTube video from the given URL and saves it to the specified output path,
    displaying a progress bar and the video title.
    """
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    pbar = tqdm(total=video.filesize, unit='B', unit_scale=True, desc=f'Downloading {yt.title}')
    video.register_on_progress_callback(lambda event: pbar.update(event.bytes_read))
    video.download(output_path)
    pbar.close()
    print(f"{yt.title} downloaded successfully.")


def parse_arguments():
    """
    Parses command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Download YouTube videos.")
    parser.add_argument('--yt', nargs='+', required=True,
                        help='URL of the YouTube video to download. Use --yt multiple times to add more.')
    parser.add_argument('--to', default='./',
                        help='Directory path where the downloaded videos should be saved. Creates the directory if it doesn\'t exist. Defaults to current working directory.')

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
            print("Download completed.")
        except Exception as e:
            if e == "get_throttling_function_name: could not find match for multiple":
                print("Video could not be downloaded due to an error with the API of YouTube")
            else:
                print(f"Failed to download video: {e}")


if __name__ == "__main__":
    main()
