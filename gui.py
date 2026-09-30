from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QScrollArea, QLineEdit, QGridLayout, QInputDialog
from database import search_player, search_item, update_player_field
from PySide6.QtGui import QPainter, QPixmap
from item_gui import InventoryWidget
from PySide6.QtCore import Qt
from player import Player
import sys


# ----- Background Widget ----- #

class BackgroundWidget(QWidget):

    def __init__(self, image_path):
        super().__init__()

        self.background = QPixmap(image_path)

    def paintEvent(self, event):

        painter = QPainter(self)

        background = self.background.scaled(
            self.size(),
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )

        x = (self.width() - background.width()) // 2
        y = (self.height() - background.height()) // 2

        painter.drawPixmap(x, y, background)


# ----- App ----- #
app = QApplication(sys.argv)


# ----- Main Window ----- #
window = QWidget()
window.setWindowTitle("KAL Online Admin Panel v0.5")
window.resize(900, 600)


# ----- Main Layout ----- #
layout = QVBoxLayout()
window.setLayout(layout)

inventory = InventoryWidget()


# ----- Player Search ----- #
search_layout = QHBoxLayout()
search_label = QLabel("Player Name:")
search_input = QLineEdit()
search_input.setMaximumWidth(250)
search_button = QPushButton("Search")
search_button.setMaximumWidth(80)

search_layout.addWidget(search_label)
search_layout.addWidget(search_input)
search_layout.addWidget(search_button)

search_layout.addStretch()

layout.addLayout(search_layout)


# ----- Scroll Area ----- #
scroll_area = QScrollArea()
scroll_area.setWidgetResizable(True)

# ----- Scroll Container ----- #
scroll_widget = BackgroundWidget("test1.jpg")
scroll_area.setWidget(scroll_widget)

scroll_widget.setStyleSheet("""
    QLabel {
        color: white;
    }
""")

# ----- Player Layout ----- #
player_layout = QHBoxLayout()
scroll_widget.setLayout(player_layout)

# ----- Player Left Column ----- #
left_layout = QVBoxLayout()

# ----- Left Menu Block ----- #
uid_layout = QGridLayout()
uid_label = QLabel("UID: ")
uid_button = QLabel("Player UID")
uid_button.setMaximumWidth(70)
uid_value = QLabel()

uid_layout.addWidget(uid_label, 0, 0)
uid_layout.addWidget(uid_value, 0, 1)
uid_layout.addWidget(uid_button, 0, 2)


pid_layout = QGridLayout()
pid_label = QLabel("PID: ")
pid_button = QLabel("Player PID")
pid_button.setMaximumWidth(70)
pid_value = QLabel()

pid_layout.addWidget(pid_label, 0, 0)
pid_layout.addWidget(pid_value, 0, 1)
pid_layout.addWidget(pid_button, 0, 2)


admin_layout = QGridLayout()
admin_label = QLabel("Admin: ")
admin_button = QPushButton("Change")
admin_button.setMaximumWidth(70)
admin_value = QLabel()

admin_layout.addWidget(admin_label, 0, 0)
admin_layout.addWidget(admin_value, 0, 1)
admin_layout.addWidget(admin_button, 0, 2)



name_layout = QGridLayout()
name_label = QLabel("Name: ")
name_button = QPushButton("Change")
name_button.setMaximumWidth(70)
name_value = QLabel()

name_layout.addWidget(name_label, 0, 0)
name_layout.addWidget(name_value, 0, 1)
name_layout.addWidget(name_button, 0, 2)


char_class_layout = QGridLayout()
char_class_label = QLabel("Class: ")
char_class_button = QPushButton("Change")
char_class_button.setMaximumWidth(70)
char_class_value = QLabel()

char_class_layout.addWidget(char_class_label, 0, 0)
char_class_layout.addWidget(char_class_value, 0, 1)
char_class_layout.addWidget(char_class_button, 0, 2)


specialty_layout = QGridLayout()
specialty_label = QLabel("Specialty: ")
specialty_button = QPushButton("Change")
specialty_button.setMaximumWidth(70)
specialty_value = QLabel()

specialty_layout.addWidget(specialty_label, 0, 0)
specialty_layout.addWidget(specialty_value, 0, 1)
specialty_layout.addWidget(specialty_button, 0, 2)


level_layout = QGridLayout()
level_label = QLabel("Level: ")
level_button = QPushButton("Change")
level_button.setMaximumWidth(70)
level_value = QLabel()

level_layout.addWidget(level_label, 0, 0)
level_layout.addWidget(level_value, 0, 1)
level_layout.addWidget(level_button, 0, 2)


contribute_layout = QGridLayout()
contribute_label = QLabel("Contribute: ")
contribute_button = QPushButton("Change")
contribute_button.setMaximumWidth(70)
contribute_value = QLabel()

contribute_layout.addWidget(contribute_label, 0, 0)
contribute_layout.addWidget(contribute_value, 0, 1)
contribute_layout.addWidget(contribute_button, 0, 2)


exp_layout = QGridLayout()
exp_label = QLabel("Exp: ")
exp_button = QPushButton("Change")
exp_button.setMaximumWidth(70)
exp_value = QLabel()

exp_layout.addWidget(exp_label, 0, 0)
exp_layout.addWidget(exp_value, 0, 1)
exp_layout.addWidget(exp_button, 0, 2)


gid_layout = QGridLayout()
gid_label = QLabel("GID: ")
gid_button = QPushButton("Change")
gid_button.setMaximumWidth(70)
gid_value = QLabel()

gid_layout.addWidget(gid_label, 0, 0)
gid_layout.addWidget(gid_value, 0, 1)
gid_layout.addWidget(gid_button, 0, 2)


grole_layout = QGridLayout()
grole_label = QLabel("GRole: ")
grole_button = QPushButton("Change")
grole_button.setMaximumWidth(70)
grole_value = QLabel()

grole_layout.addWidget(grole_label, 0, 0)
grole_layout.addWidget(grole_value, 0, 1)
grole_layout.addWidget(grole_button, 0, 2)


strength_layout = QGridLayout()
strength_label = QLabel("Strength: ")
strength_button = QPushButton("Change")
strength_button.setMaximumWidth(70)
strength_value = QLabel()

strength_layout.addWidget(strength_label, 0, 0)
strength_layout.addWidget(strength_value, 0, 1)
strength_layout.addWidget(strength_button, 0, 2)


health_layout = QGridLayout()
health_label = QLabel("Health: ")
health_button = QPushButton("Change")
health_button.setMaximumWidth(70)
health_value = QLabel()

health_layout.addWidget(health_label, 0, 0)
health_layout.addWidget(health_value, 0, 1)
health_layout.addWidget(health_button, 0, 2)

# ----- Connect  Left Layout ----- #
left_layout.addLayout(uid_layout)
left_layout.addLayout(pid_layout)
left_layout.addLayout(admin_layout)
left_layout.addLayout(name_layout)
left_layout.addLayout(char_class_layout)
left_layout.addLayout(specialty_layout)
left_layout.addLayout(level_layout)
left_layout.addLayout(contribute_layout)
left_layout.addLayout(exp_layout)
left_layout.addLayout(gid_layout)
left_layout.addLayout(grole_layout)
left_layout.addLayout(strength_layout)
left_layout.addLayout(health_layout)

left_layout.addStretch()

# ----- Player Right Column ----- #
right_layout = QVBoxLayout()


intelligence_layout = QGridLayout()
intelligence_label = QLabel("Intelligence: ")
intelligence_button = QPushButton("Change")
intelligence_button.setMaximumWidth(70)
intelligence_value = QLabel()

intelligence_layout.addWidget(intelligence_label, 0, 0)
intelligence_layout.addWidget(intelligence_value, 0, 1)
intelligence_layout.addWidget(intelligence_button, 0, 2)


wisdom_layout = QGridLayout()
wisdom_label = QLabel("Wisdom: ")
wisdom_button = QPushButton("Change")
wisdom_button.setMaximumWidth(70)
wisdom_value = QLabel()

wisdom_layout.addWidget(wisdom_label, 0, 0)
wisdom_layout.addWidget(wisdom_value, 0, 1)
wisdom_layout.addWidget(wisdom_button, 0, 2)


dexterity_layout = QGridLayout()
dexterity_label = QLabel("Dexterity: ")
dexterity_button = QPushButton("Change")
dexterity_button.setMaximumWidth(70)
dexterity_value = QLabel()

dexterity_layout.addWidget(dexterity_label, 0, 0)
dexterity_layout.addWidget(dexterity_value, 0, 1)
dexterity_layout.addWidget(dexterity_button, 0, 2)


curhp_layout = QGridLayout()
curhp_label = QLabel("CurHP: ")
curhp_button = QPushButton("Change")
curhp_button.setMaximumWidth(70)
curhp_value = QLabel()

curhp_layout.addWidget(curhp_label, 0, 0)
curhp_layout.addWidget(curhp_value, 0, 1)
curhp_layout.addWidget(curhp_button, 0, 2)


curmp_layout = QGridLayout()
curmp_label = QLabel("CurMP: ")
curmp_button = QPushButton("Change")
curmp_button.setMaximumWidth(70)
curmp_value = QLabel()

curmp_layout.addWidget(curmp_label, 0, 0)
curmp_layout.addWidget(curmp_value, 0, 1)
curmp_layout.addWidget(curmp_button, 0, 2)


pupoint_layout = QGridLayout()
pupoint_label = QLabel("PUPoint: ")
pupoint_button = QPushButton("Change")
pupoint_button.setMaximumWidth(70)
pupoint_value = QLabel()

pupoint_layout.addWidget(pupoint_label, 0, 0)
pupoint_layout.addWidget(pupoint_value, 0, 1)
pupoint_layout.addWidget(pupoint_button, 0, 2)


supoint_layout = QGridLayout()
supoint_label = QLabel("SUPoint: ")
supoint_button = QPushButton("Change")
supoint_button.setMaximumWidth(70)
supoint_value = QLabel()

supoint_layout.addWidget(supoint_label, 0, 0)
supoint_layout.addWidget(supoint_value, 0, 1)
supoint_layout.addWidget(supoint_button, 0, 2)


killed_layout = QGridLayout()
killed_label = QLabel("Killed: ")
killed_button = QPushButton("Change")
killed_button.setMaximumWidth(70)
killed_value = QLabel()

killed_layout.addWidget(killed_label, 0, 0)
killed_layout.addWidget(killed_value, 0, 1)
killed_layout.addWidget(killed_button, 0, 2)


map_layout = QGridLayout()
map_label = QLabel("Map: ")
map_button = QPushButton("Change")
map_button.setMaximumWidth(70)
map_value = QLabel()

map_layout.addWidget(map_label, 0, 0)
map_layout.addWidget(map_value, 0, 1)
map_layout.addWidget(map_button, 0, 2)


x_layout = QGridLayout()
x_label = QLabel("X: ")
x_button = QPushButton("Change")
x_button.setMaximumWidth(70)
x_value = QLabel()

x_layout.addWidget(x_label, 0, 0)
x_layout.addWidget(x_value, 0, 1)
x_layout.addWidget(x_button, 0, 2)


y_layout = QGridLayout()
y_label = QLabel("Y: ")
y_button = QPushButton("Change")
y_button.setMaximumWidth(70)
y_value = QLabel()

y_layout.addWidget(y_label, 0, 0)
y_layout.addWidget(y_value, 0, 1)
y_layout.addWidget(y_button, 0, 2)


z_layout = QGridLayout()
z_label = QLabel("Z: ")
z_button = QPushButton("Change")
z_button.setMaximumWidth(70)
z_value = QLabel()

z_layout.addWidget(z_label, 0, 0)
z_layout.addWidget(z_value, 0, 1)
z_layout.addWidget(z_button, 0, 2)


right_layout.addLayout(intelligence_layout)
right_layout.addLayout(wisdom_layout)
right_layout.addLayout(dexterity_layout)
right_layout.addLayout(curhp_layout)
right_layout.addLayout(curmp_layout)
right_layout.addLayout(pupoint_layout)
right_layout.addLayout(supoint_layout)
right_layout.addLayout(killed_layout)
right_layout.addLayout(map_layout)
right_layout.addLayout(x_layout)
right_layout.addLayout(y_layout)
right_layout.addLayout(z_layout)

right_layout.addStretch()



# ----- Add Player Columns ----- #
player_layout.addLayout(left_layout)
player_layout.addLayout(right_layout)

# ----- Add Scroll Area to Main Layout ----- #
layout.addWidget(scroll_area)

layout.addWidget(inventory)



# ----- Functions ----- #

def change_value(field, pid):
    new_value, ok = QInputDialog.getText(
        window,
        f"Change {field}",
        f"New value for {field}:"
    )

    if ok:
        update_player_field(field, new_value, pid)


def search_button_clicked():
    inventory.clear_items()

    global current_player

    charname = search_input.text()
    result = search_player(charname)

    if result is None:
        return

    current_player = result
    items = search_item(current_player.pid)
    inventory.show_items(items)
    show_player(current_player)


def show_player(player):

    uid_value.setText(str(player.uid))
    pid_value.setText(str(player.pid))
    admin_value.setText(str(player.admin))
    name_value.setText(str(player.name))
    char_class_value.setText(str(player.char_class))
    specialty_value.setText(str(player.specialty))
    level_value.setText(str(player.level))
    contribute_value.setText(str(player.contribute))
    exp_value.setText(str(player.exp))
    gid_value.setText(str(player.gid))
    grole_value.setText(str(player.grole))
    strength_value.setText(str(player.strength))
    health_value.setText(str(player.health))
    intelligence_value.setText(str(player.intelligence))
    wisdom_value.setText(str(player.wisdom))
    dexterity_value.setText(str(player.dexterity))
    curhp_value.setText(str(player.curhp))
    curmp_value.setText(str(player.curmp))
    pupoint_value.setText(str(player.pupoint))
    supoint_value.setText(str(player.supoint))
    killed_value.setText(str(player.killed))
    map_value.setText(str(player.map))
    x_value.setText(str(player.x))
    y_value.setText(str(player.y))
    z_value.setText(str(player.z))

search_button.clicked.connect(search_button_clicked)

admin_button.clicked.connect(lambda: change_value("Admin", current_player.pid))
name_button.clicked.connect(lambda: change_value("Name", current_player.pid))
char_class_button.clicked.connect(lambda: change_value("Class", current_player.pid))
specialty_button.clicked.connect(lambda: change_value("Specialty", current_player.pid))
level_button.clicked.connect(lambda: change_value("Level", current_player.pid))
contribute_button.clicked.connect(lambda: change_value("Contribute", current_player.pid))
exp_button.clicked.connect(lambda: change_value("Exp", current_player.pid))
gid_button.clicked.connect(lambda: change_value("GID", current_player.pid))
grole_button.clicked.connect(lambda: change_value("GRole", current_player.pid))
strength_button.clicked.connect(lambda: change_value("Strength", current_player.pid))
health_button.clicked.connect(lambda: change_value("Health", current_player.pid))
intelligence_button.clicked.connect(lambda: change_value("Intelligence", current_player.pid))
wisdom_button.clicked.connect(lambda: change_value("Wisdom", current_player.pid))
dexterity_button.clicked.connect(lambda: change_value("Dexterity", current_player.pid))
curhp_button.clicked.connect(lambda: change_value("CurHP", current_player.pid))
curmp_button.clicked.connect(lambda: change_value("CurMP", current_player.pid))
pupoint_button.clicked.connect(lambda: change_value("PUPoint", current_player.pid))
supoint_button.clicked.connect(lambda: change_value("SUPoint", current_player.pid))
killed_button.clicked.connect(lambda: change_value("Killed", current_player.pid))
map_button.clicked.connect(lambda: change_value("Map", current_player.pid))
x_button.clicked.connect(lambda: change_value("X", current_player.pid))
y_button.clicked.connect(lambda: change_value("Y", current_player.pid))
z_button.clicked.connect(lambda: change_value("Z", current_player.pid))


# ----- Start Application ----- #
window.show()

sys.exit(app.exec())