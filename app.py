import json

from flask import Flask

app = Flask("shoe")


@app.route("/")
def show_pos():
    f = open("bb.txt", "r")
    bbs = f.read()
    # bbs = [b.strip().split(" ") for b in bbs]
    # print(bbs)
    # ret = {"status": "success", "bbs": bbs}
    return bbs
