# EastSt.

East Street Restaurant (stylised as 'EastSt.') is a fictional establishment located on 23A East Street, Newtonwards, Northern Ireland.

This site has been designed to allow imagined customers the ability to access info regarding and place bookings with the restaurant, as well featuring an administrative area allowing restaurant managers to oversee the bookings of all users so that they can properly run the restaurant.

[LIVE LINK TO SITE](https://east-street-bc0671035c95.herokuapp.com/) (Note: to open links in this document in a new tab, hold CTRL + Click)

![Overview](static/images/readme/overview.png)

## Table Of Contents
- [Introduction](#eastst)
- [Strategy](#strategy)
  - [Milestone 1 - Initial Setup](#milestone-1---initial-setup)
  - [Milestone 2 - Main Site Pages](#milestone-2---main-site-pages)
  - [Milestone 3 - Booking Site Access](#milestone-3---booking-site-access)
  - [Milestone 4 - CRUD Functionality](#milestone-4---crud-functionality)
  - [Milestone 5 - Additional Coding](#milestone-5---additional-coding)
- [Scope](#scope)
- [Structure](#structure)
- [Skeleton](#skeleton)
  - [Wireframe Models](#wireframe-models)
  - [Database Model](#database-model)
- [Surface](#surface)
  - [Design & Typography](#design--typography)
  - [Features Implemented](#features-implemented)
  - [Features To Be Implemented](#features-to-be-implemented)
  - [Technology & Resources](#technology--resources)
- [Deployment](#deployment)
  - [Heroku Deployment](#heroku-deployment)
  - [Forking The Repository](#forking-the-respository)
  - [Cloning The Repository](#cloning-the-respository)
- [Credits & Acknowledgements](#credits--acknowledgements)

## UX Design

The site is aimed at helping customers to easily access information regarding the restaurant opening/closing times, menu, and location, as well as providing a simple interface for making, viewing, updating, and deleting bookings made with the restaurant. 

## Strategy

### Milestones & User Stories
This project was developed with 5 milestones (epics) in mind. From each of these milestones a number of dev goals and user stories were created, each one given a prioritisation using the MoSCoW method. The detail of these milestones, goals and stories is outlined below; further detail regarding sprints, MoSCoW desgination and acceptance criteria (covered under Structure) are included on the [GitHub Projects Kanban Board](https://github.com/users/ndsurgenor/projects/5) created for the project.

![Kanban](static/images/readme/kanban.png)

#### Milestone 1 - Initial Setup
- 1.1 - Dev Goal: set up Django and its supporting libraries via the IDE in order for development to begin
- 1.2 - Dev Goal: set up the Django project and app
- 1.3 - Dev Goal: create an early Heroku deployment to ensure all is working from the very start and allow continuous testing throughout production

#### Milestone 2 - Main Site Pages
- 2.1 - User Story: as a Site Visitor/User I want to access info/links from the home page so that I can easily discern information and make a booking
- 2.2 - User Story: as a Site Visitor/User I want to view the opening times so that I can see when the restaurant is open before I book
- 2.3 - User Story: as a Site Visitor/User I want to view the restaurant menu so that I can see what food is available before booking
- 2.4 - User Story: as a Site Visitor/User I want to view the location/address of the restaurant so that I know where the restaurant is located

#### Milestone 3 - Booking Site Access
- 3.1 - User Story: as a Site Admin I want to view all customer details/bookings so that I can plan for required table numbers/sizes
- 3.2 - User Story: as a Site Visitor I want to sign up to the site so that I can make bookings
- 3.3 - User Story: as a Site User I want to sign in to the site so that I can make/view/adjust/delete bookings
- 3.4 - User Story: as a Site User I want to be able to log out from the booking area so that no-one can change my details inadvertently or otherwise

#### Milestone 4 - CRUD Functionality
- 4.1 - User Story: as a Site User I want to make an online booking so that I can secure a table for a particular date, time & group size
- 4.2 - User Story: as a Site User I want to view my booking(s) so that I can see if it has been recorded correctly and remind myself of its details
- 4.3 - User Story: as a Site User I want to access/adjust my booking(s) so that I can correct an error/make necessary changes
- 4.4 - User Story: as a Site User I want to cancel my booking(s) so that it/they no longer appear(s) on the system
- 4.5 - User Story: as a Site Admin I want to have the ability to accept/reject new bookings so that I can manage customer numbers within the restaurant

#### Milestone 5 - Additional Coding
- 5.1 - User Story: as a Site Admin I want to prevent bookings being made for unavailable dates/times so that bookings are not made when the restaurant is closed
- 5.2 - User Story: as a Site User I want to have on-screen confirmation during the authorisation/booking process so that I know my input has been recorded correctly
- 5.3 - Dev Goal: set up 404, 403 and 500 pages to correctly handle access/server issues when the site is in use

## Scope

Using these milestones, goals, and stories to guide my thinking, the following was planned as the Scope of the project:

- Responsive Design allowing full functionality and appropraite resizing on all devices from 360px upwards
- Use of Toggle-menu and hidden elements (e.g. home page image) when site is viewed on tablet/mobile devices
- A main section of the site containing all restaurant information (non-restricted access):
  - Opening Times
  - Menu
  - Location
- A booking section of the site allowing CRUD functionality for end users (restricted access):
  - Sign Up/In/Out
  - Make Bookings
  - View Bookings
  - Adjust Bookings
  - Cancel Bookings
- An admin backend to the site allowing CRUD functionality for site admin (restricted access):
  - View All Bookings
  - Confirm Bookings

## Structure

With Strategy and Scope now in place, focus shifted to setting acceptance criteria for each of the above, thereby informing exactly what features to include as part of the project. These acceptance criteria were added to each Dev Goal and User Story on the afforementioned Kanban board to act as an ensurance that task would be completed to the fulless extent needed.

### Features
Hovering over a Refernce number below will display a desciption of that Dev Goal/User Story while clicking the link will return you to the relevant Milestone section of this document.

**Milestone**|**Ref**|**Type**|**Acceptence Criteria/Features**
:-----:|:-----:|:-----:|-----
Initial Setup|[1.1](#milestone-1---initial-setup "Set up Django and its supporting libraries via the IDE in order for development to begin")|Dev Goal|<ul><li>Install server: django-gunicorn</li><li>Install PostgreSQL library: dj_database_url psycopg2</li><li>Install image host: dj3-cloudinary-storage</li><li>Install sign-up/in/out functionality: django-allauth</li><li>Create requirements.txt file</li></ul>
Initial Setup|[1.2](#milestone-1---initial-setup "Set up the Django project and app")|Dev Goal|<ul><li>Create Django project: east-street</li><li>Create app: booking-sys</li><li>Update the settings.py file</li><li>Migrate changes</li></ul>
Initial Setup|[1.3](#milestone-1---initial-setup "Create an early Heroku deployment to ensure all is working from the very start and allow continuous testing throughout production")|Dev Goal|<ul><li>Create app on Heroku</li><li>Set up ElephantSQL</li><li>Set up the env.py file</li><li>Update the settings.py file</li><li>Set config vars and deploy app</li></ul>
Main Site|[2.1](#milestone-2---main-site-pages "As a Site Visitor/User I want to access info/links from the home page so that I can easily discern information and make a booking")|User Story|<ul><li>A home page displaying opening times of the restaurant</li><li>A home page also displaying a quick link to the booking area of the site</li><li>A navbar providing clear links to menu and location info</li><li>A highlighted link to the booking area in the navbar</li><li>A footer providing summarised info and social links</li></ul>
Main Site|[2.2](#milestone-2---main-site-pages "As a Site Visitor/User I want to view the opening times so that I can see when the restaurant is open before I book")|User Story|<ul><li>A static page showing the opening day/times of the restaurant</li><li>Elements that display/resize/scroll when viewed on different sized devices</li></ul>
Main Site|[2.3](#milestone-2---main-site-pages "As a Site Visitor/User I want to view the restaurant menu so that I can see what food is available before booking")|User Story|<ul><li>A static page showing the food and prices within the restaurant</li><li>Elements that display/resize/scroll when viewed on different sized devices</li></ul>
Main Site|[2.4](#milestone-2---main-site-pages "As a Site Visitor/User I want to view the location/address of the restaurant so that I know where the restaurant is located")|User Story|<ul><li>A static page showing the map location and transport options for the restaurant</li><li>Elements that display/resize/scroll when viewed on different sized devices</li></ul>
Booking Site |[3.1](#milestone-3---booking-site-access "As a Site Admin I want to view all customer details/bookings so that I can plan for required table numbers/sizes")|User Story|<ul><li>An admin area only allowing access to the site admin/superuser</li><li>A link to the database to clearly display the details of each booking i.e. entry in the database</li></ul>
Booking Site|[3.2](#milestone-3---booking-site-access "As a Site Visitor I want to sign up to the site so that I can make bookings")|User Story|<ul><li>A sign-up form requiring username, email and password details</li></ul>
Booking Site|[3.3](#milestone-3---booking-site-access "As a Site User I want to sign in to the site so that I can make/view/adjust/delete bookings")|User Story|<ul><li>A sign-in form requiring username, email and password details</li></ul>
Booking Site|[3.4](#milestone-3---booking-site-access "As a Site User I want to be able to log out from the booking area so that no-one can change my details inadvertently or otherwise")|User Story|<ul><li>A sign-out form requiring the user to confirm that they wish to sign out</li></ul>
CRUD|[4.1](#milestone-4---crud-functionality "As a Site User I want to make an online booking so that I can secure a table for a particular date, time & group size")|User Story|<ul><li>A booking form with date, time, and group size fields which saves those details to the database</li><li>A navbar link to the form to allow access from a different area of the booking site</li></ul>
CRUD|[4.2](#milestone-4---crud-functionality "As a Site User I want to view my booking(s) so that I can see if it has been recorded correctly and remind myself of its details")|User Story|<ul><li>A list of bookings particular to that user which displays automatically after they have submitted a valid booking</li><li>A navbar link to the list of bookings to allow access from a different area of the booking site</li></ul>
CRUD|[4.3](#milestone-4---crud-functionality "As a Site User I want to access/adjust my booking(s) so that I can correct an error/make necessary changes")|User Story|<ul><li>A button beside each entry in the booking list to allow updating of its details</li><li>The displaying of the current details within the booking form when clicking said button</li><li>The option of returning to the list without making changes</li> <li>The updating of these details to the database when the user changes values and clicks 'Confirm'</li></ul>
CRUD|[4.4](#milestone-4---crud-functionality "As a Site User I want to cancel my booking(s) so that it/they no longer appear(s) on the system")|User Story|<ul><li>A button beside each entry in the booking list to allow for its deletion</li><li>The displaying of the details to be deleted alongside a warning when clicking said button</li><li>The option of returning to the list without making changes</li><li>The deletion of the booking on the database when the user clicks 'Confirm'</li></ul>
CRUD|[4.5](#milestone-4---crud-functionality "As a Site Admin I want to have the ability to accept/reject new bookings so that I can manage customer numbers within the restaurant")|User Story|<ul><li>A list of all bookings made in the admin area of the site</li><li>A dropdown option for each individual booking allowing for selection of 'Confirmed' or 'Cancelled'</li></ul>
Additional|[5.1](#milestone-5---additional-coding "As a Site Admin I want to prevent bookings being made for unavailable dates/times so that bookings are not made when the restaurant is closed")|User Story|<ul><li>The option to only select a date beyond that of today</li><li>The option to only select between the days of Wednesday to Sunday inclusive on the booking form</li><li>The option to only select between the hours of 12.30pm and 9.45pm inclusive on the booking form</li><li>The option to only select between the group size of 1 and 12 inclusive on the booking form</li></ul>
Additional|[5.2](#milestone-5---additional-coding "As a Site User I want to have on-screen confirmation during the authorisation/booking process so that I know my input has been recorded correctly")|User Story|<ul><li>An alert for successfully signing in/out</li><li>An alert for successfully making/updating bookings</li><li>An alert for successfully deleting bookings</li></ul>
Additional|[5.3](#milestone-5---additional-coding "Set up 404, 403 and 500 pages to correctly handle access/server issues when the site is in use")|Dev Goal|<ul><li>A 403 Error page which provides a link back to a valid area of the site</li><li>A 404 Error page which provides a link back to a valid area of the site</li><li>A 500 Error page which provides a link back to a valid area of the site</li></ul>

## Skeleton

Now that specific features had been decided upon, a wireframing tool was used to give guidance as to how these features would look in practice while a database design app helped to image the flow of data within the site before commiting it to code.

### Wireframe Models
All of the site-design models which follow can be viewed on one page [using the following link](https://cacoo.com/diagrams/V4VlzIhRUc2eQPq5/2A59E)

### Main Site Pages
- Home
- Menu
- Location

![Home](static/images/readme/wireframe-home.png)
![Menu](static/images/readme/wireframe-menu.png)
![Location](static/images/readme/wireframe-location.png)

### Authorisation Pages
- Sign Up
- Sign In
- Sign Out

![Authorisation](static/images/readme/wireframe-authorisation.png)

### Booking Pages
- New/Update Booking
- Delete Booking
- Current Bookings

![New](static/images/readme/wireframe-new.png)
![Delete](static/images/readme/wireframe-delete.png)
![Current](static/images/readme/wireframe-current.png)


### Database Model

The database model was created on the basis of django-allauth handling the creation of authorised users, while the booking model would be coded by myself. The relationship between these two tables is a one-to-many by connection of the user_id and contact_id fields i.e. a single user can create many bookings, but each booking can only belong to one user.

![Database](static/images/readme/database-diagram.png)

## Surface
With wireframe and database models in place, actual features of the site could now be coded using HTML, Bootstrap, CSS, and JavaScript, all according to the criteria listed above.

### Design & Typography
  - [Libre Baskerville](https://fonts.google.com/specimen/Libre+Baskerville) was chosen as the font for h1 and h2 elements throughout the site to give a refined 'serif' look to major headings
  - All other text on the site is styled using [Noto Sans](https://fonts.google.com/noto/specimen/Noto+Sans) to provide a minimalist contrast to the headings and be clearly legible for larger portions of text
  - The main colours selected for the site were chosen as a variation on a monochromatic scheme thus creating a refined, modern look to reflect the style of the restaurant. Specifically these colours and their hexdecimal codes are:
    - Eerie Black #1B1B1B
    - Dark Slate Grey #2F4F4F
    - Dim Grey #696969
    - Gainsboro #DCDCDC
    - Ghost White #F8F8FF    
  - The background image and landing page image were selected from the [Pexels](https://www.pexels.com/) library ([specific credit below](#credits--acknowledgements)) and chosen to reflect elements of the colour scheme

    ![Colours](static/images/readme/colour-board.png)

### Features implemented

#### Brand & Favicon
  - The 

#### Navbar
> &bull; A navbar providing clear links to menu and location info  
&bull; A highlighted link to the booking area in the navbar

#### Footer
> &bull; A footer providing summarised info and social links

#### Home Page
> &bull; A home page displaying opening times of the restaurant  
&bull; A home page also displaying a quick link to the booking area of the site  
&bull; Elements that display/resize/scroll when viewed on different sized devices

#### Menu Page
> &bull; A static page showing the food and prices within the restaurant  
&bull; Elements that display/resize/scroll when viewed on different sized devices

#### Location Page
> &bull; A static page showing the map location and transport options for the restaurant  
&bull; Elements that display/resize/scroll when viewed on different sized devices

#### Booking Admin
> &bull; An admin area only allowing access to the site admin/superuser  
&bull; A link to the database to clearly display the details of each booking i.e. entry in the database

#### Sign Up/In/Out Forms
> &bull; A sign-up form requiring username, email and password details  
&bull; A sign-in form requiring username, email and password details  
&bull; A sign-out form requiring username, email and password details

#### Booking Form
> &bull; A booking form with date, time, and group size fields which saves those details to the database  
&bull; The option to only select between the days of Wednesday to Sunday inclusive on the booking form  
&bull; The option to only select between the hours of 12.30pm and 9.30pm inclusive on the booking form  
&bull; The option to only select between the group size of 1 and 12 inclusive on the booking form  
&bull; A navbar link to the form to allow access from a different area of the booking site

#### User Booking List
> &bull; A list of bookings praticular to that user which displays automatically after they have submitted a valid booking  
&bull; A navbar link to the list of bookings to allow access from a different area of the booking site

#### Booking Update Capabilities
> &bull; A button beside each entry in the booking list to allow updating of its details  
&bull; The displaying of the current details within the booking form when clicking said button  
&bull; The option of returning to the list without making changes  
&bull; The updating of these details to the database when the user changes values and clicks 'Confirm'

#### Booking Deletion Capabilities

> &bull; A button beside each entry in the booking list to allow for its deletion  
&bull; The displaying of the details to be deleted alongside a warning when clicking said button  
&bull; The option of returning to the list without making changes  
&bull; The deletion of the booking on the database when the user clicks 'Confirm'

#### Booking Overview for Admin
> &bull; A list of all bookings made in the admin area of the site  
&bull; A dropdown option for each individual booking allowing for selection of 'Confirmed' or 'Cancelled'

#### Error Pages
> &bull; A 403 Error page which provides a link back to a valid area of the site  
&bull; A 404 Error page which provides a link back to a valid area of the site  
&bull; A 500 Error page which provides a link back to a valid area of the site

### Features to be implemented
- Blocked out dates on calendar
- Blocked out times associated with dates
- Email notifcation to admin of customer made booking
- Email notifcation to customer of booking status update
- Ability to add menu items
- Ability to input closing times, dates, group numbers
- Only status can be changed by staff to avoid accidentally changing bookings

### Technology & Resources

#### Technologies Used
In order to code and design these featured the following technologies were utilised:

- Python Modules
  - asgiref==3.7.2
  - cloudinary==1.34.0
  - dj-database-url==0.5.0
  - dj3-cloudinary-storage==0.0.6
  - Django==3.2.20
  - django-allauth==0.55.0
  - gunicorn==21.2.0
  - oauthlib==3.2.2
  - psycopg2==2.9.7
  - PyJWT==2.8.0
  - python3-openid==3.2.0
  - requests-oauthlib==1.3.1
  - sqlparse==0.4.4
  - urllib3==1.26.15
- [Django](https://www.djangoproject.com/)
  - Used as the main Python framework in the development of this project
  - django-allauth is employed as the means of managing user accounts used for the booking system
  - Jinga/Django templating is used for queries to the database to insert data from it onto the site pages 
- [Heroku](https://heroku.com)
  - Used as the cloud-based deployement platform for this project
- [ElephantSQL](https://elephantsql.com)
  - Used as the database hosting service
- HTML
  - Used as the base coding language for templates and site content
- [Bootstrap](https://getbootstrap.com/)
  - Used as the main means of design layout and formatting throghout the site
- CSS
  - Used to modify Bootstrap behaviour where required and create additional custom stylings
- JavaScript
  - Used to create a timed automatic-dismisal of on-screen alerts

#### Packages Used
- [Gitpod](https://gitpod.io) was used to code the site and transfer files between the editor and the repository
- [GitHub](https://github.com) was used to store the files for this project
- [Cacoo](https://cacoo.com) was used to develop the wireframe models for the site deisgn
- [DrawSQL](https://drawsql.app) was used to create the database models and diagram
- [Google Maps](https://www.google.com/maps) was used to create the specific map for the Location page
- [Google Fonts](https://fonts.google.com/) was used to style the text throughout the site
- [Coolors](https://coolors.co/) was used to help create the colour scheme
- PowerPoint, MS Paint and the Windows Photo app were used to produce the image files for this document

#### Reference Materials
- [Django documentation](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/) was referenced frequently in order to achieve CRUD functionality and associated views
- [Django-allauth documentation](https://docs.allauth.org/en/latest/) was referenced frequently in order to implement its features correctly
- [Code Institute](https://codeinstitute.net/) course materials and walkthrough projects provided many reference points for implementing features of this project
- Documentation for similar projects by [MattBCoding](https://github.com/MattBCoding/pp4-the-pantry) and [Gareth-McGirr](https://github.com/Gareth-McGirr/Portfolio-Project-4-SizzleAndSteak) was referenced frequently when creating the READ.md and TESTING.md files
- Any other resources used are directly referenced where appropriate

## Deployment

### Heroku Deployment
This site was deployed to and is currently [hosted on the Heroku platform](https://east-street-bc0671035c95.herokuapp.com/). The steps for deploying to Heroku, using ElephantSQL as the database host, are as follows:

#### ElephantSQL Setup
  1. Navigate to [ElephantSQL](https://www.elephantsql.com/) and create an account/log in
  2. Click 'Create New Instance' in the top right
  3. Enter an Instance/Database name, choose a Plan (free version will suffice) then click 'Select Region'
  4. Select a region from the dropdown, click 'Review' and then 'Create instance'
  5. Return to the dashboard and click on the instance name
  6. In the URL section click the copy icon to copy the database URL

#### Django Project Settings
  7. In the project workspace, navigate to/create a file named 'Procfile' (remember the capital 'P')
  8. Add the following code replacing ```<myapp>``` with the actual app name then save the file:
      ``` python
      web: gunicorn <myapp>.wsgi
      ```
  9. Now navigate to/create a file named 'env.py'
  10. Add the following code, replacing ```<myurl>``` with the URL just copied from ElephantSQL and ```<mykey>``` with a string of your choice then save the file:
      ``` python
      import os

      os.environ["DATABASE_URL"]=<myurl>
      os.environ["SECRET_KEY"]=<mykey>
      ```
  11. Open 'settings.py' and add the following near the top of the code:
      ```python
      import os
      import dj_database_url
      if os.path.isfile('env.py'):
        import env
      ```
  12. Further down the page, replace any current instance of the SECRET_KEY variable with:
      ``` python
      SECRET_KEY = os.environ.get('SECRET_KEY')
      ```
  13. Replace the DATABASES variable with
      ```python
      DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        }
      ```
  14. Save the file then run ```python manage.py migrate``` in the terminal
  15. Commit and push these changes to the repository

#### Heroku Setup
  16. Navigate to [Heroku](https://heroku.com) and create an account/log in
  17. Click 'New' in the top right and select 'Create New App'
  18. Enter an App name (must be unique), choose a region, and then click 'Create app'
  19. Select 'Settings' in the menubar
  20. Click 'Reveal Config Vars' and add the following:<br>
    - DATABASE_URL: the DATABASE_URL copied from ElephantSQL<br>
    - SECRET_KEY: The SECRET_KEY string you created<br>
    - PORT: 8000
  21. Click 'Deploy' in the menubar tab then 'GitHub' under 'Deployment method'
  22. Select the repository you want to deploy and click 'Connect'
  23. Scroll down and click 'Deploy Branch' to complete the process

### Forking the Respository
1. Login to/create your [GitHub](https://github.com) account
2. Navigate to the EastSt. GitHub Repository: https://github.com/ndsurgenor/east-street
3. Towards the top right, under the main banner, click 'Fork'
4. Adjust the form fields if desired, then click 'Create fork' to finish

### Cloning the Respository/Running Locally
1. Login to/create your [GitHub](https://github.com) account
2. Navigate to the EastSt. GitHub Repository: https://github.com/ndsurgenor/east-street
3. Click the '<> Code' dropdown button and ensure 'HTTPS' is selected
4. Click the copy icon (two overlapped squares) beside the repository URL
5. Open your local IDE and create a new project, ensuring git is installed
6. Run ```git clone copied-git-url``` in the terminal to finish

## Credits & Acknowledgements
- Background image by [Lisa Fotios](https://www.pexels.com/photo/restaurant-interior-776538/)
- Landing page image by [Analogicus](https://www.pexels.com/photo/wooden-welcome-signage-on-green-wooden-door-5395777/)
- Brand logo, social media, and location page icons by [FontAwesome](https://fontawesome.com)
- Menu text adapted from dinner menu by [Yugo Belfast](https://yugobelfast.com/wp-content/uploads/2022/07/Yugo_Dinner.pdf)
- README.md and TESTING.md structure/outline adapted from documentation by [MattBCoding](https://github.com/MattBCoding) and [Gareth-McGirr](https://github.com/Gareth-McGirr)
- Many thanks to my Code Institute tutor [Graeme Taylor](https://github.com/G-Taylor) for his invaluable guidance and support in building this project