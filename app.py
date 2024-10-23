from flask import Flask, render_template
from config import app, db
from routes.Book_bp import book_bp
from routes.Category_bp import category_bp

app.register_blueprint(book_bp)
app.register_blueprint(category_bp)

@app.route("/")
def index():
  return render_template("index.html")

if __name__ == "__main__":
  db.create_all()
  app.run(port=5001, debug=True)