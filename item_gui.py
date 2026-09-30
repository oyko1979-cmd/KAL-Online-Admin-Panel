from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QScrollArea, QPushButton, QDialog, QComboBox, QLineEdit
from item import Item
from database import update_item_field, get_player_pid, send_item_to_player


class ItemRow(QWidget):
    def __init__(self, item):
        super().__init__()

        self.item = item

        self.row_layout = QHBoxLayout()
        self.setLayout(self.row_layout)

        self.change_button = QPushButton("Change")
        self.send_button = QPushButton("Send")

        self.iid_value = QLabel(str(item.iid))
        self.index_value = QLabel(str(item.index))
        self.prefix_value = QLabel(str(item.prefix))
        self.info_value = QLabel(str(item.info))
        self.num_value = QLabel(str(item.num))

        self.row_layout.addWidget(self.iid_value)
        self.row_layout.addWidget(self.index_value)
        self.row_layout.addWidget(self.prefix_value)
        self.row_layout.addWidget(self.info_value)
        self.row_layout.addWidget(self.num_value)

        self.row_layout.addWidget(self.change_button)
        self.row_layout.addWidget(self.send_button)

        self.change_button.clicked.connect(self.change_item)
        self.send_button.clicked.connect(self.send_item_dialog)


    def send_item_dialog(self):
        self.send_dialog = QDialog(self)
        self.send_dialog.setWindowTitle("Send Item")
        self.send_dialog.resize(300, 150)

        send_dialog_layout = QVBoxLayout()
        self.send_dialog.setLayout(send_dialog_layout)

        self.send_input = QLineEdit()

        self.send_button = QPushButton("Send to Playername")

        send_dialog_layout.addWidget(self.send_input)
        send_dialog_layout.addWidget(self.send_button)

        self.send_button.clicked.connect(self.send_item)
        self.send_dialog.exec()


    def change_item(self):
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("Change Item")
        self.dialog.resize(300, 150)

        dialog_layout = QVBoxLayout()
        self.dialog.setLayout(dialog_layout)

        self.combo = QComboBox()

        self.combo.addItem("Prefix")
        self.combo.addItem("Info")
        self.combo.addItem("Num")

        self.change_value = QLineEdit()

        self.save_button = QPushButton("Save")

        dialog_layout.addWidget(self.combo)
        dialog_layout.addWidget(self.change_value)
        dialog_layout.addWidget(self.save_button)

        self.save_button.clicked.connect(self.save_item_change)
        self.dialog.exec()


    def save_item_change(self):
        field = self.combo.currentText()
        value = self.change_value.text()

        update_item_field(self.item.iid, field, value)
        self.change_value.setText("Success")


    def send_item(self):
        iid = self.item.iid
        target_player_name = self.send_input.text()
        target_player_pid = get_player_pid(target_player_name)

        if not target_player_pid:
            self.send_input.setText("Player does not exist")
            return
        
        send_item_to_player(target_player_pid, iid)
        self.send_input.setText("Success")
        
        



class InventoryWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.inventory_layout = QVBoxLayout()
        self.setLayout(self.inventory_layout)
        self.item_layout = QVBoxLayout()

        scroll_container = QWidget()
        scroll_container.setLayout(self.item_layout)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(scroll_container)

        self.label_layout = QHBoxLayout()

        iid_label = QLabel("IID")
        index_label = QLabel("Index")
        prefix_label = QLabel("Prefix")
        info_label = QLabel("Info")
        num_label = QLabel("Num")
        change_button_label = QLabel("Change")
        send_button_label = QLabel("Send")

        self.label_layout.addWidget(iid_label)
        self.label_layout.addWidget(index_label)
        self.label_layout.addWidget(prefix_label)
        self.label_layout.addWidget(info_label)
        self.label_layout.addWidget(num_label)

        self.label_layout.addWidget(change_button_label)
        self.label_layout.addWidget(send_button_label)

        self.inventory_layout.addLayout(self.label_layout)
        self.inventory_layout.addWidget(self.scroll_area)


    def show_items(self, items):
        print("SHOW ITEMS:", items)
        for item in items:
            row = ItemRow(item)
            self.item_layout.addWidget(row)


    def clear_items(self):
        while self.item_layout.count():
            item = self.item_layout.takeAt(0)
            
            if item is not None:
                widget = item.widget()

                if widget is not None:
                    widget.deleteLater()
