# EastSt.

East Street Restaurant (stylised as 'EastSt.') is a fictional establishment located on 23A East Street, Newtonwards, Northern Ireland.

This site has been designed to allow imagined customers the ability to access info regarding and place bookings with the restaurant, as well featuring an administrative area allowing restaurant managers to oversee the bookings of all users so that they can properly run the restaurant.

[LIVE LINK TO SITE](https://east-street-bc0671035c95.herokuapp.com/) (Note: to open links in this document in a new tab, hold CTRL + Click)

![Overview](static/images/readme/overview.png)

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

**Milestone**|**Ref**|**Type**|**Description**|**Acceptence Criteria/Features**
:-----:|:-----:|:-----:|:-----:|-----
Initial Setup|[1.1](#milestone-1---initial-setup)|Dev Goal||<ul><li>Install server: django-gunicorn</li><li>Install PostgreSQL library: dj_database_url psycopg2</li><li>Install image host: dj3-cloudinary-storage</li><li>Install sign-up/in/out functionality: django-allauth</li><li>Create requirements.txt file</li></ul>
Initial Setup|1.2|Dev Goal|Set up the Django project and app|<ul><li>Create Django project: east-street</li><li>Create app: booking-sys</li><li>Update the settings.py file</li><li>Migrate changes</li></ul>
Initial Setup|1.3|Dev Goal|Create an early Heroku deployment to ensure all is working from the very start and allow continuous testing throughout production|<ul><li>Create app on Heroku</li><li>Set up ElephantSQL</li><li>Set up the env.py file</li><li>Update the settings.py file</li><li>Set config vars and deploy app</li></ul>
Main Site|2.1|User Story|As a Site Visitor/User I want to access info/links from the home page so that I can easily discern information and make a booking|<ul><li>A home page displaying opening times of the restaurant</li><li>A home page also displaying a quick link to the booking area of the site</li><li>A navbar providing clear links to menu and location info</li><li>A highlighted link to the booking area in the navbar</li><li>A footer providing summarised info and social links</li></ul>
Main Site|2.2|User Story|As a Site Visitor/User I want to view the opening times so that I can see when the restaurant is open before I book|<ul><li>A static page showing the opening day/times of the restaurant</li><li>Elements that display/resize/scroll when viewed on different sized devices</li></ul>
Main Site|2.3|User Story|As a Site Visitor/User I want to view the restaurant menu so that I can see what food is available before booking|<ul><li>A static page showing the food and prices within the restaurant</li><li>Elements that display/resize/scroll when viewed on different sized devices</li></ul>
Main Site|2.4|User Story|As a Site Visitor/User I want to view the location/address of the restaurant so that I know where the restaurant is located|<ul><li>A static page showing the map location and transport options for the restaurant</li><li>Elements that display/resize/scroll when viewed on different sized devices</li></ul>
Booking Site |3.1|User Story|As a Site Admin I want to view all customer details/bookings so that I can plan for required table numbers/sizes|<ul><li>An admin area only allowing access to the site admin/superuser</li><li>A link to the database to clearly display the details of each booking i.e. entry in the database</li></ul>
Booking Site|3.2|User Story|As a Site Visitor I want to sign up to the site so that I can make bookings|<ul><li>A sign-up form requiring username, email and password details</li></ul>
Booking Site|3.3|User Story|As a Site User I want to sign in to the site so that I can make/view/adjust/delete bookings|<ul><li>A sign-in form requiring username, email and password details</li></ul>
Booking Site|3.4|User Story|As a Site User I want to be able to log out from the booking area so that no-one can change my details inadvertently or otherwise|<ul><li>A sign-out form requiring the user to confirm that they wish to sign out</li></ul>
CRUD|4.1|User Story|As a Site User I want to make an online booking so that I can secure a table for a particular date, time & group size|<ul><li>A booking form with date, time, and group size fields which saves those details to the database</li><li>A navbar link to the form to allow access from a different area of the booking site</li></ul>
CRUD|4.2|User Story|As a Site User I want to view my booking(s) so that I can see if it has been recorded correctly and remind myself of its details|<ul><li>A list of bookings particular to that user which displays automatically after they have submitted a valid booking</li><li>A navbar link to the list of bookings to allow access from a different area of the booking site</li></ul>
CRUD|4.3|User Story|As a Site User I want to access/adjust my booking(s) so that I can correct an error/make necessary changes|<ul><li>A button beside each entry in the booking list to allow updating of its details</li><li>The displaying of the current details within the booking form when clicking said button</li><li>The option of returning to the list without making changes</li> <li>The updating of these details to the database when the user changes values and clicks 'Confirm'</li></ul>
CRUD|4.4|User Story|As a Site User I want to cancel my booking(s) so that it/they no longer appear(s) on the system|<ul><li>A button beside each entry in the booking list to allow for its deletion</li><li>The displaying of the details to be deleted alongside a warning when clicking said button</li><li>The option of returning to the list without making changes</li><li>The deletion of the booking on the database when the user clicks 'Confirm'</li></ul>
CRUD|4.5|User Story|As a Site Admin I want to have the ability to accept/reject new bookings so that I can manage customer numbers within the restaurant|<ul><li>A list of all bookings made in the admin area of the site</li><li>A dropdown option for each individual booking allowing for selection of 'Confirmed' or 'Cancelled'</li></ul>
Additional|5.1|User Story|As a Site Admin I want to prevent bookings being made for unavailable dates/times so that bookings are not made when the restaurant is closed|<ul><li>The option to only select a date beyond that of today</li><li>The option to only select between the days of Wednesday to Sunday inclusive on the booking form</li><li>The option to only select between the hours of 12.30pm and 9.45pm inclusive on the booking form</li><li>The option to only select between the group size of 1 and 12 inclusive on the booking form</li></ul>
Additional|5.2|User Story|As a Site User I want to have on-screen confirmation during the authorisation/booking process so that I know my input has been recorded correctly|<ul><li>An alert for successfully signing in/out</li><li>An alert for successfully making/updating bookings</li><li>An alert for successfully deleting bookings</li></ul>
Additional|5.3|Dev Goal|Set up 404, 403 and 500 pages to correctly handle access/server issues when the site is in use|<ul><li>A 403 Error page which provides a link back to a valid area of the site</li><li>A 404 Error page which provides a link back to a valid area of the site</li><li>A 500 Error page which provides a link back to a valid area of the site</li></ul>

## Skeleton
### Wireframe

[LINK TO WIREFRAME DIAGRAM](https://cacoo.com/diagrams/V4VlzIhRUc2eQPq5/2A59E)

### Database Design

## Surface

Now that this thinking had been done

### Features implemented

#### Brand & Favicon

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