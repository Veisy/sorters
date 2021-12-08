from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMainWindow

from src.algorithms.bubble_sorter import BubbleSorter
from src.algorithms.counting_sorter import CountingSorter
from src.algorithms.heap_sorter import HeapSorter
from src.algorithms.insertion_sorter import InsertionSorter
from src.algorithms.merge_sorter import MergeSorter
from src.algorithms.quick_sorter import QuickSorter
from src.algorithms.radix_sorter import RadixSorter
from src.ui.mpl_sorting_widget import MplSortingWidget


class MainSortingWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize widgets.
        self.frame_line = QtWidgets.QFrame(self)
        self.frame_line_2 = QtWidgets.QFrame(self)
        self.frame_line_3 = QtWidgets.QFrame(self)
        self.frame_line_4 = QtWidgets.QFrame(self)
        self.frame_line_5 = QtWidgets.QFrame(self)

        self.label = QtWidgets.QLabel(self)
        self.label_array_size = QtWidgets.QLabel(self)
        self.label_speed = QtWidgets.QLabel(self)
        self.label_min_value = QtWidgets.QLabel(self)
        self.label_max_value = QtWidgets.QLabel(self)

        self.pushButton_return_main_menu = QtWidgets.QPushButton(self)
        self.pushButton_create_array = QtWidgets.QPushButton(self)
        self.pushButton_manuel_array = QtWidgets.QPushButton(self)
        self.pushButton_fibonacci = QtWidgets.QPushButton(self)
        self.pushButton_clear = QtWidgets.QPushButton(self)
        self.pushButton_start_sorting = QtWidgets.QPushButton(self)
        self.pushButton_compare = QtWidgets.QPushButton(self)
        self.pushButton_pause = QtWidgets.QPushButton(self)
        self.pushButton_stop = QtWidgets.QPushButton(self)
        self.pushButton_resume = QtWidgets.QPushButton(self)
        self.pushButton_back = QtWidgets.QPushButton(self)
        self.pushButton_search = QtWidgets.QPushButton(self)

        self.dial_animation_speed = QtWidgets.QDial(self)

        self.lineEdit_array_size = QtWidgets.QLineEdit(self)
        self.lineEdit_max_value = QtWidgets.QLineEdit(self)
        self.lineEdit_min_value = QtWidgets.QLineEdit(self)
        self.lineEdit_search = QtWidgets.QLineEdit(self)
        self.lineEdit_fibonacci = QtWidgets.QLineEdit(self)

        self.comboBox_sorting_algorithms = QtWidgets.QComboBox(self)
        self.checkBox_seed = QtWidgets.QCheckBox(self)
        self.spinBox_seed = QtWidgets.QSpinBox(self)

        self.action_xlsx = QtWidgets.QAction(self)
        self.action_csv = QtWidgets.QAction(self)
        self.action_txt = QtWidgets.QAction(self)
        self.actionCsv_File = QtWidgets.QAction(self)
        self.actionText_File = QtWidgets.QAction(self)
        self.actionExcel_File = QtWidgets.QAction(self)

        self.menuBar = QtWidgets.QMenuBar(self)
        self.menu_file = QtWidgets.QMenu(self.menuBar)
        self.menu_import = QtWidgets.QMenu(self.menu_file)
        self.menu_save = QtWidgets.QMenu(self.menu_file)

        self.mpl_sorting_widget = MplSortingWidget(self)

        # Colors
        self.color_primary = None
        self.color_primary_dark = None
        self.color_secondary = None
        self.color_secondary_light = None
        self.color_complementary = None
        self.color_text = None
        self.color_widget_background = None
        self.color_text_button = None
        self.color_button_background = None
        self.color_border = None
        self.color_button_background_hover = None
        self.color_text_button_hover = None
        self.color_slider = None
        self.color_warning_background = None
        self.color_positive_background = None
        self.color_positive_background_hover = None
        self.color_neutral_background = None
        self.color_neutral_background_hover = None

        # Setup widget properties.
        self.setupUi()

    def setupUi(self):
        self.set_colors()
        self.__set_main_window()
        self.__set_sorting_container()
        self.__set_frames()
        self.__set_labels()
        self.__set_buttons()
        self.__set_dials()
        self.__set_line_edits()
        self.__set_combo_boxes()
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
        self.label_array_size.setText(_translate("MainSortingWindow", "Array Size"))
        self.pushButton_clear.setToolTip(_translate("MainSortingWindow", "Clear the fields"))
        self.pushButton_clear.setText(_translate("MainSortingWindow", "Clear"))
        self.pushButton_start_sorting.setToolTip(_translate("MainSortingWindow", "Start sorting animation."))
        self.pushButton_start_sorting.setText(_translate("MainSortingWindow", "SORT"))
        self.pushButton_compare.setToolTip(_translate("MainSortingWindow", "Compare sorting algorithms."))
        self.pushButton_compare.setText(_translate("MainSortingWindow", "COMPARE"))
        self.label_speed.setText(_translate("MainSortingWindow", " Speed"))
        self.pushButton_manuel_array.setToolTip(_translate("MainSortingWindow", "Manual array entrance"))
        self.pushButton_manuel_array.setText(_translate("MainSortingWindow", "Manual Array"))
        self.checkBox_seed.setToolTip(
            _translate("MainWindow_SortingWindow", "Constant array for every parameters."))
        self.checkBox_seed.setText(_translate("MainWindow_SortingWindow", "Seed Array"))
        self.pushButton_return_main_menu.setToolTip(_translate("MainSortingWindow", "Back to Home Window"))
        self.label_min_value.setText(_translate("MainSortingWindow", "Min Value"))
        self.lineEdit_min_value.setToolTip(_translate("MainSortingWindow", "Enter min value."))
        self.label_max_value.setText(_translate("MainSortingWindow", "Max Value"))
        self.lineEdit_max_value.setToolTip(_translate("MainSortingWindow", "Enter max value."))
        self.pushButton_search.setText(_translate("MainSortingWindow", "Search"))
        self.pushButton_search.setToolTip(_translate("MainSortingWindow", "Search in array."))
        self.pushButton_fibonacci.setText(_translate("MainSortingWindow", "Fibonacci"))
        self.pushButton_fibonacci.setToolTip(_translate("MainSortingWindow", "Create fibonacci sequence."))
        self.pushButton_pause.setText(_translate("MainSortingWindow", "Pause"))
        self.pushButton_pause.setToolTip(_translate("MainSortingWindow", "Pause animation."))
        self.pushButton_resume.setText(_translate("MainSortingWindow", "Resume"))
        self.pushButton_resume.setToolTip(_translate("MainSortingWindow", "Resume animation."))
        self.pushButton_stop.setText(_translate("MainSortingWindow", "Stop"))
        self.pushButton_resume.setToolTip(_translate("MainSortingWindow", "Stop animation."))
        self.pushButton_back.setText(_translate("MainSortingWindow", "Back"))
        self.pushButton_back.setToolTip(_translate("MainSortingWindow", "Show previous sorting step."))
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
        self.color_secondary_light = "rgb(150, 150, 150)"

        self.color_warning_background = "rgb(100, 0, 0)"
        self.color_positive_background = '#0a5d00'
        self.color_positive_background_hover = '#089000'
        self.color_neutral_background = '#3949ab'
        self.color_neutral_background_hover = '#6f74dd'

        self.color_complementary = '#796e01'

        self.color_text = self.color_secondary
        self.color_widget_background = self.color_primary
        self.color_text_button = self.color_primary
        self.color_button_background = self.color_primary_dark
        self.color_text_button_hover = self.color_secondary
        self.color_button_background_hover = self.color_secondary_light
        self.color_border = self.color_secondary
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
        self.mpl_sorting_widget.setGeometry(QtCore.QRect(0, 20, 1215, 450))
        self.mpl_sorting_widget.setStyleSheet("background-color: " + self.color_widget_background + ";")
        self.mpl_sorting_widget.setObjectName("mpl_sorting_widget")
        self.mpl_sorting_widget.raise_()

    def __set_frames(self):
        self.frame_line.setGeometry(QtCore.QRect(160, 600, 20, 200))
        self.frame_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_line.setObjectName("frame_line")
        self.frame_line.raise_()

        self.frame_line_2.setGeometry(QtCore.QRect(320, 600, 20, 200))
        self.frame_line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_line_2.setObjectName("frame_line_2")
        self.frame_line_2.raise_()

        self.frame_line_3.setGeometry(QtCore.QRect(530, 600, 20, 200))
        self.frame_line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_line_3.setObjectName("frame_line_3")
        self.frame_line_3.raise_()

        self.frame_line_4.setGeometry(QtCore.QRect(730, 600, 20, 200))
        self.frame_line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_line_4.setObjectName("frame_line_4")
        self.frame_line_4.raise_()

        self.frame_line_5.setGeometry(QtCore.QRect(870, 600, 20, 200))
        self.frame_line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_line_5.setObjectName("frame_line_5")
        self.frame_line_5.raise_()

    def __set_labels(self):
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setGeometry(QtCore.QRect(490, 10, 271, 41))
        self.label.setStyleSheet("color: " + self.color_text + ";\n"
                                 "\n"
                                 "font: 24pt \"MV Boli\";\n"
                                 "border-radius:20px\n"
                                 "")
        self.label.raise_()

        self.label_array_size.setAlignment(QtCore.Qt.AlignCenter)
        self.label_array_size.setObjectName("label_2")
        self.label_array_size.setGeometry(QtCore.QRect(35, 595, 101, 31))
        self.label_array_size.setStyleSheet("#label_2{\n"
                                            "color: " + self.color_text + ";\n"
                                            "font: 11pt \\\"MV Boli\\\";\n"
                                            "\n"
                                            "}")
        self.label_array_size.raise_()

        self.label_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_speed.setObjectName("label_3")
        self.label_speed.setGeometry(QtCore.QRect(793, 478, 71, 21))
        self.label_speed.setStyleSheet("#label_3{\n"
                                       "color: " + self.color_text + ";\n"
                                       "font: 12pt \\\"MV Boli\\\";\n"
                                       "\n"
                                       "}\n"
                                       "")
        self.label_speed.setVisible(False)
        self.label_speed.raise_()

        self.label_min_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_min_value.setObjectName("label_array_range")
        self.label_min_value.setGeometry(QtCore.QRect(200, 690, 101, 31))
        self.label_min_value.setStyleSheet("color: " + self.color_text + ";\n"
                                           "font: 11pt \\\"MV Boli\\\";")
        self.label_min_value.raise_()

        self.label_max_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_max_value.setObjectName("label_array_range_2")
        self.label_max_value.setGeometry(QtCore.QRect(200, 595, 101, 31))
        self.label_max_value.setStyleSheet("color: " + self.color_text + ";\n"
                                           "font: 11pt \\\"MV Boli\\\";")
        self.label_max_value.raise_()


    def __set_buttons(self):
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
        self.pushButton_return_main_menu.setObjectName("pushButton_return_main_menu")
        self.pushButton_return_main_menu.raise_()

        self.pushButton_create_array.setGeometry(QtCore.QRect(370, 610, 130, 40))
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

        self.pushButton_manuel_array.setGeometry(QtCore.QRect(370, 660, 130, 40))
        self.pushButton_manuel_array.setMinimumSize(QtCore.QSize(30, 40))
        self.pushButton_manuel_array.setMaximumSize(QtCore.QSize(130, 40))
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

        self.pushButton_fibonacci.setGeometry(QtCore.QRect(910, 685, 80, 40))
        self.pushButton_fibonacci.setMinimumSize(QtCore.QSize(30, 40))
        self.pushButton_fibonacci.setMaximumSize(QtCore.QSize(130, 40))
        self.pushButton_fibonacci.setStyleSheet("#pushButton_fibonacci{\n"
                                                "background-color: " + self.color_button_background + ";\n"
                                                "font: 11pt MV Boli;\n"
                                                "color:" + self.color_text_button + ";\n"
                                                "border:1px solid " + self.color_border + ";\n"
                                                "border-radius:20px;\n"
                                                "}\n"
                                                "#pushButton_fibonacci:hover{\n"
                                                "background-color: " + self.color_button_background_hover + ";\n"
                                                "    color: " + self.color_text_button_hover + ";\n"
                                                "\n"
                                                "}")
        self.pushButton_fibonacci.setObjectName("pushButton_fibonacci")
        self.pushButton_fibonacci.raise_()

        self.pushButton_clear.setGeometry(QtCore.QRect(385, 720, 130, 40))
        self.pushButton_clear.setMinimumSize(QtCore.QSize(30, 40))
        self.pushButton_clear.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButton_clear.setStyleSheet("#pushButton_clear{\n"
                                            "background-color: " + self.color_warning_background + ";\n"
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

        self.pushButton_start_sorting.setGeometry(QtCore.QRect(570, 610, 140, 40))
        self.pushButton_start_sorting.setMinimumSize(QtCore.QSize(70, 40))
        self.pushButton_start_sorting.setMaximumSize(QtCore.QSize(140, 40))
        self.pushButton_start_sorting.setStyleSheet("#pushButton_start_sorting{\n"
                                                    "background-color: " + self.color_positive_background + ";\n"
                                                    "font: 11pt MV Boli;\n"
                                                    "color:" + self.color_text_button + ";\n"
                                                    "border:1px solid " + self.color_border + ";\n"
                                                    "border-radius:20px;\n"
                                                    "}\n"
                                                    "#pushButton_start_sorting:hover{\n"
                                                    "background-color: " + self.color_positive_background_hover + ";\n"
                                                    "    color: " + self.color_text_button_hover + ";\n"
                                                    "\n"
                                                    "}")
        self.pushButton_start_sorting.setObjectName("pushButton_start_sorting")
        self.pushButton_start_sorting.raise_()

        self.pushButton_compare.setGeometry(QtCore.QRect(570, 750, 140, 40))
        self.pushButton_compare.setMinimumSize(QtCore.QSize(70, 40))
        self.pushButton_compare.setMaximumSize(QtCore.QSize(140, 40))
        self.pushButton_compare.setStyleSheet("#pushButton_compare{\n"
                                              "background-color: " + self.color_neutral_background + ";\n"
                                              "font: 11pt MV Boli;\n"
                                              "color:" + self.color_text_button + ";\n"
                                              "border:1px solid " + self.color_border + ";\n"
                                              "border-radius:20px;\n"
                                              "}\n"
                                              "#pushButton_compare:hover{\n"
                                              "background-color: " + self.color_neutral_background_hover + ";\n"
                                              "    color: " + self.color_text_button_hover + ";\n"
                                              "\n"
                                              "}")
        self.pushButton_compare.setObjectName("pushButton_compare")
        self.pushButton_compare.raise_()

        self.pushButton_pause.setGeometry(QtCore.QRect(450, 450, 80, 40))
        self.pushButton_pause.setMinimumSize(QtCore.QSize(80, 40))
        self.pushButton_pause.setMaximumSize(QtCore.QSize(160, 40))
        self.pushButton_pause.setStyleSheet("#pushButton_pause{\n"
                                            "background-color: " + self.color_button_background + ";\n"
                                            "font: 11pt MV Boli;\n"
                                            "color:" + self.color_text_button + ";\n"
                                            "border:1px solid " + self.color_border + ";\n"
                                            "border-radius:20px;\n"
                                            "}\n"
                                            "#pushButton_pause:hover{\n"
                                            "background-color: " + self.color_button_background_hover + ";\n"
                                            "    color: " + self.color_text_button_hover + ";\n"
                                            "\n"
                                            "}")
        self.pushButton_pause.setObjectName("pushButton_pause")
        self.pushButton_pause.setVisible(False)
        self.pushButton_pause.raise_()

        self.pushButton_resume.setGeometry(QtCore.QRect(550, 450, 80, 40))
        self.pushButton_resume.setMinimumSize(QtCore.QSize(80, 40))
        self.pushButton_resume.setMaximumSize(QtCore.QSize(160, 40))
        self.pushButton_resume.setStyleSheet("#pushButton_resume{\n"
                                             "background-color: " + self.color_button_background + ";\n"
                                             "font: 11pt MV Boli;\n"
                                             "color:" + self.color_text_button + ";\n"
                                             "border:1px solid " + self.color_border + ";\n"
                                             "border-radius:20px;\n"
                                             "}\n"
                                             "#pushButton_resume:hover{\n"
                                             "background-color: " + self.color_button_background_hover + ";\n"
                                             "    color: " + self.color_text_button_hover + ";\n"
                                             "\n"
                                             "}")
        self.pushButton_resume.setObjectName("pushButton_resume")
        self.pushButton_resume.setVisible(False)
        self.pushButton_resume.raise_()

        self.pushButton_stop.setGeometry(QtCore.QRect(650, 450, 80, 40))
        self.pushButton_stop.setMinimumSize(QtCore.QSize(80, 40))
        self.pushButton_stop.setMaximumSize(QtCore.QSize(160, 40))
        self.pushButton_stop.setStyleSheet("#pushButton_stop{\n"
                                           "background-color: " + self.color_warning_background + ";\n"
                                           "font: 11pt MV Boli;\n"
                                           "color:" + self.color_text_button + ";\n"
                                           "border:1px solid " + self.color_border + ";\n"
                                           "border-radius:20px;\n"
                                           "}\n"
                                           "#pushButton_stop:hover{\n"
                                           "background-color: " + self.color_button_background_hover + ";\n"
                                           "    color: " + self.color_text_button_hover + ";\n"
                                           "\n"
                                           "}")
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.pushButton_stop.setVisible(False)
        self.pushButton_stop.raise_()

        self.pushButton_back.setGeometry(QtCore.QRect(350, 450, 80, 40))
        self.pushButton_back.setMinimumSize(QtCore.QSize(80, 40))
        self.pushButton_back.setMaximumSize(QtCore.QSize(160, 40))
        self.pushButton_back.setStyleSheet("#pushButton_back{\n"
                                           "background-color: " + self.color_button_background + ";\n"
                                           "font: 11pt MV Boli;\n"
                                           "color:" + self.color_text_button + ";\n"
                                           "border:1px solid " + self.color_border + ";\n"
                                           "border-radius:20px;\n"
                                           "}\n"
                                           "#pushButton_back:hover{\n"
                                           "background-color: " + self.color_button_background_hover + ";\n"
                                           "    color: " + self.color_text_button_hover + ";\n"
                                           "\n"
                                           "}")
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_back.setVisible(False)
        self.pushButton_back.raise_()

        self.pushButton_search.setGeometry(QtCore.QRect(770, 685, 80, 40))
        self.pushButton_search.setMinimumSize(QtCore.QSize(80, 40))
        self.pushButton_search.setMaximumSize(QtCore.QSize(160, 40))
        self.pushButton_search.setStyleSheet("#pushButton_search{\n"
                                             "background-color: " + self.color_button_background + ";\n"
                                             "font: 11pt MV Boli;\n"
                                             "color:" + self.color_text_button + ";\n"
                                             "border:1px solid " + self.color_border + ";\n"
                                             "border-radius:20px;\n"
                                             "}\n"
                                             "#pushButton_search:hover{\n"
                                             "background-color: " + self.color_button_background_hover + ";\n"
                                             "    color: " + self.color_text_button_hover + ";\n"
                                             "\n"
                                             "}")
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_search.raise_()

    def __set_dials(self):
        self.dial_animation_speed.setGeometry(QtCore.QRect(770, 430, 121, 121))
        self.dial_animation_speed.setStyleSheet("#dial_animation_speed{\n"
                                                "background-color: " + self.color_slider + ";\n"
                                                "}")
        self.dial_animation_speed.setMaximum(100)
        self.dial_animation_speed.setWrapping(True)
        self.dial_animation_speed.setNotchTarget(10.0)
        self.dial_animation_speed.setNotchesVisible(True)
        self.dial_animation_speed.setObjectName("dial_animation_speed")
        self.dial_animation_speed.setVisible(False)
        self.dial_animation_speed.raise_()

    def __set_line_edits(self):
        self.lineEdit_array_size.setGeometry(QtCore.QRect(45, 630, 81, 41))
        self.lineEdit_array_size.setValidator(QIntValidator(1, 1000, self))
        self.lineEdit_array_size.setStyleSheet("background-color: " + self.color_widget_background + ";\n"
                                               "font: 13pt \"MV Boli\";\n"
                                               "color:" + self.color_text + ";\n"
                                               "border:1px solid " + self.color_border + ";")
        self.lineEdit_array_size.setText("")
        self.lineEdit_array_size.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_array_size.setObjectName("lineEdit_array_length")
        self.lineEdit_array_size.raise_()

        self.lineEdit_min_value.setGeometry(QtCore.QRect(210, 725, 81, 41))
        self.lineEdit_min_value.setStyleSheet("#lineEdit_min_value{\n"
                                              "background-color: " + self.color_widget_background + ";\n"
                                              "font: 12pt  MV Boli;\n"
                                              "color:" + self.color_text + ";\n"
                                              "border:1px solid " + self.color_border + ";\n"
                                              "}")
        self.lineEdit_min_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_min_value.setObjectName("lineEdit_min_value")
        self.lineEdit_min_value.setValidator(QIntValidator(-100000, 100000, self))
        self.lineEdit_min_value.raise_()

        self.lineEdit_max_value.setGeometry(QtCore.QRect(210, 630, 81, 41))
        self.lineEdit_max_value.setStyleSheet("#lineEdit_max_value{\n"
                                              "background-color: " + self.color_widget_background + ";\n"
                                              "font: 12pt  MV Boli;\n"
                                              "color:" + self.color_text + ";\n"
                                              "border:1px solid " + self.color_border + ";\n"
                                              "}")
        self.lineEdit_max_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_max_value.setObjectName("lineEdit_max_value")
        self.lineEdit_max_value.setValidator(QIntValidator(-100000, 100000, self))
        self.lineEdit_max_value.raise_()

        self.lineEdit_search.setGeometry(QtCore.QRect(770, 630, 81, 41))
        self.lineEdit_search.setStyleSheet("#lineEdit_search{\n"
                                           "background-color: " + self.color_widget_background + ";\n"
                                           "font: 12pt  MV Boli;\n"
                                           "color:" + self.color_text + ";\n"
                                           "border:1px solid " + self.color_border + ";\n"
                                           "}")
        self.lineEdit_search.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.lineEdit_search.setValidator(QIntValidator(-100000, 100000, self))
        self.lineEdit_search.raise_()

        self.lineEdit_fibonacci.setGeometry(QtCore.QRect(910, 630, 81, 41))
        self.lineEdit_fibonacci.setStyleSheet("#lineEdit_fibonacci{\n"
                                              "background-color: " + self.color_widget_background + ";\n"
                                              "font: 12pt  MV Boli;\n"
                                              "color:" + self.color_text + ";\n"
                                              "border:1px solid " + self.color_border + ";\n"
                                              "}")
        self.lineEdit_fibonacci.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_fibonacci.setObjectName("lineEdit_fibonacci")
        self.lineEdit_fibonacci.setValidator(QIntValidator(2, 20, self))
        self.lineEdit_fibonacci.raise_()

    def __set_combo_boxes(self):
        self.comboBox_sorting_algorithms.addItems([BubbleSorter.BUBBLE_SORT, InsertionSorter.INSERTION_SORT,
                                                  MergeSorter.MERGE_INSERTION_SORT, MergeSorter.MERGE_SORT,
                                                  CountingSorter.COUNTING_SORT, HeapSorter.HEAP_SORT,
                                                  QuickSorter.QUICK_SORT, RadixSorter.RADIX_SORT])

        self.comboBox_sorting_algorithms.setGeometry(QtCore.QRect(570, 680, 130, 40))
        self.comboBox_sorting_algorithms.setMinimumSize(QtCore.QSize(143, 40))
        self.comboBox_sorting_algorithms.setMaximumSize(QtCore.QSize(200, 40))
        self.comboBox_sorting_algorithms.raise_()

    def __set_check_boxes(self):
        self.checkBox_seed.setGeometry(QtCore.QRect(35, 700, 121, 21))
        self.checkBox_seed.setStyleSheet("#checkBox_seed{\n"
                                         "font: 11pt \"MV Boli\";\n"
                                         "color:" + self.color_text + ";\n"
                                         "}")
        self.checkBox_seed.setObjectName("checkBox_seed")
        self.checkBox_seed.raise_()

    def __set_spin_boxes(self):
        self.spinBox_seed.setGeometry(QtCore.QRect(47, 738, 81, 31))
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

        self.spinBox_seed.setVisible(self.checkBox_seed.isChecked())

    def __set_actions(self):
        self.action_txt.setObjectName("action_txt")

        self.action_xlsx.setObjectName("action_xlsx")

        self.action_csv.setObjectName("action_csv")

        self.actionText_File.setObjectName("actionText_File")

        self.actionExcel_File.setObjectName("actionExcel_File")

        self.actionCsv_File.setObjectName("actionCsv_File")

    def __set_menu(self):
        self.__set_actions()

        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1250, 21))
        self.menuBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuBar.setAutoFillBackground(False)
        self.menuBar.setStyleSheet("")
        self.menuBar.setObjectName("menuBar")

        self.menu_file.setStyleSheet("")
        self.menu_file.setObjectName("menuFile")

        self.menu_save.setObjectName("menu_save")

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
