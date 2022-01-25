from unittest import result
from flask import Flask , request,jsonify
from flask_mysqldb import MySQL
import hashlib,re, uuid,jwt,datetime
from functools import wraps
import os
import urllib.request
from werkzeug.utils import secure_filename


app = Flask(__name__)
# JWT SECRET KEY
app.config['SECRET_KEY']='004f2af45d3a4e161a7dd2d17fdae47f'

#DATABASE CONNECTION 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'Api_project'
 
# MYSQL INSTANCE 
mysql = MySQL(app)


#JWT TOKEN VERIFICATION FUNCTION

def token_req(func):
    @wraps(func)
    def decorated(*args ,**kwargs):
        token=request.headers.get('token')
        print(token)
        if not token:
            return responce_maker("error", "Token missing","Token Mising")
        try:
            payload=jwt.decode(token,app.config['SECRET_KEY'],"HS256")
            user_id=str(payload["user_id"])
            e=check_jwt_token(user_id,token)
            if e==0 :
                return responce_maker("error", "Ex Token","Ex token") 
            return func(*args ,**kwargs) 
        except:
            return responce_maker("error", "Wrong Token2","Wrong token")
    return decorated



#INDEX FILE FUNCTION 
@app.route("/")
def index():
    return "<p>Hello, World!</p>"

# FOR REGISTER ENDPOINT
@app.route("/register",methods=['POST'])
def register():
        if request.method == "POST":
            message=[]
            result=[]
            try:          
                error=0
                regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'                  
                data=request.form
                fname=data['first_name'].strip()
                sname=data['secound_name'].strip()
                email=data['email'].strip()
                password=data['password'].strip()
                if not fname:
                    error+=1
                    message.append("First name is empty")
                if not sname:
                    error+=1
                    message.append("Secound name is empty")
                if not email:
                    error+=1
                    message.append("Email is empty")
                if not password:
                    error+=1
                    message.append("Password is empty")
                if len(password) < 8:
                    error+=1
                    message.append("Password should be greater then 8  ")    
                if not re.search(regex,email): 
                    error+=1
                    message.append("Enter Currect email")
                if error>0:

                    return(responce_maker("error",result,message))
                
                password =MD5_con(password)
                cur = mysql.connection.cursor()
                try: 
                    cur.execute("INSERT INTO `user_info` (`f_name`, `s_name`, `email`, `password`) VALUES (%s,%s,%s,%s);", (fname, sname,email,password))
                    mysql.connection.commit()
                    if cur.rowcount==1:
                        cur.close()
                        message.append("Account created..")
                        return responce_maker("sucess", result,message)
                    else:
                        cur.close()
                        message.append("Something Went wrong..")
                        return responce_maker("error", result,message)
                    
                except :
                    message.append("Email alredy exist , or Something went wrong , please try again")
                    return(responce_maker("error",result,message))



                
                
            except KeyError:
                message.append("Some Key Is missing")

                return (responce_maker("error",result,message))
            


        else:
            return "<p>Invailid Request </p>"


# FOR LOGIN ENDPOINT
@app.route("/login",methods=['POST'])
def login():
    if request.method == "POST":
            message=[]
            result=[]
            try:          
                error=0
                regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'                  
                data=request.form
                email=data['email'].strip()
                password=data['password'].strip()
                if not email:
                    error+=1
                    message.append("Email is empty")
                if not password:
                    error+=1
                    message.append("Password is empty")
                if len(password) < 8:
                    error+=1
                    message.append("Password should be greater then 8  ")    
                if not re.search(regex,email): 
                    error+=1
                    message.append("Enter Currect email")
                if error>0:
                    return(responce_maker("error",result,message))
                
                cur = mysql.connection.cursor()
                
                password =MD5_con(password)
                query="SELECT * FROM user_info where email='"+email+"' and password='"+password+"'"
                cur.execute(query)
                user = cur.fetchall()
                if not user:
                    message.append("Please enter vailid email and passwoerd") 
                    return responce_maker("error",result,message)
                else:
                    message.append("login done")
                    user_id=user[0][0]
                    print(user_id)
                    token = jwt.encode({'user_id' : user_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=145)}, app.config['SECRET_KEY'], "HS256")
                    update_jwt_token(user_id,token)
                    result={'token': token}
                    return responce_maker("sucess", result,message)

            except KeyError:
                message.append("Some Key Is missing")
                return (responce_maker("error",result,message))
            


    else:
        return "<p>Invailid Request </p>"

        
# FOR BLOG CRUD 
@app.route("/blog",methods=['POST','GET','DELETE','PUT'])
@token_req
def blog():
    user_id=0
    message=[]
    result=[]
    token=request.headers.get('token')
    error=0   
    if not token:
            return responce_maker("error", "Token missing1","Token Mising")
    try:
        payload=jwt.decode(token,app.config['SECRET_KEY'],"HS256")
        user_id=str(payload["user_id"])
    except:   
        return responce_maker("error", "Token missing1","Token Mising")    
        
    if request.method == "POST":
        try:
                data=request.form
                title=data['title'].strip()
                content=data['content'].strip()
                post_type=data['post_type'].strip()
                she_date=""
                if not title:
                    error+=1
                    message.append("Title is empty")
                if not content:
                    error+=1
                    message.append("Content is empty")
                if not post_type:
                    error+=1
                    message.append("post type is empty")
                if post_type!="SHE" and post_type!="NOW":
                    error+=1
                    message.append("Post type should be 'NOW' or 'SHE'")
                

                if post_type=="SHE" :
                     she_date=data['she_date'].strip()                
                     if not she_date:
                        error+=1
                        message.append("Shedule date is empty")
                        
                if error>0:
                    return(responce_maker("error",result,message))
                
                cur = mysql.connection.cursor()
                try: 
                    cur.execute("INSERT INTO `blog` (`title`, `content`,`post_type`,`publish_by`, `she_time`) VALUES (%s,%s,%s,%s,%s);", (title, content,post_type,user_id,she_date))
                    mysql.connection.commit()
                    if cur.rowcount==1:
                        cur.close()
                        id=cur.lastrowid
                        blog_activate(id)
                        message.append("Blog saved ...")
                        return responce_maker("sucess", result,message)
                    else:
                        cur.close()
                        message.append("Something Went wrong..")
                        return responce_maker("error", result,message)
                    
                except Exception as e :
                    message.append("Something went wrong , please try again"+str(e))
                    return(responce_maker("error",result,message))

        except :
                message.append("Some Key Is missing")

                return (responce_maker("error",result,message)) 

    if request.method == "PUT" :
        try:
                data=request.form
                title=data['title'].strip()
                id=data['id'].strip()
                content=data['content'].strip()
                post_type=data['post_type'].strip()
                she_date=""
                ver=""
                val=""
                if title:
                    if ver=="":
                     ver+="`title`='"+str(title)+"'"
                    else:
                        ver+=",`title`='"+str(title)+"'"
                  

                if content:
                    if ver=="":
                     ver+="`content`='"+str(content)+"'"
                    else:
                        ver+=",`content`='"+str(content)+"'"
                  

                if post_type:
                    if ver=="":
                     ver+="`post_type`='"+str(post_type)+"'"
                    else:
                        ver+=",`post_type`='"+str(post_type)+"'"
                    if post_type!="SHE" and post_type!="NOW":
                      error+=1
                      message.append("Post type should be 'NOW' or 'SHE'")
                

                    if post_type=="SHE" :
                       she_date=data['she_date'].strip() 
                       if ver=="":
                        ver+="`she_time`= '"+str(she_date)+"'"
                       else:
                         ver+=",`she_time`='"+str(she_date)+"'"
                       
                       if ver=="":
                         ver+="`is_published`= 'NOT'"
                       else:
                         ver+=",`is_published`= 'NOT'"
                    


                       if not she_date:
                        error+=1
                        message.append("Shedule date is empty")

                       
                    

                
                  

                cur = mysql.connection.cursor()
                query="UPDATE blog set"+ver+" where id="+str(id)    
                if error>0:
                    return(responce_maker("error",result,message))
                cur.execute(query)                    
                mysql.connection.commit()
                if cur.rowcount==1:
                        blog_activate(id)
                        message.append("Blog saved ...")
                        return responce_maker("sucess", result,message)
                else:
                        cur.close()
                        message.append("Something Went wrong..")
                        return responce_maker("error", result,message)
                    
                
                

        except Exception as e:
                message.append("Some Key Is missing"+ str(e))

                return (responce_maker("error",result,message)) 
        
    if request.method == "DELETE" : 
            try:
                data=request.form
                id=data['id'].strip()
                if not id:
                    error+=1
                    message.append("Blog ID is empty")
                cur = mysql.connection.cursor()
                query="DELETE from `blog` where publish_by="+str(user_id)+" and id="+str(id)    
                if error>0:
                    return(responce_maker("error",result,message))
                cur.execute(query)                    
                mysql.connection.commit()
                if cur.rowcount==1:
                        message.append("Blog Deleted ...")
                        return responce_maker("sucess", result,message)
                else:
                        cur.close()
                        message.append("Something Went wrong..")
                        return responce_maker("error", result,message)
            except Exception as e:
                message.append("Some Key Is missing"+ str(e))

                return (responce_maker("error",result,message)) 
     
    if request.method == "GET" :
         try:
                cur = mysql.connection.cursor()
                query="SELECT * FROM BLOG where status='active' and archive=0 and publish_by="+str(user_id)
                cur.execute(query)
                blog = cur.fetchall()
                if not blog:
                    message.append("your blog box is empty") 
                    return responce_maker("sucess",result,message)
                else:
                    message.append("Done") 
                    return responce_maker("sucess",create_blog_responce(blog),message)
               
         except Exception as e:
                message.append("Something went wrong"+ str(e))

                return (responce_maker("error",result,message)) 
     

# FOR BLOG LIST ALL BLOG THAT ACTIVE       
@app.route("/blog-list",methods=['GET'])
def blog_list():
    if request.method == "GET":
            message=[]
            result=[]
            try:  
                cur = mysql.connection.cursor()
                query="SELECT * FROM BLOG where status='active' and archive=0 and is_published='YES'"
                cur.execute(query)
                blog = cur.fetchall()
                if not blog:
                    message.append("your blog box is empty") 
                    return responce_maker("sucess",result,message)
                else:
                    message.append("Done") 
                    return responce_maker("sucess",create_blog_responce(blog),message)
                       
                
            except KeyError:
                message.append("Something went wrong ")
                return (responce_maker("error",result,message))
            


    else:
        return "<p>Invailid Request </p>"


# SCHEDULE BLOG CRON FUNCTION AND ENDPOINT
@app.route("/she-blog",methods=['GET'])
def she_blog():
    from datetime import datetime
    if request.method == "GET":
            message=[]
            result=[]
            try:  
                cur = mysql.connection.cursor()
                query="SELECT * FROM BLOG where status='active' and post_type='SHE' and is_published='NOT'"
                cur.execute(query)
                blog = cur.fetchall()
                if not blog:
                    message.append(" blog box is empty") 
                    return responce_maker("sucess",result,message)
                else:
                    for b in blog:
                        date_time_str = b[8]
                        now = datetime.now()
                        if date_time_str > now :
                            print(date_time_str)
                        else:
                            publish_blog(b[0])
                           


                        


                    message.append("Done") 
                    return responce_maker("sucess","done",message)
                       
                
            except KeyError:
                message.append("Something went wrong ")
                return (responce_maker("error",result,message))
            


    else:
        return "<p>Invailid Request </p>"


# FOR ARCHIVE ENDPOINT
@app.route("/archive",methods=['POST','GET'])
@token_req
def archive():
    user_id=0
    message=[]
    result=[]
    token=request.headers.get('token')
    error=0   
    if not token:
            return responce_maker("error", "Token missing1","Token Mising")
    try:
        payload=jwt.decode(token,app.config['SECRET_KEY'],"HS256")
        user_id=str(payload["user_id"])
    except:   
        return responce_maker("error", "Token missing1","Token Mising")    
        
    if request.method == "POST" :
        try:
                data=request.form
                id=data['id'].strip()
                
                if not id:
                    error+=1
                    message.append("id is empty")
                cur = mysql.connection.cursor()
                query="UPDATE blog set archive=True where id="+str(id)    
                if error>0:
                    return(responce_maker("error",result,message))
                cur.execute(query)                    
                mysql.connection.commit()
                if cur.rowcount==1:
                        cur.close()
                        message.append("Blog archived ...")
                        return responce_maker("sucess", result,message)
                else:
                        cur.close()
                        message.append("Something Went wrong..")
                        return responce_maker("error", result,message)
                
        except Exception as e:
                message.append("Some Key Is missing"+ str(e))

                return (responce_maker("error",result,message)) 
        
    if request.method == "GET" :
         try:
                cur = mysql.connection.cursor()
                query="SELECT * FROM BLOG where status='active' and archive=1 and publish_by="+str(user_id)
                cur.execute(query)
                blog = cur.fetchall()
                if not blog:
                    message.append("your blog box is empty") 
                    return responce_maker("sucess",result,message)
                else:
                    message.append("Done") 
                    return responce_maker("sucess",create_blog_responce(blog),message)
               
         except Exception as e:
                message.append("Something went wrong"+ str(e))

                return (responce_maker("error",result,message)) 

# UPLOAD IMAGE ENDPOINT 
@app.route("/upload_image",methods=['POST'])
@token_req
def upload_image():
   try:
    user_id=0
    message=[]
    result=[]
    token=request.headers.get('token')
    error=0   
    if not token:
            return responce_maker("error", "Token missing1","Token Mising")
    try:
        payload=jwt.decode(token,app.config['SECRET_KEY'],"HS256")
        user_id=str(payload["user_id"])
    except:   
        return responce_maker("error", "Token missing1","Token Mising")    
        
    if request.method == 'POST':
      f = request.files['file']
      da=str(f.filename.split('.')[2])
      fi=f.filename.split('.')
      array_length = len(fi)
      last_element = fi[array_length - 1]

      d=datetime.datetime.utcnow() 
      filename=MD5_con(str(user_id)+str(d))+"."+last_element
      f.save(secure_filename(filename))
      message.append("image uploaded")
      return responce_maker("sucess",filename,message)
   except Exception as e :
      return jsonify({'a': e})



# FOR BLOG ACTIVATION 
def blog_activate(id):
    cur = mysql.connection.cursor()
    query="SELECT * FROM blog where id="+str(id)
    cur.execute(query)
    blog = cur.fetchall()
    blog=blog[0]
    if blog[4] == "NOW" :
        try:
                    query="Update `blog` SET status ='active', publish_date=NOW(),is_published='YES' where id = "+str(id)
                    cur.execute(query)                    
                    mysql.connection.commit()
                    if cur.rowcount==1:
                        cur.close()
                        return(1)
                    else:
                        cur.close()
                        return(0)
        except Exception as e:
            print(e)
                
# FOR PUBLISH BLOG FUNCTION
def publish_blog(id):
    cur = mysql.connection.cursor()
    try:
                    query="Update `blog` SET status ='active', publish_date=NOW(),is_published='YES' where id = "+str(id)
                    cur.execute(query)                    
                    mysql.connection.commit()
                    if cur.rowcount==1:
                        cur.close()
                        return(1)
                    else:
                        cur.close()
                        return(0)
    except Exception as e:
            print(e)
                
 # CREATING BLOG RESPONCE
def create_blog_responce(blog):
    result=[]
    for b in blog:
        data={
            'id' : b[0],
            'title':b[1],
            'content' : b[2],
            'post_type' :b[4],
            'is_published' :b[5],
            'user_id' : b[6],
            'shedule_date' : b[8],
            'status' : b[9],
            'publish_date' :b[10]

        }
        result.append(data)
    return(result)


                
# MD 5 CONVERTION 
def MD5_con(plan_text):
    plan_text =hashlib.md5(plan_text.encode())
    plan_text=plan_text.hexdigest()
    return plan_text

# JSON RESPONCE MAKER
def responce_maker(status, result,message):
   res={'status': status,'results': result,'message':message }
   return jsonify(res)


#UPDATE JWT TOKET USER
def update_jwt_token(user_id,token):
                    cur = mysql.connection.cursor()
                    cur.execute("Update `user_info` SET token =%s where id=%s", (token, user_id))
                    mysql.connection.commit()
                    if cur.rowcount==1:
                        cur.close()
                        return(1)
                    else:
                        cur.close()
                        return(0)
                
# CHECK JWT TOKEN
def check_jwt_token(user_id,token):
                cur = mysql.connection.cursor()
                query="SELECT * FROM user_info where id='"+user_id+"' and token='"+token+"'"
                cur.execute(query)
                user = cur.fetchall()
                cur.close()
                if not user:
                   return(0)
                else:
                   return(1)





if __name__ =="__main__":
    app.run(debug=True)
