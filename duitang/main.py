# encoding: utf-8
import argparse
import DuiTangPhotoCrawler
import logging


argParser = argparse.ArgumentParser(
    description="default crawler doesn't stop, can use option -n set will get number")
argParser.add_argument("-n", "--number", type=int, help="will get photo number", default=-1)
argParser.add_argument("-s", "--start", type=int, help = "start position, same pos might get not same photo", default=0)
argParser.add_argument("-kw", "--keywords", type = str, help = "the keywords of photo", required=True)
argParser.add_argument("-c", "--cat", type = str, help = """
                        photo category:
                                        celebrity 爱豆 
                                        wallpaper 壁纸 
                                        avatar 头像 
                                        emoticon 表情 
                                        movie_music_books 影视 
                                        animation 动漫 
                                        gif 动图 
                                        material 素材 
                                        moe 萌宠 
                                        painting 绘画 
                                        diy 手工 
                                        fashion 穿搭 
                                        beauty 美妆 
                                        wedding 婚礼 
                                        food 美食 
                                        home 家居 
                                        travel 旅行 
                                        photography 摄影 
                                        plant 植物 
                                        tips 生活百科 
                                        art 人文艺术 
                                        design 设计 
                                        chinoiserie 古风
                                        """, default="feed")
argParser.add_argument("-d", "--directory", help = "will download photo to which file directory", required=True)
argParser.add_argument("--overwrite", help="default overwrite target directory", default=True)
args = argParser.parse_args()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    crawler = DuiTangPhotoCrawler.DuiTangPhotoCrawler(pause=0.2,
                                                      quantity=args.number,
                                                      keywords=args.keywords,
                                                      cat=args.cat,
                                                      directory=args.directory,
                                                      pos=args.start,
                                                      overwrite=args.overwrite)
    crawler.start()