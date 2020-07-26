<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

Milestone Project Four

## Table of Contents

- [**About**](#About)
  - [Why This Project?](#Why-This-Project)
- [**UX**](#UX)
  - [User Stories](#User-Stories)
  - [Style Rationale](#Style-Rationale)
  - [Wireframes](#Wireframes)
  - [Database Schema](#Database-Schema)
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



### Why This Project?



## UX

### User Stories

### Style Rationale



### Wireframes


### Database Schema


## Features

### Functionality


### Existing Features



### Features Left to Implement

With more time and knowledge, I would like to implement some additional features to the app:


## Technologies Used

- [**Balsamiq**](https://balsamiq.com/)
    - I've used **Balsamiq** to create wireframes of my website/app before building it.
- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses **HTML** to create the basic elements and content of my app.
- [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
    - The project uses **CSS** to apply the custom styles to the elements and content of my app. The base.html file is linked directly to the custom.css stylesheet.
- [**Materialize**](https://materializecss.com/)
    - The project uses the **Materialize** framework to add a responsive grid system, prebuilt components, plugins built on jQuery, and Materialize styles to my app, before adding my custom styles.
- [**jQuery**](https://jquery.com)
    - The project uses **jQuery** as the primary JavaScript functionality. This is both the standard jQuery that is built with Materialize components, and my custom jQuery used in my script.js file.
- [**Python**](https://www.python.org/)
    - The project uses **Python** as the back-end programming language for my app.
- [**Django**](https://www.djangoproject.com/)
    - The project uses **Django** as the Python web framework.
- [**Jinja**](https://jinja.palletsprojects.com/en/2.10.x/)
    - The project uses **Jinja** for templating with Python and Django in the HTML code. I used **Jinja** to simplify my HTML code, avoid repetition, and allow simpler linking of the back-end to the front-end.
- [**Stripe API**](https://stripe.com/gb)
    - The project uses **Stripe** to make secure payments for logging and upvoting Feature Requests. The project uses Stripe's test payment functionality.
- [**C3.js**](https://c3js.org/)
    - The project uses **C3.js** to render interactive charts and graphs for the dashboard.
- [**SQLite**](https://www.sqlite.org/index.html)
    - The project uses **SQLite** as the relational database to hold the backend information for the varions models used, when running locally.
- [**PostgreSQL**](https://www.postgresql.org/)
    - The project uses Heroku's **PostgreSQL** relational database to hold the backend information for the various models used, when deployed remotely.
- [**Google Fonts**](https://fonts.google.com/)
    - The project uses **Google Fonts** to style the text and suit my chosen theme. The brand logo uses the *_Open Sans_* font and the rest of the site uses the *_Roboto_* font.
- [**Font Awesome**](https://fontawesome.com/)
    - The project uses **Font Awesome** for the various icons in my app.

### Version Control

- [**Git**](https://git-scm.com/)
    - I've used **Git** as a version control system to regularly add and commit changes made to project in AWS Educate Cloud9, before pushing them to GitHub.
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
- I used the [Esprima Syntax Validator tool](http://esprima.org/demo/validate.html) to validate my JavaScript syntax.
- I used the [Pep8 Online tool](http://pep8online.com/) to validate my Python syntax.

### Automated Testing


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

### Media And Static Folders


## Credits

### Content


### Media


### Acknowledgements


### Disclaimer

This project is for educational purposes only.
