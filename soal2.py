class Employee:
    # Constructor/inisialisasi untuk objek employee
    # Menyimpan data dasar karyawan: nama, posisi, jam kerja, dan tugas yg diselesaikan
    def __init__(self, name, role, hours_worked, task_completed):
        self.name = name                   # Nama karyawan 
        self.role = role                   # Posisi/jabatan 
        self.hours_worked = hours_worked   # Total jam kerja 
        self.task_completed = task_completed # Jumlah tugas yang diselesaikan
    
    # Metode work dibuat "kosong" dan akan diisi oleh kelas turunan
    # Ini adalah contoh abstraksi - setiap jenis karyawan akan bekerja dengan cara berbeda
    def work(self):
        pass
    
    # Metode evaluate_performance juga dibuat "kosong" untuk diisi kelas turunan
    # Ini karena cara mengevaluasi performa berbeda-beda untuk tiap posisi
    def evaluate_performance(self):
        pass


class SoftwareEngineer(Employee):
    # Constructor untuk Software Engineer
    # Perhatikan role sudah ditetapkan "Software Engineer" jadi tidak perlu diinput lagi
    def __init__(self, name, hours_worked, task_completed):
        # Panggil constructor parent dengan role yang sudah fixed
        super().__init__(name, "Software Engineer", hours_worked, task_completed)
    
    # Implementasi cara kerja software engineer
    def work(self):
        print(f"{self.name} (Software Engineer) is coding.")
    
    # Implementasi cara evaluasi performa software engineer
    # Software Engineer dinilai dengan ratio tugas/jam kerja
    def evaluate_performance(self):
        # Hitung ratio performa (task/jam), hindari division by zero
        performance_ratio = self.task_completed / self.hours_worked if self.hours_worked > 0 else 0
        
        # Tentukan rating berdasarkan ratio:
        # - High: >= 1 task per jam
        # - Medium: >= 0.5 task per jam
        # - Low: < 0.5 task per jam
        if performance_ratio >= 1:
            return "High Performance"
        elif performance_ratio >= 0.5:
            return "Medium Performance"
        else:
            return "Low Performance"


class DataScientist(Employee):
    # Constructor untuk Data Scientist
    def __init__(self, name, hours_worked, task_completed):
        # Panggil constructor parent dengan role yang sudah fixed
        super().__init__(name, "Data Scientist", hours_worked, task_completed)
    
    # Implementasi cara kerja data scientist
    def work(self):
        print(f"{self.name} (Data Scientist) is analyzing data.")
    
    # Implementasi cara evaluasi performa data scientist
    # Data Scientist punya standar performa yang berbeda dari Software Engineer
    def evaluate_performance(self):
        # Hitung ratio performa
        performance_ratio = self.task_completed / self.hours_worked if self.hours_worked > 0 else 0
        
        # Data scientist punya threshold yang lebih rendah karena analisis data biasanya lebih kompleks
        # - High: >= 0.8 task per jam
        # - Medium: >= 0.4 task per jam
        # - Low: < 0.4 task per jam
        if performance_ratio >= 0.8:
            return "High Performance"
        elif performance_ratio >= 0.4:
            return "Medium Performance"
        else:
            return "Low Performance"


class ProductManager(Employee):
    # Constructor untuk Product Manager
    def __init__(self, name, hours_worked, task_completed):
        # Panggil constructor parent dengan role yang sudah fixed
        super().__init__(name, "Product Manager", hours_worked, task_completed)
    
    # Implementasi cara kerja product manager
    def work(self):
        print(f"{self.name} (Product Manager) is managing the product roadmap.")
    
    # Implementasi cara evaluasi performa product manager
    def evaluate_performance(self):
        # Hitung ratio performa
        performance_ratio = self.task_completed / self.hours_worked if self.hours_worked > 0 else 0
        
        # Product Manager punya standar evaluasi sendiri:
        # - High: >= 1 task per jam
        # - Medium: >= 0.6 task per jam (lebih tinggi dari DS tapi sama dengan SE untuk high)
        # - Low: < 0.6 task per jam
        if performance_ratio >= 1:
            return "High Performance"
        elif performance_ratio >= 0.6:
            return "Medium Performance"
        else:
            return "Low Performance"


# Fungsi untuk menampilkan performa karyawan
# Bisa menerima objek dari tipe karyawan apapun (polymorphism)
def show_performance(employee):
    employee.work()  # Panggil metode work (akan berbeda tergantung tipe karyawan)
    rating = employee.evaluate_performance()  # Evaluasi performa (juga berbeda per tipe)
    print(f"Performance Rating: {rating}\n")


# Buat beberapa contoh karyawan
alice = SoftwareEngineer("Alice", 40, 45)  # 45 tugas dalam 40 jam
bob = DataScientist("Bob", 50, 20)  # 20 tugas dalam 50 jam
charlie = ProductManager("Charlie", 45, 30)  # 30 tugas dalam 45 jam
david = SoftwareEngineer("David", 30, 10)  # 10 tugas dalam 30 jam

# Tampilkan performa masing-masing karyawan
show_performance(alice)    # Alice: ratio 45/40 = 1.125 (High Performance)
show_performance(bob)      # Bob: ratio 20/50 = 0.4 (Medium Performance)
show_performance(charlie)  # Charlie: ratio 30/45 = 0.67 (Medium Performance)
show_performance(david)    # David: ratio 10/30 = 0.33 (Low Performance)
