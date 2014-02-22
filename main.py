#!/usr/bin/env python3
#
# Copyright 2014 Dabo Ross <http://www.daboross.net/>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from flask import Flask, request
from pushbullet import PushBullet

with open('myfile.txt', 'r', encoding="UTF-8") as f:
    global api_key, device
    api_key = f.readline()
    device = f.readline()
push = PushBullet(api_key)
app = Flask(__name__)
@app.route("/notify", methods=["POST"])
def hello():
    push.push_note(device, "Web notice", request.data)
    return """200\n"""

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5445)
    app.run(host="127.0.0.1", port=5445)