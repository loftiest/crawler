#### 用法
  使用`crawl_photo.py`启动脚本，需要指定一些必须参数。

#### 脚本参数
  使用命令`python crawl_photo.py --help`或者`python crawl_photo.py -h`查看详细参数。
  ```
  options:
  -h, --help            查看脚本帮助
  -n NUMBER, --number NUMBER
                        期望获取到的图片数量，取决于是否有这么多图片。当图片数量足够，可能会多获取几张。
  -s START, --start START
                        从哪个位置开始获取图片
  -kw KEYWORDS, --keywords KEYWORDS 必填
                        图片的关键字。多个关键字使用加号或者空格隔开
  -c CAT, --cat CAT     图片分类: 
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
  -d DIRECTORY, --directory DIRECTORY 必填
                        图片保存的指定目录
  --overwrite OVERWRITE
                        是否清空目录。默认清空指定目录，设置False不清空目录

  ```