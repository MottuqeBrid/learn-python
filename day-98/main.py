# multiProcessing in python
import multiprocessing
import time
import requests


def download_file(url, name):
    print(f"Downloading {name}...")
    respose = requests.get(url)
    open(f"day-98/images/{name}.jpg", "wb").write(respose.content)
    print(f"Downloaded {name}")


if __name__ == "__main__":
    url = "https://picsum.photos/200/300"
    pros = []

    for i in range(50):
        # download_file(url, f"image-{i+1}")
        p = multiprocessing.Process(target=download_file, args=[url, f"image-{i+1}"])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()
