## Lưu ý khi thực hiện cấu hình graph-telegram
```
curl https://raw.githubusercontent.com/huydv398/ViettelCO_DOCS/main/Zabbix5/Install.sh | bash

yum groupinstall 'Development Tools'
yum install centos-release-scl
yum install rh-python36
scl enable rh-python36 bash
yum -y install python2-pip
pip install --upgrade pip
pip2 install --upgrade pip
pip -V
yum install -y wget curl

pip install --upgrade 
echo "PySocks==1.6.8
requests==2.20.0
requests-oauthlib==0.6.2" > requirements.txt
pip install -r requirements.txt

cd /usr/lib/zabbix/alertscripts/zbxtg_settings.py


wget https://raw.githubusercontent.com/ableev/Zabbix-in-Telegram/master/zbxtg.py

cp zbxtg.py zbxtg_group.py
wget https://raw.githubusercontent.com/huydv398/Zabbix-in-Telegram/master/zbxtg_settings.example.py
cp zbxtg_settings.example.py zbxtg_settings.py


chmod +x *
```

Sửa file /usr/lib/zabbix/alertscripts/zbxtg_settings.py

Sửa API_token
```
sed -i '3 d' /usr/lib/zabbix/alertscripts/zbxtg_settings.py
sed -i '2 a tg_key = "5037996407:AAEnzLFgIYLFC77Q1cy3kxGKluCR40B8Qmc"' /usr/lib/zabbix/alertscripts/zbxtg_settings.py
```

Sửa địa chỉ Ip của zabbix_server
```
sed -i '15 d' /usr/lib/zabbix/alertscripts/zbxtg_settings.py
sed -i '14 a zbx_server = "http://10.4.105.10/zabbix/" ' /usr/lib/zabbix/alertscripts/zbxtg_settings.py
```

Thay đổi user /pass đăng nhập quản trị
```
sed -i '16 d' /usr/lib/zabbix/alertscripts/zbxtg_settings.py
sed -i '15 a zbx_api_user = "Admin"' /usr/lib/zabbix/alertscripts/zbxtg_settings.py

sed -i '17 d' /usr/lib/zabbix/alertscripts/zbxtg_settings.py
sed -i '16 a zbx_api_pass = "zabbix"' /usr/lib/zabbix/alertscripts/zbxtg_settings.py
```

Thực hiện lệnh để sử dụng version 
```
sed -i '21 d' /usr/lib/zabbix/alertscripts/zbxtg_settings.py
sed -i '21 a zbx_server_version = 4' /usr/lib/zabbix/alertscripts/zbxtg_settings.py
```
đổi thông tin DB
```
sed -i '50 d' /usr/lib/zabbix/alertscripts/zbxtg_settings.py
sed -i '49 a zbx_db_password = "Pw123@@123"' /usr/lib/zabbix/alertscripts/zbxtg_settings.py
sed -i '49 a zbx_db_password = "Pw123@@123"' /usr/lib/zabbix/alertscripts/zbxtg_settings.py
sed -i '49 a zbx_db_password = "Pw123@@123"' /usr/lib/zabbix/alertscripts/zbxtg_settings.py
sed -i '49 a zbx_db_password = "Pw123@@123"' /usr/lib/zabbix/alertscripts/zbxtg_settings.py
```

./zbxtg.py "@huyts9" "*first part of a message*" "__second part of a message__" --debug --markdown 
 

 
---{{{TRIGGER.SEVERITY}}}{TRIGGER.NAME}
Host: *{HOST.NAME}*
Problem: *{TRIGGER.SEVERITY}*

Trigger Name: *{TRIGGER.NAME}*
Time: *{EVENT.DATE} , {EVENT.TIME}*
Event ID: *{EVENT.ID}*
Desc: *{TRIGGER.DESCRIPTION}*

*Last value*: *{ITEM.LASTVALUE1} ({TIME})*
zbxtg;graphs
zbxtg;graphs_period=10800
zbxtg;graphs_width=900
zbxtg;graphs_height=300
zbxtg;itemid:{ITEM.ID1}
zbxtg;title:{HOST.HOST} - {TRIGGER.NAME}


---{{OK}}{TRIGGER.NAME}
Host: *{HOST.NAME} ({HOST.IP})*
Problem: *{TRIGGER.SEVERITY}*

Trigger Name: *{TRIGGER.NAME}*
Time: *{EVENT.RECOVERY.DATE}, {EVENT.RECOVERY.TIME} *
Event ID: *{EVENT.ID}*
​

Last value: *{ITEM.LASTVALUE1} ({TIME})*
zbxtg;graphs
zbxtg;graphs_period=10800
zbxtg;graphs_width=900
zbxtg;graphs_height=300
zbxtg;itemid:{ITEM.ID1}
zbxtg;title:{HOST.HOST} - {TRIGGER.NAME}
