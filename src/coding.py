import functools
from flask import *
from src.dbconnection import *
from _datetime import *

app = Flask(__name__)
app.secret_key="123"




def login_required(func):
	@functools.wraps(func)
	def secure_function():
		if "lid" not in session:
			return render_template('login_index.html')
		return func()
	return secure_function

@app.route('/logout')
@login_required
def logout():
	session.clear()
	return redirect('/')

@app.route("/lg")
def log():
    return render_template("login.html")





@app.route("/")
def aaa():
    return render_template("homp.html")


@app.route("/pr")
def fr():
    return render_template("fruit.html")

@app.route("/cont")
def con():
    return render_template("contact.html")

@app.route("/ser")
def se():
    return render_template("service.html")

#LOGIN FUNCTION
@app.route('/login', methods=['post', 'get'])
def login():
    username = request.form['textfield']
    password = request.form['textfield2']
    qry = "SELECT * FROM `login` WHERE `username`=%s AND `password`=%s"
    val = (username, password)
    res = selectone(qry, val)

    if res is None:
        return '''<script>alert("invalid"); window.location="/"</script>'''
    elif res['type'] == 'admin':
        session['lid']=res['login_id']
        return redirect('/admhome')
    elif res['type'] == 'user':
        session['lid'] = res['login_id']
        return redirect('/userdashboard')
    else:
        return '''<script>alert("invalid"); window.location="/"</script>'''



@app.route("/admhome")
@login_required
def admhome():
    return render_template("admin home.html")


@app.route("/category")
@login_required
def category():
    qry = "SELECT * FROM `category` ORDER BY `category_name`"
    res = selectall(qry)
    return render_template("CATEGORY.html",val=res)

@app.route("/addcategory")
@login_required
def addcategory():
    return render_template("ADD CATEGORY.html",)

#ADD CATEGORY
@app.route('/addcat', methods=['post'])
def addcat():
    catname = request.form['textfield']
    catimg = request.files['file']
    im = datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    catimg.save("static/cat/category"+im)
    qry = "INSERT INTO `category` VALUES (NULL,%s,%s)"
    val = (catname, im)
    iud(qry, val)
    return '''<script>alert("Category added successfuly");window.location="category"</script>'''

#UPDATE CATEGORY
@app.route("/upcat")
def upcat():
    id = request.args.get('id')
    session['cid'] = id
    q="SELECT * FROM `category` WHERE category_id=%s"
    res=selectone(q,id)
    return render_template("UPDATE CATEGORY.html",val=res)

@app.route("/updcat",methods=['post'])
def updcat():
    catname = request.form['textfield']
    catimg = request.files['file']
    im = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    catimg.save("static/cat/category" + im)
    qry = "UPDATE `category` SET `category_name`=%s,`image`=%s WHERE `category_id`=%s"
    val = (catname, im,session['cid'])
    iud(qry, val)
    return '''<script>alert("Category updated successfuly");window.location="category"</script>'''

@app.route("/delcat",methods=['post','get'])
def delcat():
    id = request.args.get('id')
    session['cid'] = id
    q = "DELETE FROM `category` WHERE `category_id`=%s"
    iud(q,id)
    return '''<script>alert("Category removed successfuly");window.location="category"</script>'''



@app.route("/addmanproduct")
def addmanproduct():
    #query for viewing products
    q = "SELECT `category`.`category_name`,`products`.*  FROM `category`JOIN`products` ON `products`.`category_id`=`category`.`category_id` order by `products`.`p_name` "
    res = selectall(q)
    return render_template("AD MANAGE PRODUCT.html",val=res)

@app.route("/search1",methods=['post'])
def searchp():
    sr = request.form['textfield']
    q="SELECT * FROM `products` WHERE `p_name` LIKE '%"+sr+"%'"
    res=selectall(q)
    return render_template("AD MANAGE PRODUCT.html",val=res)


@app.route("/addproduct")
def addproduct():
    #for category dropdown
    q = "SELECT DISTINCT `category_id`,`category_name` FROM `category`"
    res = selectall(q)
    return render_template("ADD PRODUCT.html",val=res)


#ADD PRODUCT
@app.route('/addpro', methods=['post'])
def addpro():
    proname = request.form['textfield']
    detl = request.form['textarea']
    price = request.form['textfield2']
    stok = request.form['textfield3']
    catg = request.form['select']
    qty = request.form['qty']
    proimg = request.files['file']

    im = datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    proimg.save("static/pro/product"+im)
    qry = "INSERT INTO `products` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s)"
    val = (catg, proname, detl, price, stok,qty, im)
    iud(qry, val)
    return '''<script>alert("product added successfuly");window.location="addmanproduct"</script>'''


#updating product details
@app.route("/editpro")
def editpro():
    q = "SELECT DISTINCT `category_id`,`category_name` FROM `category`"
    res1 = selectall(q)
    id = request.args.get('id')
    session['pid']=id
    q1 = "SELECT `category`.`category_name`,`products`.*  FROM `category`JOIN`products` ON `products`.`category_id`=`category`.`category_id` where products.product_id=%s"
    res = selectone(q1,id)
    return render_template("EDIT PRODUCT.html",val=res,val1=res1)


@app.route("/editproduct",methods=['post'])
def editproduct():
    proname = request.form['textfield']
    detl = request.form['textarea']
    price = request.form['textfield2']
    stok = request.form['textfield3']
    catg = request.form['select']
    qty = request.form['qty']
    proimg = request.files['file']
    if proimg.filename=="":
        q = "UPDATE products SET  `category_id` = %s, `p_name` = %s, `details` = %s, `price` = %s, `stock` = %s, `quantity` =%s WHERE product_id=%s "
        val = (catg, proname, detl, price, stok,qty,session['pid'])
        iud(q, val)
        return '''<script>alert("Product updated successfuly");window.location="addmanproduct"</script>'''

    else:
        im = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        proimg.save("static/pro/product" + im)
        q = "UPDATE products SET `category_id` = %s, `p_name` = %s, `details` = %s, `price` = %s, `stock` = %s, `quantity` =%s,`image` = %s WHERE product_id=%s "
        val = (catg, proname, detl, price, stok,qty,im,session['pid'])
        iud(q, val)
        return '''<script>alert("Product updated successfuly");window.location="addmanproduct"</script>'''

@app.route("/delpro",methods=['post','get'])
def delpro():
    id = request.args.get('id')
    session['pid'] = id
    q = "DELETE FROM `products` WHERE `product_id`=%s"
    iud(q,id)
    return '''<script>alert("Product removed successfuly");window.location="addmanproduct"</script>'''

#products search
@app.route("/serpro",methods=['post','get'])
def serpro():
    ps = request.form['textfield']



@app.route("/addmanhome")
def addmanhome():
    #for viewing home-stay
    q = "SELECT * FROM `homestay`"
    res = selectall(q)
    return render_template("HOME-STAY.html",val=res)


@app.route("/addhomestay")
def addhomestay():
    return render_template("ADD HOMESTAY.html")


#for adding homestay
@app.route('/adhom',methods=['post'])
def adhom():
    homname = request.form['textfield4']
    detl = request.form['textarea']
    rate = request.form['textfield2']
    status = request.form['radiobutton']
    homimg = request.files['file']
    im = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    homimg.save("static/hom/hom" + im)
    qry = "INSERT INTO `homestay` VALUES(NULL,%s,%s,%s,%s,%s)"
    val = (homname, detl, rate, im, status)
    iud(qry, val)
    return '''<script>alert("Home-stay added successfuly");window.location="addmanhome"</script>'''

#updating home-stay
@app.route("/editho")
def editho():
    id = request.args.get('id')
    session['hid']=id
    q1 = "SELECT * FROM `homestay` WHERE `h_id`=%s"
    res = selectone(q1,id)
    return render_template("EDIT HOMESTAY.html",val=res)


@app.route("/edithom",methods=['post'])
def edithom():
    homname = request.form['textfield4']
    detl = request.form['textarea']
    rate = request.form['textfield2']
    status = request.form['radiobutton']
    homimg = request.files['file']
    if homimg.filename=="":
        q = "UPDATE `homestay` SET `h_name`=%s,`details`=%s,`rate`=%s,`status`=%s WHERE `h_id`=%s"
        val = (homname,detl, rate, status,session['hid'])
        iud(q, val)
        return '''<script>alert("Home-stay updated successfuly");window.location="addmanhome"</script>'''

    else:
        im = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        homimg.save("static/hom/hom" + im)
        q = "UPDATE `homestay` SET `h_name`=%s,`details`=%s,`rate`=%s,`image`=%s,`status`=%s WHERE `h_id`=%s"
        val = (homname, detl, rate, im ,status, session['hid'])
        iud(q, val)
        return '''<script>alert("Home-stay updated successfuly");window.location="addmanhome"</script>'''



#removing home-stay
@app.route("/delhom",methods=['post','get'])
def delhom():
    id = request.args.get('id')
    session['hid'] = id
    q = "DELETE FROM `homestay` WHERE `h_id`=%s"
    iud(q,id)
    return '''<script>alert("Home-stay removed successfuly");window.location="addmanhome"</script>'''

@app.route("/allorders")
def allorders():
    return render_template("ALL ORDERS.html")


@app.route("/canceldorders")
def canceldorders():
    return render_template("CANCELLED ORDERS.html")


@app.route("/allbooking")
def allbooking():
    return render_template("ALL BOOKINGS.html")


@app.route("/allfeed")
def allfeed():
    return render_template("ALL FEEDBACKS.html")


@app.route("/register")
def register():
    q = "SELECT `username` FROM `login`"
    k = selectall(q)
    return render_template("user/Register.html",val=k)

@app.route("/registration",methods=['post','get'])
def registration():
    try:
        fname=request.form['textfield']
        lname=request.form['textfield2']
        gender=request.form['radiobutton']
        place=request.form['textfield3']
        post = request.form['textfield4']
        pincode = request.form['textfield5']
        phone = request.form['textfield6']
        email = request.form['textfield7']
        username = request.form['textfield8']
        password = request.form['textfield9']

        qry = "INSERT INTO `login` VALUES(NULL,%s,%s,'user')"
        val = (username, password)
        id = iud(qry, val)

        qry1 = "INSERT INTO `register` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val1 = (str(id), fname, lname, gender, place, post, pincode, phone, email)
        iud(qry1, val1)
        return '''<script>alert("Registerd successfuly");window.location="lg"</script>'''
    except Exception as e:
         return '''<script>alert("Usename unavailable");window.location="register"</script>'''



@app.route("/userdashboard")
def userdashboard():
    return render_template("user/dash.html")


@app.route("/userhome")
def userhome():
    q="SELECT * FROM `register` WHERE `login_id`=%s"
    val=selectone(q,session['lid'])
    return render_template("user/usrdash.html")

@app.route("/csearch",methods=['post'])
def csearch():
    sr = request.form['textfield']
    if sr == "":
        return '''<script>alert('enter a category name');window.location="userhome"</script>'''
    else:
        q = "SELECT * FROM `category` WHERE `category_name` LIKE '%" + sr + "%'"
        res = selectall(q)
        return render_template("user/VIEW CATEGORY.html",val=res)



@app.route("/search",methods=['post'])
def search():
    sr = request.form['textfield']
    if sr == "":
        return '''<script>alert('enter a product name');window.location="userhome"</script>'''
    else:
        q = "SELECT * FROM `products` WHERE `p_name` LIKE '%" + sr + "%'"
        res = selectall(q)
        return render_template("user/PRODUCT.html", val=res)


@app.route("/forg")
def forg():
    #ph = request.form['textfield3']
    #q="SELECT `login`.* FROM `login` JOIN `register` ON `login`.`login_id`=`register`.`login_id` WHERE `phone`=%s"
    #val = (ph)
    #res = selectone(q, val)
    return render_template("user/forpas.html")

@app.route("/forgo",methods=['post','get'])
def forgot():
    ph = request.form['textfield3']
    q = "SELECT `login`.* FROM `login` JOIN `register` ON `login`.`login_id`=`register`.`login_id` WHERE `phone`=%s"
    val=(ph)
    res=selectone(q,val)
    return render_template("user/forgsh.html",val1=res)


@app.route("/updprof")
@login_required
def updprof():
    q1 = "SELECT * FROM `register` WHERE register.login_id=%s"
    res=selectone(q1,session['lid'])
    return render_template("updprof.html",val=res)


@app.route("/updpro",methods=['post','get'])
def updpro():
    fname = request.form['textfield']
    lname = request.form['textfield2']
    gender = request.form['radiobutton']
    place = request.form['textfield3']
    post = request.form['textfield4']
    pincode = request.form['textfield5']
    phone = request.form['textfield6']
    email = request.form['textfield7']
    qry1 = "UPDATE `register` SET `first_name`=%s,`last_name`=%s,`gender`=%s,`place`=%s,`post`=%s,`pin`=%s,`phone`=%s,`email_id`=%s WHERE `login_id`=%s"
    val1 = (fname, lname, gender, place, post, pincode, phone, email,session['lid'])
    iud(qry1, val1)
    return '''<script>alert("profile updated successfuly");window.location="userhome"</script>'''


@app.route("/viewcategory")
@login_required
def viewcategory():
    qry = "SELECT * FROM `category`"
    res = selectall(qry)
    return render_template("user/VIEW CATEGORY.html",val=res)

@app.route("/products")
@login_required
def products():
    id = request.args.get('id')
    session['category_id'] = id
    qry = "SELECT `category`.`category_name`,`products`.* FROM `products` JOIN `category` ON `category`.`category_id`=`products`.`category_id` WHERE `products`.`category_id`=%s"
    res = selectall2(qry,str(id))
    q2="SELECT `category_name` FROM `category` WHERE `category_id`=%s"
    re2=selectone(q2,str(id))
    return render_template("user/PRODUCT.html",val=res,val1=re2)


@app.route("/viewproduct")
def viewproduct():
    id = request.args.get('id')
    session['pro_id'] = id
    q="SELECT * FROM `products` WHERE `product_id`=%s"
    res=selectone(q,str(session['pro_id']))
    q1="SELECT * FROM `register` WHERE `login_id`=%s"
    res2=selectone(q1,session['lid'])
    return render_template("user/VIEW PRODUCT.html",val=res,val2=res2)

@app.route("/viewproduct_alert")
@login_required
def viewproduct_alert():
    q="SELECT * FROM `products` WHERE `product_id`=%s"
    res=selectone(q,str(session['pro_id']))
    q1="SELECT * FROM `register` WHERE `login_id`=%s"
    res2=selectone(q1,session['lid'])
    return render_template("user/VIEW PRODUCT.html",val=res,val2=res2)


@app.route("/buynow",methods=['post'])
def buynow():
    btn=request.form['Submit2']
    if btn == "BUY NOW":
        qty = request.form['select']
        add = request.form['textarea']
        pid=session['pro_id']
        lid=session['lid']
        q="SELECT `price`,`stock` FROM `products` WHERE `product_id`=%s"
        res = selectone(q,pid)
        if int(res['stock'])>=int(qty):
            totpr = int(res['price'])*int(qty)
            # nqty= int(res['stock'])-int(qty)
            qr="INSERT INTO `order` VALUES(null,%s,curdate(),%s,'pending','0',%s)"
            val = (lid, totpr, add)
            oid=iud(qr,val)
            qry="INSERT INTO `order_item`  VALUES(null,%s,%s,%s,'pending')"
            val1= (oid, pid, qty)
            iud(qry,val1)
            # qr1="UPDATE `products` SET `stock`=%s WHERE `product_id`=%s"
            # val2=(nqty,pid)
            # iud(qr1,val2)
            return render_template("user/payment.html",pr=totpr)
        else:
            return "<script>alert('quantity unavailable');window.location='/viewproduct?id="+pid+"'</script>"
    else:
        qty = request.form['select']
        add = request.form['textarea']
        pid = session['pro_id']
        lid = session['lid']
        q = "SELECT `price` FROM `products` WHERE `product_id`=%s"
        res = selectone(q, pid)
        totpr = int(res['price']) * int(qty)
        qr = "INSERT INTO `order` VALUES(null,%s,'0',%s,'cart','0',%s)"
        val = (lid, totpr, add)
        oid = iud(qr, val)
        d = "INSERT INTO `order_item`  VALUES(null,%s,%s,%s,'cart')"
        val1 = (oid, pid, qty)
        iud(qry, val1)
        return render_template("user/CART.html")



@app.route("/paymt")
def paymt():
    return render_template("user/payment.html")



@app.route("/cart")
def cart():
    return render_template("user/CART.html")


@app.route("/order")
def order():
    return render_template("user/ORDER FROM CART.html")


@app.route("/myorders")
def myorders():
    return render_template("user/MY ORDERS.html")


@app.route("/homestay")
@login_required
def homestay():
    qry = "SELECT * FROM `homestay`"
    res = selectall(qry)
    return render_template("user/HOMESTAY.html",val=res)


@app.route("/viewhomes")
@login_required
def homes():
    id = request.args.get('id')
    session['ho_id'] = id
    qry = "SELECT * FROM `homestay` WHERE `h_id`=%s"
    res = selectone(qry, session['ho_id'])
    return render_template("user/VIEW HOMESTAY.html",val=res)


@app.route("/booking")
def booking():
    return render_template("user/BOOKING.html")


@app.route("/mybooking")
def mybooking():
    return render_template("user/MY BOOKINGS.html")


@app.route("/adfeedbak")
def adfeedbak():
    return render_template("user/ADD FEEDBACK.html")


app.run(debug=True)
