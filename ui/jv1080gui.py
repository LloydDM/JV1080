# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jv1080.ui'
#
# Created: Thu May 14 08:29:35 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName(_fromUtf8("TabWidget"))
        TabWidget.resize(636, 480)
        TabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tab_common = QtGui.QWidget()
        self.tab_common.setObjectName(_fromUtf8("tab_common"))
        self.groupBox_patchname = QtGui.QGroupBox(self.tab_common)
        self.groupBox_patchname.setGeometry(QtCore.QRect(10, 10, 251, 61))
        self.groupBox_patchname.setObjectName(_fromUtf8("groupBox_patchname"))
        self.line_patchname = QtGui.QLineEdit(self.groupBox_patchname)
        self.line_patchname.setGeometry(QtCore.QRect(10, 20, 111, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.line_patchname.setFont(font)
        self.line_patchname.setText(_fromUtf8(""))
        self.line_patchname.setMaxLength(12)
        self.line_patchname.setObjectName(_fromUtf8("line_patchname"))
        self.button_changename = QtGui.QPushButton(self.groupBox_patchname)
        self.button_changename.setGeometry(QtCore.QRect(130, 20, 111, 25))
        self.button_changename.setObjectName(_fromUtf8("button_changename"))
        self.groupBox_tempo = QtGui.QGroupBox(self.tab_common)
        self.groupBox_tempo.setGeometry(QtCore.QRect(270, 10, 101, 61))
        self.groupBox_tempo.setObjectName(_fromUtf8("groupBox_tempo"))
        self.spinBox_tempo = QtGui.QSpinBox(self.groupBox_tempo)
        self.spinBox_tempo.setGeometry(QtCore.QRect(10, 20, 81, 25))
        self.spinBox_tempo.setMinimum(20)
        self.spinBox_tempo.setMaximum(250)
        self.spinBox_tempo.setObjectName(_fromUtf8("spinBox_tempo"))
        self.dial_patchlevel = QtGui.QDial(self.tab_common)
        self.dial_patchlevel.setGeometry(QtCore.QRect(32, 100, 50, 64))
        self.dial_patchlevel.setMaximum(127)
        self.dial_patchlevel.setTracking(True)
        self.dial_patchlevel.setOrientation(QtCore.Qt.Horizontal)
        self.dial_patchlevel.setInvertedAppearance(False)
        self.dial_patchlevel.setInvertedControls(False)
        self.dial_patchlevel.setWrapping(False)
        self.dial_patchlevel.setNotchTarget(5.0)
        self.dial_patchlevel.setNotchesVisible(True)
        self.dial_patchlevel.setObjectName(_fromUtf8("dial_patchlevel"))
        self.label_patchlevel = QtGui.QLabel(self.tab_common)
        self.label_patchlevel.setGeometry(QtCore.QRect(20, 80, 71, 21))
        self.label_patchlevel.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_patchlevel.setLineWidth(0)
        self.label_patchlevel.setObjectName(_fromUtf8("label_patchlevel"))
        self.label = QtGui.QLabel(self.tab_common)
        self.label.setGeometry(QtCore.QRect(30, 170, 59, 15))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        TabWidget.addTab(self.tab_common, _fromUtf8(""))
        self.tab_effects = QtGui.QWidget()
        self.tab_effects.setObjectName(_fromUtf8("tab_effects"))
        TabWidget.addTab(self.tab_effects, _fromUtf8(""))
        self.tab_control = QtGui.QWidget()
        self.tab_control.setObjectName(_fromUtf8("tab_control"))
        TabWidget.addTab(self.tab_control, _fromUtf8(""))
        self.tab_wave = QtGui.QWidget()
        self.tab_wave.setObjectName(_fromUtf8("tab_wave"))
        TabWidget.addTab(self.tab_wave, _fromUtf8(""))
        self.tab_lfo = QtGui.QWidget()
        self.tab_lfo.setObjectName(_fromUtf8("tab_lfo"))
        TabWidget.addTab(self.tab_lfo, _fromUtf8(""))
        self.tab_pitch = QtGui.QWidget()
        self.tab_pitch.setObjectName(_fromUtf8("tab_pitch"))
        TabWidget.addTab(self.tab_pitch, _fromUtf8(""))
        self.tab_tvf = QtGui.QWidget()
        self.tab_tvf.setObjectName(_fromUtf8("tab_tvf"))
        TabWidget.addTab(self.tab_tvf, _fromUtf8(""))
        self.tab_tva = QtGui.QWidget()
        self.tab_tva.setObjectName(_fromUtf8("tab_tva"))
        TabWidget.addTab(self.tab_tva, _fromUtf8(""))

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.dial_patchlevel, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label.setNum)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget", None))
        self.groupBox_patchname.setTitle(_translate("TabWidget", "Patch Name", None))
        self.line_patchname.setInputMask(_translate("TabWidget", "nnnnnnnnnnnn; ", None))
        self.line_patchname.setPlaceholderText(_translate("TabWidget", "12 Chars Max", None))
        self.button_changename.setText(_translate("TabWidget", "Change Name", None))
        self.groupBox_tempo.setTitle(_translate("TabWidget", "Patch Tempo", None))
        self.spinBox_tempo.setSuffix(_translate("TabWidget", " BPM", None))
        self.label_patchlevel.setText(_translate("TabWidget", "Patch Level", None))
        self.label.setText(_translate("TabWidget", "TextLabel", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_common), _translate("TabWidget", "COMMON", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_effects), _translate("TabWidget", "EFFECTS", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_control), _translate("TabWidget", "CONTROL", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_wave), _translate("TabWidget", "WAVE", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_lfo), _translate("TabWidget", "LFO", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_pitch), _translate("TabWidget", "PITCH", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_tvf), _translate("TabWidget", "TVF", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_tva), _translate("TabWidget", "TVA", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())