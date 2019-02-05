Arch Linux Mei Repository
====

### Usage

Add repo

```
[dctxmei]
Server = https://downloads.dctxmei.me/archlinux/$arch
```

to your /etc/pacman.conf .

Add PGP Keys

```
# pacman-key --recv-keys 50BF8B712DCAD7EA
# pacman-key --finger 50BF8B712DCAD7EA
# pacman-key --lsign-key 50BF8B712DCAD7EA
```

or

```
# curl -L downloads.dctxmei.me/public.key | pacman-key --add -
# pacman-key --finger 50BF8B712DCAD7EA
# pacman-key --lsign-key 50BF8B712DCAD7EA
```

### Idea

1. Do not compile packages owned by archlinuxcn.
2. But if there is an error, then do it yourself.

### Build

1. 配置 dctxmei 源并安装 devtools-user
2. 配置 `PACKAGER` 至 `$XDG_CONFIG_HOME/pacman/makepkg.conf` 或 `~/.makepkg.conf`
3. 配置编译所需源至 /etc/pacman.conf
