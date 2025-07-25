# AI Icon Generator based on PyQt

It's an AI icon generator which uses api keys from aliyun.
You can use the newest text-to-image models by using this program easily
without typing in most of common prompts.
The api keys can be gotten from
[Aliyun Bailian](https://bailian.console.aliyun.com/?tab=model#/api-key)

## How to compile the project?

Install python modules first

~~~shell
pip install -r requirements.txt
~~~

Personally, I use nuitka to package the project.


Run this command in your shell

~~~shell
nuitka --lto=yes --windows-console-mode=disable --standalone --enable-plugin=pyqt5 --remove-output --follow-imports --output-dir=build/ --include-data-files=./zh_CN.qm=./zh_CN.qm .\main.py
~~~

**Done!**

# Image Preview
English
![The image of the program](assets/img.png)

Chinese
![The image of the program(Chinese Version)](assets/img_1.png)


## Outer links
[Github](https://github.com/HongyiHuang398/QtIconGen_tongyi)