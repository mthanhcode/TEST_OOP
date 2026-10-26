class DienThoai:
    def __init__(self, MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan):
        self.MaMay = MaMay
        self.TenMay = TenMay
        self.HangSanXuat = HangSanXuat
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan

    def thongtindienthoai(self):
        print(f"Ma may: {self.MaMay}")
        print(f"Ten may: {self.TenMay}")
        print(f"Hang san xuat: {self.HangSanXuat}")
        print(f"Dung luong pin: {self.DungLuongPin} mAh")
        print(f"Gia ban: {self.GiaBan} VND")


if __name__ == "__main__":
    dt01 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    dt02 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

    dt01.thongtindienthoai()
    print()
    dt02.thongtindienthoai()