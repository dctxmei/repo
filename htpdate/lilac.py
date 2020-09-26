#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    run_cmd(['sed \'/^$/d\' -i htpdate.service'])
    for line in edit_file('htpdate.service'):
        if line.startswith('Description='):
            line = "Description=HTTP based time synchronization tool"
        elif line.startswith('Description='):
            line = line + '\n' + "Documentation=man:htpdate"
        elif line.startswith('Documentation='):
            line = line + '\n' + "After=network.target nss-lookup.target"
        elif line.endswith('[Service]'):
            line = '\n' + line
        elif line.startswith('ExecStart='):
            line = "ExecStart=/usr/bin/htpdate -D -s -i /run/htpdate.pid www.pool.ntp.org www.ntp.br www.wikipedia.org"
        elif line.endswith('[Install]'):
            line = '\n' + line
        print(line)
    run_cmd(['updpkgsums'])
