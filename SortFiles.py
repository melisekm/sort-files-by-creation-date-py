import os
from datetime import datetime

extensions = [".jpg", ".mp4", ".png"]


def get_extension(name):
    _, file_extension = os.path.splitext(name)
    return file_extension


def run():
    with os.scandir() as dir_entries:
        os.mkdir(".\\Sorted")
        for entry in dir_entries:
            extension = get_extension(entry.name)
            if extension.casefold() in extensions:
                creation_time = entry.stat().st_mtime
                try:
                    directory_name = ".\\Sorted\\" + datetime.utcfromtimestamp(creation_time).strftime(
                        "%Y-%m-%d"
                    )
                    os.mkdir(directory_name)
                except OSError:
                    pass
                finally:
                    file_name = directory_name + "\\" + entry.name
                    os.replace(entry.path, file_name)


if __name__ == "__main__":
    run()