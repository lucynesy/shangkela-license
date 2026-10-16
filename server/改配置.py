# -*- coding: utf-8 -*-
"""改服务器授权配置（实验用）
用法: python 改配置.py <到期日 YYYY-MM-DD> [吊销编号,逗号分隔]
"""
import io, sys, datetime
expiry = sys.argv[1] if len(sys.argv) > 1 else (datetime.date.today() + datetime.timedelta(days=30)).isoformat()
revoked = sys.argv[2] if len(sys.argv) > 2 else ""
txt = ("# 上课啦 · 远程授权配置\n"
       "expiry: %s\n"
       "revoked: %s\n"
       "updated: %s\n" % (expiry, revoked, datetime.date.today().isoformat()))
io.open("config.txt", "w", encoding="utf-8", newline="\n").write(txt)
print("已更新 config.txt：")
print(txt)
