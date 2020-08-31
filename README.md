<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

Milestone Project Four


### Live App Link

Click the link below to run my project in the live environment:

[myFit](https://myfit.herokuapp.com/)

### Repository Link

Click the link below to visit my project's GitHub repository:

[myFit GitHub Repository](https://github.com/Pysched/Dm-MyFit)


## About
MyFit is an e-commerence Full-Stack site, developed as my milestone 4 project with Code Institue as part of the Full-Stack software development course. The main purpose of the site is to sell clothing, equipment and nutrition products to customer who have signed up and registered with the site.

The site also encourages engagment through the deployment of a review system for each product, whereby customers can rate products and leave reviews for other users to get a better insight into a products value. 

Users are also able to send email enquires to the site with their questions and queries and feedback from the application informs customers that this has been submitted.

Users can also purchase products through the stripe authentication service for payments and upon payment submission are presented with billing informaiton and the facility to review their orders. 

Users also recieve an email to their own email address from the site informing them of their purchases. 

Further engagment with site includes the signing up process whereby user have to check a verification link, sent to the email they provide, in order to access site functionality.

Further features where planned initially for this project. Those included a membership system that reuired the user to sign up various packages and have access to excerices and tutorial videos. Extensive amounts of time where put into it, however I was unable to get it to work properly and to my sheer disappointment, a versioning issue at the last hurdle required me to remove it from the final submission. 

There should be large elements of both the membership apps and course apps in the commit history.

Nonetheless the amount of knowledge, techniques that I learnt in this project cannot be understated. Thereis quite a large amount of work involved in developing a django site, combined with learning python syntax and methodologies. 

I thoroughly enjoyed my time developing this project, and will be adding finishing touches and flourishes to it after it has been submitted and marked and is safe to do so in my own time.

The deployed site can be viewed at: https://myfit.herokuapp.com/ 

To make test payments please use the following details to ensure success:
- Card number 4242 4242 4242 4242
- Expiry 04 24
- CVC 242
- ZIP CODE - 42424


## UX

The best sites are those that are easy to navigate, easy to use and are logical without being stale in there implementation. To this end I created my site to follow these guiding principles. 

A prominant navigation system both in the header area and in the footer, accompanied by a back to top button, enables users regardless of there position on the page to be able to use and get to a navigation area with ease. 

Error handling and user feedback are a core element of the user experience. There a many predefined error messages and progress messages that inform the user at each interaction point of their progress. 

This is further enhanced through the email feedback forms that are sent to users either from a query or a purchase.

Authentication of payments and user login are a core element of the site. as the sites aim as a business is to sell products, and to ensure that the customer gets their product as well as ensuring the business makes profit, there is a requireemtn to use any of the core funcationality of the site that a user must register with details. 

Further details are required to make purchases, with previous purchases detail available within the user profile seciton for users to review their buying history.


### User Stories

The site plan and general development was devised together with user stories. These stories aided in the development of the functionality of the site, as they focused me, the developer to focus on the key task required to make the site functional from the perspective of the user.

#### Customer

- To use a site that sells sports clothing and deliveres to my address.
- to be able to browse a large selection of clothes, including shoes, shorts, tops, and jackets. 
- To be able to browse sports equipment, sports accessories, and gym equipment
- To be able to browse for nutrtion products to aid my excercise ambitions
- To filter my searches by price, rating, alphabet, category and brand
- To type a search for a product and to see results
- To get feedback from the system I am using so I know what I'm doing what I have does
- To select, review and purchase items by quantity and size
- To have product details available to me to help me make my decisions
- To view a list of all products
- To have a shopping cart that holds my current selection
- The ability to review my previous orders and bring up that orders details
- To recieve notification in email form that my order has been processed.
- To have afully funcationly authentification system for sign up and payments
- To be able to review products and rate them, so that others may learn from my experience
- To review the comments left by others to help me make my decisions about a product
- To be able to send a message to the business owner and reieve confirmation


#### Business Owner
- To have a admin management system(django-admin) that allows me to review my products(django-admin), customers(django-admin) and transactions(django-admin & stripe payments system)
- The ability to add, remove, review and update the products I host on my site
- To receive feedback from customers who use the site
- to have customers leave feedback on products based on their expereinces

### Style Rationale
The site was designed in a way that would be visually appealing and eye catching for important places, signs and interactions. This was done through the choice of colour pallete, call to action buttons, font and layout. 

#### Fonts
The font used for the is site was Seoige. This was chosen as it is a clear font, easy to read and not abrasive on the eyes.

#### Colours
* ![#0c82f1]'#0c82f1' Was used as a strong primary colour to draw attent to branding, buttons, borders and elements
* ![#343a40] '#343a40' Was used as a contrasting dark gray colour to balance the strong blue used in the site. Combined these clours give a modern impression for the site.
* ![#rgb(12, 130, 241)] 'rgb(12, 130, 241)' was used as a softer blue contract for on hover states 

- Bootstrap helper colours where used to illustrate the rest of the site


### Wireframes
My initial wireframes consisted of a rough outline of how I preceived the site taking shape. I had a strong idea of the colour plaete, that being, dark greys, strong blues, white and black. A polished feel. The site sturucture really came to be based on the features I was creating for the product. I had several other variations as time went on, in terms of a fuller flshed out membership system, courses system where video urls would be embedded etc.. 

However the following links are the basis of from where I started designing and creating the application. 

This evolved as the project progresses and the features I was creating took shape.

[Home page](https://res.cloudinary.com/pysched/image/upload/c_scale,h_762/v1598842014/20200831_034453_gfdfqj.jpg)

[Products page](https://res.cloudinary.com/pysched/image/upload/c_scale,h_838/v1598842015/20200831_034424_fn60vi.jpg)

[Membership page](https://res.cloudinary.com/pysched/image/upload/c_scale,h_745/v1598842016/20200831_034330_f5alnx.jpg)

[Product detail and review section ](https://res.cloudinary.com/pysched/image/upload/c_scale,h_745/v1598842017/20200831_034352_ziyvix.jpg)

[Contact page](https://res.cloudinary.com/pysched/image/upload/c_scale,h_744/v1598842017/20200831_034407_rtkkxb.jpg)


## Features

### Existing Features

#### Header and Navigation System
* Main branding logo that is visable on all screen sizes that acts as a home button aswell.
* Search bar, for searching of products and search terms. This feature is available on all screen sizes
* Shopping bag icon with a live update of the cost of goods currently in a users bag

#### Homepage
* Main image illustrates the theme and mood of the site, that of excerices related content
* Links to the shop and to sign up are stringly positioned to draw the users eye to those first point of call sections


#### Contact Us
* The contact us page is a place where users and custoemr with any issues can contact the site owners to provided a subject title, user name and message.
* A confirmation message informs the user that they have performed an action by sending a message to the site.

#### Products page
* The products Page contains 251 products, that are presented in total upon landing on the page
* Each product when hovered over has a scale css element attached to it, to provide the user with a closer look at t he image
* Each product is arranged within a card element, thathas the products 

#### Product details Page

* On selection of a product, the user is taken to the product deatils page
* Product details; sku, rating, price, description, recommended for, add to cart button are present
* Reviews and ratings left by registered users

#### Reviews

* On product detail page, a registered user has the option to leave a review and to rate the product. This is made via a form that has an input field for ratings with options from no rating to 5. 

#### Bag

* on the bag page, the user can see its selected products displayed on top of each other. Each product from the bag contains its image, name, price, quantity selected and the subtotal which is price multiplied by quantity
* the user has the option to update each products quantity or remove it
* on bottom right of the page, the grand total with delivery included is displayed and two buttons. One to proceed to checkout and one to go back and shop more

#### Checkout

* Checkout form with required fields
* Payment form from Stripe that takes: card number, CVC, expiry date and ZIP code
* Order summary, with product details, quantity, sizes, delivery charge and grandtotal.

#### Emails

* Upon signing up to the site the user is sent an activation email, this email actually arrivals at the address provided

#### Register and login

* Register form asks for details and checks for confirms matches
* login form check sagainst saved details
* Confirmation email for registering
* Facility to change password or forgotten password fix

#### Profile

* Registered users can use this link to check their order history
* This feature isnt availe to non registered users
* Previous orders can be selected and read from the database to the order history form

#### Contact

* contains the contact details of the business: email and phone number
* contains a form for message

#### Footer

* Has branding logo that is a home button
* Has clickable and functioning links to navigation and sign up or register
* Copyright logo


### Features Left to Implement / Future Implement

With more time and knowledge, I would like to implement some additional features to the app:

* A tiered membership system that spans 3 levels. At each level a customer would gain access to additional contain and value for their subscriptions

* A courses app, that would have  numerours excerices training routines embedded within it, that could be accessed depending on the customers membership level

* A blog app, that would encourage fellow users to discuss excercise realted activties, routines food plans and how they are progressing through various activities

## Technologies

### Tools

* [GitPod](https://gitpod.com/) - Developed in the IDE and version control
* [GitHub](https://github.com/) - Repository
* [Heroku](https://heroku.com/) - Application hosting and deployment
* [AWS S3](https://aws.amazon.com/s3/) - Housing of Static and Media Files
* [Stripe](https://stripe.com/) - Secure Payment system
* [Sqlite3](https://www.sqlite.org/index.html) - Gitpod provided database
* [PostgreSQL](https://www.postgresql.org/) - database provided by Heroku for production


### Libraries and frameworks

* [Django3](https://www.djangoproject.com/) - a high-level Python Web framework that encourages rapid development
* [Bootsrap4](https://getbootstrap.com/) - for layout and responsive design
* [FontAwesome](https://fontawesome.com/) - icons implementation
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - a template language for python used to bring logic into templates
* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - a library that enables python code to modify AWS service

### Languages

* HTML
* CSS
* Javascript
* JQuery
* Python 3.8

## Development Debugging

For this app, testing was made manually and with validator services. During development I constantly used Chrome Developer Tools in order to ensure responsivness on all devices.
During development, in settings.py, Django's debugger was set to:

```python
debug = False
```

This was so to ensure that when the app encounters an error, Django gives a detailed report of what happened and why the error occured.

### Validators

* [W3C HTML Validator](https://validator.w3.org/) - this tool checks the .html files validity
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - this tool checks the .css files validity
* [Pep8 online](http://pep8online.com/) - this ensures that the python code is legit and does not contain formatting errors


## Technologies Used

- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses **HTML** to create the basic elements and content of my app.
- [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
    - The project uses **CSS** to apply the custom styles to the elements and content of my app. The base.html file is linked directly to the custom.css stylesheet.
- [**JavaScript**](https://jquery.com)
    - The project uses **Javascript** as the primary JavaScript functionality. This is both the standard jQuery that is built with Materialize components, and my custom jQuery used in my script.js file.
- [**Bootstrap**](https://bootstrap.com/)
    - The project uses the **Bootstrap** framework to add a responsive grid system, prebuilt components, plugins built on jQuery, and Bootstrap class and styles to my app, before adding my custom styles.
- [**Python**](https://www.python.org/)
    - The project uses **Python** as the back-end programming language for my app.
- [**Django**](https://www.djangoproject.com/)
    - The project uses **Django** as the Python web framework.
- [**Stripe API**](https://stripe.com/gb)
    - The project uses **Stripe** to make secure payments for logging and upvoting Feature Requests. The project uses Stripe's test payment functionality.
- [**SQLite**](https://www.sqlite.org/index.html)
    - The project uses **SQLite** as the relational database to hold the backend information for the varions models used, when running locally.
- [**PostgreSQL**](https://www.postgresql.org/)
    - The project uses Heroku's **PostgreSQL** relational database to hold the backend information for the various models used, when deployed remotely.
- [**AWS S3**](https://www.aws.amazon.com/s3/)
    - The object storage service S3 was used to house the staic css and media files and provide scalability, security and performance to the site.
- [**Font Awesome**](https://fontawesome.com/)
    - The project uses **Font Awesome** for the various icons in my app.

## Back-end Technologies
- [**Python3**](https://python.org) 
    - Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages.

### Version Control

- [**GitPod**](https://gitpod.com/)
    - I've used **GitPod** as a version control system to regularly add and commit changes made to project in its ide, before pushing them to GitHub.
- [**GitHub**](https://github.com/)
    - I've used **GitHub** as a remote repository to push and store the committed changes to my project from Git.

### Hosting

- [**Heroku**](https://www.heroku.com/)
    - I've used **Heroku** as the hosting platform to deploy my app.

## Testing

### Testing Features and User Stories 

Responsiveness and interactions where tested by myself throught he following steps:

#### Navbar

* Navigation through the use of the branding Logo
* Use all navbar links to ensure that they take the user to the correct location
* Check that tha approiate navbar links are presented based on whether a user is logged in or not.
* Check that the product manamgenet link is present when the superuser is logged in.

#### Search bar

* Type in search terms that relate the the products, their description and similar terms, check whether they return the correct products
* Check that typing in other terms return no results and that that message displays for error feedback
* Make a search without an input. See if your receive an error and you get redirected to the products page

#### Home Page

* check responsiveness for the text and call to action buttons on the page
* Check both links to ensure they take users to the correct location
* On successful sign / registration athe user is redirected back here and a success message toast is presented


#### Products Page

* Check that when landing on the products page for the first time, that all products are presented and the additional navigation system for those products is available
* Ensure the responsiveness of the cards reacts as the page scales up and down between the breakpoints
* Hover over an image and see that it scales up to preview the image better
* Click the image to go to the products details page
* Click the back to top button to see that it works and that th ecustom javascript smoothscrolling is working
* Click on the filter dropdown box and check that the orderby of the prodcuts matches the filters
* Use the prodcuts navigation system to check that the products 


#### Product details

* Check responsiveness of product details display on different screens
* choose a quantity and click add to cart. See if a success message appears that contains the product selected, total price, delivery and button to go for checkout
* Type a bigger than 99 or smaller than 1 quantity. Check for error message
* Try remove 1 unit as default quantity. Click add to bag. See if you get an error message
* Check if a user that is not logged in can write a review
* Check if a logged in user can write a review
* check to see if the comments are displayed correctly: username, date, star rating, subject
* introduce different star ratings. Check if the star rating selected is displayed correct. 


#### Bag page

* Select the shopping cart from the main nav and see if the user is redirected to the bag
* Select the toast cart afer adding a product to your bag, and see if you can go to the bag page 
* Ensure the accuracy of selected products and quantities
* Type a bigger than 99 or smaller than 1 quantity. Check for error message
* Try remove 1 unit as default quantity. Click add to bag. See if you get an error message
* Click the increment and decrement buttons and click update. See if the updated quantity is the one selected
* Click remove and see if the product is removed from the bag
* Remove all products and see if the back is empty
* Check if the total price, delivery and grand total are calculated correct

#### Checkout page

* Check if a non logged in user can access the checkout page
* When a logged in user, click on secure checkout button and see if you are redirected to checkout page
* Check if the order summary is displayed with the selected products. On mobile, see if the order summary is hidden
* As a user not logged in see if the delivery information form fields are empty
* As a logged in user see if the delivery information fields are prepopulated with your details provided in your profile

#### Payment

For payments testing the following details should be use:

* Card number: 4242 4242 4242 4242
* CVC: any 3 digits
* Date: any future date
* ZIP Code: any 5 digits

Try the following scenarios:

* Type a wrong card number
* Try required fields on delivery details form

#### Checkout success

* Redirected to the checkout success page?
* Click link to return to shopping products
* Review the order history page

#### Profile page

* Profile link is not present to non logged in users
* Check if previous order histroy is listed and availbe to be reviewed
* Update your delivery details and click the button
* Check for required error with the delivery details update form

#### Contact page

* Click the email address in the contact us section and see if the mailto is working
* Try send a message
* After submission the users provided name is displayed on the form


### Additional Testing

In addition to my own testing, I also asked family members, friends and the Slack community to test my app and provide any feedback.

### Code Validation

- I used the [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) to validate my HTML code.
- I used the [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my CSS code.
- I used the [Pep8 Online tool](http://pep8online.com/) to validate my Python syntax.

### Bugs / Problems

* The styling of the navbar area requires more tweaking to along properly
* The contact us form email logic was implemeted elsewhere in the site, but due to time constrants was unable to be finished working
* The bag toast sometimes appears when other messages are triggered
* Several styling issues on pages to be resolved
* The name attribute displayed on the contact form page after submisson has the parenthesis and quoates with it, these show havea  function to remove them


## Deployment

This application can run locally or deployed to a live environment

### Local Deployment

This example provides a step by step guide to deploying the site locally through Github Respository and Gitpod IDE

1. Navigate to the GitHub Repository: 

[myFit GitHub Repository](https://github.com/Pysched/Dm-MyFit)

1. Set up a virtual environment via this command in the terminal session:

    ```python
    python3 -m venv env
    ```

1. Activate the .venv with the command:

    ```python
    \env\Scripts\activate.bat
    ```

1. Install all required modules with the command:

    ```python
    pip3 install -r requirements.txt
    ```

1. Create a env.py file and add it to your .gitignore

1. Copy the following into the env.py file:

    ```python
    import os

    os.environ['SECRET_KEY'] = 'User Defined value'
    os.environ['DATABASE_URL'] = 'User Defined value'
    os.environ['STRIPE_PUBLIC_KEY'] = 'User Defined value'
    os.environ['STRIPE_SECRET_KEY'] = 'User Defined value'
    os.environ['STRIPE_WH_SECRET'] = 'User Defined value'
    os.environ['AWS_ACCESS_KEY_ID'] = 'User Defined value'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'User Defined value'
    os.environ['DEVELOPMENT'] = '1'
    ```

1. Set up the databases by running the following management command in your terminal:

    ```python
    python3 manage,py makemigrations
    python3 manage.py migrate
    ```

1. Create the superuser to enable access to the django admin:

    ```python
    python3 manage.py createsuperuser
    ```

1. Start your server by running the following command in your terminal:

    ```python
    python3 manage.py runserver
    ```

### Heroku Deployment

1. Create and account or login to Heroku 

2. Create a new app, specifying a unique app name and global region

3. Provision a Postgre database through selecting the resources tab and selecting the Free tier option.

4. In Reveal Vars - Add the values from your settings.py file to heroku:

    ```python
    AWS_ACCESS_KEY_ID = User defined value
    AWS_SECRET_ACCESS_KEY = User defined value
    DATABASE_URL = User defined value
    EMAIL_HOST_PASS = User defined value
    EMAIL_HOST_USER = User defined value
    SECRET_KEY = User defined value
    STRIPE_PUBLIC_KEY = User defined value
    STRIPE_SECRET_KEY = User defined value
    STRIPE_WH_SECRET = User defined value
    USE_AWS - True
    ```

5. Migrate the database tables with the following command:

    ```python
    python3 manage.py migrate
    ```

6. In order to have access to the admin, create an admin account with the following command:

    ```python
    python3 manage.py createsuperuser
    ```

7. Load the json data into the database, ensuring to load the categories first so that the products know where they are going:

    ```python
    python3 manage.py loaddata categories.json
    python3 manage.py loaddata products.json
    ```

8. Save all the django/python/allauth, gunicorn, boto3 etc.. packages requirements:

    ```python
    pip3 freeze > requirements.txt
    ```

9. Create Procfile:

    ```python
    echo web: gunicorn myfit.wsgi:application > Procfile
    ```

10. Add the files and push them to Github:

    ```python
    git add .
    git commit -m text description
    git push
    ```

11. Deploy branch in Heroku

12. In settings.py add ['myfit.herokuapp.com', 'localhost'] to Allowed Hosts





### Running Code Locally

To run my code locally, users can download a local copy of my code to their desktop by completing the following steps:

1. Go to [my GitHub repository](https://github.com/Pysched/MS4-myFit-DM)
2. Click on 'Clone or download' under the repository name.
3. Copy the clone URL for the repository in the 'Clone with HTTPs section'.
4. Open 'Git Bash' in your local IDE.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, then paste the URL you copied in Step 3:

    ```git clone https://github.com/USERNAME/REPOSITORY```

7. Press `Enter` to complete the process and create your local clone.
8. Complete one of the two below steps in your local workspace to set your own credentials for the environment variables:
    - Enter and save your own credentials in the `.baschrc` file; or
    - Create a `.env,py` file with your own credentials and import this into the `settings.py` file
9. Install the `requirements.txt` file by running the below command in your CLI Terminal:

    ```sudo pip3 install -r requirements.txt```

10. Run one of the following commands in your Terminal to launch the Django project:

    ```python3 manage.py runserver```

11. Click the `http://` link that loads, and the project should load. If it doesn't load when you click the link, copy and paste it into a new browser tab instead.
12. Run the following commands to migrate the database models and create a super user:

    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser
    ```

Once the migrations are completed and the super user has been created successfully, the site should be running locally. To deploy the site remotely, follow the instructions in the [Deployment](#Deployment) section.


## Credits

### Media

The images used in this site are used for educational purposes only and no attempt is being made to defraud any organisation. These images have been sourced from the web to illustrate the projects potential.

All credit goes to those referenced in the urls.

### Acknowledgements

Inspiration for the product review system was found from a tutorial found here: https://www.youtube.com/watch?v=OvTs8BMLb7o

Inspiration for the contact form was found from a tutorial found at these tutorials: 
https://www.youtube.com/watch?reload=9&v=w4ilq6Zk-08
https://www.youtube.com/watch?v=xNqnHmXIuzU&frags=pl%2Cwn


The shopping system, checkout, shopping bag, and general framework for the site was developed out of the learning material provided by Code insitute tutorials, and customised to suit the project. 

Inspiration for several elements of the site and inspiration of carrying on after too many hours of banging my hand against a keyboard was taken from fellow students in the slack community. and also being able to review other students work and see how they got on with there implementation of systems was a great aid to me endeavors.



### Disclaimer

This project is for educational purposes only.
