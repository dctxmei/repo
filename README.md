Arch Linux Mei Repository
====

### Usage

Add repo

```
[dctxmei]
Server = https://repo.dctxmei.me/$arch
```
to your /etc/pacman.conf .

Add PGP Keys

```
$ curl https://repo.dctxmei.me/dctxmei.key | sudo pacman-key --add -
$ sudo pacman-key --lsign-key dctxmei@gmail.com
```

### Idea

1. Do not compile packages owned by archlinuxcn.
2. But if there is an error, then do it yourself.
