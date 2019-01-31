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
