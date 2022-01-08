import json
import requests
import sys


class AwsLinkGenerator:
    aws_links = []
    memories_data = []

    def __init__(self, path_to_json):
        self.path_to_json = path_to_json

    def load_json(self):
        with open(self.path_to_json) as f:
            self.memories_data = json.load(f)

    def get_file_type(self, file_url):
        url = file_url.split('?')[0]
        return url.split('.')[-1]

    def handle_link_generation(self):
        # define an array to hold real download links
        aws_url_list = []
        # iterate over snapchat json
        count = 1
        for memory in self.memories_data['Saved Media']:
            # send a post request to get AWS link
            response = requests.post(memory['Download Link'])
            url = response.content.decode('utf-8')
            # save the link to the array
            # we need: data, filetype, aws link
            aws_url_list.append({
                'date': memory['Date'][:len(memory['Date']) - 4],
                'fileType': self.get_file_type(url),
                'awsLink': url
            })
            sys.stdout.write(f'finished {count}\r')
            count += 1
        # write the aws url array to a different json file
        with open('aws_links.json', 'w') as output:
            json.dump(aws_url_list, output)


if __name__ == "__main__":
    link_generator = AwsLinkGenerator('./memories_history.json')
    link_generator.load_json()
    link_generator.handle_link_generation()
