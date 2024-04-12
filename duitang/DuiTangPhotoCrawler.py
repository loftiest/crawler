import os
import urllib.parse as up
import requests
import time
import logging
import shutil

class DuiTangPhotoCrawler:
    __logger = logging.getLogger("DuiTangPhotoCrawler")
    __headers = {
        "user-agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 78.0.3904.108Safari / 537.36",
        'Connection': 'close'
    }
    def __init__(self, **kwargs):
        self.quantity = kwargs['quantity']
        self.pause = float(kwargs['pause'])
        self.directory = kwargs['directory']
        self.pos = int(kwargs['pos'])
        self.overwrite = bool(kwargs['overwrite'])
        keywords = up.quote(self.__keywords_process(kwargs['keywords']))
        self.url = f"https://www.duitang.com/napi/blog/list/by_search/?include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&kw={keywords}&type={kwargs['cat']}&start="

    def __keywords_process(self, keywords: str) -> str:
        return str.replace(keywords, " ", "+")

    def __directory_process(self):
        if(self.directory[-1] != "/"):
            self.directory += "/"

        if not os.path.isdir(self.directory):
            os.mkdir(self.directory)
            return

        if self.overwrite:
            shutil.rmtree(self.directory)
            os.mkdir(self.directory)

    def start(self) -> bool:
        self.__logger.info("Crawler start.")
        self.__directory_process()

        while self.quantity > 0:
            url = self.url + str(self.pos)
            self.__logger.info(f"will request: {url}")
            response = requests.get(url, headers=self.__headers)
            if response.status_code != 200:
                self.__logger.error(f"request error, request content: {response.content}")
                return False
            photo_paths = self.__decode_data(response.json())
            if photo_paths == []:
                return True
            self.__download_photo(photo_paths)
            self.pos += 24
            self.quantity -= len(photo_paths)
            time.sleep(self.pause)
        self.__logger.info("Crawler stop.")
        return True


    def __decode_data(self, data) -> list[str]:
        object_list = data['data']['object_list']
        if(object_list == None or object_list == []):
            return []
        return [obj['photo']['path'] for obj in object_list]

    def __download_photo(self, photo_paths: list[str]) -> bool:
        for path in photo_paths:
            self.__logger.info(f"will download: {path}")
            response = requests.get(path, self.__headers)
            if response.status_code != 200:
                self.__logger.error(f"download error, request content: {response.content}")
            file_name = path.split("/")[-1]
            with open(self.directory + file_name, "wb") as file:
                file.write(response.content)
            self.__logger.info(f"Download: {path} Successfully!")
            time.sleep(self.pause)