<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

Milestone Project Four

## Table of Contents

- [**About**](#About)
- [**UX**](#UX)
  - [User Stories](#User-Stories)
  - [Style Rationale](#Style-Rationale)
  - [Wireframes](#Wireframes)
- [**Features**](#Features)
  - [Functionality](#Functionality)
  - [Existing Features](#Existing-Features)
  - [Features Left To Implement](#Features-Left-To-Implement)
- [**Technologies Used**](#Technologies-Used)
  - [Version Control](#Version-Control)
  - [Hosting](#Hosting)
- [**Testing**](#Testing)
  - [Testing User Stories](#Testing-User-Stories)
  - [Responsive and Functional Testing](#Responsive-and-Functional-Testing)
  - [Additional Testing](#Additional-Testing)
  - [Code Validation](#Code-Validation)
  - [Automated Testing](#Automated-Testing)
  - [Bugs / Problems](#Bugs-/-Problems)
- [**Deployment**](#Deployment)
  - [Live App Link](#Live-App-Link)
  - [Repository Link](#Repository-Link)
  - [Running Code Locally](#Running-Code-Locally)
  - [Media And Static Folders](#Media-And-Static-Folders)
- [**Credits**](#Credits)
  - [Content](#Content)
  - [Media](#Media)
  - [Acknowledgements](#Acknowledgements)
  - [Disclaimer](#Disclaimer)

## About
MyFit is an e-commerence Full-Stack site, developed as my milestone 4 project with Code Institue as part of the Full-Stack software development course. The main purpose of the site is to sell clothing, equipment and nutrition products to customer who have signed up and registered with the site.

The site also encourages engagment through the deployment of a review system for each product, whereby customers can rate products and leave reviews for other users to get a better insight into a products value. 

Users are also able to send email enquires to the site with their questions and queries and feedback from the applicaiton informs customers that this has been subitted.

Users can also purchase products through the stripe authentication service for payments and upon payment submission are presented with billing informaiton and the facility to review their orders. 

Users also recieve an email to their own email address from the site informing them of their purchases. 

Further engagment with site includes the signing up process whereby user have to check a verification link, sent to the email they provide, in order to access site functionality.

Further features where planned initially for this project. Those included a membership system that reuired the user to sign up various packages and have access to excerices and tutorial videos. Extensive amounts of time where put into it, however I was unable to get it to work properly and to my sheer disappointment, a versioning issue at the last hurdle required me to remove it from the final submission. 

There should be large elemts of both memberhip apps and course apps in the commit history.

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



## Features

### Functionality
* The abillity to sign up through a username, email and password combination to ensure individual access to the site and profile features
* 

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



### Features Left to Implement


### Future Implement

With more time and knowledge, I would like to implement some additional features to the app:

* A tiered membership system that spans 3 levels. At each level a customer would gain access to additional contain and value for their subscriptions

* A courses app, that would have  numerours excerices training routines embedded within it, that could be accessed depending on the customers membership level

* A blog app, that would encourage fellow users to discuss excercise realted activties, routines food plans and how they are progressing through various activities


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

### Testing User Stories


### Responsive and Functional Testing


### Additional Testing

In addition to my own testing, I also asked family members, friends and the Slack community to test my app and provide any feedback.

### Code Validation

- I used the [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) to validate my HTML code.
    - The W3C Validator tool doesn't recognise the Jinja templating, which has resulted in it showing a lot of errors in relation to the Jinja code. However, all other code is validating fine.
- I used the [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my CSS code.
- I used the [Pep8 Online tool](http://pep8online.com/) to validate my Python syntax.

### Bugs / Problems


## Deployment

I used GitHub for my version control and Heroku to host the live version of my project. To deploy my website to Heroku, I used the following steps:

1. Created the app in Heroku.
2. Went to the **Resources** tab in Heroku and searched for **Heroku Postgres** in the 'Add-Ons' section.
3. Selected the free **Hobby** level.
4. Updated the `.bashrc` file within my local workspace with the `DATABASE_URL` details, and the `settings.py` to connect to the database using the `dj_database_url` package.
5. Ran the `python3 manage.py makemigrations`, `python3 manage.py migrate`, `python3 manage.py createsuperuser` commands to migrate the models into Heroku Postgres and create a new super user in the new PostgreSQL database.
5. Went to the **Settings** tab in Heroku and clicked on the **Reveal Config Vars** button.
6. Copied and pasted all of the `.bashrc` default variables in Heroku's Config Vars section.
7. Went to the **Deploy** tab in Heroku, connected my app to my GitHub repository and selected **Enable Automatic Deployment** as the deployment method.
8. Went to the **Developers** section in Stripe and clicked on **API Keys**.
9. Copied and pasted the **Publishable Key** and **Secret Key** and set them as the `STRIPE_PUBLISHABLE` and `STRIPE_SECRET` environment variables in the `.bashrc` file within my local workspace.
10. Updated the `settings.py` with the new Stripe environment variables.

15. Created a `custom_storages.py` file with classes to route to the relevant location settings for static and media files.
16. Updated the `settings.py` file with the relevant configuration for static and media file storage.
17. Ran the `python3 manage.py collectstatic` command to push the static files to my S3 bucket.
18. Created a requirements.txt file using the following command in the terminal window:

    ```sudo pip3 freeze --local > requirements.txt```

19. Created a Procfile using the following command in the terminal window:

    ```echo web: gunicorn myFit.wsgi:application > Procfile```

20. Ran the `git add .`, `git commit -m "<commit-message>"` and `git push` commands to push all changes to my GitHub repository.

The app was successfully deployed to Heroku at this stage.

### Live App Link

Click the link below to run my project in the live environment:

[myFit](https://github.com/Pysched/MS4-myFit-DM)

### Repository Link

Click the link below to visit my project's GitHub repository:

[myFit GitHub Repository](https://github.com/Pysched/MS4-myFit-DM)

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

Inspiration for sevral elements of the site and inspiration of carrying on after too many hours of banging my hand against a keyboard was taken from fellow students in the slack community, and also being able to review other students work and see how they got on and how they implemented there systems.

### Disclaimer

This project is for educational purposes only.
