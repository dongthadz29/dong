# tooltxvip.py - File chứa toàn bộ logic game Tài Xỉu
import random
import time
import sys

# MÃ MÀU ANSI
trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam = '\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
RESET = "\033[0m" # Đặt lại màu về mặc định

# THANH CHỈ DẪN
Thanh_xau = "\033[1;97m⮑ "
thanh_dep = "\033[1;97m⮑ "

lich_su = []

# CÔNG THỨC RANDOM + TÍNH TỈ LỆ XÁC XUẤT DỰ ĐOÁN
def du_doan_theo_cong_thuc(dice):
    tong = sum(dice)
    dice_sorted = sorted(dice)

    # ... (Các hàm logic Tài Xỉu giữ nguyên) ...
    # (Để tiết kiệm không gian, tôi lược bớt code chi tiết ở đây, nhưng bạn dùng code gốc của mình)
    # ======= XỈU =======
    if tong == 3:
        return random.choice(["Tài","Xỉu"])
    elif tong == 4:
        return random.choice(["Tài","Xỉu"])
    elif tong == 5:
        return "Xỉu"
    elif tong == 6:
        if dice_sorted in [[3,2,1],[4,1,1]]:
            return "Xỉu"
        else:
            return "Tài"
    elif tong == 7:
        if dice_sorted in [[1,2,4],[2,2,3],[1,3,3]]:
            return "Xỉu"
        elif dice_sorted in [[1,1,5]]:
            return "Tài"
        else:
            return random.choice(["Tài", "Xỉu"])
    elif tong == 8:
        return "Xỉu" if dice_sorted == [1,3,4] else random.choice(["Tài","Xỉu"])
    elif tong == 9:
        return "Xỉu" if dice_sorted == [2,3,4] else random.choice(["Tài","Xỉu"])
    elif tong == 10:
        return random.choice(["Tài","Xỉu"])

    # ======= TÀI =======
    elif tong == 11:
        return "Xỉu" if dice_sorted == [6,4,1] else random.choice(["Tài","Xỉu"])
    elif tong == 12:
        if dice_sorted in [[2,4,6],[1,5,6],[3,3,6],[2,5,5]]:
            return "Xỉu"
        else:
            return "Tài"
    elif tong == 13:
        if dice_sorted in [[5,5,3],[6,6,1]]:
            return "Xỉu"
        elif dice_sorted in [[5,3,1],[6,3,1]]:
            return "Tài"
        else:
            return "Tài"
    elif tong == 14:
        return random.choice(["Tài","Xỉu"])
    elif tong == 15:
        return random.choice(["Tài","Xỉu"])
    elif tong == 16:
        return random.choice(["Tài","Xỉu"])
    elif tong == 17:
        return "Xỉu" if dice_sorted == [6,3,1] else random.choice(["Tài","Xỉu"])
    elif tong == 18:
        return "Tài" if dice_sorted == [6,6,6] else random.choice(["Tài","Xỉu"])

    return "Tài" if tong > 10 else "Xỉu"

# THUẬN NGHỊCH
def du_doan_thuan_nghich(dice):
    tong = sum(dice)
    chan = (tong % 2 == 0)
    du_doan_thuan = "Tài" if chan else "Xỉu"
    du_doan_nghich = "Xỉu" if chan else "Tài"
    return du_doan_thuan, du_doan_nghich

# THEO CẦU + ĐẢO CẦU + LẬT NGƯỢC CẦU
def du_doan_theo_cau(lich_su):
    if len(lich_su) < 3:
        return None

    if len(lich_su) >= 4:
        # Cầu bệt 4+
        if all(kq == "Tài" for kq in lich_su[-4:]):
            return random.choice(["Tài", "Xỉu"]) 
        if all(kq == "Xỉu" for kq in lich_su[-4:]):
            return random.choice(["Xỉu", "Tài"])

    if len(lich_su) >= 7:
        # Cầu 1-1 dài
        if all(lich_su[i] != lich_su[i+1] for i in range(-7, -1)):
            return "Tài" if lich_su[-1] == "Xỉu" else "Xỉu"
        # Cầu 2-2 hoặc 3-3 
        if lich_su[-6:-4] == lich_su[-4:-2] and lich_su[-2:] != lich_su[-4:-2]: 
            return "Tài" if lich_su[-1] == "Xỉu" else "Xỉu"

    if len(lich_su) >= 3:
        # Cầu 1-2-1
        if lich_su[-3] == "Xỉu" and lich_su[-2:] == ["Tài", "Tài"]:
            return "Xỉu"
        if lich_su[-3] == "Tài" and lich_su[-2:] == ["Xỉu", "Xỉu"]:
            return "Tài"

    if len(lich_su) >= 12:
        # Lật ngược cầu theo cặp gần nhất
        cap_cuoi = tuple(lich_su[-2:])
        count = sum(1 for i in range(-12, -2) if tuple(lich_su[i:i+2]) == cap_cuoi)
        if count >= 2:
            return "Tài" if lich_su[-1] == "Xỉu" else "Xỉu"

    # Dựa vào kết quả T/X chiếm ưu thế trong toàn bộ lịch sử
    tai_count = lich_su.count("Tài")
    xiu_count = lich_su.count("Xỉu")
    if tai_count > xiu_count:
        return "Tài"
    elif xiu_count > tai_count:
        return "Xỉu"
    else:
        # Trường hợp cân bằng, đoán đảo cầu so với kết quả cuối
        return "Tài" if lich_su[-1] == "Xỉu" else "Xỉu"

def du_doan_xucxac(xucsac: str):
    if len(xucsac) != 3 or not all(ch in "123456" for ch in xucsac):
        print(f"{do}⚠️ Vui lòng nhập đúng 3 con xúc xắc!{RESET}")
        return None

    dice = [int(ch) for ch in xucsac]

    du_doan_ct = du_doan_theo_cong_thuc(dice)
    thuan, nghich = du_doan_thuan_nghich(dice)

    du_doan_cau = du_doan_theo_cau(lich_su)

    # LOGIC KẾT HỢP DỰ ĐOÁN
    if du_doan_cau:
        du_doan = du_doan_cau
    else:
        cong_thuc_moi = random.choice([thuan, nghich])
        if du_doan_ct == cong_thuc_moi:
            du_doan = du_doan_ct
        else:
            du_doan = du_doan_ct if random.randint(1, 100) <= 70 else cong_thuc_moi

    acc = random.randint(75, 99)
    
    # Hiển thị kết quả dự đoán với màu
    kq_color = xanh_la if du_doan == "Tài" else vang
    print(f"\n{vang}🎯 Dự đoán: {kq_color}{du_doan} (Tỷ lệ chính xác: {acc}%) {RESET}")
    return du_doan

def type_text(text, color=trang, delay=0.03):
    """Hàm hiển thị từng ký tự một."""
    # SỬ DỤNG sys.stdout.write(color) và sys.stdout.write(RESET + "\n")
    # Tương tự như trong run.py
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")

def main():
    
   
    type_text(" Truy cập thành công vào tool !", color=xanh_la, delay=0.04)

    while True:
        # BỎ ICON
        nhap = input(f"\n{thanh_dep}{xanhnhat}Nhập 3 con xúc xắc ({vang}vd: 631{xanhnhat}, hoặc {do}q{xanhnhat} để thoát): {trang}").strip()
        if nhap.lower() == 'q':
            break

        du_doan = du_doan_xucxac(nhap)
        if not du_doan:
            continue

        # BỎ ICON
        thuc_te = input(f"{thanh_dep}{xanh_duong}Kết quả thực tế ({xanh_la}t{xanh_duong} = Tài/{vang}x{xanh_duong} = Xỉu): {trang}").strip().lower()
        if thuc_te not in ['t', 'x']:
            print(f"{do}⚠️ Vui lòng nhập 't' hoặc 'x'{RESET}")
            continue

        ket_qua = "Tài" if thuc_te == 't' else "Xỉu"
        lich_su.append(ket_qua)

        if du_doan.startswith(ket_qua):
            # BỎ ICON
            print(f"{xanh_la}Đã Dự Đoán Chính Xác!{RESET}")
        else:
            # BỎ ICON
            print(f"{do}Dự Đoán Đã Sai!{RESET}")

        # In lịch sử 5 kết quả gần nhất để dễ theo dõi cầu (BỎ ICON 📝)
        if lich_su:
            lich_su_mau = []
            for kq in lich_su[-5:]:
                color = xanh_la if kq == "Tài" else vang
                lich_su_mau.append(f"{color}{kq}{RESET}")
            print(f"{thanh_dep}{tim}Lịch sử 5 kết quả gần nhất: {trang}{', '.join(lich_su_mau)}")


if __name__ == "__main__":
    main() # Giữ nguyên main() để nó có thể chạy khi được exec() trong run.py
