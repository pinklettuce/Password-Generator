#! /usr/bin/env python3
a='';exec("a+=chr(__import__('random').randint(30,128));"*int(__import__('sys').argv[1]));print("[+] Password: %s"%a)
