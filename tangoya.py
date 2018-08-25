# -*- coding: utf-8 -*-
import urllib.error
import urllib.request
import os
import subprocess

def make_filename(base_dir, number, url):
    ext = os.path.splitext(url)[1]      # 拡張子を取得
    filename = number + ext        # 番号に拡張子をつけてファイル名にする
    fullpath = os.path.join(base_dir, filename)
    return fullpath

def download_img(url, path):
    try:
        data = urllib.request.urlopen(url).read()
        with open(path, mode="wb") as f:
            f.write(data)
    except urllib.error.URLError as e:
        print(e)

def URL_fix(url):
    url = str(url)
    url = url.replace("b'", "")
    url = url.replace(r"\n'", "")
    if "https" not in url:
        url = "https:" + url
    return url

what = input("何の画像をいらすとやから探してくる？：")
path = input("どこのフォルダに保存する？：")

command = "irasutoya " + str(what)  # ！ここに実行したいコマンドを書く！
proc = subprocess.Popen(
    command,
    shell=True,  # シェル経由($ sh -c "command")で実行。
    stdin=subprocess.PIPE,  # 1
    stdout=subprocess.PIPE,  # 2
    stderr=subprocess.PIPE)  # 3
stdout_data, stderr_data = proc.communicate()  # 処理実行を待つ(†1)
url = URL_fix(stdout_data)

path = make_filename(path,'0',url)
download_img(url, path)