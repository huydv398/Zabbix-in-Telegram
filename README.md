# Zabbix-in-Telegram
Zabbix Notifications with graphs in Telegram

### Đặc trưng
- [x] Đồ thị dựa trên dữ liệu mới nhất được gửi trực tiếp đến trình nhắn tin của bạn
- [x] Bạn có thể gửi tin nhắn cả trong cuộc trò chuyện riêng tư và group/supergroup
- [x] Lưu chatid dưới dạng tệp tạm thời
- [x] Simple markdown and HTML được hỗ trợ
- [x] Emoji - Biểu tượng cảm xúc (you can use emoji instead of severity, see [the wiki article](https://github.com/ableev/Zabbix-in-Telegram/wiki/Trigger-severity-as-Emoji)) (abbix chưa hỗ trợ mã hóa utf8mb4)
- [x] Bản đồ địa điểm

### TODOs - VIỆC CẦN LÀM
- Quản lý zabbix đơn giản thông qua lệnh của bot - ở trạng thái dev
- Khả năng gửi đồ thị phức tạp hoặc một phần của màn hình


### Cấu hình / Cài đặt

**ĐỌC WIKI NẾU BẠN CÓ VẤN ĐỀ VỚI LỖI**: https://github.com/ableev/Zabbix-in-Telegram/wiki

**Trước hết**: Bạn cần cài đặt các mô-đun thích hợp cho python, điều này là bắt buộc để hoạt động! </br>

Thực hiện lệnh:
```
yum install -y wget curl 
echo "PySocks==1.6.8
requests==2.20.0
requests-oauthlib==0.6.2" > requirements.txt

pip install -r requirements.txt
```
Kết quả
```
[root@zabbix-srv ~]# echo "PySocks==1.6.8
> requests==2.20.0
> requests-oauthlib==0.6.2" > requirements.txt
[root@zabbix-srv ~]# cat requirements.txt
PySocks==1.6.8
requests==2.20.0
requests-oauthlib==0.6.2
[root@zabbix-srv ~]# pip2 install -r requirements.txt
Collecting PySocks==1.6.8 (from -r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/53/12/6bf1d764f128636cef7408e8156b7235b150ea31650d0260969215bb8e7d/PySo                         cks-1.6.8.tar.gz (283kB)
    100% |████████████████████████████████| 286kB 854kB/s
Collecting requests==2.20.0 (from -r requirements.txt (line 2))
  Downloading https://files.pythonhosted.org/packages/f1/ca/10332a30cb25b627192b4ea272c351bce3ca1091e541245cccbace6051d8/requ                         ests-2.20.0-py2.py3-none-any.whl (60kB)
    100% |████████████████████████████████| 61kB 1.4MB/s
Collecting requests-oauthlib==0.6.2 (from -r requirements.txt (line 3))
  Downloading https://files.pythonhosted.org/packages/df/f1/bf7fcb853c7a0abfd53c7ef71a72ad6737f120b08260de76ec1b286acd4a/requ                         ests_oauthlib-0.6.2-py2.py3-none-any.whl
Collecting idna<2.8,>=2.5 (from requests==2.20.0->-r requirements.txt (line 2))
  Downloading https://files.pythonhosted.org/packages/4b/2a/0276479a4b3caeb8a8c1af2f8e4355746a97fab05a372e4a2c6a6b876165/idna                         -2.7-py2.py3-none-any.whl (58kB)
    100% |████████████████████████████████| 61kB 1.4MB/s
Collecting certifi>=2017.4.17 (from requests==2.20.0->-r requirements.txt (line 2))
  Downloading https://files.pythonhosted.org/packages/37/45/946c02767aabb873146011e665728b680884cd8fe70dde973c640e45b775/cert                         ifi-2021.10.8-py2.py3-none-any.whl (149kB)
    100% |████████████████████████████████| 153kB 1.4MB/s
Collecting chardet<3.1.0,>=3.0.2 (from requests==2.20.0->-r requirements.txt (line 2))
  Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/char                         det-3.0.4-py2.py3-none-any.whl (133kB)
    100% |████████████████████████████████| 143kB 1.2MB/s
Collecting urllib3<1.25,>=1.21.1 (from requests==2.20.0->-r requirements.txt (line 2))
  Downloading https://files.pythonhosted.org/packages/01/11/525b02e4acc0c747de8b6ccdab376331597c569c42ea66ab0a1dbd36eca2/urll                         ib3-1.24.3-py2.py3-none-any.whl (118kB)
    100% |████████████████████████████████| 122kB 1.5MB/s
Collecting oauthlib>=0.6.2 (from requests-oauthlib==0.6.2->-r requirements.txt (line 3))
  Downloading https://files.pythonhosted.org/packages/e8/5d/9dd1c29e5a786525f6342f6c1d812ed2e37edc653ad297048c1668988053/oaut                         hlib-3.1.1-py2.py3-none-any.whl (146kB)
    100% |████████████████████████████████| 153kB 1.5MB/s
Installing collected packages: PySocks, idna, certifi, chardet, urllib3, requests, oauthlib, requests-oauthlib
  Running setup.py install for PySocks ... done
Successfully installed PySocks-1.6.8 certifi-2021.10.8 chardet-3.0.4 idna-2.7 oauthlib-3.1.1 requests-2.20.0 requests-oauthli                         b-0.6.2 urllib3-1.24.3

```

 * Đặt các file cấu hình trong `AlertScriptsPath` thư mục `/usr/lib/zabbix/alertscripts/` , đường dẫn được tìm bên trong `zabbix_server.conf`</br>Tùy vào từng máy tìm đường `AlertScriptsPath` trong file `zabbix_server.conf`

    ```
    [root@zabbix-srv ~]# cat /etc/zabbix/zabbix_server.conf | grep alertscripts
    # AlertScriptsPath=${datadir}/zabbix/alertscripts
    AlertScriptsPath=/usr/lib/zabbix/alertscripts
    [root@zabbix-srv ~]#
    ```

  * Tải file `zbxtg.py` và `zbxtg_settings.example.py` đặt trong thư mục `/usr/lib/zabbix/alertscripts`:
     ```
    [root@zabbix-srv ~]# cd /usr/lib/zabbix/alertscripts
    [root@zabbix-srv alertscripts]# wget https://raw.githubusercontent.com/huydv398/Zabbix-in-Telegram/master/zbxtg_settings.example.py
    [root@zabbix-srv alertscripts]# wget https://raw.githubusercontent.com/huydv398/Zabbix-in-Telegram/master/zbxtg.py
    ```


 * Tạo `zbxtg_settings.py` (copy từ file `zbxtg_settings.example.py`)
 ```
 [root@zabbix-srv alertscripts]# cp zbxtg_settings.example.py zbxtg_settings.py
 ```
  * Thêm quyền thực thi cho file:
  ```
    [root@zabbix-srv alertscripts]# chmod +x *
  ```
  * Tạo một bot Telegram và lấy API key (Ví dụ: `1234566407:AAEnzLFgIYLFC77Q1cy3kxGKluCR40ABCD`)
  *  Rồi thay đổi các thành phần bên trong để có thể gửi được nội dung về telegram:
      ```
      vi zbxtg_settings.py
      ```
  Thay đổi thông tin sau:
  ```
  #API Token Telegram
  tg_key = "XYZ" 

  #change 
  tg_key = "bot1234566407:AAEnzLFgIYLFC77Q1cy3kxGKluCR40ABCD"
  ```

  ```
  #Zb-server  
  zbx_server = "http://127.0.0.1/zabbix/"
  zbx_api_user = "Admin"
  zbx_api_pass = "zabbix"

  #Change:
  zbx_server = "http://192.168.174.51/zabbix/" #192.168.174.51:Your IP zabbix server 
  zbx_api_user = "Admin" 
  zbx_api_pass = "zabbix"
  ```
  ```
  #Database
  zbx_db_database = "zabbix"
  zbx_db_user = "zbxtg"
  zbx_db_password = "zbxtg"

  #Change:
  zbx_db_database = "zabbix"
  zbx_db_user = "Database-name"
  zbx_db_password = "Passw0rD"
  ```
* Test script:
  ```
  ./zbxtg.py "@usernametele" "first part of a message" "second part of a message"
  ```
  ![Imgur](https://i.imgur.com/swmPSxq.png)

## Tạo Media types
 * Tạo mới media type for Telegram in Zabbix web interface  settings:</br><img src="https://i.imgur.com/lHb3MlO.png" width="400px"></br>Đặt tên cho **Media type**</br><img src="https://i.imgur.com/8z5p4hH.png" width="400px">
### Tab Media type
* **Name**: `canhbao-tele`
 * **Type**: `Script`
 * **Script name**: `zbxtg.py`
 * Thêm các Tham số sau vào **Script parameters**
   * `{ALERT.SENDTO}`
   * `{ALERT.SUBJECT}`
   * `{ALERT.MESSAGE}`
   * `--debug`
   * `--markdown`

   <img src="https://i.imgur.com/1jtWwTl.png" width="400px">
### Tab Message templates
* Thêm mẫu cảnh báo:</br>![Imgur](https://i.imgur.com/w5GRO2q.png)
  * ![Imgur](https://i.imgur.com/Le30l7s.png)
  * ![Imgur](https://i.imgur.com/ux63XSs.png)
  * ![Imgur](https://i.imgur.com/gUQTtKj.png)
* Kết quả:</br>![Imgur](https://i.imgur.com/qfEQLTI.png)
### Tab Options
Điền thông tin và Chọn Update</br>
![Imgur](https://i.imgur.com/RSQakG8.png)
## Tạo Actions
Tạo Action: **Configuration** -> **Actions** -> **Create action**</br>![Imgur](https://i.imgur.com/gFlrciK.png)
* Name: `actiontele` </br>![Imgur](https://i.imgur.com/Jpej0tp.png)
* Add **Operations**</br>![Imgur](https://i.imgur.com/35zwhdU.png)
  * Send to users:  `Admin (Zabbix Administrator)`
  * Send only to: `canhbao-tele` (Name của media type)
  * Custom message: Check box
  * Subject: `{{{TRIGGER.SEVERITY}}}{TRIGGER.NAME}`
  * Message:
    ```
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

    ```
  * Click Add để hoàn thành</br>![Imgur](https://i.imgur.com/pXfOrpY.png)
* Add **Recovery operations**
  * Click **Add**</br>![Imgur](https://i.imgur.com/J1Zbj1K.png)
  * Send to users:  `Admin (Zabbix Administrator)`
  * Send only to: `canhbao-tele` (Name của media type)
  * Custom message: Check box
  * Subject: `{{OK}}{TRIGGER.NAME}`
  * Message:
    ```
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


    ```
  * Click Add để hoàn thành</br>![Imgur](https://i.imgur.com/XdAQNrh.png)
* Click Add để hoàn tất</br>![Imgur](https://i.imgur.com/MAkw8wo.png)
## Cấu hình cho User 
* Chọn **Administator** -> **Users** -> **Admin**</br> ![Imgur](https://i.imgur.com/QmHbf8o.png)
* Chuyển Tab Users -> Media</br> ![Imgur](https://i.imgur.com/8vYW7i2.png)
* THêm thông tin:
  * Type: `canhbao-tele`
  * Sent to: có thể là `id tele` hoặc `@username`</br> ![Imgur](https://i.imgur.com/zgLxwpi.png)

Kiểm tra lại:
Thực hiện test tại **Media type** - **canhbao-tele** -> **test**, điền vào sent to `ID` hoặc `@username` </br> ![Imgur](https://i.imgur.com/6pm88SH.png)
#### Debug

* Câu lệnh test: </br>
`./zbxtg.py "@username" "first part of a message" "second part of a message" --debug`
 * `@username` telegram hỗ trợ `@username` tương đương với ID
 * For `first part of a message` and `second part of a message` là nội dung để gửi đến telegram khi thực hiện test

## Gửi thông báo về group telegram.
![Imgur](https://i.imgur.com/gx89xNn.png)

username: `@huydv_bot`
api Token: `1330822781:AAHN9wcBYMzZyl8vZa5mjuQnLEsiFjvxOns`

* Thêm bot vào Group.</br>![Imgur](https://i.imgur.com/8iNbUjy.png)
* Lấy ID group: Truy cập đường dẫn kèm api token [link](https://api.telegram.org/(bot1330822781:AAHN9wcBYMzZyl8vZa5mjuQnLEsiFjvxOns/getUpdates))</br>![Imgur](https://i.imgur.com/LhrFhuk.png)</br>id: `-670816547`
* Sửa file: `vi /var/tmp/zbxtg/uids.txt`
  * Thêm nội dung sau vào file: `username;private;id` ở đây thực tế là: `huydv_bot;private;-670816547`
  * Thực hiện Test lệnh: `[root@zabbix-srv alertscripts]# ./zbxtg.py "@huydv_bot" "*first part of a message*" "__second part of a message__" --markdown --debug`
    ```
    [root@zabbix-srv alertscripts]# ./zbxtg.py "@huydv_bot" "*first part of a message*" "__second part of a message__" --markdown
    [root@zabbix-srv alertscripts]#
    ```
* Test trên web: </br>![Imgur](https://i.imgur.com/heUp6xQ.png)

* Test gửi đến username: `@huydv_bot`</br> ![Imgur](https://i.imgur.com/AFA1WrB.png)

* Thêm media: Administrator -> User -> Tab Media</br>Type: `canhbao-tele`</br>Send to: `@huydv_bot` </br>![Imgur](https://i.imgur.com/IOYUtue.png)

* Khi cảnh báo sẽ được hiển thị như sau:</br>![Imgur](https://i.imgur.com/Axy7Kl4.png)
* Khi trạng trở về mức bình thường - Recovery operations:</br>![Imgur](https://i.imgur.com/WrdkXwm.png)