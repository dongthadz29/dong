# golikett_core.py (Đặt trên GitHub)

# Built-in libraries
import os
import sys
import time
import socket
import requests
from time import sleep
from datetime import datetime

# Third-party libraries
import cloudscraper
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich import box
from pystyle import Colors, Colorate

# Màu sắc
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
purple = "\033[35m"
hong = "\033[1;95m"
thanh_xau = "\033[1;97m-> "

# Thời gian hiện tại
now = datetime.now()
date = now.strftime("Ngày: %d/%m/%Y")
thoigian = now.strftime("Giờ: %H:%M:%S")

# Lấy IP LAN
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_lan = s.getsockname()[0]
s.close()

# Lấy IP công cộng và vị trí
ip_public = requests.get("https://api.ipify.org").text
location_data = requests.get(f"https://ipinfo.io/{ip_public}/json").json()
city = location_data.get("city", "Unknown")
country = location_data.get("country", "Unknown")

# Kiểm tra kết nối mạng
def kiem_tra_mang():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
    except OSError:
        print("Mạng không ổn định hoặc bị mất kết nối. Vui lòng kiểm tra lại mạng.")
        sys.exit()

kiem_tra_mang()

# Hàm hiển thị banner
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    console = Console()
    panel1 = Panel("[#CCCCCC]╔═╗┌─┐┬  ┬┬┌─┌─┐\n║ ╦│ ││  │├┴┐├┤ \n╚═╝└─┘┴─┘┴┴ ┴└─┘[/]", box=box.ROUNDED, border_style="#FF9966")
    panel2 = Panel("[#FFFF66]Admin: Gia Thông[/]\n[#CCFFCC]Box Zalo: https://zalo.me/g/cdomty095\nTelegram: @Dongthadz[/]", box=box.ROUNDED, border_style="#FFCC66")
    panel3 = Panel("[#9966CC]Name: Tool Golike[/]\n[#FF9966]Version: 1.0[/]", box=box.ROUNDED, border_style="#66CC33")
    panel4 = Panel(f"[#6666FF]Ip: {ip_lan}[/]\n[#6666CC]Vị Trí: {city},{country}[/]", box=box.ROUNDED, border_style="#3333CC")
    panel5 = Panel(f"[#BBBBBB]{thoigian}\n{date}[/]", box=box.ROUNDED, border_style="#6666CC")
    console.print(Columns([panel1, panel2]))
    console.print(Columns([panel3, panel4, panel5]))

# Hàm chính của GoLike
def main():
    banner()
    console = Console()
    panel6 = Panel("[#FF9966]Lấy thông tin[/]", box=box.ROUNDED, border_style="#CCFFCC")
    console.print(Columns([panel6]))

    # Xử lý Authorization và Token
    try:
        with open("Authorization.txt", "x"):
            pass
        with open("token.txt", "x"):
            pass
    except:
        pass

    with open("Authorization.txt", "r") as Authorization, open("token.txt", "r") as t:
        author = Authorization.read().strip()
        token = t.read().strip()

    if not author:
        author = input("Nhập Authorization: ")
        token = input("Nhập Token: ")
        with open("Authorization.txt", "w") as Authorization, open("token.txt", "w") as t:
            Authorization.write(author)
            t.write(token)
    else:
        banner()
        panel7 = Panel("[#FF9966][[/][#CCFFCC]1[/][#FF9966]] Để sử dụng lại tài khoản Golike cũ[/]\n[#FF9966][[/][#CCFFCC]2[/][#FF9966]] Để thay đổi tài khoản Golike mới[/]", box=box.ROUNDED, border_style="#CCFFCC", title="Xác nhận thông tin", title_align="center")
        console.print(Columns([panel7]))
        select = input("Nhập số: ")
        kiem_tra_mang()
        if select == "2":
            for i in range(1, 101):
                sys.stdout.write(f"\r\x1b[38;5;157mĐANG TIẾN HÀNH XÓA AUTH CŨ\033[0m")
                sys.stdout.flush()
                sleep(0.03)
            os.system('cls' if os.name == 'nt' else 'clear')
            banner()
            console.print(Columns([Panel("[#FF9966]Lấy thông tin[/]", box=box.ROUNDED, border_style="#CCFFCC")]))
            author = input("Nhập Auth Golike Mới: ")
            token = input("Nhập Token Golike Mới: ")
            with open("Authorization.txt", "w") as Authorization, open("token.txt", "w") as t:
                Authorization.write(author)
                t.write(token)

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json;charset=utf-8',
        'Authorization': author,
        't': token,
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'Referer': 'https://app.golike.net/account/manager/bluesky',
    }

    scraper = cloudscraper.create_scraper()

    def chonacc():
        json_data = {}
        try:
            response = scraper.get('https://gateway.golike.net/api/bluesky-account', headers=headers, json=json_data).json()
            return response
        except:
            sys.exit()

    def nhannv(account_id):
        try:
            params = {'account_id': account_id, 'data': 'null'}
            response = scraper.get('https://gateway.golike.net/api/advertising/publishers/bluesky/jobs', headers=headers, params=params, json={})
            return response.json()
        except:
            sys.exit()

    def hoanthanh(ads_id, account_id):
        try:
            json_data = {'ads_id': ads_id, 'account_id': account_id, 'async': True, 'data': None}
            response = scraper.post('https://gateway.golike.net/api/advertising/publishers/bluesky/complete-jobs', headers=headers, json=json_data, timeout=6)
            return response.json()
        except:
            sys.exit()

    def baoloi(ads_id, object_id, account_id, loai):
        try:
            json_data1 = {
                'description': 'Tôi đã làm Job này rồi',
                'users_advertising_id': ads_id,
                'type': 'ads',
                'provider': 'tiktok',
                'fb_id': account_id,
                'error_type': 6,
            }
            scraper.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1)
            json_data2 = {'ads_id': ads_id, 'object_id': object_id, 'account_id': account_id, 'type': loai}
            scraper.post('https://gateway.golike.net/api/advertising/publishers/bluesky/skip-jobs', headers=headers, json=json_data2)
        except:
            sys.exit()

    # Chọn tài khoản
    chontktiktok = chonacc()
    def dsacc():
        if chontktiktok.get("status") != 200:
            console.print(Panel("[#FF9966]Auth hoặc Token sai[/]", box=box.ROUNDED, border_style="#CCFFCC"))
            sys.exit()
        acc_list = ""
        for i in range(len(chontktiktok["data"])):
            acc_list += f"[{i+1}] {chontktiktok['data'][i]['name']}\n"
        console.print(Panel(acc_list.strip(), title="Danh sách acc", box=box.ROUNDED, border_style="#CCFFCC"))

    dsacc()

    while True:
        try:
            luachon = int(input("Chọn tài khoản: "))
            if luachon > len(chontktiktok["data"]):
                luachon = int(input("Acc này không có trong danh sách, nhập lại: "))
            account_id = chontktiktok["data"][luachon - 1]["id"]
            break
        except:
            print("Sai định dạng")

    while True:
        try:
            banner()
            console.print(Panel("[#FF9966]Setup làm nhiệm vụ[/]", box=box.ROUNDED, border_style="#CCFFCC"))
            delay = int(input("Nhập delay: "))
            break
        except:
            print("Sai Định Dạng")

    proxy_input = input("Nhập proxy (host:port hoặc user:pass@host:port), Enter nếu không dùng đến: ").strip()
    proxies = {"http": f"http://{proxy_input}", "https": f"http://{proxy_input}"} if proxy_input else None

    banner()
    console.print(Panel("[#FF9966][[/][#CCFFCC]1[/][#FF9966]] Để làm nhiệm vụ follow và tim[/]\n[#FF9966][[/][#CCFFCC]2[/][#FF9966]] Để làm nhiệm vụ follow[[/][#CCFFCC]OFF[/][#FF9966]][/]\n[#FF9966][[/][#CCFFCC]3[/][#FF9966]] Để làm nhiệm vụ tim[[/][#CCFFCC]OFF[/][#FF9966]][/]", box=box.ROUNDED, border_style="#CCFFCC", title="Chọn nhiệm vụ", title_align="center"))

    while True:
        try:
            loai_nhiem_vu = int(input("Chọn loại nv: "))
            if loai_nhiem_vu in [1, 2, 3]:
                break
            else:
                print("Vui lòng chọn số từ 1 đến 3")
        except:
            print("Sai định dạng! Vui lòng nhập số.")

    dem = 0
    tong = 0
    dsaccloi = []
    accloi = ""
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    print(f"\x1b[38;5;157m╭──────────────────── Console ────────────────────╮\033[0m")
    print(f"\x1b[38;5;157m│\033[0m \x1b[38;5;216m[\033[0m\x1b[38;5;157m!\033[0m\x1b[38;5;216m] Chưa có dữ liệu thực hiện nhiệm vụ \033[0m         \x1b[38;5;157m│\033[0m")
    print(f"\x1b[38;5;157m╰─────────────────────────────────────────────────╯\033[0m")

    while True:
        print('\r\x1b[38;5;157mĐang tìm nhiệm vụ\033[0m', end="\r")
        max_retries = 3
        retry_count = 0
        nhanjob = None

        while retry_count < max_retries:
            try:
                nhanjob = nhannv(account_id)
                if nhanjob and nhanjob.get("status") == 200 and nhanjob["data"].get("link") and nhanjob["data"].get("object_id"):
                    break
                else:
                    retry_count += 1
                    time.sleep(2)
            except:
                retry_count += 1
                time.sleep(1)

        if not nhanjob or retry_count >= max_retries:
            continue

        ads_id = nhanjob["data"]["id"]
        link = nhanjob["data"]["link"]
        object_id = nhanjob["data"]["object_id"]
        job_type = nhanjob["data"]["type"]

        if (loai_nhiem_vu == 1 and job_type not in ["follow", "like"]) or \
           (loai_nhiem_vu == 2 and job_type != "follow") or \
           (loai_nhiem_vu == 3 and job_type != "like"):
            baoloi(ads_id, object_id, account_id, job_type)
            continue

        for remaining_time in range(delay, -1, -1):
            color = "\x1b[38;5;157m" if remaining_time % 2 == 0 else "\x1b[38;5;157m"
            print(f"\r{color}Đang thực hiện nhiệm vụ[{remaining_time}s] ", end="")
            time.sleep(1)
        print("\r                          \r", end="")
        color = "\x1b[38;5;157m"
        print(f"\r{color}Đang nhận tiền", end="\r")

        max_attempts = 2
        attempts = 0
        nhantien = None
        while attempts < max_attempts:
            try:
                nhantien = hoanthanh(ads_id, account_id)
                if nhantien and nhantien.get("status") == 200:
                    break
            except:
                pass
            attempts += 1

        if nhantien and nhantien.get("status") == 200:
            dem += 1
            tien = nhantien["data"]["prices"]
            tong += tien
            local_time = time.localtime()
            hour, minute, second = local_time.tm_hour, local_time.tm_min, local_time.tm_sec
            h = f"0{hour}" if hour < 10 else hour
            m = f"0{minute}" if minute < 10 else minute
            s = f"0{second}" if second < 10 else second
            banner()
            console.print(Panel(f"[#FF9966]Tổng nhiệm vụ đã làm: {dem} job[/]\n[#FF9966]Tổng tiền: {tong}đ[/]", box=box.ROUNDED, border_style="#CCFFCC", title="Thông số", title_align="center"))
            console.print(Panel(f"[#FF9966][[/][#CCFFCC]{h}:{m}:{s}[/][#FF9966]] Thực hiện thành công job {job_type} +{tien}đ[/]", box=box.ROUNDED, border_style="#CCFFCC", title="Console", title_align="center"))
            time.sleep(0.7)
        else:
            try:
                baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
                print("                                              ", end="\r")
                print("\x1b[38;5;157mBỏ qua nhiệm vụ\033[0m ", end="\r")
                sleep(1)
            except:
                pass

if __name__ == "__main__":
    main()
