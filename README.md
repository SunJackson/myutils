## 邮件发送脚本

emailutils.py

- 多用户接收
- 支持附件

## ssh远程连接监控脚本

sshutils.py

- 远程连接ssh
- 执行指令

## 10分钟邮箱注册

tenminutesemail.py

- 注册临时邮箱
- 监控邮件内容

## 爬虫常用工具

spiderutils.py

- 将浏览器请求头转换成字典
- 伪造userAgent
- 获取代理IP



邮箱 SMTP/POP 地址端口


| 邮箱类型     |    POP3地址         |     POP3端口         |  POP3端口           |  POP3端口      | 备注      |
| :--- | :----------------        | ---------------:     | :--------------    | ------------: |--------- |
| gmail      | pop.gmail.com      |   SSL启用 端口：995    |   smtp.gmail.com   |   SSL启用 端口：587 |
| sina.com   | pop3.sina.com.cn   |   端口：110           |   smtp.sina.com.cn |   端口：25    |
| tom.com    | pop.tom.com        |   端口：110           |   smtp.tom.com     |   端口：25    |
| 21cn.com   | pop.21cn.com       |   端口：110           |   smtp.21cn.com     |   端口：25    |
| 163.com    | pop.163.com        |   端口：110           |   smtp.163.com     |   端口：25    |
| yahoo.com  | pop.mail.yahoo.com |   SSL不启用端口：110<br>SSL启用端口：995 |   mtp.mail.yahoo.com     |   SSL不启用端口：25<br>SSL启用端口：465    |
| Foxmail    | pop.foxmail.com    |   端口：110           |   smtp.foxmail.com |   端口：25    |
| sohu.com   | pop3.sohu.com      |   端口：110           |   smtp.sohu.com     |   端口：25    |
| QQ邮箱      | pop.qq.com         |   端口：110           |   smtp.qq.com       |   端口：25    |
| QQ企业邮箱  | pop.exmail.qq.com  |  SSL启用 端口：995    |  smtp.exmail.qq.com | SSL启用 端口：587/465 | SMTP需要验证 |
| aliyun     | pop3.mxhichina.com   | SSL不启用端口：110<br>SSL启用端口：995 | smtp.mxhichina.com  | SSL不启用端口：25<br>SSL启用端口：465  |


