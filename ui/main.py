import sys

from PyQt6.QtWidgets import QApplication

creators = ['hesam2079@gmail.com', 'amirhosseinfallah.1998@gmial.com']
app_name = 'Sport News Grabber'

# import welcome
#
# app = QApplication(sys.argv)
# window = welcome.ClickableLink('Sport News Grabber', ['hesam'], 5000)
# window.show()
# sys.exit(app.exec())

from input_values import InputWindow

app = QApplication(sys.argv)
window = InputWindow('Sport News Grabber', ['hesam'])
window.show()
team_name = window.get_team_name()
print(team_name)
sys.exit(app.exec())