import functools
from flask import *
from src.dbconnection import *
from _datetime import *
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key="123"




def login_required(func):
	@functools.wraps(func)
	def secure_function():
		if "lid" not in session:
			return render_template('login.html')
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
    else:
        if(res['username']==username and res['password']==password):
            if res['type'] == 'admin':
                session['lid']=res['login_id']
                return redirect('/admhome')
            elif res['type'] == 'user':
                session['lid'] = res['login_id']
                q="SELECT `first_name`,`last_name` FROM `register` WHERE `login_id`=%s"
                v=selectone(q,session['lid'])
                session['lnam']=v;
                return redirect('/userdashboard')
            else:
                return '''<script>alert("invalid"); window.location="/lg"</script>'''
        else:
            return '''<script>alert("password doesn't match"); window.location="/lg"</script>'''




@app.route("/admhome")
@login_required
def admhome():
    return render_template("admin home.html")

@app.route("/adm")
@login_required
def admh():
    return render_template("adm.html")


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
@login_required
def addcat():
    catname = request.form['textfield']
    catimg = request.files['file']
    stat = request.form['radiobutton']
    im = datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    catimg.save("static/cat/category"+im)
    qry = "INSERT INTO `category` VALUES (NULL,%s,%s,%s)"
    val = (catname, im, stat)
    iud(qry, val)
    return '''<script>alert("Category added successfuly");window.location="category"</script>'''


#UPDATE CATEGORY
@app.route("/upcat")
@login_required
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
    stat = request.form['radiobutton']
    im = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    catimg.save("static/cat/category" + im)
    qry = "UPDATE `category` SET `category_name`=%s,`image`=%s,`status`=%s WHERE `category_id`=%s"
    val = (catname, im, stat, session['cid'])
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
@login_required
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
    q = "SELECT DISTINCT `category_id`,`category_name` FROM `category` where `status`='Enabled'"
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

    q3="SELECT * FROM `products` WHERE `p_name`=%s"
    v=(proname)
    r=selectone(q3,v)
    if r is None:
        im = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        proimg.save("static/pro/product" + im)
        qry = "INSERT INTO `products` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s)"
        val = (catg, proname, detl, price, stok, qty, im)
        iud(qry, val)
        return '''<script>alert("product added successfuly");window.location="addmanproduct"</script>'''
    else :
        return '''<script>alert("product already added");window.location="addproduct"</script>'''

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

# #products search
# @app.route("/serpro",methods=['post','get'])
# def serpro():
#     ps = request.form['textfield']



@app.route("/addmanhome")
@login_required
def addmanhome():
    #for viewing home-stay
    q = "SELECT * FROM `homestay`"
    res = selectall(q)
    return render_template("HOME-STAY.html",val=res)


@app.route("/addhomestay")
@login_required
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
@login_required
def allorders():
    return render_template("ALL ORDERS.html")


@app.route("/report")
@login_required
def report():
    return render_template("report.html")



@app.route("/allbooking")
@login_required
def allbooking():
    return render_template("ALL BOOKINGS.html")



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
    r=session['lnam']
    print(r)
    return render_template("user/usrdash.html",vl=r)

# @app.route("/csearch",methods=['post'])
# def csearch():
#     sr = request.form['textfield']
#     if sr == "":
#         return '''<script>alert('enter a category name');window.location="viewcategory"</script>'''
#     else:
#         q = "SELECT * FROM `category` WHERE `category_name` LIKE '%" + sr + "%'"
#         res = selectall(q)
#         return render_template("user/VIEW CATEGORY.html",val=res)



@app.route("/search",methods=['post'])
def search():
    sr = request.form['textfield']
    q = "SELECT `products`.* FROM `products` JOIN `category` ON `products`.`category_id`=`category`.`category_id` WHERE `p_name` LIKE '%" + sr + "%' AND `status`='Enabled'"
    res = selectall(q)
    return render_template("user/PRODUCT.html", val=res)

    # if sr == "":
    #     return '''<script>alert('enter a product name');window.location="userdashboard"</script>'''
    # else:
        #q = "SELECT * FROM `products` WHERE `p_name` LIKE '%" + sr + "%'"



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
    return '''<script>alert("profile updated successfuly");window.location="userdashboard"</script>'''


@app.route("/viewcategory")
@login_required
def viewcategory():
    qry = "SELECT * FROM `category` where `status`='Enabled' ORDER BY `category_name`"
    res = selectall(qry)
    return render_template("user/VIEW CATEGORY.html",val=res)

@app.route("/products")
@login_required
def products():
    id = request.args.get('id')
    session['category_id'] = id
    qry = "SELECT `category`.`category_name`,`products`.* FROM `products` JOIN `category` ON `category`.`category_id`=`products`.`category_id` WHERE `products`.`category_id`=%s"
    res = selectall2(qry,str(id))
    # q2="SELECT `category_name` FROM `category` WHERE `category_id`=%s"
    # re2=selectone(q2,str(id))
    return render_template("user/PRODUCT.html",val=res)

@app.route("/sort",methods=['post'])
def sort():
    sr = request.form['sort']
    print(sr)
    if sr == 'Sort by Name':
        q = "SELECT `products`.* FROM `products` JOIN `category` ON `products`.`category_id`=`category`.`category_id` WHERE `products`.`category_id`=%s ORDER BY `p_name`"
        res = selectall2(q,session['category_id'])
        return render_template("user/PRODUCT.html", val=res)
    elif sr == 'Sort by Price High to Low':
        q = "SELECT `products`.* FROM `products` JOIN `category` ON `products`.`category_id`=`category`.`category_id` WHERE `products`.`category_id`=%s ORDER BY `price`DESC"
        res = selectall2(q,session['category_id'])
        return render_template("user/PRODUCT.html", val=res)
    else:
        q = "SELECT `products`.* FROM `products` JOIN `category` ON `products`.`category_id`=`category`.`category_id` WHERE `products`.`category_id`=%s ORDER BY `price`ASC"
        res = selectall2(q,session['category_id'])
        return render_template("user/PRODUCT.html", val=res)


@app.route("/viewproduct")
@login_required
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
        if qty == "":
            return "<script>alert('Please enter a quantity');window.location='/viewproduct?id="+pid+"'</script>"
        elif int(qty)<=0:
            return "<script>alert('quantity unavailable');window.location='/viewproduct?id="+pid+"'</script>"
        elif int(res['stock'])>=int(qty):
            q = "SELECT * FROM `products` WHERE `product_id`=%s"
            res = selectone(q, str(session['pro_id']))
            q1 = "SELECT * FROM `register` WHERE `login_id`=%s"
            res2 = selectone(q1, session['lid'])

            totpr = int(res['price'])*int(qty)
            session['totl']=totpr
            nqty= int(res['stock'])-int(qty)
            session['netqty']=nqty

            qr="INSERT INTO `order` VALUES(null,%s,curdate(),%s,'pending','pending',%s)"
            val = (lid, totpr, add)
            oid=iud(qr,val)
            session['oid']=oid
            qry="INSERT INTO `order_item`  VALUES(null,%s,%s,%s,'pending')"
            val1= (oid, pid, qty)
            iud(qry,val1)


            q3="INSERT INTO `payment` VALUES(NULL,%s,%s,'online','pending',NULL)"
            val3=(oid,totpr)
            iud(q3, val3)

            return render_template("user/buynow.html",pr=totpr,p=qty,val=res,val2=res2)
        else:
            return "<script>alert('quantity unavailable');window.location='/viewproduct?id="+pid+"'</script>"
    else:
        # qty = request.form['select']
        qty = request.form['select']
        add = request.form['textarea']
        pid = session['pro_id']
        lid = session['lid']
        qry = "SELECT * FROM `order_item` WHERE `product_id`=%s AND `order_id` IN(SELECT `order_id` FROM `order` WHERE `user_id`=%s AND `status`='cart') "
        val=(pid,lid)
        print(qry,val)
        rescart=selectone(qry,val)
        if rescart is None:
            if int(qty)<0:
                return "<script>alert('quantity unavailable');window.location='/viewproduct?id=" + pid + "'</script>"
            else:
                qry="SELECT * FROM `order` WHERE `status`='cart' AND `user_id`=%s"
                res=selectone(qry,lid)
                if res is None:
                    qr = "INSERT INTO `order` VALUES(null,%s,'0','0','cart','0',%s)"
                    val = (lid, add)
                    oid = iud(qr, val)
                    d = "INSERT INTO `order_item`  VALUES(null,%s,%s,%s,'cart')"
                    val1 = (oid, pid, qty)
                    iud(d, val1)
                else:
                    oid = res['order_id']
                    d = "INSERT INTO `order_item`  VALUES(null,%s,%s,%s,'cart')"
                    val1 = (oid, pid, qty)
                    iud(d, val1)
                return "<script>alert('Product added to cart successfully');window.location='/viewproduct?id=" + pid + "'</script>"
        else:
            return "<script>alert('Product is already in the cart');window.location='/viewproduct?id=" + pid + "'</script>"


@app.route("/viewcart")
@login_required
def viewcart():
    qry = "SELECT `products`.*,`order_item`.`quantity` as q,oi_id,`order_item`.`quantity`*`products`.`price` AS qtp  FROM `products` JOIN `order_item` ON `products`.`product_id`=`order_item`.`product_id` JOIN `order` ON `order`.`order_id`=`order_item`.`order_id` WHERE `order`.`status`='cart' AND `user_id`=%s"
    res = selectall2(qry, session['lid'])

    qry = "SELECT  SUM(`order_item`.`quantity`*`products`.`price`) AS tp,`order`.`order_id` FROM `products` JOIN `order_item` ON `products`.`product_id`=`order_item`.`product_id` JOIN `order` ON `order`.`order_id`=`order_item`.`order_id` WHERE `order`.`status`='cart' AND `user_id`=%s"
    res1 = selectone(qry, session['lid'])
    val = res1['tp']
    val5 = res1['order_id']

    q2 = "SELECT SUM(`order_item`.`quantity`*`products`.`price`) AS tp ,`products`.*,`order_item`.`quantity` as q,oi_id  FROM `products` JOIN `order_item` ON `products`.`product_id`=`order_item`.`product_id` JOIN `order` ON `order`.`order_id`=`order_item`.`order_id` WHERE `order_item`.`status`='cart' AND `order`.`user_id`=%s GROUP BY `products`.`product_id`"
    res2 = selectone(q2, session['lid'],)
    val = res1['tp']

    q1 = "SELECT * FROM `register` WHERE `login_id`=%s"
    res2 = selectone(q1, session['lid'])

    q3 ="SELECT COUNT(`order_item`.`status`) FROM `order_item` JOIN `order` ON `order_item`.`order_id`=`order`.`order_id` WHERE `order_item`.`status`='cart' AND `order`.`user_id`=%s"
    re =selectone(q3, session['lid'])
    return render_template("user/cart1.html",val=res,tp=val,data=val5,ad=res2,co=re)

@app.route("/delcart",methods=['post','get'])
def delcart():
    id = request.args.get('id')
    session['oid'] = id
    q = "DELETE FROM `order_item` WHERE `oi_id`=%s"
    iud(q, id)
    return "<script>alert('Product removed from cart successfully');window.location='/viewcart'</script>"


@app.route("/paymt")
def paymt():
    return render_template("user/buynow.html")

@app.route("/paym",methods=['post', 'get'])
def paym():
    payscr = request.files['file']
    im = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    payscr.save("static/paym/paym" + im)

    pid = session['pro_id']

    qty=session['netqty']
    qr="UPDATE `order` SET `status`='paid' WHERE `order_id`=%s"
    iud(qr,session['oid'])

    q="UPDATE `order_item` SET `status`='paid' WHERE `order_id`=%s"
    iud(q,session['oid'])

    q1="UPDATE `products` SET `stock`=%s WHERE `product_id`=%s"
    val=(qty,pid)
    iud(q1,val)

    q3="UPDATE `payment` SET `status`='paid',`scrshot`=%s WHERE `order_id`=%s"
    val3=(im,session['oid'])
    iud(q3, val3)

    return "<script>alert('Order placed successfuly');window.location='/viewproduct?id=" + pid + "'</script>"


@app.route("/order/<oid>/<tp>")
def order(oid,tp):
    session['ord']=oid;
    session['totpr']=tp;

    q="INSERT INTO `payment` VALUES(NULL,%s,%s,'online','paid',NULL)"
    val=(oid,tp)
    iud(q,val)

    iud("UPDATE `order` SET `price`=%s WHERE `order_id`=%s",(tp,oid))
    res = selectall2("SELECT * FROM `order_item` WHERE `order_id`=%s",oid)
    print(res)

    # iud("UPDATE `order_item` SET `status` ='cod' WHERE `order_id`=%s",(oid))
    qp="SELECT `products`.`stock` FROM `products` JOIN `order_item` ON `products`.`product_id`=`order_item`.`product_id` JOIN `order` ON `order_item`.`order_id`=`order`.`order_id` WHERE `order`.`order_id`=%s"
    re=selectall2(qp,session['ord'])


    if res:
        for i in res:
            q="select * from products where product_id=%s"
            r=selectone(q,i['product_id'])
            if int(i['quantity']) > int(r['stock']):
                return "<script>alert('quantity unavailable');window.location='/viewcart'</script>"
            elif int(i['quantity']) == 0:
                return "<script>alert('zero quantity unavailable');window.location='/viewcart'</script>"
        else:
            return "<script>alert('you are proceeding to payment');window.location='/paycart'</script>"

    return "<script>alert('there is no product in cart to order');window.location='/viewcart'</script>"

@app.route("/paycart")
def paycart():
    re=session['totpr']
    return render_template("user/paycart.html",val=re)


@app.route("/cartpay",methods=['post', 'get'])
def cartpay():
    payscr = request.files['file']
    im = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    payscr.save("static/paym/paym" + im)
    q = "UPDATE `payment` SET `scrshot`=%s WHERE `order_id`=%s"
    val=(im,session['ord'])
    iud(q,val)

    q1="UPDATE `order` SET `date`=curdate(),`status` = 'paid',`del_date`='pending',`price`=%s WHERE `order_id`=%s"
    va=(session['totpr'],session['ord'])
    iud(q1,va)

    q2="UPDATE `order_item` SET `status` ='paid' WHERE `order_id`=%s"
    va1=(session['ord'])
    iud(q2,va1)

    oid=session['ord'];
    res = selectall2("SELECT * FROM `order_item` WHERE `order_id`=%s", oid)
    print(res,"eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    # if res:
    for i in res:
        print(i['quantity'],i['product_id'], "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        iud("UPDATE `products` SET `stock`=`stock`-(%s) WHERE `product_id`=%s",(int(i['quantity']), i['product_id']))

    return "<script>alert('order placed successfuly');window.location='/viewcart'</script>"



    # return "<script>alert('paid successfuly');window.location='/paycart'</script>"


@app.route("/myorders")
def myorders():
    q="SELECT * from `order` WHERE `order`.`user_id`=%s AND `order`.`status`!='canceled' AND `order`.`status`!='cart'"
    res=selectall2(q,session['lid'])
    return render_template("user/MY ORDERS.html",val=res)

@app.route("/vieworder")
def vorders():
    id = request.args.get('id')
    session['od'] = id
    q="SELECT `order_item`.*,`products`.`p_name`,`products`.`qty`,`products`.`image` FROM `order` JOIN `order_item` ON `order`.`order_id`=`order_item`.`order_id` JOIN `products`ON `order_item`.`product_id`=`products`.`product_id` WHERE `order`.`order_id`=%s"
    res=selectall2(q,str(id))
    return render_template("vorder.html",val=res)

@app.route("/vieworder1")
def vorder():
    id = request.args.get('id')
    session['od'] = id
    q="SELECT `order_item`.*,`products`.`p_name`,`products`.`qty`,`products`.`image` FROM `order` JOIN `order_item` ON `order`.`order_id`=`order_item`.`order_id` JOIN `products`ON `order_item`.`product_id`=`products`.`product_id` WHERE `order`.`order_id`=%s"
    res=selectall2(q,str(id))
    return render_template("vorder1.html",val=res)

@app.route("/cancelorder")
def canorders():
    id = request.args.get('id')
    session['caod'] = id
    q2="SELECT `order`.`del_date` FROM `order` WHERE `order_id`=%s"
    re=selectone(q2, str(id))
    today = date.today()
    if re['del_date'] == str(today):
        return '''<script>alert("cant cancel");window.location='/myorders'</script>'''
    else:
        q = "UPDATE `order` SET `status`='canceled' WHERE `order_id`=%s"
        iud(q, str(id))

        qr = "UPDATE `order_item` SET `status`='canceled' WHERE `order_item`.`order_id`=%s"
        iud(qr, str(id))

        res = selectall2("SELECT * FROM `order_item` WHERE `order_id`=%s", str(id))
        if res:
            for i in res:
                iud("UPDATE `products` SET `stock`=`stock`+(%s) WHERE `product_id`=%s",
                    (int(i['quantity']), i['product_id']))
                # return "<script>alert('order placed');window.location='/viewcart'</script>"
        return "<script>alert('order canceled');window.location='/myorders'</script>"




@app.route("/allorder")
def alorders():
    q="SELECT `order`.*,`register`.`first_name`,`register`.`last_name`,`payment`.`scrshot` FROM `payment` JOIN `order` ON `payment`.`order_id`=`order`.`order_id`JOIN `login` ON `order`.`user_id`=`login`.`login_id` JOIN `register` ON `login`.`login_id`=`register`.`login_id` WHERE `order`.`status`!='cart' and `order`.`status`!='canceled' and `order`.`status`!='deliverd'"
    re=selectall(q)
    return render_template("ALL ORDERS.html",v=re)

@app.route("/deldate")
def deldate():
    id2 = request.args.get('id2')
    session['usd'] = id2
    q2="SELECT `register`.`email_id` FROM `register` JOIN `login` ON `register`.`login_id`=`login`.`login_id` WHERE `login`.`login_id`=%s"
    r1=selectone(q2,session['usd'])

    id = request.args.get('id')
    session['od'] = id


    q3 = "SELECT `products`.`p_name` as products FROM `products` JOIN `order_item` ON `products`.`product_id`=`order_item`.`product_id` JOIN `order` ON `order_item`.`order_id`=`order`.`order_id` WHERE `order`.`order_id`=%s"
    res1 = selectone(q3, session['od'])
    print(res1)

    q4 = "SELECT `products`.`p_name` FROM `products` JOIN `order_item` ON `products`.`product_id`=`order_item`.`product_id` JOIN `order` ON `order_item`.`order_id`=`order`.`order_id` WHERE `order`.`order_id`=%s"
    res2 = selectall2(q4, session['od'])

    p=[]
    for i in res2:
        p.append(i['p_name'])
    p1 = ','.join(p)
    print(','.join(p))
    d = datetime.now().strftime("%Y-%m-%d")
    return render_template("delivery.html",d=d,val=r1,pp = p1)

@app.route("/delivry",methods=['post'])
def delv():
    deld = request.form['t1']
    email=request.form['t3']
    session['eml']=email

    pr = request.form['prdct']
    session['prdct'] = pr



    q="UPDATE `order` SET `del_date`=%s WHERE `order_id`=%s"
    val1=(deld,session['od'])
    iud(q,val1)

    q3="SELECT `products`.`p_name` FROM `products` JOIN `order_item` ON `products`.`product_id`=`order_item`.`product_id` JOIN `order` ON `order_item`.`order_id`=`order`.`order_id` WHERE `order`.`order_id`=%s"
    res1=selectall2(q3,session['od'])

    q1="INSERT INTO `notification` VALUES(NULL,%s,curdate(),'your order for ' %s ' will be deliverd on ' %s ,curtime())"
    val2=(session['od'],pr,deld)
    iud(q1,val2)

    message="Your order of products "+pr+ "will be deliverd on "+deld+". \n Thank you for choosing us."
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("alenchristy0201@gmail.com", "xcbkvqojsymwwgyn")
    server.sendmail("alenchristy0201@gmail.com", email, message)



    return "<script>alert('delivery added');window.location='/allorder'</script>"

@app.route("/outfdel")
def outfdel():
    q5 = "SELECT `order`.`status` FROM `order` WHERE `order_id`=%s and `status`='Out for delivery'"
    rs = selectone(q5, session['od'])
    q2 = "SELECT `order`.`del_date` FROM `order` WHERE `order_id`=%s"
    re = selectone(q2, session['od'])
    today = date.today()
    if re['del_date'] != str(today):
        print(str(today))
        return "<script>alert('cant add out for delivery for this order');window.location='/allorder'</script>"
    elif rs is not None:
        return "<script>alert('out for delivery already added');window.location='/allorder'</script>"
    else:
        q = "UPDATE `order` SET `status`='Out for delivery' WHERE `order_id`=%s"
        iud(q, session['od'])
        pr = session['prdct']
        q1 = "INSERT INTO `notification` VALUES(NULL,%s,curdate(),'Your order of products ' %s ' is out for delivery and will be deliverd between 09:00 AM & 04:00 PM',curtime())"
        val2 = (session['od'], pr)
        iud(q1, val2)

        email = session['eml']
        message = "Your order of products " + pr + " is out for delivery. \nThank you for choosing us"
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("alenchristy0201@gmail.com", "xcbkvqojsymwwgyn")
        server.sendmail("alenchristy0201@gmail.com", email, message)
        return "<script>alert('order is out for delivery');window.location='/allorder'</script>"


@app.route("/deliverd")
def delvrd():
    q="UPDATE `order` SET `status`='deliverd' WHERE `order_id`=%s"
    iud(q,session['od'])

    pr = session['prdct']
    q1 = "INSERT INTO `notification` VALUES(NULL,%s,curdate(),'Your order of products ' %s ' is deliverd',curtime())"
    val2 = (session['od'],pr)
    iud(q1, val2)


    email = session['eml']
    message = "Your order of products "+pr+ " is deliverd. \nThank you for choosing us"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("alenchristy0201@gmail.com", "xcbkvqojsymwwgyn")
    server.sendmail("alenchristy0201@gmail.com", email, message)

    return "<script>alert('order is deliverd');window.location='/allorder'</script>"

@app.route("/rejectpay")
def rejpy():
    q="UPDATE `order` SET `status`='canceled' WHERE `order_id`=%s"
    iud(q,session['od'])
    q = "UPDATE `order_item` SET `status`='canceled' WHERE `order_id`=%s"
    iud(q, session['od'])
    q1 = "INSERT INTO `notification` VALUES(NULL,%s,curdate(),'Your order of products is rejected due to payment error',curtime())"
    val2 = (session['od'])
    iud(q1, val2)
    # return "<script>alert('order is rejected');window.location='/allorder'</script>"


    #new code for quantiy updating

    res = selectall2("SELECT * FROM `order_item` WHERE `order_id`=%s", session['od'])
    if res:
        for i in res:
            iud("UPDATE `products` SET `stock`=`stock`+(%s) WHERE `product_id`=%s",(int(i['quantity']), i['product_id']))
            # return "<script>alert('order placed');window.location='/viewcart'</script>"
    return "<script>alert('order canceled');window.location='/allorder'</script>"



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
    d=datetime.now().strftime("%Y-%m-%d")
    return render_template("user/BOOKING.html",d=d)


@app.route("/bookingm",methods=['post'])
def bookingm():
    fdat = request.form['textfield2']
    qr="SELECT * FROM `booking` WHERE `book_dat`=%s and `h_id`=%s"
    v=(fdat,session['ho_id'])
    res=selectone(qr,v)
    print(res)
    if res is None:
        q = "INSERT INTO `booking` VALUES(NULL,%s,%s,curdate(),'booked',%s)"
        val1 = (session['ho_id'], session['lid'], fdat)
        iud(q, val1)
        return "<script>alert('booked successfuly');window.location='/booking'</script>"
    else:
        return "<script>alert('booking date unavialable choose another date');window.location='/booking'</script>"


@app.route("/notif")
def notif():
    q="SELECT `notification`.* FROM `notification` JOIN `order` ON `notification`.`a_id`=`order`.`order_id` WHERE `order`.`user_id`=%s"
    v=selectall2(q,session['lid'])

    q1="SELECT COUNT(notifi) FROM `notification` JOIN `order` ON `notification`.`a_id`=`order`.`order_id` WHERE `order`.`user_id`=%s"
    re = selectone(q1, session['lid'])
    print(re)

    return render_template("user/notif.html",val=v,vl=re)



@app.route("/mybooking")
def mybooking():
    q="SELECT `booking`.*,`homestay`.* FROM `booking` JOIN `homestay` ON `booking`.`h_id`=`homestay`.`h_id` WHERE `user_id`=%s and `booking`.`status`!='canceled'"
    res=selectall2(q,session['lid'])
    return render_template("user/MY BOOKINGS.html",v=res)


@app.route("/cancelbook")
def canbook():
    id = request.args.get('id')
    session['cabo'] = id
    q="UPDATE `booking` SET `status`='canceled' WHERE `b_id`=%s"
    iud(q,str(id))
    return "<script>alert('booking canceled');window.location='/mybooking'</script>"

@app.route("/allbook")
def allbook():
    q="SELECT `booking`.*,`homestay`.*,`register`.* FROM `homestay` JOIN `booking` ON `booking`.`h_id`=`homestay`.`h_id` JOIN `login` ON `booking`.`user_id`=`login`.`login_id` JOIN `register` ON `login`.`login_id`=`register`.`login_id` WHERE `booking`.`status` !='canceled'"
    res=selectall(q)
    return render_template("ALL BOOKINGS.html",v=res)

@app.route("/aceptbook")
def acptbook():
    id = request.args.get('id')
    session['bokid'] = id
    q = "SELECT * FROM `booking` WHERE `b_id`=%s"
    res = selectone(q, str(id))
    if res['status'] == 'rejected':
        return "<script>alert('already rejected');window.location='/allbook'</script>"
    elif res['status'] == 'accepted':
        return "<script>alert('already accepted');window.location='/allbook'</script>"
    else:
        q = "UPDATE `booking` SET `status`='accepted' WHERE `b_id`=%s"
        iud(q, str(id))
        return "<script>alert('booking accepted');window.location='/allbook'</script>"


@app.route("/rejectbook")
def rejbook():
    id = request.args.get('id')
    session['boid'] = id
    q="SELECT * FROM `booking` WHERE `b_id`=%s"
    res=selectone(q, str(id))
    if res['status'] == 'rejected':
        return "<script>alert('already rejected');window.location='/allbook'</script>"
    elif res['status'] == 'accepted':
        return "<script>alert('already accepted');window.location='/allbook'</script>"
    else:
        q = "UPDATE `booking` SET `status`='rejected' WHERE `b_id`=%s"
        iud(q, str(id))
        return "<script>alert('booking rejected');window.location='/allbook'</script>"



@app.route("/fmin",methods=['post'])
def fmin():
    print(request.form)
    cnt=request.form['cnt']
    cnt1=request.form['cnt1']
    qry="UPDATE `order_item` SET `quantity`=%s WHERE `oi_id`=%s"
    val=(cnt,cnt1)
    iud(qry,val)

    qry="SELECT SUM(`order_item`.`quantity`*`products`.`price`) AS tp FROM `products` JOIN `order_item` ON `order_item`.`product_id`=`products`.`product_id` WHERE `order_item`.`order_id` IN(SELECT `order_id` FROM `order_item` WHERE `oi_id`=%s)"
    res=selectone(qry,cnt1)
    val=res['tp']

    return str(val)


app.run(debug=True)
