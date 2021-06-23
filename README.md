# Steps to running locally
git clone https://github.com/faisaluddin/gramener_exercise.gitc <br/>
cd gramener_exercise <br/>
pip install -r requirements.txt <br/>
python manage.py migrate <br/>
python manage.py runserver <br/>

The app is deployed at https://gramener-faisal.herokuapp.com/

# Task
Implement a REST API (with GET, PUT, DELETE) options that can take a mathematical operation as function type (e.g. add, subtract, multiple) etc
When we call a function with relevant arguments, it should return/display the result of the operation.
We should be able to add/remove a new “function” e.g. (division, factorial etc.)

# Solution
Inorder to implement the above task. Created a table which will store operation_name, operation description and actual python function that user will pass. The actual func will also be stored in file system, so that when user calls it via GET request it can be executed easily.

# Usage
New operation can be created using the POST HTTP request, it will require operation_name, description and python func like below.(Make sure the operation_name and function name is same)
![image](https://user-images.githubusercontent.com/12785657/123029962-9b445500-d3ff-11eb-8665-5cf5695130d7.png)
Then this func can be used by using the id of the func and passing the required params like below
![image](https://user-images.githubusercontent.com/12785657/123030093-d5155b80-d3ff-11eb-8f8a-7012ed827881.png)
Where here 2 is the id of the resource and 4, 6 are params





