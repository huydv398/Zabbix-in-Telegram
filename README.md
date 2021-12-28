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
- Khả năng gửi đồ thị phức tạp hoặc một phần của màn hìnhn


### Cấu hình / Cài đặt

**ĐỌC WIKI NẾU BẠN CÓ VẤN ĐỀ VỚI LỖI**: https://github.com/ableev/Zabbix-in-Telegram/wiki

**Trước hết**: Bạn cần cài đặt các mô-đun thích hợp cho python, điều này là bắt buộc để hoạt động! </br>
                  Để làm như vậy, hãy nhập `pip install -r requirements.txt` dòng lệnh của bạn!

 * Đặt `zbxtg.py` trong `AlertScriptsPath` thư mục `/usr/lib/zabbix/alertscripts/` , đường dẫn được đặt bên trong `zabbix_server.conf`
    ```
    [root@zabbix-srv ~]# cat /etc/zabbix/zabbix_server.conf | grep alertscripts
    # AlertScriptsPath=${datadir}/zabbix/alertscripts
    AlertScriptsPath=/usr/lib/zabbix/alertscripts
    [root@zabbix-srv ~]#
    ```
 * Đặt `zbxtg_group.py` cùng thư mục `/usr/lib/zabbix/alertscripts/` được copy nội dung từ file `zbxtg.py`
 * Tạo `zbxtg_settings.py` (copy từ file `zbxtg_settings.example.py`) Rồi thay đổi các thành phần bên trong để có thể gửi được nội dung về telegram
  * Tạo một bot Telegram và lấy API key
 * Tạo mới media type for Telegram in Zabbix web interface  settings:
  <img src="https://i.imgur.com/lHb3MlO.png" width="400px">
  <img src="https://i.imgur.com/8z5p4hH.png" width="400px">

 * Hoặc nếu muốn gửi vào nhóm telegram
 <img src="https://i.imgur.com/Hx92QdF.png" width="400px">

 * Create a new actions like this:
 <img src="https://i.imgur.com/JTPppu7.png" width="400px">
    ```
    Last value: {ITEM.LASTVALUE1} ({TIME})
    zbxtg;graphs
    zbxtg;graphs_period=10800
    zbxtg;itemid:{ITEM.ID1}
    zbxtg;title:{HOST.HOST} - {TRIGGER.NAME}
    ``` 

<img src="https://i.imgur.com/lg4gooJ.png" width="400px">
<img src="https://i.imgur.com/tDgMJ7z.png" width="400px">
<img src="https://i.imgur.com/t0o8ETH.png" width="400px">
<img src="https://i.imgur.com/I9KonhG.png" width="400px">
<img src="https://i.imgur.com/TKgcBk5.png" width="400px">

* add media type
<img src="https://i.imgur.com/Hx92QdF.png" width="400px">



  * Private:

  <img src="https://i.imgur.com/GVDlTU5.png" width="400px">

  * Group:

  <img src="https://i.imgur.com/TgcCqDf.png" width="400px">

#### Annotations
```
zbxtg;graphs -- enables attached graphs
zbxtg;graphs_period=10800 -- set graphs period (default - 3600 seconds)
zbxtg;graphs_width=700 -- set graphs width (default - 900px)
zbxtg;graphs_height=300 -- set graphs height (default - 300px)
zbxtg;itemid:{ITEM.ID1} -- define itemid (from trigger) for attach
zbxtg;itemid:{ITEM.ID1},{ITEM.ID2},{ITEM.ID3} -- same, but if you want to send two or more graphs, use complex trigger
zbxtg;title:{HOST.HOST} - {TRIGGER.NAME} -- graph's title
zbxtg;debug -- enables debug mode, some logs and images will be saved in the tmp dir (temporary doesn't affect python version)
zbxtg;channel -- enables sending to channels
zbxtg;to:username1,username2,username3 -- now you don't need to create dedicated profiles and add media for them, use this option in action to send messages to those user(s)
zbxtg;to_group:Group Name One,Group Name Two -- the same but for groups
```

You can use markdown or html formatting in your action: https://core.telegram.org/bots/api#markdown-style + https://core.telegram.org/bots/api#html-style. 

#### Debug

* Câu lệnh test: </br>
`./zbxtg.py "@username" "first part of a message" "second part of a message" --debug`
 * For `@username` substitute your Telegram username, chat-id
 * For `first part of a message` and `second part of a message` just substitute something like "test" "test" (for Telegram it's doesn't matter between subject and body)
 * You can skip the `"` if it's one word for every parameter, these are optional

---


### Known issues

#### MEDIA_CAPTION_TOO_LONG
If you see this error, it means that you rich the limit of caption with 200 symbols in it (Telegram API's limitaion).
Such captions will be automatically cut to 200 symbols.

#### Zabbix 3.0 and higher (3.2, 3.4, 4.0, 4.2, 4.4)
https://github.com/ableev/Zabbix-in-Telegram/wiki/Working-with-Zabbix-3.0
