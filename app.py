from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 模擬資料庫 (暫存在記憶體)
posts = [
    {"title": "第一篇文章", "author": "麒安", "content": "這是我的第一篇 Flask 部落格文章！"},
    {"title": "第二篇文章", "author": "小艾", "content": "Flask 真是太好用了！"},
]

@app.route('/')
def index():
    """首頁顯示所有文章"""
    return render_template('index.html', posts=posts)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    """新增文章頁面"""
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']

        posts.append({
            "title": title,
            "author": author,
            "content": content
        })

        return redirect(url_for('index'))

    return render_template('new_post.html')

if __name__ == '__main__':
    app.run(debug=True)
