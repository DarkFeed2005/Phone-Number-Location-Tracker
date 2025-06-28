# File: main.py
import sys
import phonenumbers
from phonenumbers import geocoder, carrier
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from opencage.geocoder import OpenCageGeocode
import folium
import webbrowser

API_KEY = "eb927c8c90184db5a9db0835499dd54a"  # 🔐 Replace with your actual OpenCage key

class NumberLocator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📍 Phone Number Location Finder")
        self.setFixedWidth(400)

        layout = QVBoxLayout()

        self.label = QLabel("Enter phone number (e.g., +94xxxxxxxx):")
        layout.addWidget(self.label)

        self.input = QLineEdit()
        layout.addWidget(self.input)

        self.button = QPushButton("Find Location")
        self.button.clicked.connect(self.find_location)
        layout.addWidget(self.button)

        self.output = QLabel("")
        layout.addWidget(self.output)

        self.setLayout(layout)

    def find_location(self):
        number = self.input.text()
        try:
            # Parse and get general location and carrier
            parsed_number = phonenumbers.parse(number)
            location = geocoder.description_for_number(parsed_number, "en")
            service_provider = carrier.name_for_number(parsed_number, "en")

            # Get coordinates via OpenCage
            geocoder_api = OpenCageGeocode(API_KEY)
            results = geocoder_api.geocode(location)

            if results and len(results):
                lat = results[0]['geometry']['lat']
                lng = results[0]['geometry']['lng']
                
                # Generate map
                map_location = folium.Map(location=[lat, lng], zoom_start=10)
                folium.Marker([lat, lng], popup=location).add_to(map_location)
                map_file = "location_map.html"
                map_location.save(map_file)
                
                self.output.setText(f"📍 {location}\n📡 {service_provider}\n🌐 Opening map…")
                webbrowser.open(map_file)
            else:
                self.output.setText("❗Location not found. Try a different number.")
        except Exception as e:
            self.output.setText(f"⚠️ Error: {e}")

app = QApplication(sys.argv)
window = NumberLocator()
window.show()
sys.exit(app.exec_())