# -*- coding: utf-8 -*-
import urllib.error
import urllib.request
import os
import subprocess


def make_filename(base_dir, number, url):  # 拡張子がpngのファイルを指定フォルダ内に作る関数
    ext = os.path.splitext(url)[1]  # 拡張子を取得
    filename = number + ext  # 番号に拡張子をつけてファイル名にする
    full_path = os.path.join(base_dir, filename)
    return full_path


def download_img(url, path):  # urlをもらって、その先の画像を保存する関数
    try:
        data = urllib.request.urlopen(url).read()
        with open(path, mode="wb") as f:
            f.write(data)
    except urllib.error.URLError as e:
        print(e)


def url_fix(url_string):  # urlの体裁を整える関数
    url_string = str(url_string)
    url_string = url_string.replace("b'", "")
    url_string = url_string.replace(r"\n'", "")
    if "https" not in url_string:
        url_string = "https:" + url_string
    return url_string


what = input("何の画像をいらすとやから探してくる？：")    # ここで単語を指定
folder = input("どこのフォルダに保存する？：")              # ここでフォルダを指定

command = "irasutoya " + str(what)  # ！ここに実行したいコマンドを書く！
proc = subprocess.Popen(
    command,
    shell=True,              # シェル経由($ sh -c "command")で実行。
    stdin=subprocess.PIPE,   # 1
    stdout=subprocess.PIPE,  # 2
    stderr=subprocess.PIPE)  # 3
stdout_data, stderr_data = proc.communicate()  # 処理実行を待つ(†1)

img_url = url_fix(stdout_data)  # urlの体裁を整えて

img_path = make_filename(folder, '0', img_url)  # ファイルを作って
download_img(img_url, img_path)  # 画像をダウンロード
