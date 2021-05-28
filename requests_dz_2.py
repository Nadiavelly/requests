import requests

class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, file_path):
        """Метод загруджает файл file_path на яндекс диск"""

        name = file_path.split('/')[-1]
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload?', params={'path': name}, headers={'Authorization': f'OAuth {self.token}'})
        href = response.json()['href']

        with open('c:/my_folder/text.txt', 'rb') as f:
            requests.put(href, files={'file' : f})

        return 201


if __name__ == '__main__':
    uploader = YaUploader(' ')
    result = uploader.upload('c:/my_folder/file.txt')
    print(str(result))
