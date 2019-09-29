from flask import Flask,render_template ,redirect, url_for , request,jsonify
import sqlite3 as sql
import datetime
import hashlib

conn=sql.connect("database.db")
app = Flask(__name__)
@app.route('/home')
def home():
    return render_template("new_user.html")
@app.route('/home1')
def home1():
    return render_template("login.html")    

@app.route("/user_created",methods=["POST","GET"])
def user_created():
    if request.method=='POST':
        user_id=request.form['user_id']
        name = request.form['name']
        contact_no = request.form['contact_no']
        email_id = request.form['email']
        password = request.form['password']
    
    conn = sql.connect("database.db") 
    insert_command = "INSERT INTO register (user_id,name,contact_no,email_id,password) values\
                        ('"+user_id+"',"+"'"+name+"','"+contact_no+"','"+email_id+"','"+password+"');"
    conn.execute(insert_command)
    conn.commit()    
    
    return render_template("selfielessacts.html")


@app.route("/user_created1",methods=["POST","GET"])
def user_created1():
    if request.method=='POST':
        user_id=request.form['user_id']
        password = request.form['password']

    conn = sql.connect("database.db") 
    
    a="select user_id from register;"
    a1=list(conn.execute(a))
    conn.commit()
    a1=[i[0] for i in a1]
    b="select password from register;"
    b1=list(conn.execute(b))
    conn.commit()
    b1=[i[0] for i in b1]
    try:
        k=a1.index(user_id)  
        if(password==b1[k]):
            return render_template("selfielessacts.html")
        else:
            return render_template("new_user.html")	
    except:
        return render_template("new_user.html")        
def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d-%m-%Y:%S-%M-%H')
        return True
    except ValueError:
        return False
def is_sha1(maybe_sha1):
    if len(maybe_sha1)!= 40:
        return False
    try:
        sha_int = int(maybe_sha1, 16)
    except ValueError:
        return False
    return True
def isBase64(sb):
        try:
                if type(sb) == str:
                        sb_bytes = bytes(sb, 'ascii')
                elif type(sb) == bytes:
                        sb_bytes = sb
                else:
                        raise ValueError("Argument must be string or bytes")
                return base64.b64encode(base64.b64decode(sb_bytes)) == sb_bytes
        except Exception:
                return False
#api1
@app.route("/api/v1/users",methods=["POST","GET","PUT","DELETE"])
def add_user_api():
    if request.method=='POST':
        userdata= (request.get_json())
        user_id=userdata['user_id']
        password=userdata['password']
        conn = sql.connect("database.db")
        a="select user_id from register;"
        a1=list(conn.execute(a))
        conn.commit()
        a1=[i[0] for i in a1]
        if (user_id in a1) or(len(user_id)==0):
            return jsonify({}),400 #bad request
        else:        
            insert_command = "INSERT INTO register values\
                           ('"+user_id+"','"+password+"');"
            conn.execute(insert_command)
            conn.commit()
            #password=hashlib.sha1(password.encode('utf-8'))
            if is_sha1(password)==True:
                return jsonify({}),201 #request complete,created
            else:
                return jsonify({}),400 #bad request    
    elif request.method=='GET':
        conn = sql.connect("database.db")
        a="select user_id from login;"
        a1=list(conn.execute(a))
        conn.commit()
        a1=[i[0] for i in a1]
        if(len(a1)==0): 
            return jsonify({}),204 #no content  
        else:     
            return jsonify(a1),200#Ok                
    else:
        return jsonify({}),405 #wrong method   
   
        
#api2
@app.route("/api/v1/users/<cuser_id>",methods=["POST","GET","PUT","DELETE"])
def del_user_api(cuser_id):
    if request.method=='DELETE':
        conn = sql.connect("database.db") 
        a="select user_id from register;"
        a1=list(conn.execute(a))
        conn.commit()
        a1=[i[0] for i in a1]
        if cuser_id in a1:
            conn = sql.connect("database.db")
            command="delete from register where user_id='"+cuser_id+"';"
            conn.execute(command)
            conn.commit() 
            return jsonify({}),200#request OK
        else:
               return jsonify({}),400#bad request
    else:        
        return jsonify({}),405#wrong method                            
        ''' 
        a="select user_id from register;"
        a1=list(conn.execute(a))
        conn.commit()
        a1=[i[0] for i in a1]
        for i in a1:
            if(cuser_id==i):
                return jsonify({}),200 
'''
#api3&4
@app.route("/api/v1/categories",methods=["POST","GET","PUT","DELETE"])  
def cate_api():
    if request.method=='GET':
        dcate={}
        conn = sql.connect("database.db")
        a="select category from cate;"
        a1=list(conn.execute(a))
        conn.commit()
        a1=[i[0] for i in a1]
        b="select num from cate;"
        b1=list(conn.execute(b))
        conn.commit()
        b1=[i[0] for i in b1]
        if(len(a1)==0):
            return jsonify({}),204 #no content  
        else:     
            dcate=dict(zip(a1,b1))
            return jsonify({'dcate':dcate}),200#Ok
    elif request.method=='POST':
            userdata= (request.get_json())
            category=userdata['category']
            conn = sql.connect("database.db")
            a="select category from cate;"
            a1=list(conn.execute(a))
            conn.commit()
            a1=[i[0] for i in a1]
            if category in a1:
                return jsonify({}),400 #bad request
            else:    
                conn = sql.connect("database.db")
                insert_command = "INSERT INTO cate values\
                           ('"+category+"',0);"
                conn.execute(insert_command)
                conn.commit()
            return jsonify({}),201#success
    else:
        return jsonify({}),405 #wrong method           
     
            
#api4
'''
@app.route("/api/v1/categories1",methods=["POST","GET","PUT","DELETE"])  
def  add_cat():          
    if request.method=='POST':
            userdata= (request.get_json())
            category=userdata['category']
            num=userdata['num']
            return jsonify({}),201
'''
#api5
@app.route("/api/v1/categories/<ccate>",methods=["POST","GET","PUT","DELETE"])
def del_cat(ccate):
    if request.method=='DELETE':
        conn = sql.connect("database.db") 
        a="select category from cate;"
        a1=list(conn.execute(a))
        conn.commit()
        a1=[i[0] for i in a1]
        if ccate in a1:   
            conn = sql.connect("database.db")
            command="delete from cate where category='"+ccate+"';"
            conn.execute(command)
            conn.commit() 
            return jsonify({}),200
        else:
               return jsonify({}),400
    else:
         return jsonify({}),405           
#api6&8
@app.route("/api/v1/categories/<cname>/acts",methods=["POST","GET","PUT","DELETE"])  
def api6(cname):
    if request.method=='GET':
        st=request.args.get('start',type=int,default=-1)
        ed=request.args.get('end',type=int,default=-1)
        if((st==-1) or (ed==-1)):   
            l=[]
            a2=[]
            l1=['act','user','time_stamp','cap','upv','imgB64']
            conn=sql.connect("database.db")
            b="select category from upload;"
            b1=list(conn.execute(b))
            conn.commit()
            b1=[i[0] for i in b1]
            if cname in b1:
                conn=sql.connect("database.db")
                a="select act_id,username,time_stamp,cap,upvotes,imgB64 from upload where category='"+cname+"';"
                a1=list(conn.execute(a))
                conn.commit()
                c="select count(act_id) from upload where category='"+cname+"';"
                c1=list(conn.execute(c))
                conn.commit()
                c1=[i[0] for i in c1]
                if((c1[0])<=100):
                        d={}
                        for i in range(len(a1)):
                            l.append(list(a1[i]))
                        for i in range(len(a1)):
                            d=dict(zip(l1,l[i]))
                            a2.append(d)
                        return jsonify({'a2':a2}),200
                else:    
                    return jsonify({}),413
            else:
                return jsonify({}),204            

        else:
                l=[]
                a2=[]
                l1=['act','user','time_stamp','cap','upv','imgB64']
                conn=sql.connect("database.db")
                b="select category from upload;"
                b1=list(conn.execute(a))
                conn.commit()
                b1=[i[0] for i in b1]
                if cname in b1:
                    conn=sql.connect("database.db")
                    a="select act_id,username,time_stamp,cap,upvotes,imgB64 from upload where category='"+cname+"';"
                    a1=list(conn.execute(a))
                    conn.commit()
                    if((ed-st+1)<=100):
                        if((len(a1)<ed) and (len(a1)>st)):
                            d={}
                            for i in range(len(a1)):
                                l.append(list(a1[i]))
                            for i in range(len(a1)):
                                d=dict(zip(l1,l[i]))
                                a2.append(d)
                            return jsonify({'a2':a2}),200
                    else:    
                        return jsonify({}),413    
                else:
                    return jsonify({}),204        
    else:
        return jsonify({}),405             
                    

#api7
@app.route("/api/v1/categories/<cname>/acts/size",methods=["POST","GET","PUT","DELETE"])  
def no_cate_api(cname):
    if request.method=='GET':
        conn = sql.connect("database.db")
        a="select category from cate;"
        a1=list(conn.execute(a))
        conn.commit()
        a1=[i[0] for i in a1]
        k=a1.index(cname)
        b="select num from cate;"
        b1=list(conn.execute(b))
        conn.commit()
        b1=[i[0] for i in b1]
        if (cname in a1) and (b1[k]!=0):    
            return jsonify(b1[k]),200
        else:       
            return jsonify({}),204
    else:
        return jsonify({}),405
#api8
'''
@app.route("/api/v1/categories6/<cname>/acts?start=<int:st>&end=<int:ed>",methods=["POST","GET","PUT","DELETE"])  
def api8(cname,st,ed):
    if request.method=='GET':
        l=[]
        a2=[]
        l1=['act','user','cap','upv']
        conn=sql.connect("database.db")
        a="select act_id,username,cap,upvotes from upload where category='"+cname+"';"
        a1=list(conn.execute(a))
        conn.commit()
        if((len(a1)<100) and (len(a1)>50)):
            d={}
            for i in range(71):
                l.append(list(a1[i]))
            for i in range(71):
                d=dict(zip(l1,l[i]))
                a2.append(d)
            return jsonify({'a2':a2}),200
        else:    
            return jsonify({}),405
'''
#api9
@app.route("/api/v1/acts/upvote",methods=["POST","GET","PUT","DELETE"])  
def api_upv():
    if request.method=='POST':
        userdata= (request.get_json())
        act_id=userdata['act_id']
        conn=sql.connect("database.db")
        a="select act_id from upload;"
        a1=list(conn.execute(a))
        conn.commit()
        a1=[i[0] for i in a1]
        if int(act_id) in a1:        
            conn=sql.connect("database.db")
            b="update upload set upvotes = upvotes + 1 WHERE act_id="+act_id+";"
            conn.execute(b)    
            conn.commit()
            return jsonify({}),200#OK
        else:
             return jsonify({}),400#bad request   
    else:
        return jsonify({}),405 #wrong method     
#api10
@app.route("/api/v1/acts/<cid>",methods=["POST","GET","PUT","DELETE"])
def del_act(cid):
    if request.method=='DELETE':
        conn = sql.connect("database.db") 
        a="select act_id from upload;"
        a1=list(conn.execute(a))
        conn.commit()
        a1=[i[0] for i in a1]
        if int(cid) in a1:
            conn = sql.connect("database.db")
            command="delete from upload where act_id="+cid+";"
            conn.execute(command)
            conn.commit() 
            return jsonify({}),200#request OK
        else:
               return jsonify({}),400#bad request
    else:
        return jsonify({}),405 #wrong method 

#api11
@app.route("/api/v1/acts",methods=["POST","GET","PUT","DELETE"])
def upl_api():
        if request.method=='POST':
            userdata= (request.get_json())
            category=userdata['category']
            act_id=userdata['act_id']
            username=userdata['username']
            cap=userdata['cap']
            time_stamp=userdata['time_stamp']
            imgB64=userdata['imgB64']
            if isBase64(imgB64)==False:
                return jsonify({}), 400
            if validate(time_stamp)==False:
                return jsonify({}), 400    
            conn=sql.connect("database.db")
            a="select act_id from upload;"
            a1=list(conn.execute(a))
            conn.commit()
            a1=[i[0] for i in a1]
            if int(act_id) in a1:
                return jsonify({}),400#bad request
            else:    
                conn=sql.connect("database.db")
                insert_command = "INSERT INTO upload values\
                            ('"+category+"','"+act_id+"','"+username+"','"+cap+"',0,'"+time_stamp+"','"+imgB64+"');"
                conn.execute(insert_command)
                conn.commit()
                return jsonify({}),201 
        else:
            return jsonify({}),405#wrong method

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
