import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import urllib.parse
from PyQt5.QtGui import QDesktopServices

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI-Programmierung")
        
        layout = QGridLayout()  # Ändern Sie das Layout zu QHBoxLayout
        layout_bottom = QVBoxLayout()

        # Menüleiste erstellen
        menubar = self.menuBar()

        # Dateimenü erstellen und zur Menüleiste hinzufügen
        filemenu = menubar.addMenu("File")

        # Aktion "Save" erstellen
        save = QAction("save", self)
        # Verknüpfen Sie das "triggered" Signal der Aktion "Save" mit der Methode menu_save
        save.triggered.connect(self.menu_save)

        # Aktion "Quit" erstellen
        quit = QAction("Quit", self)
        # Verknüpfen Sie das "triggered" Signal der Aktion "Quit" mit der Methode menu_quit
        quit.triggered.connect(self.menu_quit)

        Karte = QAction("Karte", self)
        Karte.triggered.connect(self.karte_anzeigen)

        Laden = QAction("Laden", self)
        Laden.triggered.connect(self.menu_laden)


        # Fügen Sie die Aktionen "Save" und "Quit" zum Dateimenü hinzu
        filemenu.addAction(save)
        filemenu.addAction(quit)

        # Das "File" Menü ist nun vollständig konfiguriert und enthält die Aktionen "Save" und "Quit".



        # Definition der Button-/Eingabefelder mit Art (Feld zum Bearbeiten, Rollmenu, Datumfeld, usw), Button-/Eingabefeldbreite wird definiert / Einen Rahmen um Button und Eingabefeld, "Funktion" zur Feldselektion
        Vorname = QLineEdit()
        Vorname.setObjectName("Vorname")  # Dem Button-/Eingabefelder einen Namen zuweisen (keine Beschriftung!) <<- Nicht zwingend erforderlich aber nützlich, damit später auf das Widget zugegriffen werden kann z.B. mit "findChild()"
        Vorname.setStyleSheet("border: 1px solid black;")
        Vorname.installEventFilter(self)

        Nachname = QLineEdit()
        Nachname.setObjectName("Nachname")  # Setzen Sie den Objektnamen auf "Nachname"
        Nachname.setFixedWidth(300)
        Nachname.setStyleSheet("border: 1px solid black;")
        Nachname.installEventFilter(self)

        ageSpinBox = QDateEdit()
        ageSpinBox.setObjectName("ageSpinBox")  # Setzen Sie den Objektnamen auf "ageSpinBox"
        ageSpinBox.setFixedWidth(300)
        ageSpinBox.setStyleSheet("border: 1px solid black;")
        ageSpinBox.installEventFilter(self) 

        Adresse = QLineEdit()
        Adresse.setObjectName("Adresse")  # Setzen Sie den Objektnamen auf "Adresse"
        Adresse.setFixedWidth(300)
        Adresse.setStyleSheet("border: 1px solid black;")
        Adresse.installEventFilter(self)

        PLZ = QLineEdit()
        PLZ.setObjectName("PLZ")  # Setzen Sie den Objektnamen auf "PLZ"
        PLZ.setFixedWidth(300)
        PLZ.setStyleSheet("border: 1px solid black;")
        PLZ.installEventFilter(self)

        Ort = QLineEdit()
        Ort.setObjectName("Ort")  # Setzen Sie den Objektnamen auf "Ort"
        Ort.setFixedWidth(300)
        Ort.setStyleSheet("border: 1px solid black;")
        Ort.installEventFilter(self)

        Land = QComboBox()
        Land.setObjectName("Land")  # Setzen Sie den Objektnamen auf "Land"
        Land.addItems(["Deutschlannd", "Frankreich", "Italien", "Schweiz"])
        Land.setFixedWidth(300)
        Land.installEventFilter(self)

        Save = QPushButton("Save")  #Erstellung Savebutton
        Save.clicked.connect(self.menu_save)  # Verknüpfen Sie das Signal clicked der Schaltfläche "Save" mit der Methode menu_save
        Karte = QPushButton("Karte")  #Erstellung Savebutton
        Karte.clicked.connect(self.karte_anzeigen)  # Verknüpfen Sie das Signal clicked der Schaltfläche "Save" mit der Methode menu_save
        Laden = QPushButton("Laden")  #Erstellung Savebutton
        Laden.clicked.connect(self.menu_laden)  # Verknüpfen Sie das Signal clicked der Schaltfläche "Save" mit der Methode menu_save




                                
        #Beschriftung aller Button-/Eingabefelder
        VornameLabel = QLabel("Vorname:") #Beschriftung aller Button-/Eingabefelder
        NachnameLabel = QLabel("Nachname:")
        GeburtstagLabel = QLabel("Geburtstag:")
        AdresseLabel = QLabel("Adresse:")
        PLZLabel = QLabel("PLZ:")
        OrtLabel = QLabel("Ort:")
        LandLabel = QLabel("Land:")

        # Hinzufügen der Button-/Eingabefelder zum Layout
        layout.addWidget(menubar)
        layout.addWidget(Vorname,1,1)
        layout.addWidget(Nachname,2,1)
        layout.addWidget(ageSpinBox,3,1)
        layout.addWidget(Adresse,4,1)
        layout.addWidget(PLZ,5,1)
        layout.addWidget(Ort,6,1)
        layout.addWidget(Land,7,1)

        layout_bottom.addWidget(Karte)
        layout_bottom.addWidget(Laden)
        layout_bottom.addWidget(Save)

        
        layout.addLayout(layout_bottom, 8, 0, 1, 2) 



        #Hinzufügen der Button-/Eingabefelderbeschriftung
        layout.addWidget(VornameLabel,1,0)
        layout.addWidget(NachnameLabel,2,0)
        layout.addWidget(GeburtstagLabel,3,0)
        layout.addWidget(AdresseLabel,4,0)
        layout.addWidget(PLZLabel,5,0)
        layout.addWidget(OrtLabel,6,0)
        layout.addWidget(LandLabel,7,0)

        # Zentrales Widget erstellen und layout hinzufügen / dient zur Organisiation des Hauptfenstern / Alle Widget gehören dem Center Widget an.
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenstergröße festlegen
        self.setGeometry(100, 100, 400, 200)  # Setzen Sie die Größe des Fensters

        # Fenster anzeigen
        self.show()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.FocusIn:  # Überprüfen, ob das Feld den Fokus erhält
            obj.setStyleSheet("border: 1px solid blue;")  # Blauen Rahmen setzen, wenn das Feld den Fokus erhält
        elif event.type() == QEvent.FocusOut:  # Überprüfen, ob das Feld den Fokus verliert
            obj.setStyleSheet("border: 1px solid black;")  # Schwarzen Rahmen setzen, wenn das Feld den Fokus verliert
        return super().eventFilter(obj, event)

    def menu_save(self):
        # Daten aus den Widgets abrufen
        vorname = self.findChild(QLineEdit, "Vorname").text()
        nachname = self.findChild(QLineEdit, "Nachname").text()
        geburtstag = self.findChild(QDateEdit, "ageSpinBox").date().toString("yyyy-MM-dd")
        adresse = self.findChild(QLineEdit, "Adresse").text()
        plz = self.findChild(QLineEdit, "PLZ").text()
        ort = self.findChild(QLineEdit, "Ort").text()
        land = self.findChild(QComboBox, "Land").currentText()
        QMessageBox.information(self, "Speichervorgang", "Deine Informationen wurden abgespeichert!")

        # Datei öffnen und Daten schreiben
        datei = open("output.txt", "w")
        datei.write(f"{vorname},{nachname},{geburtstag},{adresse},{plz},{ort},{land}\n")
        datei.close()  # Datei schließen

        print("Daten wurden in output.txt gespeichert.")

    def menu_quit(self):
        print("Menu Quit wurde gewählt...")
        self.close()  # Hauptfenster schließen = beenden!

    def karte_anzeigen(self):
        address = self.findChild(QLineEdit, "Adresse").text()
        plz = self.findChild(QLineEdit, "PLZ").text()
        ort = self.findChild(QLineEdit, "Ort").text()
        land = self.findChild(QComboBox, "Land").currentText()

        # URL für Google Maps zusammensetzen
        encoded_address = urllib.parse.quote(address)
        encoded_plz = urllib.parse.quote(plz)
        encoded_ort = urllib.parse.quote(ort)
        encoded_land = urllib.parse.quote(land)

        url = f"https://www.google.com/maps/place/{encoded_address}+{encoded_plz}+{encoded_ort}+{encoded_land}"

        # Google Maps im Standard-Webbrowser öffnen
        QDesktopServices.openUrl(QUrl(url))

    def menu_laden(self):

            # Dateidialog anzeigen, um die Datei auszuwählen
        file_path, _ = QFileDialog.getOpenFileName(self, "Datei auswählen", "", "Textdateien (*.txt)")
            
        if file_path:

            file = open(file_path, "r")
            data = file.readline().strip().split(",")  # Daten aus der Datei lesen und aufteilen
                
            vorname, nachname, geburtstag, adresse, plz, ort, land = data  # Daten auf Felder verteilen
            
            # Daten in die Felder eintragen
            self.findChild(QLineEdit, "Vorname").setText(vorname)
            self.findChild(QLineEdit, "Nachname").setText(nachname)
            # Annahme: Geburtstag ist ein QDateEdit-Feld, also umwandeln und setzen
            self.findChild(QDateEdit, "ageSpinBox").setDate(QDate.fromString(geburtstag, "yyyy-MM-dd"))
            self.findChild(QLineEdit, "Adresse").setText(adresse)
            self.findChild(QLineEdit, "PLZ").setText(plz)
            self.findChild(QLineEdit, "Ort").setText(ort)
                
             # Index des Landes im ComboBox finden und setzen
            index = self.findChild(QComboBox, "Land").findText(land)
            if index != -1:
                self.findChild(QComboBox, "Land").setCurrentIndex(index)
                
                QMessageBox.information(self, "Laden abgeschlossen", "Daten geladen.")
            else:
                QMessageBox.warning(self, "Keine Datei ausgewählt", "keine Datei ausgewählt.")

        file.close()  # Datei schließen
                


def main():
    app = QApplication(sys.argv)  # Qt Applikation
    fenster = Fenster()            # Instanz Fenster erstellen
    sys.exit(app.exec_())          # Applikations-Loop starten

if __name__ == '__main__':
    main()
