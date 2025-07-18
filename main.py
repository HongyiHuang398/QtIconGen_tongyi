import subprocess
import sys
from configparser import ConfigParser
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets

import MainWindow
import os
from pathlib import Path
from PIL import Image
from io import BytesIO


class MyWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_config()
        self.load_config()

        self.lineEdit.editingFinished.connect(self.handle_editing_finished)
        self.pushButton.clicked.connect(self.send_request)
        self.pushButton_2.clicked.connect(self.open_color_selector)
        self.imagePreviewList.itemDoubleClicked.connect(self.open_image_selected)

    def open_image_selected(self):
        subprocess.run(['start',
                        self.imagePreviewList.selectedItems()[0].data(QtCore.Qt.ItemDataRole.UserRole)],
                       shell=True)

    def open_color_selector(self):
        color = QtWidgets.QColorDialog().getColor()
        self.label_4.setText(color.name())

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

        prompt = f"flat ios app icon for {self.lineEdit_2.text()} with {self.label_4.text()} color,"
        prompt_map = {
            "视觉风格": (" the visual style should be", QtWidgets.QCheckBox),
            "材质质感": (" the texture should be", QtWidgets.QCheckBox),
            "色彩": (" the color style should be", QtWidgets.QCheckBox),
            "边框形状": (" the border shape should be", QtWidgets.QRadioButton)
        }

        prompt_lines = []

        for groupbox in self.scrollArea.widget().children():
            if not isinstance(groupbox, QtWidgets.QGroupBox):
                continue

            title = groupbox.title()
            if title in prompt_map:
                prefix, widget_type = prompt_map[title]
                selected = [
                    box.text()
                    for box in groupbox.findChildren(widget_type)
                    if box.isChecked()
                ]

                if selected:
                    options = ", ".join(selected)
                    prompt_lines.append(f"{prefix} {options}")

        prompt += ";".join(prompt_lines)
        prompt += self.lineEdit_3.text()

        print(prompt)
        print('----已发送请求, 请等待----')
        try:
            thread = Thread(target=self.request_image,args=(prompt,))
            thread.start()
        except:
            print("错误，请输入正确的Api key!")

    def request_image(self,prompt):
        from http import HTTPStatus
        from urllib.parse import urlparse, unquote
        from pathlib import PurePosixPath
        import requests
        from dashscope import ImageSynthesis
        import os
        rsp = ImageSynthesis.call(api_key=self.lineEdit.text(),
                                  model=self.comboBox.currentText(),
                                  prompt=prompt,
                                  n=int(self.image_amount.text()),
                                  size=self.icon_size.currentText())
        print('response: %s' % rsp)
        if rsp.status_code == HTTPStatus.OK:
            output_dir = Path("outputs")
            output_dir.mkdir(exist_ok=True)
            counter = 1
            for result in rsp.output.results:
                print(f"\r当前进度[{counter}/{len(rsp.output.results)}]")
                file_name = Path(PurePosixPath(unquote(urlparse(result.url).path)).parts[-1]).stem
                file_name += self.image_format.currentText()
                with Image.open(BytesIO(requests.get(result.url).content)) as img:
                    img = img.convert("RGB")
                    img.save(output_dir / file_name, quality=100)
                item = QtWidgets.QListWidgetItem()
                item.setData(QtCore.Qt.ItemDataRole.UserRole, str(output_dir / file_name))
                item.setIcon(QtGui.QIcon(str(output_dir / file_name)))
                self.imagePreviewList.addItem(item)
                counter += 1
        else:
            print('sync_call Failed, status_code: %s, code: %s, message: %s' %
                  (rsp.status_code, rsp.code, rsp.message))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
