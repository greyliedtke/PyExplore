from flask import Flask, render_template
import markdown
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Path to the directory containing Markdown files
    mdf = 'WebBook/mdf/Overview.md'
    with open(mdf, 'r', encoding='utf-8') as f:
        content = f.read()
        html_content = markdown.markdown(content)

    return render_template('base.html', content=html_content)

if __name__ == '__main__':
    app.run(debug=True, port=1234)
