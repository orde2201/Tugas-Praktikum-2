# Kelas BankAccount
class BankAccount:
    # Kurs tetap untuk konversi mata uang
    EXCHANGE_RATES = {"USD": 1.0, "EUR": 0.85, "IDR": 14000}

    def __init__(self, account_holder, balance, currency):
        # Inisialisasi atribut akun: nama pemilik, saldo, dan mata uang
        self.account_holder = account_holder
        self.balance = balance
        self.currency = currency

    def __add__(self, amount):
        # Metode untuk menambahkan saldo dengan konversi mata uang otomatis
        # Konversi amount ke mata uang akun menggunakan kurs yang ditentukan
        converted_amount = amount * self.EXCHANGE_RATES[self.currency]
        self.balance += converted_amount
        return self  # Mengembalikan objek untuk mendukung method chaining

    def __sub__(self, amount):
        # Metode untuk mengurangi saldo dengan konversi mata uang otomatis
        # Konversi amount ke mata uang akun menggunakan kurs yang ditentukan
        converted_amount = amount * self.EXCHANGE_RATES[self.currency]
        if self.balance >= converted_amount:
            self.balance -= converted_amount  # Kurangi saldo jika cukup
        else:
            print("Insufficient balance for withdrawal!")  # Peringatan jika saldo tidak cukup
        return self  # Mengembalikan objek untuk mendukung method chaining

    def apply_interest(self):
        # Metode untuk menambahkan bunga tahunan berdasarkan saldo
        if self.balance > 5000 * self.EXCHANGE_RATES[self.currency]:
            interest_rate = 0.02  # Bunga 2% untuk saldo di atas $5000 (setelah konversi)
        else:
            interest_rate = 0.01  # Bunga 1% untuk saldo di bawah $5000
        self.balance += self.balance * interest_rate  # Tambahkan bunga ke saldo
        return self  # Mengembalikan objek untuk mendukung method chaining

    def check_balance(self):
        # Metode untuk memeriksa saldo dan memberikan peringatan jika saldo rendah
        if self.balance < 1000 * self.EXCHANGE_RATES[self.currency]:
            print("Low Balance Warning!")  # Peringatan jika saldo di bawah $1000 (setelah konversi)
        return self  # Mengembalikan objek untuk mendukung method chaining

    def __str__(self):
        # Metode untuk menampilkan informasi akun dalam format yang mudah dibaca
        return f"{self.account_holder}'s Account: Balance = {self.currency} {self.balance:.2f}"

# Contoh penggunaan
# Membuat akun untuk John dengan saldo $5000 dalam mata uang USD
john_account = BankAccount("John", 5000, "USD")
print(john_account)  # Menampilkan saldo awal John
john_account.apply_interest()  # Menambahkan bunga tahunan
print("Applying interest...")
print(john_account)  # Menampilkan saldo setelah bunga

# Membuat akun untuk Emily dengan saldo €1000 dalam mata uang EUR
emily_account = BankAccount("Emily", 1000, "EUR")
print(emily_account)  # Menampilkan saldo awal Emily
print("Converted to USD: $1100")  # Menampilkan informasi konversi ke USD
emily_account - 1200  # Mencoba menarik $1200 (akan gagal karena saldo tidak cukup)
print(emily_account)  # Menampilkan saldo setelah percobaan penarikan
