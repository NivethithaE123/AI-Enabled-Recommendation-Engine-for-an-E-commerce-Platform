from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

users = {}
cart = []
wishlist = []
ratings = {}

products = [

# 🔹 ELECTRONICS (15+)
{"name": "Dell Laptop", "price": 50000, "image": "laptop1.jpg", "category": "Electronics"},
{"name": "HP Laptop", "price": 55000, "image": "laptop2.jpg", "category": "Electronics"},
{"name": "Lenovo Laptop", "price": 48000, "image": "laptop3.jpg", "category": "Electronics"},
{"name": "ASUS Gaming Laptop", "price": 75000, "image": "laptop4.jpg", "category": "Electronics"},
{"name": "Acer Laptop", "price": 47000, "image": "laptop5.jpg", "category": "Electronics"},

{"name": "Samsung Phone", "price": 20000, "image": "phone1.jpg", "category": "Electronics"},
{"name": "Realme Phone", "price": 15000, "image": "phone2.jpg", "category": "Electronics"},
{"name": "iPhone 14", "price": 80000, "image": "phone3.jpg", "category": "Electronics"},
{"name": "OnePlus Phone", "price": 30000, "image": "phone4.jpg", "category": "Electronics"},
{"name": "Redmi Phone", "price": 18000, "image": "phone5.jpg", "category": "Electronics"},

{"name": "Sony Headphones", "price": 3000, "image": "head1.jpg", "category": "Electronics"},
{"name": "Boat Headphones", "price": 1500, "image": "head2.jpg", "category": "Electronics"},
{"name": "JBL Speaker", "price": 2500, "image": "speaker1.jpg", "category": "Electronics"},
{"name": "Bluetooth Speaker", "price": 2000, "image": "speaker2.jpg", "category": "Electronics"},
{"name": "Smart Watch", "price": 3500, "image": "watch1.jpg", "category": "Electronics"},

# 🔹 MEN FASHION (15+)
{"name": "Men Casual Shirt", "price": 1200, "image": "mshirt1.jpg", "category": "Fashion"},
{"name": "Men Formal Shirt", "price": 1500, "image": "mshirt2.jpg", "category": "Fashion"},
{"name": "Men Printed Shirt", "price": 1300, "image": "mshirt3.jpg", "category": "Fashion"},
{"name": "Men T-Shirt", "price": 800, "image": "mshirt4.jpg", "category": "Fashion"},
{"name": "Men Polo T-Shirt", "price": 1000, "image": "mshirt5.jpg", "category": "Fashion"},

{"name": "Men Jeans Blue", "price": 2000, "image": "mjeans1.jpg", "category": "Fashion"},
{"name": "Men Jeans Black", "price": 2200, "image": "mjeans2.jpg", "category": "Fashion"},
{"name": "Men Slim Fit Jeans", "price": 2400, "image": "mjeans3.jpg", "category": "Fashion"},

{"name": "Men Shoes", "price": 2500, "image": "mshoes1.jpg", "category": "Fashion"},
{"name": "Men Sneakers", "price": 3000, "image": "mshoes2.jpg", "category": "Fashion"},
{"name": "Running Shoes", "price": 2800, "image": "mshoes3.jpg", "category": "Fashion"},

{"name": "Men Jacket", "price": 3500, "image": "mjacket1.jpg", "category": "Fashion"},
{"name": "Men Hoodie", "price": 2000, "image": "mjacket2.jpg", "category": "Fashion"},

# 🔹 WOMEN FASHION (15+)
{"name": "Women Party Dress", "price": 2500, "image": "wdress1.jpg", "category": "Fashion"},
{"name": "Women Summer Dress", "price": 1800, "image": "wdress2.jpg", "category": "Fashion"},
{"name": "Women Traditional Dress", "price": 3000, "image": "wdress3.jpg", "category": "Fashion"},
{"name": "Women Casual Dress", "price": 2000, "image": "wdress4.jpg", "category": "Fashion"},

{"name": "Women Top", "price": 1200, "image": "wtop1.jpg", "category": "Fashion"},
{"name": "Women Crop Top", "price": 1400, "image": "wtop2.jpg", "category": "Fashion"},

{"name": "Women Jeans", "price": 2000, "image": "wjeans1.jpg", "category": "Fashion"},
{"name": "Women Skinny Jeans", "price": 2200, "image": "wjeans2.jpg", "category": "Fashion"},

{"name": "Handbag Stylish", "price": 2200, "image": "bag1.jpg", "category": "Fashion"},
{"name": "Ladies Sandals", "price": 1200, "image": "wsandals1.jpg", "category": "Fashion"},
{"name": "High Heels", "price": 1800, "image": "wsandals2.jpg", "category": "Fashion"},

# 🔹 HOME APPLIANCES (10+)
{"name": "LG Refrigerator", "price": 30000, "image": "fridge1.jpg", "category": "Home"},
{"name": "Samsung Refrigerator", "price": 35000, "image": "fridge2.jpg", "category": "Home"},
{"name": "Double Door Fridge", "price": 40000, "image": "fridge3.jpg", "category": "Home"},

{"name": "Washing Machine LG", "price": 25000, "image": "wash1.jpg", "category": "Home"},
{"name": "Washing Machine Samsung", "price": 27000, "image": "wash2.jpg", "category": "Home"},

{"name": "Microwave Oven", "price": 12000, "image": "micro1.jpg", "category": "Home"},
{"name": "Air Conditioner Voltas", "price": 40000, "image": "ac1.jpg", "category": "Home"},
{"name": "Ceiling Fan", "price": 2000, "image": "fan1.jpg", "category": "Home"},
{"name": "Mixer Grinder", "price": 3500, "image": "mixer1.jpg", "category": "Home"},

# 🔹 BOOKS
{"name": "Python Programming Book", "price": 600, "image": "book1.jpg", "category": "Books"},
{"name": "AI Book", "price": 800, "image": "book2.jpg", "category": "Books"},
{"name": "Data Science Book", "price": 900, "image": "book3.jpg", "category": "Books"},
{"name": "Machine Learning Book", "price": 1000, "image": "book4.jpg", "category": "Books"},

# 🔹 BEAUTY
{"name": "Face Cream", "price": 400, "image": "cream1.jpg", "category": "Beauty"},
{"name": "Perfume", "price": 1200, "image": "perfume1.jpg", "category": "Beauty"},
{"name": "Shampoo", "price": 300, "image": "shampoo1.jpg", "category": "Beauty"},
{"name": "Face Wash", "price": 250, "image": "facewash1.jpg", "category": "Beauty"},

# 🔹 MORE BEAUTY PRODUCTS
{"name": "Lipstick Matte Red", "price": 499, "image": "lip1.jpg", "category": "Beauty"},
{"name": "Lipstick Nude Shade", "price": 550, "image": "lip2.jpg", "category": "Beauty"},
{"name": "Lip Balm", "price": 199, "image": "lipbalm.jpg", "category": "Beauty"},
{"name": "Foundation Cream", "price": 899, "image": "foundation.jpg", "category": "Beauty"},
{"name": "Compact Powder", "price": 399, "image": "powder.jpg", "category": "Beauty"},
{"name": "Eyeliner", "price": 299, "image": "eyeliner.jpg", "category": "Beauty"},
{"name": "Mascara", "price": 450, "image": "mascara.jpg", "category": "Beauty"},
{"name": "Makeup Kit", "price": 1500, "image": "makeupkit.jpg", "category": "Beauty"},
{"name": "Nail Polish Set", "price": 350, "image": "nail.jpg", "category": "Beauty"},
{"name": "Hair Serum", "price": 600, "image": "serum.jpg", "category": "Beauty"},

# 🔹 MORE FASHION (MEN & WOMEN)
{"name": "Men Kurta", "price": 1800, "image": "kurta.jpg", "category": "Fashion"},
{"name": "Men Blazer", "price": 4000, "image": "blazer.jpg", "category": "Fashion"},
{"name": "Women Saree", "price": 2500, "image": "saree.jpg", "category": "Fashion"},
{"name": "Women Lehenga", "price": 5000, "image": "lehenga.jpg", "category": "Fashion"},
{"name": "Women Handbag Premium", "price": 3000, "image": "bag2.jpg", "category": "Fashion"},

# 🔹 MORE ELECTRONICS
{"name": "Smart TV", "price": 45000, "image": "tv.jpg", "category": "Electronics"},
{"name": "Tablet", "price": 20000, "image": "tablet.jpg", "category": "Electronics"},
{"name": "Power Bank", "price": 1500, "image": "powerbank.jpg", "category": "Electronics"},
{"name": "Wireless Earbuds", "price": 2500, "image": "earbuds.jpg", "category": "Electronics"},

# 🔹 MORE HOME PRODUCTS
{"name": "Dining Table", "price": 15000, "image": "table.jpg", "category": "Home"},
{"name": "Sofa Set", "price": 30000, "image": "sofa.jpg", "category": "Home"},
{"name": "Wall Clock", "price": 800, "image": "clock.jpg", "category": "Home"},

# 🔹 MORE BOOKS
{"name": "Deep Learning Book", "price": 1200, "image": "book5.jpg", "category": "Books"},
{"name": "Web Development Book", "price": 700, "image": "book6.jpg", "category": "Books"},
]

# 🔥 TOP DEALS
def get_top_deals():
    return sorted(products, key=lambda x: x['price'])[:8]

# 🤖 IMPROVED AI
def ai_reply(msg):
    msg = msg.lower()

    if "hi" in msg or "hello" in msg:
        return "Hello 👋 Welcome to Shopping World! How can I help you?"

    elif "phone" in msg:
        return "We have great phones in Electronics section 📱"

    elif "dress" in msg or "fashion" in msg:
        return "Check Fashion category 👗 for trending styles!"

    elif "cheap" in msg or "low price" in msg:
        return "Check Top Deals 🔥 for best prices!"

    elif "beauty" in msg:
        return "Explore Beauty section 💄 for cosmetics!"

    else:
        return "I can help you find products 😊 Try: phone, dress, beauty..."

# 🏠 HOME
@app.route('/')
def home():
    return render_template("index.html",
                           products=products,
                           deals=get_top_deals(),
                           ratings=ratings)

# 🔍 SEARCH
@app.route('/search')
def search():
    query = request.args.get('query')
    result = [p for p in products if query.lower() in p['name'].lower()]
    return render_template("index.html",
                           products=result,
                           deals=get_top_deals(),
                           ratings=ratings)

# 📂 CATEGORY
@app.route('/category/<name>')
def category(name):
    filtered = [p for p in products if p['category'] == name]
    return render_template("index.html",
                           products=filtered,
                           deals=get_top_deals(),
                           ratings=ratings)

# 🛒 CART
@app.route('/add_to_cart/<name>')
def add_to_cart(name):
    for p in products:
        if p['name'] == name:
            cart.append(p)
    return redirect('/')

@app.route('/remove_from_cart/<name>')
def remove_from_cart(name):
    for item in cart:
        if item['name'] == name:
            cart.remove(item)
            break
    return redirect('/cart')

@app.route('/cart')
def view_cart():
    total = sum(i['price'] for i in cart)
    return render_template("cart.html", cart=cart, total=total)

# ❤️ WISHLIST
@app.route('/add_to_wishlist/<name>')
def add_to_wishlist(name):
    for p in products:
        if p['name'] == name and p not in wishlist:
            wishlist.append(p)
    return redirect('/')

@app.route('/remove_from_wishlist/<name>')
def remove_from_wishlist(name):
    for i in wishlist:
        if i['name'] == name:
            wishlist.remove(i)
            break
    return redirect('/wishlist')

@app.route('/wishlist')
def view_wishlist():
    return render_template("wishlist.html", wishlist=wishlist)

# ⭐ FIXED RATING PER PRODUCT
@app.route('/rate/<name>/<int:value>')
def rate(name, value):
    ratings[name] = value
    return redirect('/')

# 💳 PAYMENT
# 💳 PAYMENT PAGE
@app.route('/payment')
def payment():
    return render_template("payment.html")


# 💳 PROCESS PAYMENT (FIX FOR 404 ERROR)
@app.route('/process_payment', methods=['POST'])
def process_payment():
    method = request.form.get('method')

    if method == "cod":
        name = request.form.get('name')
        phone = request.form.get('phone')
        address = request.form.get('address')

        if not name or not phone or not address:
            return "Please fill all COD details ❗"

        return render_template("success.html",
                               msg=f"Order placed successfully for {name} (Cash on Delivery)")

    elif method == "upi":
        return render_template("success.html",
                               msg="Payment Successful via UPI ✅")

    return "Payment Failed ❌"

# 🤖 CHAT API
@app.route('/chat', methods=['POST'])
def chat():
    msg = request.form['msg']
    return jsonify({"reply": ai_reply(msg)})

# 🔐 LOGIN
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if users.get(request.form['username']) == request.form['password']:
            return redirect('/')
        return render_template("login.html", error="Invalid login")
    return render_template("login.html")

# 🔐 SIGNUP
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        users[request.form['username']] = request.form['password']
        return redirect('/login')
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)