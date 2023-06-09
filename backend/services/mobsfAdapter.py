
import json
from typing import IO
from io import BytesIO, StringIO
import requests
import os
from flask import abort

class MobSFAdapter:
    def __init__(self,configRepository):
        self.config = configRepository.get()
    def safeRequest(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except requests.exceptions.ConnectionError as e:
                abort(400,description=f"Cannot connect to MobSF API")
            except requests.exceptions.MissingSchema as e:
                abort(400,description="Invalid MobSF API URL")
            return result
        return wrapper
    @safeRequest
    def upload(self,filename:str,file:IO):
        file.seek(0)
        files=[
        ('file',(filename,file,'application/octet-stream'))
        ]
        headers = {'Authorization': self.config['MOBSF_API_KEY']}
        url = self.config['MOBSF_URL']
        response = requests.post(f'{url}/api/v1/upload', files=files,headers=headers)
            
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.json())
            abort(response.status_code,description=f'Error sending file to MobSF: {response.status_code} {response.reason}')
    @safeRequest
    def scan(self,hash,scanType,filename):
        headers = {'Authorization': self.config['MOBSF_API_KEY']}
        url = self.config['MOBSF_URL']
        data = {
            "hash":hash,
            "scan_type":scanType,
            "file_name":filename
        }
        response = requests.post(f'{url}/api/v1/scan',data=data,headers=headers)
        
        if response.status_code == 200:
            return response.content
        else:
            print(response.json())
            abort(response.status_code,description=f'Error scanning file with MobSF: {response.status_code} {response.reason}')
    @safeRequest
    def getPDFReport(self,hash):
        url = self.config['MOBSF_URL']
        headers = {'Authorization': self.config['MOBSF_API_KEY']}
        response = requests.post(f'{url}/api/v1/download_pdf',data={
            "hash":hash,
        },headers=headers)
        if response.status_code == 200:
            return BytesIO(response.content)
        else:
            print(response.json())
            abort(response.status_code,description=f'Error getting report from MobSF: {response.status_code} {response.reason}')
