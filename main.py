#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
from login import GolikeAuth
from golike_api import GolikeAPI

def clear_screen():
    """Xóa màn hình"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """In banner"""
    print("\n" + "="*60)
    print("🎯 GOLIKE AUTO - MENU CHÍNH")
    print("="*60)

def print_menu():
    """In menu chính"""
    print("\n1. 📊 Xem thông tin tài khoản")
    print("2. 🎵 Làm nhiệm vụ TikTok")
    print("3. 📘 Làm nhiệm vụ Facebook")
    print("4. 📷 Làm nhiệm vụ Instagram")
    print("0. 🚪 Thoát")
    print("="*60)

def show_user_info(api: GolikeAPI):
    """Hiển thị thông tin tài khoản"""
    clear_screen()
    print("\n" + "="*60)
    print("📊 THÔNG TIN TÀI KHOẢN")
    print("="*60)
    
    user_info = api.get_user_info()
    if user_info:
        # Lấy danh sách đợi duyệt trước để tính total_pending
        pending_logs = api.get_pending_logs(limit=30)
        total_pending = 0
        
        if pending_logs:
            for log in pending_logs:
                price = log.get('prices', 0)
                total_pending += price
        
        # Hiển thị thông tin tài khoản với total_pending tính từ danh sách job
        print(f"\n👤 Tên: {user_info['name']}")
        print(f"💰 Coin: {user_info['coin']:,}")
        print(f"⏳ Tiền đợi duyệt: {total_pending:,}")
        print(f"🎭 Role: {user_info['role']}")
    else:
        print("\n❌ Không thể lấy thông tin tài khoản")
    
    input("\n\nNhấn Enter để quay lại menu...")

def do_tiktok_jobs(api: GolikeAPI):
    """Làm nhiệm vụ TikTok"""
    clear_screen()
    print("\n" + "="*60)
    print("🎵 LÀM NHIỆM VỤ TIKTOK")
    print("="*60)
    
    # Lấy danh sách tài khoản TikTok
    accounts = api.get_accounts('tiktok')
    
    if not accounts:
        print("\n❌ Không tìm thấy tài khoản TikTok nào!")
        input("\nNhấn Enter để quay lại menu...")
        return
    
    print(f"\n📱 Tìm thấy {len(accounts)} tài khoản TikTok:")
    print("-"*60)
    for idx, acc in enumerate(accounts, 1):
        print(f"{idx}. @{acc.get('unique_username')} - {acc.get('nickname')}")
    print("-"*60)
    
    try:
        choice = int(input("\nChọn tài khoản (0 để quay lại): "))
        if choice == 0:
            return
        
        if choice < 1 or choice > len(accounts):
            print("❌ Lựa chọn không hợp lệ!")
            time.sleep(2)
            return
        
        selected_account = accounts[choice - 1]
        account_id = selected_account.get('id')
        
        print(f"\n✅ Đã chọn: @{selected_account.get('unique_username')}")
        
        # Nhập số job muốn làm
        num_jobs = int(input("\nNhập số job muốn làm (0 để làm không giới hạn): "))
        
        print("\n" + "="*60)
        print("🚀 BẮT ĐẦU LÀM JOB")
        print("="*60)
        
        job_count = 0
        total_earned = 0
        
        while True:
            if num_jobs > 0 and job_count >= num_jobs:
                break
            
            # Lấy job
            job = api.get_tiktok_jobs(account_id)
            
            if not job:
                print("\n⚠️ Không còn job nào!")
                break
            
            ads_id = job.get('id')
            object_id = job.get('object_id')
            object_type = job.get('object_type')
            price = job.get('price', 0)
            
            print(f"\n📌 Job #{job_count + 1}")
            print(f"   Type: {object_type}")
            print(f"   Object ID: {object_id}")
            print(f"   Price: {price:,}")
            
            # Hoàn thành job
            result = api.complete_tiktok_job(ads_id, account_id)
            
            if result and result.get('success'):
                job_count += 1
                total_earned += price
                print(f"   ✅ Hoàn thành! Tổng: {total_earned:,}")
            else:
                error_msg = result.get('message', 'Unknown error') if result else 'No response'
                print(f"   ❌ Lỗi: {error_msg}")
            
            # Delay giữa các job
            time.sleep(3)
        
        print("\n" + "="*60)
        print("📊 KẾT QUẢ")
        print("="*60)
        print(f"✅ Đã hoàn thành: {job_count} job")
        print(f"💰 Tổng thu nhập: {total_earned:,}")
        
    except ValueError:
        print("\n❌ Vui lòng nhập số hợp lệ!")
    except KeyboardInterrupt:
        print("\n\n⚠️ Đã dừng bởi người dùng!")
    except Exception as e:
        print(f"\n❌ Lỗi: {e}")
    
    input("\n\nNhấn Enter để quay lại menu...")

def do_facebook_jobs(api: GolikeAPI):
    """Làm nhiệm vụ Facebook"""
    clear_screen()
    print("\n" + "="*60)
    print("📘 LÀM NHIỆM VỤ FACEBOOK")
    print("="*60)
    print("\n⚠️ Chức năng đang phát triển...")
    input("\nNhấn Enter để quay lại menu...")

def do_instagram_jobs(api: GolikeAPI):
    """Làm nhiệm vụ Instagram"""
    clear_screen()
    print("\n" + "="*60)
    print("📷 LÀM NHIỆM VỤ INSTAGRAM")
    print("="*60)
    print("\n⚠️ Chức năng đang phát triển...")
    input("\nNhấn Enter để quay lại menu...")

def main():
    """Hàm main"""
    clear_screen()
    
    # Khởi tạo auth
    auth = GolikeAuth()
    
    # Kiểm tra token đã lưu
    saved_token = auth.load_token()
    
    if saved_token:
        print("🔑 Tìm thấy token đã lưu, đang đăng nhập...")
        success, user_data = auth.login(saved_token)
        
        if not success:
            print("\n❌ Token không hợp lệ hoặc đã hết hạn!")
            saved_token = None
    
    # Nếu chưa có token hoặc token không hợp lệ
    if not saved_token:
        print("\n" + "="*60)
        print("🔐 ĐĂNG NHẬP GOLIKE")
        print("="*60)
        print("\nVui lòng nhập Authorization Token:")
        print("(Lấy từ: https://app.golike.net -> F12 -> Network -> Headers)")
        
        token = input("\nToken: ").strip()
        
        if not token:
            print("\n❌ Token không được để trống!")
            return
        
        success, user_data = auth.login(token)
        
        if not success:
            print("\n❌ Đăng nhập thất bại!")
            return
    
    # Khởi tạo API
    api = GolikeAPI(auth)
    
    # Menu chính
    while True:
        clear_screen()
        print_banner()
        print_menu()
        
        try:
            choice = input("\nChọn chức năng: ").strip()
            
            if choice == '1':
                show_user_info(api)
            elif choice == '2':
                do_tiktok_jobs(api)
            elif choice == '3':
                do_facebook_jobs(api)
            elif choice == '4':
                do_instagram_jobs(api)
            elif choice == '0':
                print("\n👋 Tạm biệt!")
                break
            else:
                print("\n❌ Lựa chọn không hợp lệ!")
                time.sleep(1)
        
        except KeyboardInterrupt:
            print("\n\n👋 Tạm biệt!")
            break
        except Exception as e:
            print(f"\n❌ Lỗi: {e}")
            time.sleep(2)

if __name__ == "__main__":
    main()
