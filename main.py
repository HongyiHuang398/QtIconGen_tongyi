import logging
import sys
import time
from io import BytesIO
from pathlib import Path
from threading import Thread

from PIL import Image
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from dashscope import ImageSynthesis

import Ui_MainWindow
from Utility import *


class MyWindow(QMainWindow, Ui_MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_component_properties()

        self.image_path = QUrl()
        self.trans = None
        self.load_config()

        self.api_key_lineEdit.editingFinished.connect(self.handle_editing_finished)
        self.generate_image_pushButton.clicked.connect(self.send_request)
        self.icon_color_select_pushButton.clicked.connect(self.open_color_selector)
        self.imagePreviewList.itemDoubleClicked.connect(self.open_image_selected)
        self.upload_image_pushButton.clicked.connect(self.upload_image)

        self.en_US_radio_Button.clicked.connect(self.select_en_us)
        self.zh_CN_radio_Button.clicked.connect(self.select_zh_cn)

        self.mode_text_to_image_radioButton.clicked.connect(lambda: (self.upload_image_pushButton.setEnabled(False),
                                                                     self.image_preview.setPixmap(QPixmap())))
        self.mode_image_edit_radioButton.clicked.connect(lambda: self.upload_image_pushButton.setEnabled(True))

    def auto_add_themes(self):
        keys = QStyleFactory.keys()
        for theme in keys:
            action = QAction(theme, self)
            self.menu.addAction(action)
            action.triggered.connect(
                lambda checked, t=theme: (QApplication.instance().setStyle(QStyleFactory.create(t)),
                                          self.handle_editing_finished()))

    def upload_image(self):
        url, _ = QFileDialog.getOpenFileUrl(self,
                                            filter="Image files (*.jpg *.png);;")
        pixmap = QPixmap(QImage(url.toLocalFile())).scaled(QSize(32, 32), Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.image_preview.setPixmap(pixmap)
        self.image_path = url

    def setup_component_properties(self):
        containers = [
            (self.visual_style_groupBox, "visual"),
            (self.hue_groupBox, "hue"),
            (self.texture_groupBox, "texture"),
            (self.shape_groupBox, "shape")
        ]

        for container, prefix in containers:
            children = container.findChildren(QCheckBox) + container.findChildren(QRadioButton)

            for child in children:
                prompt_key = child.text()

                child.setProperty("prompt_key", prompt_key)

    def select_en_us(self):
        if self.trans:
            app.removeTranslator(self.trans)
            self.trans = None
        self.retranslateUi(self)

    def select_zh_cn(self):
        if self.trans:
            app.removeTranslator(self.trans)
            self.trans = None
        self.trans = QTranslator()
        if self.trans.load(get_embed_data("resources/lang/zh_CN.qm")):
            app.installTranslator(self.trans)
        self.retranslateUi(self)

    def open_image_selected(self):
        selected_items = self.imagePreviewList.selectedItems()
        if selected_items:
            file_path = selected_items[0].data(Qt.ItemDataRole.UserRole)
            QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))

    def open_color_selector(self):
        color = QColorDialog().getColor()
        self.icon_color_select.setText(color.name())

    def handle_editing_finished(self):
        configIni.setValue("client/api_key", self.api_key_lineEdit.text())
        lang = 'en_US' if self.en_US_radio_Button.isChecked() else 'zh_CN'
        configIni.setValue("client/lang", lang)
        configIni.setValue("client/theme", QApplication.instance().style().name())
        configIni.sync()
        logging.info("Saved successfully")

    def load_config(self):
        self.api_key_lineEdit.setText(configIni.value("client/api_key"))
        if configIni.value("client/lang") == 'en_US':
            self.select_en_us()
        else:
            self.select_zh_cn()
            self.zh_CN_radio_Button.setChecked(True)
        QApplication.instance().setStyle(configIni.value("client/theme"))

    def send_request(self):
        prompt_parts = [
            f"flat ios app icon for {self.icon_name_lineEdit.text()} with {self.icon_color_select.text()} color"]

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
            for child in (container.findChildren(QCheckBox) + container.findChildren(QRadioButton)):
                if (isinstance(child, QCheckBox) and child.isChecked()) or \
                        (isinstance(child, QRadioButton) and child.isChecked()):
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
        logging.info(f"Original Prompt: {prompt}")
        logging.info('----Send request, please wait...----')
        self.statusbar.showMessage(self.tr("Request sent, please wait..."), 5000)

        try:
            self.request_image(prompt)
        except Exception as e:
            logging.error(e)

    def request_image(self, prompt):
        if self.mode_text_to_image_radioButton.isChecked():
            thread = Thread(target=self.request_text_to_image, args=(prompt,))
            thread.start()
        else:
            if QUrl.isValid(self.image_path):
                thread = Thread(target=self.request_image_edit, args=(prompt,))
                thread.start()
            else:
                self.statusbar.showMessage(self.tr("Request failed, image not found"), 5000)
                QMessageBox.warning(self, self.tr("Image not found"),
                                    self.tr("Cannot find the image, please make sure the path is correct."))

    def request_text_to_image(self, prompt):
        rsp = ImageSynthesis.call(api_key=self.api_key_lineEdit.text(),
                                  model=self.model_select_comboBox.currentText(),
                                  prompt=prompt,
                                  n=int(self.icon_amount_lineEdit.text()),
                                  size=self.icon_size_comboBox.currentText())
        self.process_rsp(rsp)

    def request_image_edit(self, prompt):
        rsp = ImageSynthesis.call(api_key=self.api_key_lineEdit.text(),
                                  model="wanx2.1-imageedit",
                                  function="description_edit",
                                  prompt=prompt,
                                  base_image_url=self.image_path.toLocalFile(),
                                  n=int(self.icon_amount_lineEdit.text()))
        self.process_rsp(rsp)

    def process_rsp(self, rsp):
        from http import HTTPStatus
        from urllib.parse import urlparse, unquote
        from pathlib import PurePosixPath
        import requests
        print('response: %s' % rsp)
        logging.info(f"Status: {rsp["output"]["task_status"]}")
        if rsp["output"]["task_status"] == "SUCCEEDED":
            self.statusbar.showMessage(self.tr("Request Successfully, downloading...")
                                       , 5000)
        for item in rsp["output"]["results"]:
            if "actual_prompt" in item:
                logging.info(f"Actual Prompt: {item["actual_prompt"]}")
        if rsp.status_code == HTTPStatus.OK:
            output_dir = Path("outputs")
            output_dir.mkdir(exist_ok=True)
            counter = 1
            for result in rsp.output.results:
                logging.info(f"Process[{counter}/{len(rsp.output.results)}]")
                self.statusbar.showMessage(self.tr("Downloaded") + f" {counter}/{len(rsp.output.results)}",
                                           5000)
                file_name = Path(PurePosixPath(unquote(urlparse(result.url).path)).parts[-1]).stem
                file_name += self.output_format_comboBox.currentText()
                with Image.open(BytesIO(requests.get(result.url).content)) as img:
                    img = img.convert("RGB")
                    img.save(output_dir / file_name, quality=100)
                item = QListWidgetItem()
                item.setData(Qt.ItemDataRole.UserRole, str(output_dir / file_name))
                item.setIcon(QIcon(str(output_dir / file_name)))
                self.imagePreviewList.addItem(item)
                counter += 1
        else:
            logging.error(f'sync_call Failed, status_code: {rsp.status_code}, code: {rsp.code}, message: {rsp.message}')


def init_config():
    if not configIni.contains("client/api_key"):
        configIni.setValue("client/api_key", "")
    if not configIni.contains("client/lang"):
        configIni.setValue("client/lang", "en_US")
    configIni.sync()


if __name__ == "__main__":
    log_folder = Path("logs")
    log_folder.mkdir(exist_ok=True)
    console_handler = logging.StreamHandler(stream=sys.stdout)
    file_handler = logging.FileHandler(log_folder / f"{time.time()}.log")
    logging.basicConfig(level=logging.INFO,handlers=[console_handler,file_handler],encoding="utf-8")
    configIni = QSettings("config.ini", QSettings.Format.IniFormat)
    init_config()
    app = QApplication(sys.argv)
    window = MyWindow()
    window.auto_add_themes()
    window.show()
    sys.exit(app.exec())
