from PyQt4.QtGui import *
from PyQt4.QtCore import *
import csv
app=QApplication([])


class MainWindow(QMainWindow):

    table=QTableWidget()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.model = QStandardItemModel(self)

        self.tableView = QTableView(self)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setShowGrid(True)
        self.tableView.setGeometry(9,40,1345,650)


        fileMenu = self.menuBar().addMenu("&File")
        load=QAction("Load",self)
        load.setShortcut("Ctrl+L")
        self.connect(load,SIGNAL("triggered()"),self.Load)
        fileMenu.addAction(load)


    def Load(self):
        fileName=QFileDialog.getOpenFileName(self,'Load File')
        self.model.clear()
        #self.model.deleteLater()
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput):
                items = [
                    QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)
    def Load1(self):
        rel=QFileDialog.getOpenFileName(self,"Load File")
        self.table.insertRow(0)

        for i in rel.header.attributes:
            item = QTableWidgetItem()
            item.setText(i)
            self.table.insertColumn(self.table.columnCount())
            self.table.setItem(0, self.table.columnCount() - 1, item)

        for i in rel.content:
            self.table.insertRow(self.table.rowCount())
            for j in range(len(i)):
                item = QTableWidgetItem()
                item.setText(i[j])
                self.table.setItem(self.table.rowCount() - 1, j, item)

window=MainWindow()
window.show()
app.exec_()



