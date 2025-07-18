import sys
from configparser import ConfigParser

from PyQt5 import QtCore, QtGui, QtWidgets

import MainWindow


class MyWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_config()
        self.load_config()

        self.lineEdit.editingFinished.connect(self.handle_editing_finished)
        self.pushButton.clicked.connect(self.send_request)

    def handle_editing_finished(self):
        config = ConfigParser()
        config.read("config.ini", encoding='UTF-8')
        config['client']['api_key'] = self.lineEdit.text()
        fo = open("config.ini", 'w', encoding='UTF-8')
        config.write(fo)
        fo.close()
        print("保存成功")

    def load_config(self):
        config = ConfigParser()
        config.read('config.ini', encoding='UTF-8')
        self.lineEdit.setText(config['client']['api_key'])

    def init_config(self):
        config = ConfigParser()
        config.read("config.ini", encoding='UTF-8')
        if not config.has_section('client'):
            config.add_section('client')
        client = config['client']
        if 'api_key' not in client:
            client['api_key'] = ""
        fo = open("config.ini", 'w', encoding='UTF-8')
        config.write(fo)
        fo.close()

    def send_request(self):
        from http import HTTPStatus
        from urllib.parse import urlparse, unquote
        from pathlib import PurePosixPath
        import requests
        from dashscope import ImageSynthesis
        import os

        prompt = f"flat ios app icon for {self.lineEdit_2.text()} with {self.comboBox_2.currentText()} style, {self.lineEdit_3.text()}"
        print(prompt)
        print('----已发送请求, 请等待----')
        try:
            rsp = ImageSynthesis.call(api_key=self.lineEdit.text(),
                                      model=self.comboBox.currentText(),
                                      prompt=prompt,
                                      n=int(self.image_amount.text()),
                                      size=self.icon_size.currentText())
            print('response: %s' % rsp)
            if rsp.status_code == HTTPStatus.OK:
                # 在当前目录下保存图片
                counter = 1
                for result in rsp.output.results:
                    print(f"\r当前进度[{counter}/{len(rsp.output.results)}]")
                    file_name = PurePosixPath(unquote(urlparse(result.url).path)).parts[-1]
                    with open('./outputs/%s' % file_name, 'wb+') as f:
                        f.write(requests.get(result.url).content)
                    counter += 1
            else:
                print('sync_call Failed, status_code: %s, code: %s, message: %s' %
                      (rsp.status_code, rsp.code, rsp.message))
        except:
            print("错误，请输入正确的Api key!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
