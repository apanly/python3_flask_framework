# Flask参考文档
* http://www.pythondoc.com/flask/index.html
* https://flask-login.readthedocs.io/en/latest/#how-it-works
* [flask-debugtoolbar](http://www.pythondoc.com/flask-debugtoolbar/)
* [sqlacodegen](https://blog.csdn.net/fungleo/article/details/78865921)
    * sqlacodegen 'mysql://root:@127.0.0.1/pi3Robot' > common/models/model.py
    * sqlacodegen 'mysql://root:@127.0.0.1/pi3Robot' --tables user > common/models/User.py
* [flask-sqlacodegen](https://github.com/ksindi/flask-sqlacodegen)
    * flask-sqlacodegen 'mysql://root:@127.0.0.1/pi3Robot' --outfile "common/models/birth/__init__.py"  --flask
    * flask-sqlacodegen 'mysql://root:@127.0.0.1/pi3Robot' --tables birth --outfile "common/models/birth/__init__.py"  --flask