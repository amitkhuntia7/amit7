from flask import Flask, render_template, request,url_for,redirect
import os
import random

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    trending = [
        {'name': "Green Shyne's Angelo", 'image': 'pro5.jpg'},
        {'name': "Black Cactus", 'image': 'pro6.png'},
        {'name': "3D SOL", 'image': 'pro4.jpg'},
        {'name': "Jaadu", 'image': 'pro3.jpg'},
        {'name': "Neem Cleaner", 'image': 'pro10.jpg'},
        {'name': "Green Shyne's Power", 'image': 'pro2.jpg'},
        {'name': "Rose Hygiene", 'image': 'pro7.jpg'},
        {'name': "Lemon Drop", 'image': 'pro8.jpg'},
        {'name': "Bleach Extra", 'image': 'pro1.jpg'},
        {'name': "Sanitizer Pro", 'image': 'pro9.jpg'}
    ]

    # Mock exclusive products in 3 categories
    exclusive = {
        'new': trending,
        'special': random.sample(trending, min(9, len(trending))),
        'best': random.sample(trending, min(9, len(trending)))
    }

    return render_template("home.html", trending=trending, exclusive=exclusive)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # (You can collect form data if needed)
        return redirect(url_for("success"))
    return render_template("contact.html")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/branch")
def branch():
    return render_template("branch.html", title="Branch")

@app.route("/media")
def media():
    return render_template("media.html", title="Media")

@app.route("/search")
def search():
    query = request.args.get('query', '').strip().lower()

    category_info = {
        "bleaching powder": "Effective for disinfection and stain removal.",
        "floor cleaner": "Keeps floors spotless and germ-free.",
        "handwash": "Gentle yet powerful on germs.",
        "mosquito repellant": "Protects against mosquito-borne diseases.",
        "napthalene": "Removes odors and repels insects in wardrobes.",
        "phenyl": "Powerful disinfectant for floors and bathrooms."
    }

    # Try to match exact category
    result = category_info.get(query)

    # Try partial match if not exact
    if not result:
        for key, value in category_info.items():
            if query in key:
                result = value
                break

    return render_template("search_results.html", query=query, result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
