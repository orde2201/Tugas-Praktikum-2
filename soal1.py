from abc import ABC, abstractmethod  # Mengimpor modul ABC (Abstract Base Class) dan decorator abstractmethod

# Kelas abstrak Plant menggunakan ABC
class Plant(ABC):
    # Constructor untuk inisialisasi properti dasar tanaman
    def __init__(self, name, water_needs, fertilizer_needs):
        self.name = name                   # Nama tanaman
        self.water_needs = water_needs     # Kebutuhan air normal (dalam liter)
        self.fertilizer_needs = fertilizer_needs  # Kebutuhan pupuk normal (dalam kg)
    
    # Metode abstrak yang HARUS diimplementasikan oleh kelas turunan
    # Decorator @abstractmethod memastikan bahwa kelas turunan harus mengimplementasikan metode ini
    @abstractmethod
    def grow(self):
        pass
    
    # Metode untuk menghitung kebutuhan air dan pupuk berdasarkan kondisi cuaca
    def calculate_needs(self, rainfall, soil_moisture):
        # Menghitung kebutuhan air yang disesuaikan
        # Jika hujan >= 5mm, kebutuhan air dikurangi sebanding dengan hujan (0.5 per mm)
        # Jika hujan < 5mm, kebutuhan air tetap normal
        self.needWater = max(0, self.water_needs - (rainfall * 0.5)) if rainfall >= 5 else self.water_needs
        
        # Menghitung kebutuhan pupuk yang disesuaikan
        # Jika kelembaban tanah >= 50%, kebutuhan pupuk dikurangi menjadi 80% dari normal
        # Jika kelembaban tanah < 50%, kebutuhan pupuk tetap normal
        self.fertilizerNeeds = self.fertilizer_needs * 0.8 if soil_moisture >= 50 else self.fertilizer_needs
    
    # Metode untuk menampilkan kebutuhan yang telah disesuaikan
    def show_needs(self):
        print(f"{self.name} - Adjusted Water Needs: {self.needWater} liters")
        print(f"{self.name} - Adjusted Fertilizer Needs: {self.fertilizerNeeds} kg\n")

# Kelas turunan RicePlant yang mengimplementasikan Plant
class RicePlant(Plant):
    # Constructor untuk tanaman padi
    def __init__(self):
        # Memanggil constructor dari kelas induk dengan nilai spesifik untuk padi
        super().__init__("Rice", 20, 5)  # Padi membutuhkan 20L air dan 5kg pupuk
    
    # Implementasi metode grow yang merupakan metode abstrak dari kelas induk
    # Implementasi ini WAJIB karena metode ini ditandai sebagai abstrak di kelas induk
    def grow(self):
        print(f"{self.name} is growing in the paddy field")

# Kelas turunan CornPlant yang mengimplementasikan Plant
class CornPlant(Plant):
    # Constructor untuk tanaman jagung
    def __init__(self):
        # Memanggil constructor dari kelas induk dengan nilai spesifik untuk jagung
        super().__init__("Corn", 25, 8)  # Jagung membutuhkan 25L air dan 8kg pupuk
    
    # Implementasi metode grow untuk jagung
    def grow(self):
        print(f"{self.name} is growing in the farm")

# Fungsi untuk simulasi cuaca dan kebutuhan tanaman
def simulate_weather():
    # Membuat array dari objek tanaman yang berbeda
    plants = [RicePlant(), CornPlant()]
    
    # Data cuaca untuk masing-masing tanaman
    weather_data = [
        {"rainfall": 10, "soil_moisture": 75},  # Data untuk Rice - hujan banyak, tanah lembab
        {"rainfall": 2, "soil_moisture": 40}    # Data untuk Corn - hujan sedikit, tanah kering
    ]
    
    # Melakukan iterasi untuk setiap tanaman dan data cuacanya
    # zip() menggabungkan dua list menjadi pasangan item
    for plant, data in zip(plants, weather_data):
        plant.grow()  # Memanggil metode grow (polimorfisme - setiap tanaman memiliki implementasi berbeda)
        print(f"Weather Report: Rainfall = {data['rainfall']} mm, Soil Moisture = {data['soil_moisture']}%")
        plant.calculate_needs(data['rainfall'], data['soil_moisture'])  # Menghitung kebutuhan berdasarkan cuaca
        plant.show_needs()  # Menampilkan kebutuhan yang disesuaikan

# Jalankan simulasi
simulate_weather()
