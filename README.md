# individual-work
## illustration
This application is a shopping site written using the django framework. The user can see the item on display, click on it to view all the details of the item, and see a map of the place of shipment. Secondly, the user can add the goods to the shopping cart. The shopping car can select the quantity of the goods and automatically calculate the amount to be paid. Administrators can see the visual line chart and bar chart of the number of bad reviews for different brands, the number of exports and the sales volume of each supplier through the chart page.
### Render URL: https://linciwei-django-shopping.onrender.com
Some of the features in the project require superuser permissions to be used. If you need to, you can create them with the following code:
  
    python3 manage.py creatsuperuser
    
You can also log in directly using the super administrator account that I have created
#### username: t16cl22@abdn.ac.uk
#### passwords: feiyue1998610

# instructions
## Configuring the development environment
Before you start working with the code, you need to configure your environment.
    
    pyenv local 3.7.0 # this sets the local version of python to 3.7.0
    python3 -m venv .venv # this creates the virtual environment for you
    source .venv/bin/activate # this activates the virtual environment
    pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.
    
I will use Django (https://www.djangoproject.com) as my web framework for the application. So install that with

     pip install django

And a library for displaying css styles

    pip install whitenoise
    
## migrate data
Then we need to do data migration in order to use the site properly.

    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py parse_csv
    
 ## Start going to the website
We so this using the manage.py command tool by entering this command in the terminal:

    python3 manage.py runserver

If you're doing this on another platform, then you might need to use this instead (change the port number from 8000 as required):

    python3 manage.py runserver 0.0.0.0:8000 

If it went well, then you should have reached the homepage of the website.

## Website function introduction
#### Go to the home page

When you go to the site, you will see the homepage of the site, in the upper right corner of the page you will see a login information, you can choose to sign in or sign up, or if it is your first time using the site, you can browse without logging in first.You can go to the website by clicking the Show Now button on the screen.

#### Enter product list

After entering the website, there is a navigation bar on the left. Click the logo with three bars in the upper left corner, you can see your login status and choose to log in or register. In the middle is a list of products. You can search by the name of the product you want through the search box, you can search by the price range, and you can choose the appropriate sorting method.Click on the go to detail button at the end of each item and you will be taken to a detailed page for each item, where you can see more content and a map of where it was shipped.

#### Start shopping

After selecting the product you like, you can click the "Add to cart" button at the back to add it to the shopping cart. However, this function can only be used after registration and login. If you are not logged in, the system will jump directly to the login page.After adding to the cart, you can select the amount and the required amount will be calculated automatically in the lower right corner.You can also go to the shopping cart page via the left navigation Trolley

#### chart page

If you are an administrator, you can click on the chart button on the left to see the visualized data of these items. But this feature requires a logged-in superuser, otherwise it will go all the way to the login page until the logged-in account is a superuser






    

