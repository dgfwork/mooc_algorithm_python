```App数据抓取

```

### adb相关指令

adb  devices

adb         -s 设备 shell  # 进入终端

adb -s  127.0.0.1:62001 install 拖拽apk包  #命令安装

adb -s  127.0.0.1:62001 uninstall 包名  

安装的是文件名

这里面卸载的时候  需要先进入相应的目录查看包名

 

卸载步骤

1.进入终端 ===》进入终端之后  实际上就是操作Linux

2.进入包 找到包名

adb connect 127.0.0.1:62001

 

查看系统安装包名:adb shell pm list package

 

文件传入夜神模拟器：

adb  push pc端文件路径(这个位置拖拽即可)  /sdcard

 

将夜神模拟器里面为文件传到电脑上面

adb pull  /sdcard/test.txt  c:\apk\  不能直接到电脑根目录

这个实际上就是指明那里到那里   这个是一个精确的操作

 

adb shell screencap  /sdcard/test.png  #截图

 

### 自动化组件获取页面元素

uiautomator工具的组成  这个可以获取包名

 

这个就是帮我们获取元素的定位

====>升级之后，我们可以进行小xpath 进行定位

 

uiautomatorviewer   图形界面

uiautomator  一个测试的Java库

 

appium自动化工具

desired capability里面的四个参数：

​       platformName      Android #手机操作系统

​       platformVersion            4.2.2       #这个就是安卓的版本（在关于里面查看）

​       deviceName                  127.0.0.1:62001      安卓设备的名称

​       appPackage                   包名

​       appActivity

​       noReset                        true         

 

​       后面两个通过工具获取：

​       method1：

​              命令行打开aapt.exe 

​              aapt.exe dump badging 相应的文件名（这个位置还是拖拽进来即可）

​              appPackage     这个就在第一行

​              appActivity  找后面的参数  还可以通过管道过滤 具体如下：

​              aapt.exe dump badging 相应的文件名(拖拽)  |  find “launchable-activity”

​       method2：（推荐使用这种）

​       通过 adb shell 进入终端

​       执行这条指令 logcat | grep cm  同时打开App即可获取：

​       ![img](file:///C:/Users/SCAVEN~1/AppData/Local/Temp/msohtmlclip1/01/clip_image002.jpg)

desired capability设置完后点击保存

```

```

