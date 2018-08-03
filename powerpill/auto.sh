#!/bin/bash

sha512sums=$(grep -A 2 sha512sums PKGBUILD | tail -n 1)
md5sums=$(grep -A 2 md5sums PKGBUILD | tail -n 1)

sed -e '/sig/d' \
    -e "/$sha512sums/d" \
    -e "/$md5sums/d" \
    -e '/pgp/d' \
    PKGBUILD -i
