import subprocess
import sys
from configparser import ConfigParser
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTranslator

import MainWindow
from pathlib import Path
from PIL import Image
from io import BytesIO


class MyWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_component_properties()

        self.trans = None
        self.init_config()
        self.load_config()

        self.api_key_lineEdit.editingFinished.connect(self.handle_editing_finished)
        self.generate_image_pushButton.clicked.connect(self.send_request)
        self.icon_color_select_pushButton.clicked.connect(self.open_color_selector)
        self.imagePreviewList.itemDoubleClicked.connect(self.open_image_selected)

        self.en_US_radio_Button.clicked.connect(self.select_en_us)
        self.zh_CN_radio_Button.clicked.connect(self.select_zh_cn)

    def setup_component_properties(self):
        containers = [
            (self.visual_style_groupBox, "visual"),
            (self.hue_groupBox, "hue"),
            (self.texture_groupBox, "texture"),
            (self.shape_groupBox, "shape")
        ]

        for container, prefix in containers:
            children = container.findChildren((QtWidgets.QCheckBox, QtWidgets.QRadioButton))

            for child in children:

                prompt_key = child.text()

                child.setProperty("prompt_key", prompt_key)

    def select_en_us(self):
        if self.trans:
            QtWidgets.QApplication.removeTranslator(self.trans)
            self.trans = None
        self.retranslateUi(self)
        self.handle_editing_finished()

    def select_zh_cn(self):
        if self.trans:
            QtWidgets.QApplication.removeTranslator(self.trans)
            self.trans = None
        self.trans = QTranslator()
        if self.trans.load('zh_CN'):
            QtWidgets.QApplication.installTranslator(self.trans)
        self.retranslateUi(self)
        self.handle_editing_finished()

    def open_image_selected(self):
        subprocess.run(['start',
                        self.imagePreviewList.selectedItems()[0].data(QtCore.Qt.ItemDataRole.UserRole)],
                       shell=True)

    def open_color_selector(self):
        color = QtWidgets.QColorDialog().getColor()
        self.icon_color_select.setText(color.name())

    def handle_editing_finished(self):
        config = ConfigParser()
        config.read("config.ini", encoding='UTF-8')
        config['client']['api_key'] = self.api_key_lineEdit.text()
        config['client']['language'] = 'en_US' if self.en_US_radio_Button.isChecked() else 'zh_CN'
        fo = open("config.ini", 'w', encoding='UTF-8')
        config.write(fo)
        fo.close()
        print("保存成功")

    def load_config(self):
        config = ConfigParser()
        config.read('config.ini', encoding='UTF-8')
        self.api_key_lineEdit.setText(config['client']['api_key'])
        if config['client']['language'] == 'en_US':
            self.select_en_us()
        else:
            self.select_zh_cn()
            self.zh_CN_radio_Button.setChecked(True)

    def init_config(self):
        config = ConfigParser()
        config.read("config.ini", encoding='UTF-8')
        if not config.has_section('client'):
            config.add_section('client')
        client = config['client']
        if 'api_key' not in client:
            client['api_key'] = ""
        if 'language' not in client:
            client['language'] = "en_US"
        fo = open("config.ini", 'w', encoding='UTF-8')
        config.write(fo)
        fo.close()

    def send_request(self):
        prompt_parts = []

        prompt_parts.append(
            f"flat ios app icon for {self.icon_name_lineEdit.text()} with {self.icon_color_select.text()} color")

        containers = [
            self.visual_style_groupBox,
            self.hue_groupBox,
            self.texture_groupBox,
            self.shape_groupBox
        ]

        category_names = {
            self.visual_style_groupBox: "visual style",
            self.hue_groupBox: "color",
            self.texture_groupBox: "texture",
            self.shape_groupBox: "shape"
        }

        for container in containers:
            selected = []
            for child in container.findChildren((QtWidgets.QCheckBox, QtWidgets.QRadioButton)):
                if (isinstance(child, QtWidgets.QCheckBox) and child.isChecked()) or \
                        (isinstance(child, QtWidgets.QRadioButton) and child.isChecked()):
                    prompt_key = child.property("prompt_key")
                    if prompt_key:
                        selected.append(prompt_key)
            if len(selected) > 0:
                category = category_names.get(container, "feature")
                prompt_parts.append(f"{category}: {', '.join(selected)}")

        extra = self.extra_prompts_lineEdit.text().strip()
        if extra:
            prompt_parts.append(extra)

        prompt = ', '.join(prompt_parts)
        print("Original Prompt:", prompt)
        print('----Send request, please wait...----')
        try:
            thread = Thread(target=self.request_image, args=(prompt,))
            thread.start()
        except:
            print("Error, please enter the correct api key!")

    def request_image(self, prompt):
        from http import HTTPStatus
        from urllib.parse import urlparse, unquote
        from pathlib import PurePosixPath
        import requests
        from dashscope import ImageSynthesis
        rsp = ImageSynthesis.call(api_key=self.api_key_lineEdit.text(),
                                  model=self.model_select_comboBox.currentText(),
                                  prompt=prompt,
                                  n=int(self.icon_amount_lineEdit.text()),
                                  size=self.icon_size_comboBox.currentText())
        print('response: %s' % rsp)
        if rsp.status_code == HTTPStatus.OK:
            output_dir = Path("outputs")
            output_dir.mkdir(exist_ok=True)
            counter = 1
            for result in rsp.output.results:
                print(f"\rProcess[{counter}/{len(rsp.output.results)}]",end="")
                file_name = Path(PurePosixPath(unquote(urlparse(result.url).path)).parts[-1]).stem
                file_name += self.output_format_comboBox.currentText()
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
