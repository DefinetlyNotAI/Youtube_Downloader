# Youtube_Downloader 📎

Welcome to `Youtube_Downloader` 🌐,
Crafted with python 🐍, by DefinetlyNotAI.
This comprehensive guide is here to equip you with everything you need to use `Youtube_Downloader` effectively.

<div align="center">
    <a href="https://github.com/DefinetlyNotAI/Youtube_Downloader/issues"><img src="https://img.shields.io/github/issues/DefinetlyNotAI/Youtube_Downloader" alt="GitHub Issues"></a>
    <a href="https://github.com/DefinetlyNotAI/Youtube_Downloader/tags"><img src="https://img.shields.io/github/v/tag/DefinetlyNotAI/Youtube_Downloader" alt="GitHub Tag"></a>
    <a href="https://github.com/DefinetlyNotAI/Youtube_Downloader/graphs/commit-activity"><img src="https://img.shields.io/github/commit-activity/t/DefinetlyNotAI/Youtube_Downloader" alt="GitHub Commit Activity"></a>
    <a href="https://github.com/DefinetlyNotAI/Youtube_Downloader/languages"><img src="https://img.shields.io/github/languages/count/DefinetlyNotAI/Youtube_Downloader" alt="GitHub Language Count"></a>
    <a href="https://github.com/DefinetlyNotAI/Youtube_Downloader/actions"><img src="https://img.shields.io/github/check-runs/DefinetlyNotAI/Youtube_Downloader/main" alt="GitHub Branch Check Runs"></a>
    <a href="https://github.com/DefinetlyNotAI/Youtube_Downloader"><img src="https://img.shields.io/github/repo-size/DefinetlyNotAI/Youtube_Downloader" alt="GitHub Repo Size"></a>
</div>

# YouTube_Downloader

The `Youtube_Downloader` is a Python class designed to download great quality YouTube videos,
with the ability to download multiple videos at once.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.8 or later.
- You have installed the required Python packages from the [requirements.txt](requirements.txt) file.
- You have a working internet connection.

## Installation

If you plan to modify or extend the functionality of the `Youtube_Downloader`, clone the repository and install the required packages locally.

```bash
git clone https://github.com/DefinetlyNotAI/Youtube_Downloader.git
cd Youtube_Downloader
pip install -r requirements.txt
```

## Usage

To use the `Youtube_Downloader` class, simply instantiate it with the desired URL and download the video.
You may use as many `--url` arguments as you want, you will see the name of the video downloading.

```bash
python download.py --url "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```
or
```bash
python download.py --url "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --yt "https://www.youtube.com/watch?v=3JZ_D3ELwOQ"
```

You may also use a txt file as well as decide where to save the videos.

```bash
python download.py --from-txt C:\DIRECTORY\WITH\THE\TXT\FILE.txt --to C:\Downloads
```

If the `--to` flags directory doesn't exist it will create one for you!

An example of the txt file could be;
```txt
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://www.youtube.com/watch?v=3tmd-ClpJxA
```

Videos maintain the name's of the author and title of the video.

### Video Resolution

640 x 360 at 25 frames per second is the usual resolution that the videos are downloaded.

## Contributing

Contributions are what make the open-source community such an amazing place to learn,
inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

But don't hesitate to [open an Issue](https://github.com/DefinetlyNotAI/Youtube_Downloader/issues) 
if you have any questions or encounter any issues.

Most importantly, **don't forget to follow us!** and read our [Contributing Guide](CONTRIBUTING.md).

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## Contact

Shahm Najeeb - Nirt_12023@outlook.com

Project Link: [https://github.com/DefinetlyNotAI/Youtube_Downloader](https://github.com/DefinetlyNotAI/Youtube_Downloader)
