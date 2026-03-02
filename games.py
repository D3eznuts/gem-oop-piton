from abc import ABC, abstractmethod  
class Hero: 
    def __init__(self, nama, hp_awal): 
        self.nama = nama 
        # Enkapsulasi: HP bersifat Private (hanya bisa diakses di dalam class ini) 
        self.__hp = hp_awal 
 
    # GETTER: Cara resmi melihat HP 
    def get_hp(self): 
        return self.__hp 
 
    # SETTER: Cara resmi mengubah HP (dengan validasi) 
    def set_hp(self, nilai_baru): 
        if nilai_baru < 0: 
            self.__hp = 0  # HP tidak boleh negatif 
        elif nilai_baru > 1000: 
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.") 
            self.__hp = 1000 
        else: 
            self.__hp = nilai_baru 
 
 
 
    def diserang(self, damage): 
        # Kita pakai setter/getter bahkan di dalam class sendiri agar aman 
        sisa_hp = self.get_hp() - damage 
        self.set_hp(sisa_hp) 
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}") 
 
# -- Uji Coba -- 
hero1 = Hero("Layla", 100) 
 
# hero1.__hp = 9999     # GAGAL (Tidak akan mengubah hp asli) 
# print(hero1.__hp)     # ERROR (Tidak bisa dibaca langsung) 
 
hero1.set_hp(-50)       # Coba set negatif 
print(hero1.get_hp())   # Output: 0 (Karena dicegat oleh logika Setter)
 
 
print("\n--- Pertarungan Dimulai ---") 
# -- Main Program -- 
# Membuat Object (Instansiasi) 
hero1 = Hero("Layla", 100, 15) 
hero2 = Hero("Zilong", 120, 20) 
 
# Memanggil Method 
hero1.info() 
hero2.info()
hero1.serang(hero2) # Layla menyerang Zilong 
hero2.serang(hero1) # Zilong membalas

# Class Mage adalah anak dari class Hero 
class Mage(Hero): 
    def __init__(self, name, hp, attack_power, mana): 
        # Memanggil constructor milik Parent (Hero) 
        super().__init__(name, hp, attack_power) 
        self.mana = mana 
 
    def info(self): 
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}") 
     
    # Mage punya skill khusus 
    def skill_fireball(self, lawan): 
        if self.mana >= 20: 
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!") 
            self.mana -= 20 
            lawan.diserang(self.attack_power * 2) # Damage 2x lipat 
        else: 
            print(f"{self.name} gagal skill! Mana tidak cukup.") 
 
# -- Main Program Baru -- 
print("\n--- Update Class Hero ---") 
eudora = Mage("Eudora", 80, 30, 100) 
balmond = Hero("Balmond", 200, 10) 
 
eudora.info() 
eudora.serang(balmond)       # Serangan biasa (warisan dari Hero) 
eudora.skill_fireball(balmond) # Skill khusus Mage
 
# -- Uji Coba -- 
hero1 = Hero("Layla", 100) 
 
# hero1.__hp = 9999     # GAGAL (Tidak akan mengubah hp asli) 
# print(hero1.__hp)     # ERROR (Tidak bisa dibaca langsung) 
 
hero1.set_hp(-50)       # Coba set negatif 
print(hero1.get_hp())   # Output: 0 (Karena dicegat oleh logika Setter)

print(f"Mencoba akses paksa: {hero1._Hero__hp}") 

class GameUnit(ABC): 
     
    @abstractmethod 
    def serang(self, target): 
        pass 
 
    @abstractmethod 
    def info(self): 
        pass 
 
# 2. Implementasi pada Class Konkret 
class Hero(GameUnit): 
    def __init__(self, nama): 
        self.nama = nama 
     
    # Kita WAJIB membuat method serang, kalau tidak akan Error 
    def serang(self, target): 
        print(f"Hero {self.nama} menebas {target}!") 
 
    def info(self): 
        print(f"Saya adalah Hero: {self.nama}") 
 
class Monster(GameUnit): 
    def __init__(self, jenis): 
        self.jenis = jenis 
 
    # Implementasi serang versi Monster 
    def serang(self, target): 
        print(f"Monster {self.jenis} menggigit {target}!") 
 
    def info(self): 
        print(f"Saya adalah Monster: {self.jenis}") 
 
# -- Uji Coba -- 
# unit = GameUnit() # ERROR! Abstract class tidak bisa jadi objek. 
h = Hero("Alucard") 
m = Monster("Serigala") 
 
h.info() 
m.info()

class Archer(Hero): 
    def serang(self): 
        print(f"{self.nama} (Archer) memanah dari jauh! Jleb!") 
 
# Child Class 3 
class Fighter(Hero): 
    def serang(self): 
        print(f"{self.nama} (Fighter) memukul dengan pedang! Slash!") 
 
 
 
# -- Penerapan Polymorphism -- 
# Kita punya daftar hero campuran 
pasukan = [ 
    Mage("Eudora"), 
    Archer("Miya"), 
    Fighter("Zilong"), 
    Mage("Gord") 
] 
 
print("--- PERANG DIMULAI ---") 
 
# Satu perintah loop, tapi respon berbeda-beda (Polymorphism) 
for pahlawan in pasukan: 
    pahlawan.serang() 
    