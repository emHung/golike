# 🎯 Golike Auto - Tool tự động làm nhiệm vụ Golike

Tool tự động làm nhiệm vụ trên Golike.net hỗ trợ TikTok, Facebook, Instagram.

## 📋 Tính năng

- ✅ Đăng nhập tự động với token
- ✅ Xem thông tin tài khoản (coin, tiền đợi duyệt)
- ✅ Xem danh sách job đang chờ duyệt
- ✅ Làm nhiệm vụ TikTok tự động
- ⏳ Làm nhiệm vụ Facebook (đang phát triển)
- ⏳ Làm nhiệm vụ Instagram (đang phát triển)

## 🔧 Cài đặt

### Trên Windows/Linux/Mac:

```bash
# Clone repo
git clone <repo-url>
cd golike-auto

# Cài đặt thư viện
pip install requests
```

### Trên Termux (Android):

```bash
# Cập nhật package
pkg update && pkg upgrade

# Cài đặt Python
pkg install python

# Cài đặt git
pkg install git

# Clone repo
git clone <repo-url>
cd golike-auto

# Cài đặt thư viện
pip install requests
```

## 🚀 Sử dụng

### 1. Lấy Authorization Token

1. Truy cập https://app.golike.net
2. Đăng nhập tài khoản
3. Nhấn F12 để mở DevTools
4. Chọn tab Network
5. Refresh trang (F5)
6. Tìm request đến `gateway.golike.net`
7. Xem Headers -> Authorization
8. Copy token (bỏ chữ "Bearer ")

### 2. Chạy chương trình

```bash
python main.py
```

### 3. Menu chính

```
🎯 GOLIKE AUTO - MENU CHÍNH
============================================================
1. 📊 Xem thông tin tài khoản
2. 🎵 Làm nhiệm vụ TikTok
3. 📘 Làm nhiệm vụ Facebook
4. 📷 Làm nhiệm vụ Instagram
0. 🚪 Thoát
============================================================
```

### 4. Xem danh sách tài khoản

```bash
python List_account.py
```

## 📁 Cấu trúc file

```
golike-auto/
├── main.py              # File chính với menu
├── golike_api.py        # API wrapper cho Golike
├── login.py             # Xử lý đăng nhập
├── List_account.py      # Xem danh sách tài khoản
├── ttc.py              # Code cũ (tham khảo)
├── auth.txt            # Lưu token (tự động tạo)
└── README.md           # Hướng dẫn
```

## 🎮 Hướng dẫn làm nhiệm vụ TikTok

1. Chọn menu `2. 🎵 Làm nhiệm vụ TikTok`
2. Chọn tài khoản TikTok muốn làm
3. Nhập số job muốn làm (0 = không giới hạn)
4. Tool sẽ tự động:
   - Lấy job từ Golike
   - Hoàn thành job
   - Nhận tiền
   - Lặp lại cho đến khi đủ số job

## ⚠️ Lưu ý

- Token sẽ được lưu vào file `auth.txt` để tự động đăng nhập lần sau
- Delay giữa các job là 3 giây để tránh spam
- Nếu không còn job, tool sẽ tự động dừng
- Nhấn Ctrl+C để dừng bất cứ lúc nào

## 🐛 Xử lý lỗi

### Token không hợp lệ
- Lấy token mới từ website
- Xóa file `auth.txt` và đăng nhập lại

### Không tìm thấy tài khoản
- Kiểm tra đã thêm tài khoản trên Golike chưa
- Kiểm tra token còn hạn không

### Không có job
- Đợi một lúc để có job mới
- Thử lại sau vài phút

## 📝 License

MIT License - Tự do sử dụng và chỉnh sửa

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Tạo issue hoặc pull request.
