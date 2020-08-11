## 介绍
该项目可以识别本地图像上的文字是否违规  
## 环境
该项目基于 https://github.com/chineseocr/darknet-ocr ，需要开启这个项目的docker镜像服务  
## 展示
原图：<img src="https://github.com/yfq512/ImageReview-SensitiveWordDetection/blob/master/1.jpg" width="300" height="300" >
结果：<img src="https://github.com/yfq512/ImageReview-SensitiveWordDetection/blob/master/result.jpg" width="300" height="300" >
## 目录结构
.  
├── 1.jpg  
├── README.md  
├── __pycache__  
│   └── keywords_fit.cpython-37.pyc  
├── darknet-ocr.tar  
├── keywords.txt  
├── keywords_fit.py  
├── main.py  
└── result.jpg  
## 运行
开启docker镜像服务： docker run -it -p 8080:8080 darknet-ocr:1.0 python app.py  
运行： main.py  
## 说明
keywords.txt 内容不宜，需要自己组织数据，每行放一个敏感词汇  
