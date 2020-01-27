Dct Mei's Arch Linux Personal Software Depot
====
Hi! My name is Dct Mei. This is my Arch Linux software repository. It is only used to store some software that is not suitable for public software repositories. It mainly contains some configuration files and is currently maintained manually.

## Usage

### Add Repo

```
[dctxmei]
Server = https://dctxmei.github.io/repo/$arch
```

to your /etc/pacman.conf .

### Add PGP Keys

```
# pacman-key --recv-keys 50BF8B712DCAD7EA
# pacman-key --finger 50BF8B712DCAD7EA
# pacman-key --lsign-key 50BF8B712DCAD7EA
```

or

```
# curl https://build.archlinuxcn.org/~dctxmei/public.key | pacman-key --add -
# pacman-key --finger 50BF8B712DCAD7EA
# pacman-key --lsign-key 50BF8B712DCAD7EA
```
