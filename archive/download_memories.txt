import json
import os
from os import path
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait


class MemoriesDownloader:
    def __init__(self, path_to_json, download_location, thread_count=3):
        self.path_to_json = path_to_json
        self.download_location = download_location
        self.thread_count = thread_count
        self.split_memories = []
        self.json_data = []

    def split_into_n_parts(self, lst, n):
        """ Yield successive n-sized chunks from lst. """
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    def load_json(self):
        # for the number of threads we have, split the memories json
        # into equal parts
        with open(self.path_to_json) as f:
            self.json_data = json.load(f)
        self.split_memories = list(self.split_into_n_parts(self.json_data,
                                                           self.thread_count))

    # this is going to be used by each thread
    def handle_download(self, memories_list):
        for memory in memories_list:
            # get the full path to the memory we are about to save
            # e.g. /path/to/memory/2020-08-16,19:12:45.mp4
            file_name = ','.join(memory['date'].split(' '))
            file_name += '.' + memory['fileType']
            file_path = path.join(self.download_location, file_name)
            print('downloading', file_name)
            url = memory['awsLink']
            response = requests.get(url)
            print(file_path)
            with open(file_path, 'wb') as f:
                # download the memory to the location specified
                f.write(response.content)
            print('finished', file_path)

    # create threads and run them
    def download_memories(self):
        # create ten threads for
        executor = ThreadPoolExecutor(self.thread_count)
        # have each thread go about downloading its share of memories
        futures = [executor.submit(self.handle_download, memories)
                   for memories in self.split_memories]


if __name__ == "__main__":
    path_to_json = './aws_links.json'
    path_to_memories = './memories'
    memories_downloader = MemoriesDownloader(path_to_json, path_to_memories)
    memories_downloader.load_json()
    memories_downloader.download_memories()
