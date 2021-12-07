import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication

from src.ui.mpl_sorting_widget import MplSortingWidget


# Colors


class MainSortingWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize widgets.
        self.color_primary = None
        self.color_primary_dark = None
        self.color_secondary = None
        self.color_text = None
        self.color_widget_background = None
        self.color_text_button = None
        self.color_button_background = None
        self.color_border = None
        self.color_button_background_hover = None
        self.color_text_button_hover = None
        self.color_slider = None

        self.mpl_sorting_widget = None
        self.dial_sort_array_length = None

        self.frame_line = None
        self.frame_line_2 = None

        self.label = None
        self.label_2 = None
        self.label_3 = None
        self.label_array_range = None
        self.label_seed_array = None
        self.label_multiplier = None
        self.label_array_range_2 = None

        self.pushButton_return_main_menu = None
        self.pushButton_create_array = None
        self.pushButton_manuel_array = None
        self.pushButton_random_array = None
        self.pushButton_clear = None
        self.pushButton_radix_sort = None
        self.pushButton_counting_sort = None
        self.pushButton_quick_sort = None
        self.pushButton_heap_sort = None
        self.pushButton_bubble_sort = None
        self.pushButton_insertion_sort = None
        self.pushButton_merge_sort = None

        self.dial_animation_speed = None
        self.horizontalSlider_multiplier = None

        self.lineEdit_array_length = None
        self.lineEdit_multiplier = None
        self.lineEdit_upper_range = None

        self.lineEdit_lower_range = None

        self.checkBox_unique_array = None
        self.checkBox_unique_array_2 = None
        self.spinBox_seed = None

        self.icon1 = None
        self.icon2 = None
        self.icon3 = None
        self.icon4 = None
        self.icon5 = None

        self.action_xlsx = None
        self.action_csv = None
        self.action_txt = None
        self.actionCsv_File = None
        self.actionText_File = None
        self.actionExcel_File = None

        self.menu_import = None
        self.menu_file = None
        self.menu_save = None
        self.menuBar = None

        # Setup widget properties.
        self.setupUi()

    def setupUi(self):
        self.set_colors()
        self.__set_main_window()
        self.__set_sorting_container()
        self.__set_dials()
        self.__set_frames()
        self.__set_labels()
        self.__set_buttons()
        self.__set_sliders()
        self.__set_line_edits()
        self.__set_check_boxes()
        self.__set_spin_boxes()
        self.__set_menu()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainMainSortingWindowWindow_SortingWindow", "Sorting Methods"))
        self.label.setText(_translate("MainSortingWindow", "Sorting Methods"))
        self.pushButton_create_array.setToolTip(
            _translate("MainSortingWindow", "Create array with above parameters"))
        self.pushButton_create_array.setText(_translate("MainSortingWindow", "Create Array"))
        self.label_2.setText(_translate("MainSortingWindow", "Array\'s Length"))
        self.pushButton_clear.setToolTip(_translate("MainSortingWindow", "Clear the fields"))
        self.pushButton_clear.setText(_translate("MainSortingWindow", "Clear"))
        self.pushButton_merge_sort.setToolTip(_translate("MainSortingWindow", "Sort with Merge Sort"))
        self.pushButton_merge_sort.setText(_translate("MainSortingWindow", "Merge Sort"))
        self.pushButton_insertion_sort.setToolTip(_translate("MainSortingWindow", "Sort with Insertion Sort"))
        self.pushButton_insertion_sort.setText(_translate("MainSortingWindow", "Insertion Sort"))
        self.pushButton_bubble_sort.setToolTip(_translate("MainSortingWindow", "Sort with Bubble Sort"))
        self.pushButton_bubble_sort.setText(_translate("MainSortingWindow", "Bubble Sort"))
        self.label_3.setText(_translate("MainSortingWindow", " Speed"))
        self.pushButton_heap_sort.setToolTip(_translate("MainSortingWindow", "Sort with Heap Sort"))
        self.pushButton_heap_sort.setText(_translate("MainSortingWindow", "Heap Sort"))
        self.pushButton_quick_sort.setToolTip(_translate("MainSortingWindow", "Sort with Quick Sort"))
        self.pushButton_quick_sort.setText(_translate("MainSortingWindow", "Quick Sort"))
        self.pushButton_radix_sort.setToolTip(_translate("MainSortingWindow", "Sort with Radix Sort"))
        self.pushButton_radix_sort.setText(_translate("MainSortingWindow", "Radix Sort"))
        self.pushButton_counting_sort.setToolTip(_translate("MainSortingWindow", "Sort with Counting Sort"))
        self.pushButton_counting_sort.setText(_translate("MainSortingWindow", "Counting Sort"))
        self.pushButton_manuel_array.setToolTip(_translate("MainSortingWindow", "Enter your own array"))
        self.pushButton_manuel_array.setText(_translate("MainSortingWindow", "Enter Array by Hand"))
        self.pushButton_random_array.setToolTip(
            _translate("MainSortingWindow", "Create array with above parameters"))
        self.pushButton_random_array.setText(_translate("MainSortingWindow", "Default Array"))
        self.checkBox_unique_array.setToolTip(_translate("MainSortingWindow", "Non repeating numbers."))
        self.checkBox_unique_array.setText(_translate("MainSortingWindow", "Unique Array"))
        self.checkBox_unique_array_2.setToolTip(
            _translate("MainWindow_SortingWindow", "Constant array for every parameters."))
        self.checkBox_unique_array_2.setText(_translate("MainWindow_SortingWindow", "Seed Array"))
        self.pushButton_return_main_menu.setToolTip(_translate("MainSortingWindow", "Back to Home Window"))
        self.label_array_range.setText(_translate("MainSortingWindow", "Lower Range"))
        self.lineEdit_lower_range.setToolTip(_translate("MainSortingWindow", "Enter lower bound."))
        self.label_array_range_2.setText(_translate("MainSortingWindow", "Upper Range"))
        self.lineEdit_upper_range.setToolTip(_translate("MainSortingWindow", "Enter upper bound."))
        self.label_seed_array.setText(_translate("MainSortingWindow", "Seed Number "))
        self.label_multiplier.setText(_translate("MainSortingWindow", "Array\'s Length Multiplier"))
        self.menu_file.setTitle(_translate("MainSortingWindow", "File"))
        self.menu_save.setTitle(_translate("MainSortingWindow", "Save File"))
        self.menu_import.setTitle(_translate("MainSortingWindow", "Import File"))
        self.action_txt.setText(_translate("MainSortingWindow", "Txt File"))
        self.action_xlsx.setText(_translate("MainSortingWindow", "Xlsx File"))
        self.action_csv.setText(_translate("MainSortingWindow", "Csv File"))
        self.actionText_File.setText(_translate("MainSortingWindow", "Text File"))
        self.actionExcel_File.setText(_translate("MainSortingWindow", "Excel File"))
        self.actionCsv_File.setText(_translate("MainSortingWindow", "Csv File"))

    def set_colors(self):
        self.color_primary = "rgb(240, 240, 240)"
        self.color_primary_dark = "rgb(100, 100, 100)"
        self.color_secondary = "rgb(50, 50, 50)"

        self.color_text = self.color_secondary
        self.color_widget_background = self.color_primary
        self.color_text_button = self.color_primary
        self.color_button_background = self.color_primary_dark
        self.color_text_button_hover = self.color_secondary
        self.color_button_background_hover = self.color_primary
        self.color_border = self.color_primary_dark
        self.color_slider = self.color_primary_dark

    def __set_main_window(self):
        self.setObjectName("MainSortingWindow")
        self.resize(1250, 825)
        self.setMinimumSize(QtCore.QSize(1250, 499))
        self.setMaximumSize(QtCore.QSize(1250, 825))
        self.setStyleSheet("#MainSortingWindow{\n"
                           "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, "
                           "stop:0.158845 rgba(200, 200, 200, 255), stop:1 rgba( "
                           "240, 240, 240, 255));}")

    def __set_sorting_container(self):
        self.mpl_sorting_widget = MplSortingWidget(self)
        self.mpl_sorting_widget.setGeometry(QtCore.QRect(230, 70, 901, 491))
        self.mpl_sorting_widget.setStyleSheet("background-color: " + self.color_widget_background + ";")
        self.mpl_sorting_widget.setObjectName("mpl_sorting_widget")
        self.mpl_sorting_widget.raise_()

    def __set_frames(self):
        self.frame_line = QtWidgets.QFrame(self)
        self.frame_line.setGeometry(QtCore.QRect(180, 600, 20, 111))
        self.frame_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_line.setObjectName("frame_line")
        self.frame_line.raise_()

        self.frame_line_2 = QtWidgets.QFrame(self)
        self.frame_line_2.setGeometry(QtCore.QRect(1060, 600, 20, 111))
        self.frame_line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_line_2.setObjectName("frame_line_2")
        self.frame_line_2.raise_()

    def __set_labels(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setGeometry(QtCore.QRect(520, 10, 271, 41))
        self.label.setStyleSheet("color: " + self.color_text + ";\n"
                                 "\n"
                                 "font: 24pt \"MV Boli\";\n"
                                 "border-radius:20px\n"
                                 "")
        self.label.raise_()

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QtCore.QRect(140, 140, 101, 31))
        self.label_2.setStyleSheet("#label_2{\n"
                                   "color: " + self.color_text + ";\n"
                                   "font: 10pt \\\"MV Boli\\\";\n"
                                   "\n"
                                   "}")
        self.label_2.raise_()

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QtCore.QRect(1110, 640, 71, 21))
        self.label_3.setStyleSheet("#label_3{\n"
                                   "color: " + self.color_text + ";\n"
                                   "font: 12pt \\\"MV Boli\\\";\n"
                                   "\n"
                                   "}\n"
                                   "")
        self.label_3.raise_()

        self.label_array_range = QtWidgets.QLabel(self)
        self.label_array_range.setAlignment(QtCore.Qt.AlignCenter)
        self.label_array_range.setObjectName("label_array_range")
        self.label_array_range.setGeometry(QtCore.QRect(80, 260, 91, 41))
        self.label_array_range.setStyleSheet("color: " + self.color_text + ";\n"
                                             "font: 11pt \\\"MV Boli\\\";")
        self.label_array_range.raise_()

        self.label_array_range_2 = QtWidgets.QLabel(self)
        self.label_array_range_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_array_range_2.setObjectName("label_array_range_2")
        self.label_array_range_2.setGeometry(QtCore.QRect(210, 260, 91, 41))
        self.label_array_range_2.setStyleSheet("color: " + self.color_text + ";\n"
                                               "font: 11pt \\\"MV Boli\\\";")
        self.label_array_range_2.raise_()

        self.label_seed_array = QtWidgets.QLabel(self)
        self.label_seed_array.setAlignment(QtCore.Qt.AlignCenter)
        self.label_seed_array.setObjectName("label_seed_array")
        self.label_seed_array.setGeometry(QtCore.QRect(120, 340, 151, 41))
        self.label_seed_array.setStyleSheet("color: " + self.color_text + ";\n"
                                            "font: 11pt \\\"MV Boli\\\";")
        self.label_seed_array.raise_()

        self.label_multiplier = QtWidgets.QLabel(self)
        self.label_multiplier.setAlignment(QtCore.Qt.AlignCenter)
        self.label_multiplier.setObjectName("label_multiplier")
        self.label_multiplier.setGeometry(QtCore.QRect(90, 420, 191, 41))
        self.label_multiplier.setStyleSheet("color: " + self.color_text + ";\n"
                                            "font: 11pt \\\"MV Boli\\\";")
        self.label_multiplier.raise_()

    def __set_buttons(self):
        self.pushButton_return_main_menu = QtWidgets.QPushButton(self)
        self.pushButton_return_main_menu.setGeometry(QtCore.QRect(1190, 10, 51, 51))
        self.pushButton_return_main_menu.setStyleSheet("#pushButton_return_main_menu{\n"
                                                       "background-color: rgba(0, 0, 0,0);\n"
                                                       "border:1px;\n"
                                                       "}\n"
                                                       "#pushButton_return_main_menu:hover{\n"
                                                       "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, "
                                                       "radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), "
                                                       "stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), "
                                                       "stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, "
                                                       "238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), "
                                                       "stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));\n "
                                                       "\n"
                                                       "}\n"
                                                       "")
        self.pushButton_return_main_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/Home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_return_main_menu.setIcon(icon)
        self.pushButton_return_main_menu.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_return_main_menu.setObjectName("pushButton_return_main_menu")
        self.pushButton_return_main_menu.raise_()

        self.pushButton_create_array = QtWidgets.QPushButton(self)
        self.pushButton_create_array.setGeometry(QtCore.QRect(30, 660, 130, 40))
        self.pushButton_create_array.setMinimumSize(QtCore.QSize(30, 40))
        self.pushButton_create_array.setMaximumSize(QtCore.QSize(130, 40))
        self.pushButton_create_array.setStyleSheet("#pushButton_create_array{\n"
                                                   "background-color: " + self.color_button_background + ";\n"
                                                   "font: 11pt MV Boli;\n"
                                                   "color:" + self.color_text_button + ";\n"
                                                   "border:1px solid " + self.color_border + ";\n"
                                                   "border-radius:20px;\n"
                                                   "}\n"
                                                   "#pushButton_create_array:hover{\n"
                                                   "background-color: " + self.color_button_background_hover + ";\n"
                                                   "    color: " + self.color_text_button_hover + ";\n"
                                                   "\n"
                                                   "}")
        self.pushButton_create_array.setObjectName("pushButton_create_array")
        self.pushButton_create_array.raise_()

        self.pushButton_manuel_array = QtWidgets.QPushButton(self)
        self.pushButton_manuel_array.setGeometry(QtCore.QRect(20, 710, 161, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_manuel_array.sizePolicy().hasHeightForWidth())
        self.pushButton_manuel_array.setSizePolicy(sizePolicy)
        self.pushButton_manuel_array.setMinimumSize(QtCore.QSize(75, 40))
        self.pushButton_manuel_array.setStyleSheet("#pushButton_manuel_array{\n"
                                                   "background-color: " + self.color_button_background + ";\n"
                                                   "font: 11pt MV Boli;\n"
                                                   "color:" + self.color_text_button + ";\n"
                                                   "border:1px solid " + self.color_border + ";\n"
                                                   "border-radius:20px;\n"
                                                   "}\n"
                                                   "#pushButton_manuel_array:hover{\n"
                                                   "background-color: " + self.color_button_background_hover + ";\n"
                                                   "    color: " + self.color_text_button_hover + ";\n"
                                                   "\n"
                                                   "}")
        self.pushButton_manuel_array.setObjectName("pushButton_manuel_array")
        self.pushButton_manuel_array.raise_()

        self.pushButton_random_array = QtWidgets.QPushButton(self)
        self.pushButton_random_array.setGeometry(QtCore.QRect(30, 610, 130, 40))
        self.pushButton_random_array.setMinimumSize(QtCore.QSize(30, 40))
        self.pushButton_random_array.setMaximumSize(QtCore.QSize(130, 40))
        self.pushButton_random_array.setStyleSheet("#pushButton_random_array{\n"
                                                   "background-color: " + self.color_button_background + ";\n"
                                                   "font: 11pt MV Boli;\n"
                                                   "color:" + self.color_text_button + ";\n"
                                                   "border:1px solid " + self.color_border + ";\n"
                                                   "border-radius:20px;\n"
                                                   "}\n"
                                                   "#pushButton_random_array:hover{\n"
                                                   "background-color: " + self.color_button_background_hover + ";\n"
                                                   "    color: " + self.color_text_button_hover + ";\n"
                                                   "\n"
                                                   "}")
        self.pushButton_random_array.setObjectName("pushButton_random_array")
        self.pushButton_random_array.raise_()

        self.pushButton_clear = QtWidgets.QPushButton(self)
        self.pushButton_clear.setGeometry(QtCore.QRect(1070, 740, 131, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_clear.setSizePolicy(sizePolicy)
        self.pushButton_clear.setMinimumSize(QtCore.QSize(75, 40))
        self.pushButton_clear.setStyleSheet("#pushButton_clear{\n"
                                            "background-color: " + self.color_button_background + ";\n"
                                            "font: 11pt MV Boli;\n"
                                            "color:" + self.color_text_button + ";\n"
                                            "border:1px solid " + self.color_border + ";\n"
                                            "border-radius:20px;\n"
                                            "}\n"
                                            "#pushButton_clear:hover{\n"
                                            "background-color: " + self.color_button_background_hover + ";\n"
                                            "    color: " + self.color_text_button_hover + ";\n"
                                            "\n"
                                            "}")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_clear.raise_()

        self.pushButton_merge_sort = QtWidgets.QPushButton(self)
        self.pushButton_merge_sort.setGeometry(QtCore.QRect(350, 610, 130, 40))
        self.pushButton_merge_sort.setMinimumSize(QtCore.QSize(30, 40))
        self.pushButton_merge_sort.setMaximumSize(QtCore.QSize(130, 40))
        self.pushButton_merge_sort.setStyleSheet("#pushButton_merge_sort{\n"
                                                 "background-color: " + self.color_button_background + ";\n"
                                                 "font: 11pt MV Boli;\n"
                                                 "color:" + self.color_text_button + ";\n"
                                                 "border:1px solid " + self.color_border + ";\n"
                                                 "border-radius:20px;\n"
                                                 "}\n"
                                                 "#pushButton_merge_sort:hover{\n"
                                                 "background-color: " + self.color_button_background_hover + ";\n"
                                                 "    color: " + self.color_text_button_hover + ";\n"
                                                 "\n"
                                                 "}")
        self.pushButton_merge_sort.setObjectName("pushButton_merge_sort")
        self.pushButton_merge_sort.raise_()

        self.pushButton_insertion_sort = QtWidgets.QPushButton(self)
        self.pushButton_insertion_sort.setGeometry(QtCore.QRect(210, 660, 130, 40))
        self.pushButton_insertion_sort.setMinimumSize(QtCore.QSize(30, 40))
        self.pushButton_insertion_sort.setMaximumSize(QtCore.QSize(130, 40))
        self.pushButton_insertion_sort.setStyleSheet("#pushButton_insertion_sort{\n"
                                                     "background-color: " + self.color_button_background + ";\n"
                                                     "font: 11pt MV Boli;\n"
                                                     "color:" + self.color_text_button + ";\n"
                                                     "border:1px solid " + self.color_border + ";\n"
                                                     "border-radius:20px;\n"
                                                     "}\n"
                                                     "#pushButton_insertion_sort:hover{\n"
                                                     "background-color: " + self.color_button_background_hover + ";\n"
                                                     "    color: " + self.color_text_button_hover + ";\n"
                                                     "\n"
                                                     "}")
        self.pushButton_insertion_sort.setObjectName("pushButton_insertion_sort")
        self.pushButton_insertion_sort.raise_()

        self.pushButton_heap_sort = QtWidgets.QPushButton(self)
        self.pushButton_heap_sort.setGeometry(QtCore.QRect(350, 660, 130, 40))
        self.pushButton_heap_sort.setMinimumSize(QtCore.QSize(30, 40))
        self.pushButton_heap_sort.setMaximumSize(QtCore.QSize(130, 40))
        self.pushButton_heap_sort.setStyleSheet("#pushButton_heap_sort{\n"
                                                "background-color: " + self.color_button_background + ";\n"
                                                "font: 11pt MV Boli;\n"
                                                "color:" + self.color_text_button + ";\n"
                                                "border:1px solid " + self.color_border + ";\n"
                                                "border-radius:20px;\n"
                                                "}\n"
                                                "#pushButton_heap_sort:hover{\n"
                                                "background-color: " + self.color_button_background_hover + ";\n"
                                                "    color: " + self.color_text_button_hover + ";\n"
                                                "\n"
                                                "}")
        self.pushButton_heap_sort.setObjectName("pushButton_heap_sort")
        self.pushButton_heap_sort.raise_()

        self.pushButton_quick_sort = QtWidgets.QPushButton(self)
        self.pushButton_quick_sort.setGeometry(QtCore.QRect(490, 660, 130, 40))
        self.pushButton_quick_sort.setMinimumSize(QtCore.QSize(30, 40))
        self.pushButton_quick_sort.setMaximumSize(QtCore.QSize(130, 40))
        self.pushButton_quick_sort.setStyleSheet("#pushButton_quick_sort{\n"
                                                 "background-color: " + self.color_button_background + ";\n"
                                                 "font: 11pt MV Boli;\n"
                                                 "color:" + self.color_text_button + ";\n"
                                                 "border:1px solid " + self.color_border + ";\n"
                                                 "border-radius:20px;\n"
                                                 "}\n"
                                                 "#pushButton_quick_sort:hover{\n"
                                                 "background-color: " + self.color_button_background_hover + ";\n"
                                                 "    color: " + self.color_text_button_hover + ";\n"
                                                 "\n"
                                                 "}")
        self.pushButton_quick_sort.setObjectName("pushButton_quick_sort")
        self.pushButton_quick_sort.raise_()

        self.pushButton_bubble_sort = QtWidgets.QPushButton(self)
        self.pushButton_bubble_sort.setGeometry(QtCore.QRect(210, 610, 130, 40))
        self.pushButton_bubble_sort.setMinimumSize(QtCore.QSize(30, 40))
        self.pushButton_bubble_sort.setMaximumSize(QtCore.QSize(130, 40))
        self.pushButton_bubble_sort.setStyleSheet("#pushButton_bubble_sort{\n"
                                                  "background-color: " + self.color_button_background + ";\n"
                                                  "font: 11pt MV Boli;\n"
                                                  "color:" + self.color_text_button + ";\n"
                                                  "border:1px solid " + self.color_border + ";\n"
                                                  "border-radius:20px;\n"
                                                  "}\n"
                                                  "#pushButton_bubble_sort:hover{\n"
                                                  "background-color: " + self.color_button_background_hover + ";\n"
                                                  "    color: " + self.color_text_button_hover + ";\n"
                                                  "\n"
                                                  "}")
        self.pushButton_bubble_sort.setObjectName("pushButton_bubble_sort")
        self.pushButton_bubble_sort.raise_()

        self.pushButton_radix_sort = QtWidgets.QPushButton(self)
        self.pushButton_radix_sort.setGeometry(QtCore.QRect(770, 610, 130, 40))
        self.pushButton_radix_sort.setMinimumSize(QtCore.QSize(30, 40))
        self.pushButton_radix_sort.setMaximumSize(QtCore.QSize(130, 40))
        self.pushButton_radix_sort.setStyleSheet("#pushButton_radix_sort{\n"
                                                 "background-color: " + self.color_button_background + ";\n"
                                                 "font: 11pt MV Boli;\n"
                                                 "color: " + self.color_text_button + ";\n"
                                                 "border:1px solid " + self.color_border + ";\n"
                                                 "border-radius:20px;\n"
                                                 "}\n"
                                                 "#pushButton_radix_sort:hover{\n"
                                                 "background-color: " + self.color_button_background_hover + ";\n"
                                                 "    color: " + self.color_text_button_hover + ";\n"
                                                 "\n"
                                                 "}")
        self.pushButton_radix_sort.setObjectName("pushButton_radix_sort")
        self.pushButton_radix_sort.raise_()

        self.pushButton_counting_sort = QtWidgets.QPushButton(self)
        self.pushButton_counting_sort.setGeometry(QtCore.QRect(770, 660, 130, 40))
        self.pushButton_counting_sort.setMinimumSize(QtCore.QSize(30, 40))
        self.pushButton_counting_sort.setMaximumSize(QtCore.QSize(130, 40))
        self.pushButton_counting_sort.setStyleSheet("#pushButton_counting_sort{\n"
                                                    "background-color: " + self.color_button_background + ";\n"
                                                    "font: 11pt MV Boli;\n"
                                                    "color:" + self.color_text_button + ";\n"
                                                    "border:1px solid " + self.color_border + ";\n"
                                                    "border-radius:20px;\n"
                                                    "}\n"
                                                    "#pushButton_counting_sort:hover{\n"
                                                    "background-color: " + self.color_button_background_hover + ";\n"
                                                    "    color: " + self.color_text_button_hover + ";\n"
                                                    "\n"
                                                    "}")
        self.pushButton_counting_sort.setObjectName("pushButton_counting_sort")
        self.pushButton_counting_sort.raise_()

    def __set_dials(self):
        self.dial_sort_array_length = QtWidgets.QDial(self)
        self.dial_sort_array_length.setGeometry(QtCore.QRect(130, 90, 121, 131))
        self.dial_sort_array_length.setStyleSheet("#dial_sort_array_length{\n"
                                                  "    background-color: " + self.color_slider + ";\n"
                                                  "}")
        self.dial_sort_array_length.setNotchesVisible(True)
        self.dial_sort_array_length.setObjectName("dial_sort_array_length")
        self.dial_sort_array_length.raise_()

        self.dial_animation_speed = QtWidgets.QDial(self)
        self.dial_animation_speed.setGeometry(QtCore.QRect(1090, 590, 121, 121))
        self.dial_animation_speed.setStyleSheet("#dial_animation_speed{\n"
                                                "background-color: " + self.color_slider + ";\n"
                                                "}")
        self.dial_animation_speed.setMaximum(100)
        self.dial_animation_speed.setWrapping(True)
        self.dial_animation_speed.setNotchTarget(10.0)
        self.dial_animation_speed.setNotchesVisible(True)
        self.dial_animation_speed.setObjectName("dial_animation_speed")
        self.dial_animation_speed.raise_()

    def __set_sliders(self):
        self.horizontalSlider_multiplier = QtWidgets.QSlider(self)
        self.horizontalSlider_multiplier.setGeometry(QtCore.QRect(110, 460, 160, 22))
        self.horizontalSlider_multiplier.setStyleSheet("#horizontalSlider_multiplier{\n"
                                                       "selection-color: " + self.color_slider + ";\n"
                                                       "\n"
                                                       "}\n"
                                                       "\n"
                                                       "#horizontalSlider_multiplier:pressed{\n"
                                                       "alternate-background-color: rgb(255, 255, 0);\n"
                                                       "}")
        self.horizontalSlider_multiplier.setMinimum(1)
        self.horizontalSlider_multiplier.setMaximum(10)
        self.horizontalSlider_multiplier.setPageStep(1)
        self.horizontalSlider_multiplier.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_multiplier.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_multiplier.setObjectName("horizontalSlider_multiplier")
        self.horizontalSlider_multiplier.raise_()

    def __set_line_edits(self):
        self.lineEdit_array_length = QtWidgets.QLineEdit(self)
        self.lineEdit_array_length.setGeometry(QtCore.QRect(160, 220, 61, 41))
        self.lineEdit_array_length.setStyleSheet("background-color: " + self.color_widget_background + ";\n"
                                                 "font: 13pt \"MV Boli\";\n"
                                                 "color:" + self.color_text + ";\n"
                                                 "border:1px solid " + self.color_border + ";")
        self.lineEdit_array_length.setText("")
        self.lineEdit_array_length.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_array_length.setReadOnly(True)
        self.lineEdit_array_length.setObjectName("lineEdit_array_length")
        self.lineEdit_array_length.raise_()

        self.lineEdit_lower_range = QtWidgets.QLineEdit(self)
        self.lineEdit_lower_range.setGeometry(QtCore.QRect(90, 300, 81, 41))
        self.lineEdit_lower_range.setStyleSheet("#lineEdit_lower_range{\n"
                                                "background-color: " + self.color_widget_background + ";\n"
                                                "font: 12pt  MV Boli;\n"
                                                "color:" + self.color_text + ";\n"
                                                "border:1px solid " + self.color_border + ";\n"
                                                "}")
        self.lineEdit_lower_range.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_lower_range.setObjectName("lineEdit_lower_range")
        self.lineEdit_lower_range.raise_()

        self.lineEdit_upper_range = QtWidgets.QLineEdit(self)
        self.lineEdit_upper_range.setGeometry(QtCore.QRect(220, 300, 81, 41))
        self.lineEdit_upper_range.setStyleSheet("#lineEdit_upper_range{\n"
                                                "background-color: " + self.color_widget_background + ";\n"
                                                "font: 12pt  MV Boli;\n"
                                                "color:" + self.color_text + ";\n"
                                                "border:1px solid " + self.color_border + ";\n"
                                                "}")
        self.lineEdit_upper_range.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_upper_range.setObjectName("lineEdit_upper_range")
        self.lineEdit_upper_range.raise_()

        self.lineEdit_multiplier = QtWidgets.QLineEdit(self)
        self.lineEdit_multiplier.setGeometry(QtCore.QRect(170, 490, 51, 31))
        self.lineEdit_multiplier.setStyleSheet("background-color: " + self.color_widget_background + ";\n"
                                               "font: 13pt \"MV Boli\";\n"
                                               "color:" + self.color_text + ";\n"
                                               "border:1px solid " + self.color_border + ";")
        self.lineEdit_multiplier.setText("")
        self.lineEdit_multiplier.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_multiplier.setReadOnly(True)
        self.lineEdit_multiplier.setObjectName("lineEdit_multiplier")
        self.lineEdit_multiplier.raise_()

    def __set_check_boxes(self):
        self.checkBox_unique_array = QtWidgets.QCheckBox(self)
        self.checkBox_unique_array.setGeometry(QtCore.QRect(50, 540, 121, 21))
        self.checkBox_unique_array.setStyleSheet("#checkBox_unique_array{\n"
                                                 "font: 11pt \"MV Boli\";\n"
                                                 "color:" + self.color_text + ";\n"
                                                 "}")
        self.checkBox_unique_array.setObjectName("checkBox_unique_array")
        self.checkBox_unique_array.raise_()

        self.checkBox_unique_array_2 = QtWidgets.QCheckBox(self)
        self.checkBox_unique_array_2.setGeometry(QtCore.QRect(50, 570, 121, 21))
        self.checkBox_unique_array_2.setStyleSheet("#checkBox_unique_array_2{\n"
                                                   "font: 11pt \"MV Boli\";\n"
                                                   "color:" + self.color_text + ";\n"
                                                   "}")
        self.checkBox_unique_array_2.setObjectName("checkBox_unique_array_2")
        self.checkBox_unique_array_2.raise_()

    def __set_spin_boxes(self):
        self.spinBox_seed = QtWidgets.QSpinBox(self)
        self.spinBox_seed.setGeometry(QtCore.QRect(150, 380, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_seed.setFont(font)
        self.spinBox_seed.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox_seed.setStyleSheet("#spinBox_seed{\n"
                                        "background-color: " + self.color_widget_background + ";\n"
                                        "color: " + self.color_text + ";\n"
                                        "border:1px solid " + self.color_border + ";\n"
                                        "}")
        self.spinBox_seed.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_seed.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox_seed.setProperty("showGroupSeparator", False)
        self.spinBox_seed.setObjectName("spinBox_seed")
        self.spinBox_seed.raise_()

    def __set_icons(self):
        self.icon1 = QtGui.QIcon()
        self.icon1.addPixmap(QtGui.QPixmap(":/icons/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.icon2 = QtGui.QIcon()
        self.icon2.addPixmap(QtGui.QPixmap(":/icons/icons/read.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.icon3 = QtGui.QIcon()
        self.icon3.addPixmap(QtGui.QPixmap(":/icons/icons/txt_logo.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.icon4 = QtGui.QIcon()
        self.icon4.addPixmap(QtGui.QPixmap(":/icons/icons/2306130.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.icon5 = QtGui.QIcon()
        self.icon5.addPixmap(QtGui.QPixmap(":/icons/icons/csv-file-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    def __set_actions(self):
        self.action_txt = QtWidgets.QAction(self)
        self.action_txt.setIcon(self.icon3)
        self.action_txt.setObjectName("action_txt")

        self.action_xlsx = QtWidgets.QAction(self)
        self.action_xlsx.setIcon(self.icon4)
        self.action_xlsx.setObjectName("action_xlsx")

        self.action_csv = QtWidgets.QAction(self)
        self.action_csv.setIcon(self.icon5)
        self.action_csv.setObjectName("action_csv")

        self.actionText_File = QtWidgets.QAction(self)
        self.actionText_File.setIcon(self.icon3)

        self.actionText_File.setObjectName("actionText_File")
        self.actionExcel_File = QtWidgets.QAction(self)
        self.actionExcel_File.setIcon(self.icon4)
        self.actionExcel_File.setObjectName("actionExcel_File")

        self.actionCsv_File = QtWidgets.QAction(self)
        self.actionCsv_File.setIcon(self.icon5)
        self.actionCsv_File.setObjectName("actionCsv_File")

    def __set_menu(self):
        self.__set_icons()
        self.__set_actions()

        self.menuBar = QtWidgets.QMenuBar(self)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1250, 21))
        self.menuBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuBar.setAutoFillBackground(False)
        self.menuBar.setStyleSheet("")
        self.menuBar.setObjectName("menuBar")

        self.menu_file = QtWidgets.QMenu(self.menuBar)
        self.menu_file.setStyleSheet("")
        self.menu_file.setObjectName("menuFile")

        self.menu_save = QtWidgets.QMenu(self.menu_file)

        self.menu_save.setIcon(self.icon1)
        self.menu_save.setObjectName("menu_save")

        self.menu_import = QtWidgets.QMenu(self.menu_file)
        self.menu_import.setIcon(self.icon2)
        self.menu_import.setObjectName("menu_import")

        self.setMenuBar(self.menuBar)

        self.menu_save.addAction(self.action_txt)
        self.menu_save.addAction(self.action_xlsx)
        self.menu_save.addAction(self.action_csv)
        self.menu_import.addAction(self.actionText_File)
        self.menu_import.addAction(self.actionExcel_File)
        self.menu_import.addAction(self.actionCsv_File)
        self.menu_file.addAction(self.menu_save.menuAction())
        self.menu_file.addAction(self.menu_import.menuAction())
        self.menuBar.addAction(self.menu_file.menuAction())
