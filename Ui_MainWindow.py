# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.icon_name = QLabel(self.centralwidget)
        self.icon_name.setObjectName(u"icon_name")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.icon_name)

        self.icon_name_lineEdit = QLineEdit(self.centralwidget)
        self.icon_name_lineEdit.setObjectName(u"icon_name_lineEdit")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.icon_name_lineEdit)

        self.icon_color_select = QLabel(self.centralwidget)
        self.icon_color_select.setObjectName(u"icon_color_select")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.icon_color_select)

        self.icon_color_select_pushButton = QPushButton(self.centralwidget)
        self.icon_color_select_pushButton.setObjectName(u"icon_color_select_pushButton")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.icon_color_select_pushButton)

        self.icon_amount = QLabel(self.centralwidget)
        self.icon_amount.setObjectName(u"icon_amount")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.icon_amount)

        self.icon_amount_lineEdit = QLineEdit(self.centralwidget)
        self.icon_amount_lineEdit.setObjectName(u"icon_amount_lineEdit")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.icon_amount_lineEdit)

        self.icon_size = QLabel(self.centralwidget)
        self.icon_size.setObjectName(u"icon_size")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.icon_size)

        self.icon_size_comboBox = QComboBox(self.centralwidget)
        self.icon_size_comboBox.addItem("")
        self.icon_size_comboBox.addItem("")
        self.icon_size_comboBox.addItem("")
        self.icon_size_comboBox.setObjectName(u"icon_size_comboBox")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.icon_size_comboBox)

        self.extra_prompts = QLabel(self.centralwidget)
        self.extra_prompts.setObjectName(u"extra_prompts")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.extra_prompts)

        self.extra_prompts_lineEdit = QLineEdit(self.centralwidget)
        self.extra_prompts_lineEdit.setObjectName(u"extra_prompts_lineEdit")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.extra_prompts_lineEdit)


        self.horizontalLayout_2.addLayout(self.formLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.language_select_groupBox = QGroupBox(self.centralwidget)
        self.language_select_groupBox.setObjectName(u"language_select_groupBox")
        self.horizontalLayout = QHBoxLayout(self.language_select_groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.en_US_radio_Button = QRadioButton(self.language_select_groupBox)
        self.en_US_radio_Button.setObjectName(u"en_US_radio_Button")
        self.en_US_radio_Button.setChecked(True)

        self.horizontalLayout.addWidget(self.en_US_radio_Button)

        self.zh_CN_radio_Button = QRadioButton(self.language_select_groupBox)
        self.zh_CN_radio_Button.setObjectName(u"zh_CN_radio_Button")

        self.horizontalLayout.addWidget(self.zh_CN_radio_Button)


        self.verticalLayout_3.addWidget(self.language_select_groupBox)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mode_text_to_image_radioButton = QRadioButton(self.groupBox)
        self.mode_text_to_image_radioButton.setObjectName(u"mode_text_to_image_radioButton")
        self.mode_text_to_image_radioButton.setChecked(True)

        self.verticalLayout.addWidget(self.mode_text_to_image_radioButton)

        self.mode_image_edit_radioButton = QRadioButton(self.groupBox)
        self.mode_image_edit_radioButton.setObjectName(u"mode_image_edit_radioButton")

        self.verticalLayout.addWidget(self.mode_image_edit_radioButton)


        self.verticalLayout_3.addWidget(self.groupBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.api_key = QLabel(self.centralwidget)
        self.api_key.setObjectName(u"api_key")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.api_key)

        self.api_key_lineEdit = QLineEdit(self.centralwidget)
        self.api_key_lineEdit.setObjectName(u"api_key_lineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.api_key_lineEdit)

        self.model_select = QLabel(self.centralwidget)
        self.model_select.setObjectName(u"model_select")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.model_select)

        self.model_select_comboBox = QComboBox(self.centralwidget)
        self.model_select_comboBox.addItem("")
        self.model_select_comboBox.addItem("")
        self.model_select_comboBox.addItem("")
        self.model_select_comboBox.setObjectName(u"model_select_comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_select_comboBox.sizePolicy().hasHeightForWidth())
        self.model_select_comboBox.setSizePolicy(sizePolicy)
        self.model_select_comboBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.model_select_comboBox)

        self.output_format = QLabel(self.centralwidget)
        self.output_format.setObjectName(u"output_format")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.output_format)

        self.output_format_comboBox = QComboBox(self.centralwidget)
        self.output_format_comboBox.addItem("")
        self.output_format_comboBox.addItem("")
        self.output_format_comboBox.setObjectName(u"output_format_comboBox")
        sizePolicy.setHeightForWidth(self.output_format_comboBox.sizePolicy().hasHeightForWidth())
        self.output_format_comboBox.setSizePolicy(sizePolicy)
        self.output_format_comboBox.setInsertPolicy(QComboBox.InsertPolicy.InsertAtBottom)
        self.output_format_comboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.output_format_comboBox)

        self.generate_image_pushButton = QPushButton(self.centralwidget)
        self.generate_image_pushButton.setObjectName(u"generate_image_pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.generate_image_pushButton.sizePolicy().hasHeightForWidth())
        self.generate_image_pushButton.setSizePolicy(sizePolicy1)
        self.generate_image_pushButton.setMaximumSize(QSize(16777215, 16777215))
        self.generate_image_pushButton.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.generate_image_pushButton)

        self.upload_image_pushButton = QPushButton(self.centralwidget)
        self.upload_image_pushButton.setObjectName(u"upload_image_pushButton")
        self.upload_image_pushButton.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.upload_image_pushButton)

        self.image_preview = QLabel(self.centralwidget)
        self.image_preview.setObjectName(u"image_preview")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.image_preview)


        self.horizontalLayout_2.addLayout(self.formLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Shadow.Sunken)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 782, 202))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.visual_style_groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.visual_style_groupBox.setObjectName(u"visual_style_groupBox")
        self.gridLayout = QGridLayout(self.visual_style_groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_24 = QCheckBox(self.visual_style_groupBox)
        self.checkBox_24.setObjectName(u"checkBox_24")

        self.gridLayout.addWidget(self.checkBox_24, 4, 1, 1, 1)

        self.checkBox_23 = QCheckBox(self.visual_style_groupBox)
        self.checkBox_23.setObjectName(u"checkBox_23")

        self.gridLayout.addWidget(self.checkBox_23, 4, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.visual_style_groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 1, 1, 1, 1)

        self.checkBox_6 = QCheckBox(self.visual_style_groupBox)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout.addWidget(self.checkBox_6, 2, 1, 1, 1)

        self.checkBox_7 = QCheckBox(self.visual_style_groupBox)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout.addWidget(self.checkBox_7, 0, 0, 1, 1)

        self.checkBox_22 = QCheckBox(self.visual_style_groupBox)
        self.checkBox_22.setObjectName(u"checkBox_22")

        self.gridLayout.addWidget(self.checkBox_22, 3, 1, 1, 1)

        self.checkBox_20 = QCheckBox(self.visual_style_groupBox)
        self.checkBox_20.setObjectName(u"checkBox_20")

        self.gridLayout.addWidget(self.checkBox_20, 3, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.visual_style_groupBox)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout.addWidget(self.checkBox_5, 2, 0, 1, 1)

        self.checkBox_8 = QCheckBox(self.visual_style_groupBox)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.gridLayout.addWidget(self.checkBox_8, 0, 1, 1, 1)

        self.checkBox = QCheckBox(self.visual_style_groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.visual_style_groupBox, 0, 0, 1, 1)

        self.hue_groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.hue_groupBox.setObjectName(u"hue_groupBox")
        self.hue_groupBox.setMaximumSize(QSize(250, 16777215))
        self.gridLayout_2 = QGridLayout(self.hue_groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_4 = QCheckBox(self.hue_groupBox)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_2.addWidget(self.checkBox_4, 0, 1, 1, 1)

        self.checkBox_10 = QCheckBox(self.hue_groupBox)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.gridLayout_2.addWidget(self.checkBox_10, 4, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.hue_groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_2.addWidget(self.checkBox_3, 4, 1, 1, 1)

        self.checkBox_9 = QCheckBox(self.hue_groupBox)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout_2.addWidget(self.checkBox_9, 1, 1, 1, 1)

        self.checkBox_11 = QCheckBox(self.hue_groupBox)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.gridLayout_2.addWidget(self.checkBox_11, 0, 0, 1, 1)

        self.checkBox_12 = QCheckBox(self.hue_groupBox)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.gridLayout_2.addWidget(self.checkBox_12, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.hue_groupBox, 0, 2, 1, 1)

        self.texture_groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.texture_groupBox.setObjectName(u"texture_groupBox")
        self.gridLayout_4 = QGridLayout(self.texture_groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.checkBox_17 = QCheckBox(self.texture_groupBox)
        self.checkBox_17.setObjectName(u"checkBox_17")

        self.gridLayout_4.addWidget(self.checkBox_17, 3, 0, 1, 1)

        self.checkBox_18 = QCheckBox(self.texture_groupBox)
        self.checkBox_18.setObjectName(u"checkBox_18")

        self.gridLayout_4.addWidget(self.checkBox_18, 3, 1, 1, 1)

        self.checkBox_14 = QCheckBox(self.texture_groupBox)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.gridLayout_4.addWidget(self.checkBox_14, 0, 0, 1, 1)

        self.checkBox_26 = QCheckBox(self.texture_groupBox)
        self.checkBox_26.setObjectName(u"checkBox_26")

        self.gridLayout_4.addWidget(self.checkBox_26, 5, 1, 1, 1)

        self.checkBox_21 = QCheckBox(self.texture_groupBox)
        self.checkBox_21.setObjectName(u"checkBox_21")

        self.gridLayout_4.addWidget(self.checkBox_21, 4, 1, 1, 1)

        self.checkBox_13 = QCheckBox(self.texture_groupBox)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.gridLayout_4.addWidget(self.checkBox_13, 0, 1, 1, 1)

        self.checkBox_19 = QCheckBox(self.texture_groupBox)
        self.checkBox_19.setObjectName(u"checkBox_19")

        self.gridLayout_4.addWidget(self.checkBox_19, 4, 0, 1, 1)

        self.checkBox_25 = QCheckBox(self.texture_groupBox)
        self.checkBox_25.setObjectName(u"checkBox_25")

        self.gridLayout_4.addWidget(self.checkBox_25, 5, 0, 1, 1)

        self.checkBox_16 = QCheckBox(self.texture_groupBox)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.gridLayout_4.addWidget(self.checkBox_16, 2, 1, 1, 1)

        self.checkBox_15 = QCheckBox(self.texture_groupBox)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.gridLayout_4.addWidget(self.checkBox_15, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.texture_groupBox, 0, 1, 1, 1)

        self.shape_groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.shape_groupBox.setObjectName(u"shape_groupBox")
        self.shape_groupBox.setMaximumSize(QSize(100, 16777215))
        self.gridLayout_5 = QGridLayout(self.shape_groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.radioButton_2 = QRadioButton(self.shape_groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setChecked(False)

        self.gridLayout_5.addWidget(self.radioButton_2, 1, 1, 1, 1)

        self.radioButton = QRadioButton(self.shape_groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_5.addWidget(self.radioButton, 2, 1, 1, 1)

        self.radioButton_3 = QRadioButton(self.shape_groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setChecked(True)

        self.gridLayout_5.addWidget(self.radioButton_3, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.shape_groupBox, 0, 3, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.imagePreviewList = QListWidget(self.centralwidget)
        self.imagePreviewList.setObjectName(u"imagePreviewList")
        self.imagePreviewList.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.imagePreviewList.setIconSize(QSize(192, 192))
        self.imagePreviewList.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.imagePreviewList.setFlow(QListView.Flow.LeftToRight)
        self.imagePreviewList.setResizeMode(QListView.ResizeMode.Adjust)

        self.verticalLayout_4.addWidget(self.imagePreviewList)

        self.verticalLayout_4.setStretch(0, 8)
        self.verticalLayout_4.setStretch(1, 12)
        self.verticalLayout_4.setStretch(2, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AI Icon Generator", None))
        self.icon_name.setText(QCoreApplication.translate("MainWindow", u"Subject", None))
        self.icon_color_select.setText(QCoreApplication.translate("MainWindow", u"#1e90ff", None))
        self.icon_color_select_pushButton.setText(QCoreApplication.translate("MainWindow", u"Open color selector", None))
        self.icon_amount.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.icon_amount_lineEdit.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.icon_size.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.icon_size_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"768*768", None))
        self.icon_size_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"1024*1024", None))
        self.icon_size_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"1440*1440", None))

        self.extra_prompts.setText(QCoreApplication.translate("MainWindow", u"Extra prompts", None))
        self.language_select_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Language Select", None))
        self.en_US_radio_Button.setText(QCoreApplication.translate("MainWindow", u"en", None))
        self.zh_CN_radio_Button.setText(QCoreApplication.translate("MainWindow", u"zh", None))
#if QT_CONFIG(tooltip)
        self.groupBox.setToolTip(QCoreApplication.translate("MainWindow", u"Some options will be disabled after this", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.mode_text_to_image_radioButton.setText(QCoreApplication.translate("MainWindow", u"text-to-image", None))
        self.mode_image_edit_radioButton.setText(QCoreApplication.translate("MainWindow", u"image-edit", None))
        self.api_key.setText(QCoreApplication.translate("MainWindow", u"api_key", None))
        self.model_select.setText(QCoreApplication.translate("MainWindow", u"Model select", None))
        self.model_select_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"wanx2.1-t2i-turbo", None))
        self.model_select_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"wanx2.1-t2i-plus", None))
        self.model_select_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"wanx2.0-t2i-turbo", None))

        self.output_format.setText(QCoreApplication.translate("MainWindow", u"Output format", None))
        self.output_format_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u".png", None))
        self.output_format_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u".jpg", None))

        self.generate_image_pushButton.setText(QCoreApplication.translate("MainWindow", u"Generate images", None))
        self.upload_image_pushButton.setText(QCoreApplication.translate("MainWindow", u"Upload image", None))
        self.image_preview.setText("")
        self.visual_style_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Visual style", None))
        self.checkBox_24.setText(QCoreApplication.translate("MainWindow", u"Low Poly", None))
        self.checkBox_23.setText(QCoreApplication.translate("MainWindow", u"Pixel", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Flat", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Blender", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"3D", None))
        self.checkBox_22.setText(QCoreApplication.translate("MainWindow", u"Abstract", None))
        self.checkBox_20.setText(QCoreApplication.translate("MainWindow", u"Modern", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Neon", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"2.5D", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Cute", None))
        self.hue_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Hue", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Gradient", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"Transparent", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Morandi", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"Soft", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"Fluorescent", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"Complementary", None))
        self.texture_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Texture", None))
        self.checkBox_17.setText(QCoreApplication.translate("MainWindow", u"Frosted Glass", None))
        self.checkBox_18.setText(QCoreApplication.translate("MainWindow", u"Acrylic", None))
        self.checkBox_14.setText(QCoreApplication.translate("MainWindow", u"Liquid Metal", None))
        self.checkBox_26.setText(QCoreApplication.translate("MainWindow", u"Aluminum", None))
        self.checkBox_21.setText(QCoreApplication.translate("MainWindow", u"Clay", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u"Metal", None))
        self.checkBox_19.setText(QCoreApplication.translate("MainWindow", u"Glass", None))
        self.checkBox_25.setText(QCoreApplication.translate("MainWindow", u"Paper Art", None))
        self.checkBox_16.setText(QCoreApplication.translate("MainWindow", u"Soft", None))
        self.checkBox_15.setText(QCoreApplication.translate("MainWindow", u"Stained Glass", None))
        self.shape_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Shape", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Circle", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Square", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Rounded", None))
    # retranslateUi

