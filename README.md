# QQ合成团圆饭

本ADB助手采用了简易的策略，主要是对屏幕进行机械式点击操作 *（没有AI）* ，这样可以均衡并且利用碰撞原理分离大小不同的“饭”

## 文件内容及目录：
+ **ADB_Main.py**: 一个调用内部本人写的库(Apply, Basic)的外接入口，（输入操作已写好）直接运行即可
+ **ADB_Apply.py**: 本人根据ADB主库外加的相关操作接口，可以实现相关的腾讯春节应用操作
+ **ADB_Basic.py**: 本人自己封装的ADB主库，具体函数请看内部（不多，就几十行）
+ **Output_Basic.py**: 利用cv2/PIL/matplotlib的库写的截图显示用的库（函数都封装好了，ADB_Basic.py调用上了）

## 配置及运行方法：
+ 请安装好ADB、python并全部配置好环境变量
+ ***安装所有需要的库文件“pip install ”+库文件名（opencv-python,matplotlib,pillow）（可选,不需要即可直接在Basic.py中注释掉，已经默认注释掉）***
+ 打开手机开发者选项（网上百度）
+ 开启USB调试选项，同时在电脑上安装相应品牌的“手机助手”以获取ADB驱动（本质上，安装之后在ADB中能连上手机了，就可以卸载软件了）
+ 打开年夜饭界面，运行“ADB_Main.py”，开始享受吧！


## 免责声明：
1. 本程序是仅供学习与交流使用，仅模拟人的机械性重复操作，未修改腾讯软件相应代码，请在下载之后24小时内务必删除。
2. 非盈利谨慎使用，保护QQ，珍惜腾讯！！！造成的一切处理和后果与开发者本人无关，切勿沉迷上身。
