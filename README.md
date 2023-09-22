# EastSt.

East Street Restaurant (stylised as 'EastSt.') is a fictional establishment located on 23A East Street, Newtonwards, Northern Ireland.

This site has been designed to allow imagined customers the ability to access info regarding and place bookings with the restaurant, as well featuring an administrative area to allow restaurant managers to manage the bookings of all users so that they can properly run the restaurant.

[LIVE LINK TO SITE](https://east-street-bc0671035c95.herokuapp.com/)

![Overview](static/images/readme/overview.png)

## UX Design

The site is aimed at helping customers to easily access information regarding the restaurant opening/closing times, menu, and location, as well as providing a simple interface for making, viewing, updating, and deleting bookings made with the restaurant. 

## Strategy

### Agile Planning
This project was developed using agile methodologies designed to deliver small features in incremental sprints. Three sprints in total were created each lasting two weeks.

All projects were assigned to epics, prioritized under the labels, Must have, should have, could have. They were assigned to sprints and story pointed according to complexity. "Must have" stories were completed first, "should haves" and then finally "could haves". It was done this way to ensure that all core requirements were completed first to give the project a complete feel, with the nice to have features being added should there be capacity.

A Kanban board was created using GitHub Projects and can be located here and can be viewed to see more information on the project cards. All stories except the documentation tasks have a full set of acceptance criteria in order to define the functionality that marks that story as complete.

### Milestones & User Stories

This project was developed with 5 milestones or epics in mind. From each of these milestones a number of dev goals and user stories were created. The detail of each of these milestones, goals and stories is outlined below:

#### Milestone 1 - Initial Setup
- Dev Goal: set up Django and its supporting libraries (along with the Secret Key) via the IDE in order for development to begin
- Dev Goal: create an early deployment of the site to Heroku to ensure that all is working from the very start and allow continous testing throughout production

#### Milestone 2 - Main Site Pages
- User Story: as a Site Visitor/User I want to view/access info/links on the home page so that I can easily discern info and make a booking
- User Story: as a Site Visitor/User I want to view the opening times so that I can see when the restaurant is open before I book
- User Story: as a Site Visitor/User I want to view the restaurant menu so that I can see what food is available before booking
- User Story: as a Site Visitor/User I want to view the location/address of the restaurant so that I know where the restaurant is located

#### Milestone 3 - Booking Site Access
- User Story: as a Site Admin I want to view all customer details/bookings so that I can plan for required table numbers/sizes
- User Story: as a Site Visitor I want to sign up to the site so that I can make bookings
- User Story: as a Site User I want to sign in to the site so that I can make/view/adjust/delete bookings
- User Story: as a Site User I want to be able to log out from the booking area so that no-one can change my details inadvertently or otherwise

#### Milestone 4 - CRUD Functionality
- User Story: as a Site User I want to make an online booking so that I can secure a table for a particular date, time & group size
- User Story: as a Site User I want to view my booking(s) so that I can see if it has been recorded correctly and remind myself of its details
- User Story: as a Site User I want to access/adjust my booking(s) so that I can correct an error/make necessary changes
- User Story: as a Site User I want to cancel my booking(s) so that it/they no longer appear on the system
- User Story: as a Site Admin I want to have the ability to accept/reject new bookings so that I can manage customer numbers within the restaurant

#### Milestone 5 - Defensive Coding
- User Story: as a Site Admin I want to prevent bookings being made for unavailable dates/times so that bookings are not made when the restaurant is closed
- Dev Goal: set up 404, 403 and 500 pages to correctly handle access/server issues when the site is in use 

## Scope

Using these milestones, goals and stories to guide my thinking, the following features were planned:

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

With the Strategy and Scope now in place

### Features implemented


### Features to be implemented

## Skeleton
### Wireframe

[LINK TO WIREFRAME DIAGRAM](https://cacoo.com/diagrams/V4VlzIhRUc2eQPq5/2A59E)

### Database Design

## Surface
### Features implemented
