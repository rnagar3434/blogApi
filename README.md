# blogApi
Here is am using Flask Framework for API Development and MySql as a database
Task 1 :: Register Api
End Point : http://ip-address/register/
Method : post
Parameters :
1. first_name
2. secound_name
3. email
4. password
Note : All parameters are mandatory
Task 2 :: Login Api
Endpoint : http://ip-address/login/
Method : post
Parameters :
1. email
2. password
Note : All parameters are mandatory
2
Task 3 :BLOG Api
Endpoint : http://ip-address/blog/
Header parameters :
1. token
Method: POST ( FOR BLOG INSERT )
Parameters :
1. title
2. content
3. post_type
4. she_date
Note : post_type should be NOW or SHE
1. NOW for instant post
2. SHE for schedule date time and it should me YYYY-MM-DD HH:SS
Method : GET ( return post only current user who logged in )
Parameters :
Method : DELETE ( For Delete post )
Parameters :
1. Id [ blog id ]
Method: PUT ( FOR BLOG UPDATION )
Parameters :
5. title
6. content
7. post_type
8. she_date
Note : post_type should be NOW or SHE
3. NOW for instant post
4. SHE for schedule date time and it should me YYYY-MM-DD HH:SS
3
Task 3 :Archive :
Endpoint : http://ip-address/archive/
Header parameters :
1. token
Method : POST
Parameters :
1. id ( blog id that you want to archive )
Method : GET
Parameters :
It returns all Archive post of current user who logged in
Task 4: Upload image:
Endpoint : http://ip-address/upload-image/
Method : POST
Parameters:
1. file
note : form : multipart / form-data
it will returm the file name and you can use it by domain name+ file name
Task 5: Show All active blog :
Endpoint : http://ip-address/blog-list/
Method : GET
It will return all active blog
4
Task 6: Schedule post :
For schedule post we have to setup cron jobs for every 1 minute
Endpoint : http://ip-address/she-blog/
Method : GET
