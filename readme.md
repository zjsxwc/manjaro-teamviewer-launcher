因为每次运行 teamviewer 都需要先root运行 teamviewer 的守护进程 daemon，才能正常使用 teamviewer，

但由于我不想每次开机就自动 systemd 启动 teamviewerd daemon，毕竟 teamviewer 不是刚需，

我仅仅只想在要手动双击打开 teamviewer 时才同时启动，其对应守护进程， 所以就写了这个teamviewer脚本起动器，

在teamviewer启动前跳出对话框，让我输入sudo的root密码先启动守护进程再正常使用teamviewer。

<p><img src="https://github.com/zjsxwc/manjaro-teamviewer-launcher/blob/main/teamviewer-launcher.png?raw=true"></p>

```
yay -S teamviewer
```

```
sudo systemctl stop teamviewerd.service
sudo systemctl disable teamviewerd.service
```

```
chmod +x  teamviewer-launcher.py
```



