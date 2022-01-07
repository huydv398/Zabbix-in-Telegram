# -*- coding: utf-8 -*-

tg_key = "XYZ"  # <--telegram bot api key- Điền api-token key vào đây

zbx_tg_prefix = "zbxtg"  
zbx_tg_tmp_dir = "/var/tmp/" + zbx_tg_prefix  
zbx_tg_signature = False

zbx_tg_update_messages = True
zbx_tg_matches = {
    "problem": "PROBLEM: ",
    "ok": "OK: "
}

zbx_server = "http://127.0.0.1/zabbix/"  #Thay đổi đại chỉ đường dẫn IP full. 
zbx_api_user = "Admin" # <--thay thông tin đăng nhập username
zbx_api_pass = "zabbix"# <-- thay thông tin đăng nhập Password
zbx_api_verify = True

zbx_server_version = 3  


zbx_basic_auth = False
zbx_basic_auth_user = "zabbix"
zbx_basic_auth_pass = "zabbix"

proxy_to_zbx = None
proxy_to_tg = None
google_maps_api_key = None  # get your key, see https://developers.google.com/maps/documentation/geocoding/intro

zbx_tg_daemon_enabled = False
zbx_tg_daemon_enabled_ids = [6931850, ]
zbx_tg_daemon_enabled_users = ["ableev", ]
zbx_tg_daemon_enabled_chats = ["Zabbix in Telegram Script", ]

zbx_db_host = "localhost"
zbx_db_database = "zabbix" #<--database here
zbx_db_user = "zbxtg" #<--User here
zbx_db_password = "zbxtg" #<-- password here


emoji_map = {
    "Disaster": "🔥",
    "High": "🛑",
    "Average": "❗",
    "Warning": "⚠️",
    "Information": "ℹ️",
    "Not classified": "🔘",
    "OK": "✅",
    "PROBLEM": "❗",
    "info": "ℹ️",
    "WARNING": "⚠️",
    "DISASTER": "❌",
    "bomb": "💣",
    "fire": "🔥",
    "hankey": "💩",
}
