Arch Linux Dictator Repository
====

### Usage

Add repo

```
[archlinuxdictator]
Server = https://repo.dct.party/$arch
```
to your /etc/pacman.conf .

Add PGP Keys

```
$ curl https://repo.dct.party/archlinuxdictator.key | sudo pacman-key --add -
$ sudo pacman-key --lsign-key dctxmei@gmail.com
```
