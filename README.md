# sanic相关
https://github.com/huge-success/sanic

https://sanic-for-pythoneer.readthedocs.io/en/latest/index.html

## 部署

https://sanic.readthedocs.io/en/latest/sanic/deploying.html

https://sanic-for-pythoneer.readthedocs.io/en/latest/docs/part1/8.%E6%B5%8B%E8%AF%95%E4%B8%8E%E9%83%A8%E7%BD%B2.html#id5


### python命令行方式
python -m sanic server.app --host=0.0.0.0 --port=5005 --workers=4

### gunicorn方式
https://www.cnblogs.com/cwp-bg/p/8780204.html

gunicorn  -c config/gunicorn.py run:views.server --worker-class sanic.worker.GunicornWorker

run是启动的文件名
view.server是app的名字
# rasa相关
https://rasa.com/docs/
# fasttext相关
https://github.com/facebookresearch/fastText