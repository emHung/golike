#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import time
from login import GolikeAuth

class GolikeAPI:
    def __init__(self, auth: GolikeAuth):
        self.auth = auth
        self.headers = auth.get_headers()
    
    def get_user_info(self):
        """Lấy thông tin tài khoản"""
        try:
            response = requests.get(
                'https://gateway.golike.net/api/users/me',
                headers=self.headers
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('success'):
                    user_data = data.get('data', {})
                    return {
                        'name': user_data.get('name', 'N/A'),
                        'coin': user_data.get('coin', 0),
                        'prices': user_data.get('prices', 0),
                        'role': user_data.get('role', 'N/A')
                    }
            return None
        except Exception as e:
            print(f"❌ Lỗi khi lấy thông tin: {e}")
            return None
    
    def get_pending_logs(self, limit=30, page=1):
        """Lấy danh sách job đang chờ duyệt"""
        try:
            timestamp = int(time.time())
            response = requests.get(
                f'https://gateway.golike.net/api/advertising/publishers/tiktok/logs?limit={limit}&log_type=pending&page={page}&_t={timestamp}',
                headers=self.headers
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('success'):
                    return data.get('data', [])
            return []
        except Exception as e:
            print(f"❌ Lỗi khi lấy logs: {e}")
            return []
    
    def get_accounts(self, platform):
        """Lấy danh sách tài khoản theo platform"""
        endpoints = {
            'tiktok': 'https://gateway.golike.net/api/tiktok-account',
            'facebook': 'https://gateway.golike.net/api/fb-account'
        }
        
        endpoint = endpoints.get(platform.lower())
        if not endpoint:
            return []
        
        try:
            response = requests.get(endpoint, headers=self.headers)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('success'):
                    raw_data = data.get('data', [])
                    
                    # Facebook có cấu trúc data.data
                    if platform.lower() == 'facebook' and isinstance(raw_data, dict):
                        return raw_data.get('data', [])
                    return raw_data
            return []
        except Exception as e:
            print(f"❌ Lỗi khi lấy tài khoản {platform}: {e}")
            return []
    
    def get_tiktok_jobs(self, account_id):
        """Lấy job TikTok"""
        try:
            response = requests.get(
                f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={account_id}&data=null',
                headers=self.headers
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('success'):
                    return data.get('data')
            return None
        except Exception as e:
            print(f"❌ Lỗi khi lấy job: {e}")
            return None
    
    def complete_tiktok_job(self, ads_id, account_id, async_type=1):
        """Hoàn thành job TikTok"""
        try:
            json_data = {
                'ads_id': ads_id,
                'account_id': account_id,
                'async': async_type,
            }
            
            response = requests.post(
                'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
                headers=self.headers,
                json=json_data
            )
            
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"❌ Lỗi khi hoàn thành job: {e}")
            return None
