# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash
from contextlib import closing

# configuraion
#DEBUG = True
SECRET_KEY = 'find master secrect key'

# create our application
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def show_entries():
    entries = []
    with open('/data/FindMaster/server_info.txt', 'r') as f:
        while 1:
            line = f.readline()
            if not line:
                break
            serverinfo = line.split()
            if len(serverinfo) == 3:
                entries.append(dict(appname=serverinfo[0], port=serverinfo[1], link=serverinfo[2]))

    return render_template('show_entries.html', entries=entries)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
