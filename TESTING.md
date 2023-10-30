# EastSt. : Testing

_Note: to open links in a new tab, hold CTRL + Click_<br>
_Note: this document only contains testing info for the EastSt. site. If you require full documentation please [click here to access the README.md](README.md) file_

A number of manual  

## Table Of Contents
- [Introduction](#eastst---testing)
- [Manual Testing](#manual-testing)
    - [Navigation](#navigation)
    - [Responsiveness](#responsiveness)
    - [Authentication](#authentication)
    - [CRUD Functionality](#crud-functionality)
- [Unit Testing](#unit-testing)
- [Accessibility](#accessibility)
- [Validator Testing](#validator-testing)
- [Performance](#performance)
- [Bugs](#bugs)

## Manual Testing

### Navigation

These tests ensure that a user can successfully navigate the site using the provided navbar links, buttons, and footer icons. The booking area of the site requires a username and password to access (username _testname_ and password _test#123_ have specifically been registered for this purpose); specifics around this access are tested below under [Authentication](#authentication). Note that navigation specific to user-made bookings - i.e. page access using 'Update' and 'Delete' buttons - is covered under [CRUD Functionality](#crud-functionality).

**Test**|**Steps**|**Expected**|**Result**
-----|-----|-----|:-----:
Home page displays when using URL|<ol><li>Type https://east-street-bc0671035c95.herokuapp.com/ into the browser</li><li>Hit 'Enter'</li></ol>|Home page displays with navbar, footer and page contents|Pass
Home page displays when using navbar link|<ol><li>Navigate to 'Menu' or 'Location' page</li><li>Click 'Home' in the navbar</li></ol>|Home page displays with navbar, footer and page contents|Pass
Menu page displays when using navbar link|<ol><li>Navigate to 'Home' or 'Location' page</li><li>Click 'Menu' in the navbar</li></ol>|Menu page displays with navbar, footer and page contents|Pass
Location page displays when using navbar link|<ol><li>Navigate to 'Home' or 'Menu' page</li><li>Click 'Location' in the navbar</li></ol>|Location page displays with navbar, footer and page contents|Pass
Home page displays when clicking brand/logo on main site|<ol><li>Navigate to 'Menu' or 'Location' page</li><li>Click the brand/logo at the top-left of navbar</ol></li>|Home page displays with navbar, footer and page contents|Pass
Sign In/New Booking form displays when using 'Bookings' navbar link|<ol><li>Navigate to 'Home' page</li><li>Click 'Bookings' in the navbar</li></ol>|Sign In/New Booking form displays with navbar and footer|Pass
Sign In/New Booking form displays when using 'Book Now' button|<ol><li>Navigate to 'Home' page</li><li>Click 'Book Now' button</li></ol>|Sign In/New Booking form displays with navbar and footer|Pass
Menu page displays when using 'Menu' button|<ol><li>Navigate to 'Home' page</li><li>Reduce screen width until 'Menu' button appears below opening times</li><li>Click 'Menu' button</li></ol>|Menu page displays with navbar, footer and page contents|Pass
Booking form displays when using 'New Booking' navbar link with correct username|<ol><li>If required, sign in to booking area using preregistered details e.g. Username: _testname_; Password: _test#123_</li><li>Navigate to 'Current Bookings' page</li><li>Click 'New Booking' in the navbar</li></ol>|Booking form and username displays with navbar and footer|Pass
Current bookings display when using navbar link and only show those made by user|<ol><li>If required, sign in to booking area using preregistered details e.g. Username: _testname_; Password: _test#123_</li><li>Navigate to 'New Booking' page</li><li>Click 'Current Bookings' in the navbar</li></ol>|Booking list for signed-in user displays with navbar and footer|Pass
Sign Out page displays when using 'Logout' navbar link|<ol><li>If required, sign in to booking area using preregistered details e.g. Username: _testname_; Password: _test#123_</li><li>Navigate to 'New Booking' or 'Current Bookings' page</li><li>Click 'Logout' in the navbar</li></ol>|Sign Out page displays with navbar and footer|Pass
Sign Out page displays when clicking brand/logo on booking site|<ol><li>If required, sign in to booking area using preregistered details e.g. Username: _testname_; Password: _test#123_</li><li>Navigate to 'New Booking' or 'Current Bookings' page</li><li>Click the brand/logo at the top-left of navbar</ol></li>|Sign Out page displays with navbar and footer|Pass
Home page displays when clicking 'Sign Out' button on Sign Out page|<ol><li>If required, sign in to booking area using preregistered details e.g. Username: _testname_; Password: _test#123_</li><li>Click 'Logout' in the navabr</li><li>Click 'Sign Out' button</li></ol>|Home page displays with navbar, footer and page contents|Pass
Booking form displays when clicking 'Cancel' button on Sign Out page|<ol><li>If required, sign in to booking area using preregistered details e.g. Username: _testname_; Password: _test#123_</li><li>Click 'Logout' in the navabr</li><li>Click 'Cancel' button</li></ol>|Booking form and username displays with navbar and footer|Pass
Gmail opens in a new tab/window when clicking footer icon|<ol><li>Navigate to any page on the site</li><li>Click email icon in footer|Gmail opens in a new tab/window</li></ol>|Pass
Instagram opens in a new tab/window when clicking footer icon|<ol><li>Navigate to any page on the site</li><li>Click Instagram icon in footer</li></ol>|Instagram opens in a new tab/window|Pass
Facebook opens in a new tab/window when clicking footer icon|<ol><li>Navigate to any page on the site</li><li>Click Facebook icon in footer</li></ol>|Facebook opens in a new tab/window|Pass

### Responsiveness

These tests check that the site responds correctly at various sizes of screen, resizing, hiding, and reformatting elements where necessary. The booking area of the site requires a username and password to access (username _testname_ and password _test#123_ have specifically been registered for this purpose); specifics around this access are tested below under [Authentication](#authentication).

**Test**|**Steps**|**Expected**|**Result**
-----|-----|-----|:-----:
Navbar toggler appears on main pages at screen width of 767px or smaller|<ol><li>Navigate to 'Home', 'Menu' or 'Location' page</li><li>Reduce screen width to 767px or smaller</li></ol>|<ul><li>Navbar links no longer display in header</li><li>Toggler appears at right of navbar</li><li>'Home', 'Menu', 'Location', and 'Booking' display when toggler is clicked</li></ol>|Pass
Navbar toggler appears on booking pages at screen width of 767px or smaller|<ol><li>Navigate to 'New Booking' or 'Current Bookings' page</li><li>Reduce screen width to 767px or smaller</li></ol>|<ul><li>Navbar links no longer display in header</li><li>Toggler appears at right of navbar</li><li>'New Booking', 'Current Bookings', and 'Logout' display when toggler is clicked</li></ol>|Pass
Home page adjusts layout at screen width of 767px or smaller|<ol><li>Navigate to 'Home' page</li><li>Reduce screen width to 767px or smaller</li></ol>|<ul><li>'Open' image is hidden</li><li>Header text above opening times is hidden</li><li>'Menu' button appears below opening times</li></ul>|Pass
Menu page adjusts layout at screen width of 767px or smaller|<ol><li>Navigate to 'Menu' page</li><li>Reduce screen width to 767px or smaller</li></ol>|<ul><li>Menu text adjusts from two to one-column layout</li></ul>|Pass
Location page adjusts layout at screen width of 991px or smaller|<ol><li>Navigate to 'Location' page</li><li>Reduce screen width to 991px or smaller</li></ol>|<ul><li>Text below map adjusts from one to two-row layout</li></ul>|Pass
Current Bookings page adjusts layout at screen width of 767px or smaller|<ol><li>Navigate to 'Current Bookings' page</li><li>Reduce screen width to 767px or smaller</li></ol>|<ul><li>'Actions' table header is hidden</li><li>'Update' and 'Delete' buttons repositioned below booking details</li><li>Horizontal borders appear between booking entries</li></ul>|Pass
Current Bookings page adjusts date format at screen width of 767px or smaller|<ol><li>Navigate to 'Current Bookings' page</li><li>Reduce screen width to 767px or smaller</li></ol>|<ul><li>Booking dates adjust from 'Day, Date Month Year' format to 'dd/mm/yyyy'</li></ul>|Pass
Footer adjusts layout at screen width of 767 px or smaller|<ol><li>Navigate to any page on the site</li><li>Reduce screen width to 767px or smaller</li></ol>|<ul><li>'est. 2023' text is hidden</li><li>Social icons right-aligned with screen</li></ul>|Pass
Footer adjusts format at screen width of 575 px or smaller|<ol><li>Navigate to any page on the site</li><li>Reduce screen width to 575px or smaller</li></ol>|<ul><li>Postcode under 'Address' is hidden</li><li>'Wed-Sun' under 'Opening Hours' adjusted to 'W-S'</li></ul>|Pass
Navbar and Footer adjust layout at screen height of 800 px or smaller|<ol><li>Navigate to any page on the site</li><li>Reduce screen height to 800px or smaller</li></ol>|<ul><li>Brand, logo and navbar height reduced</li><li>Social icon size and footer height reduced</li><li>'Opening Hours' text is hidden</li></ul>|Pass

### Authentication

These tests check the sign up, sign in, and sign out functionality of the site which are essential for secure access to the booking area. The username _testname_ and password _test#123_ have specifically been registered to help determine the outcome of these tests.

**Test**|**Steps**|**Expected**|**Result**
-----|-----|-----|:-----:
User can sign up to access the booking site|<ol><li>Click 'Logout' if already signed in, otherwise navigate to Home page</li><li>Click 'Bookings' in the navbar</li><li>Click 'Sign Up' on the sign in form</li><li>Complete all fields with previously unregistered details</li><li>Click 'Sign Up'</li></ol>|<ul><li>User directed to 'New Booking' page</li><li>Alert message confirms sign up as successful</li></ul>|Pass
User cannot sign up unless a username is entered|<ol><li>Click 'Logout' if already signed in, otherwise navigate to Home page</li><li>Click 'Bookings' in the navbar</li><li>Click 'Sign Up' on the sign in form</li><li>Complete all fields except for 'Username'</li><li>Click 'Sign Up'</li></ol>|<ul><li>Sign-up form will not submit</li><li>Warning prompt alerts user to the problem</li></ul>|Pass
User cannot sign up with previously registered username|<ol><li>Click 'Logout' if already signed in, otherwise navigate to Home page</li><li>Click 'Bookings' in the navbar</li><li>Click 'Sign Up' on the sign in form</li><li>Complete all fields ensuring 'Username' is filled with previously registered details e.g. _testname_</li><li>Click 'Sign Up'</li></ol>|<ul><li>Sign-up form will not submit</li><li>Text displays saying "A user with that username already exists"</li></ul>|Pass
User can sign up without an email address|<ol><li>Click 'Logout' if already signed in, otherwise navigate to Home page</li><li>Click 'Bookings' in the navbar</li><li>Click 'Sign Up' on the sign in form</li><li>Complete all fields except for 'Email'</li><li>Click 'Sign Up'</li></ol>|<ul><li>User directed to 'New Booking' page</li><li>Alert message confirms sign up as successful</li></ul>|Pass
User cannot sign up unless a password is entered|<ol><li>Click 'Logout' if already signed in, otherwise navigate to Home page</li><li>Click 'Bookings' in the navbar</li><li>Click 'Sign Up' on the sign in form</li><li>Complete all fields except for 'Password' and/or 'Password (again)'</li><li>Click 'Sign Up'</li></ol>|<ul><li>Sign-up form will not submit</li><li>Warning prompt alerts user to the problem</li></ul>|Pass
User cannot sign up if passwords don't match|<ol><li>Click 'Logout' if already signed in, otherwise navigate to Home page</li><li>Click 'Bookings' in the navbar</li><li>Click 'Sign Up' on the sign in form</li><li>Complete all fields ensuring 'Password' and 'Password (again)' contain different data entry</li><li>Click 'Sign Up'</li></ol>|<ul><li>Sign-up form will not submit</li><li>Text displays saying "You must type the same password each time"</li></ul>|Pass
User can sign in to access the booking site|<ol><li>Click 'Logout' if already signed in, otherwise navigate to Home page</li><li>Click 'Bookings' in the navbar</li><li>Complete all fields with previously registered details e.g. Username: _testname_; Password: _test#123_</li><li>Click 'Sign In'</li></ol>|<ul><li>User directed to 'New Booking' page</li><li>Alert message confirms sign in as successful</li></ul>|Pass
User cannot sign in unless a valid username is entered|<ol><li>Click 'Logout' if already signed in, otherwise navigate to Home page</li><li>Click 'Bookings' in the navbar</li><li>Complete all fields ensuring 'Username' is filled with previously unregistered details</li><li>Click 'Sign In'</li></ol>|<ul><li>Sign-up form will not submit</li><li>Text displays saying "The username and/or password you specified are not correct"</li></ul>|Pass
User cannot sign in unless a valid password is entered|<ol><li>Click 'Logout' if already signed in, otherwise navigate to Home page</li><li>Click 'Bookings' in the navbar</li><li>Complete all fields with 'Username' as _testname_ and ensure 'Password' IS NOT _test#123_</li><li>Click 'Sign In'</li></ol>|<ul><li>Sign-up form will not submit</li><li>Text displays saying "The username and/or password you specified are not correct"</li></ul>|Pass
User can sign out from the booking site|<ol><li>if required sign in, then click 'Logout'</li><li>Click 'Sign Out'</li></ol>|<ul><li>User directed to 'Home' page</li><li>Alert message confirms sign out as successful</li></ul>|Pass

### CRUD Functionality

These tests determine if a user is able to successfully create, view, update and/or delete a booking, or not as the case may be, through the front-end capabilities of the site. In all test cases, **one must first sign in** to the booking area of the site before completing any of the other steps listed (the username _testname_ and password _test#123_ have specifically been registered for this purpose), while the desciptor 'valid details' indicates that the following is expected:

- 'Date' is not left blank
- 'Date' is not set earlier than tomorrow's date
- 'Date' is not set to Monday/Tuesday
- 'Time' is not left blank

**Test**|**Steps**|**Expected**|**Result**
-----|-----|-----|:-----:
User can make a booking|<ol><li>Navigate to 'New Booking' page</li><li>Complete all fields with valid details</li><li>Click 'Submit'</li></ol>|<ul><li>User directed to 'Current Bookings' page</li><li>Submitted details reflected on displayed list</li><li>Alert message confirms booking submitted successfully</li></ul>|Pass
User cannot make a booking unless a date is entered|<ol><li>Navigate to 'New Booking' page</li><li>Leave 'Date' blank but complete all other fields with valid details</li><li>Click 'Submit'</li></ol>|<ul><li>Booking form will not submit</li><li>Warning prompt alerts user to the problem</li></ul>|Pass
User cannot make a booking unless a time is selected|<ol><li>Navigate to 'New Booking' page</li><li>Leave 'Time' blank but complete all other fields with valid details</li><li>Click 'Submit'</li></ol>|<ul><li>Booking form will not submit</li><li>Warning prompt alerts user to the problem</li></ul>|Pass
User cannot make a booking on today's date or before|<ol><li>Navigate to 'New Booking' page</li><li>Set 'Date' earlier than tomorrow's date but complete all other fields with valid details</li><li>Click 'Submit'</li></ul>|<ul><li>Booking form will not submit</li><li>Text displays saying "A booking cannot be made any earlier than tomorrow"</li></ul>|Pass
User cannot make a booking on a Monday or Tuesday|<ol><li>Navigate to 'New Booking' page</li><li>Set 'Date' to Monday/Tuesday some time after tomorrow's date but complete all other fields with valid details</li><li>Click 'Submit'</li></ul>|<ul><li>Booking form will not submit</li><li>Text displays saying "Sorry, the restaurant is closed on a Monday/Tuesday"</li></ul>|Pass
User can view their previously made bookings|<ol><li>Navigate to 'Current Bookings' page</li></ol>|<ul><li>'Current Bookings' page displays user-made bookings</li><li>'Update' buttons apepar beside all entries not marked as 'Cancelled'</li><li>'Delete' buttons appear beside all entries</li></ul>|Pass
User can update a booking|<ol><li>Navigate to 'Current Bookings' page</li><li>Click 'Update' beside any listed booking</li><li>Complete all fields on Update Form with valid details</li><li>Click 'Confirm & Update'</li></ol>|<ul><li>User directed to 'Current Bookings' page</li><li>Updated details reflected on displayed list</li><li>Alert message confirms booking updated successfully</li></ul>|Pass
User cannot update a booking unless a date is entered|<ol><li>Navigate to 'Current Bookings' page</li><li>Click 'Update' beside any listed booking</li><li>Make 'Date' blank but leave all other fields with valid details</li><li>Click 'Submit'</li></ol>|<ul><li>Update form will not submit</li><li>Warning prompt alerts user to the problem</li></ul>|Pass
User cannot update a booking unless a time is selected|<ol><li>Navigate to 'Current Bookings' page</li><li>Click 'Update' beside any listed booking</li><li>Make 'Time' blank but leave all other fields with valid details</li><li>Click 'Submit'</li></ol>|<ul><li>Update form will not submit</li><li>Warning prompt alerts user to the problem</li></ul>|Pass
User cannot update a booking to today's date or before|<ol><li>Navigate to 'Current Bookings' page</li><li>Click 'Update' beside any listed booking</li><li>Set 'Date' earlier than tomorrow's date but leave all other fields with valid details</li><li>Click 'Submit'</li></ol>|<ul><li>Update form will not submit</li><li>Text displays saying "A booking cannot be made any earlier than tomorrow"</li></ul>|Pass
User cannot update a booking to a Monday or Tuesday|<ol><li>Navigate to 'Current Bookings' page</li><li>Click 'Update' beside any listed booking</li><li>Set 'Date' to Monday/Tuesday some time after tomorrow's date but leave all other fields with valid details</li><li>Click 'Submit'</li></ol>|<ul><li>Update form will not submit</li><li>Text displays saying "Sorry, the restaurant is closed on a Monday/Tuesday"</li></ul>|Pass
User cannot update other users' bookings|<ol><li>Navigate to 'Current Bookings' page</li><li>Click 'Update' beside any listed booking</li><li>In the page URL, change the digit given before '/update' to '10' so the URL reads https://east-street-bc0671035c95.herokuapp.com/10/update/</li><li>Hit 'Enter'</li></ol>|<ul><li>User automatically directed to 'Current Bookings' page</li><li>Update form for this entry not displayed to user</li>|Pass
Bookings marked as 'Confirmed' change to 'Pending' when updated|<ol><li>Navigate to 'Current Bookings' page</li><li>Click 'Update' beside any booking marked as 'Confirmed'</li><li>Complete all fields on Update Form with valid details</li><li>Click 'Confirm & Update'</li></ol>|<ul><li>User directed to 'Current Bookings' page</li><li>Updated details reflected on displayed list with status set to 'Pending'</li><li>Alert message confirms booking updated successfully</li></ul>|Pass
User can delete a booking|<ol><li>Navigate to 'Current Bookings' page</li><li>Click 'Delete' beside any listed booking</li><li>Click 'Confirm & Delete'</li></ol>|<ul><li>User directed to 'Current Bookings' page</li><li>Appropriate details removed from displayed list</li><li>Alert message confirms booking deleted successfully</li></ul>|Pass
User cannot delete other users' bookings|<ol><li>Navigate to 'Current Bookings' page</li><li>Click 'Delete' beside any listed booking</li><li>In the page URL, change the digit given before '/delete' to '10' so the URL reads https://east-street-bc0671035c95.herokuapp.com/10/delete/</li><li>Hit 'Enter'</li></ol>|<ul><li>User automatically directed to 'Current Bookings' page</li><li>Deletion form for this entry not displayed to user</li>|Pass

## Unit Testing

## Accessibility

## Validator Testing

## Performance

## Bugs

There are no known bugs in the current deployment of the site. A number of bugs were found, added to the [Kanban workflow](https://github.com/users/ndsurgenor/projects/5), and corrected during development. A brief summary of these bugs is provided below:

**Bug**|**Description**|**Solution**|**Result**
-----|-----|-----|:-----:
Bootstrap/CSS styling not displaying correctly|Heroku deployment not displaying the Bootstrap/CSS styling as implemented in the code. Running a server using ```python3 manage.py runserver``` displays all styling correctly|<ul><li>Connect style.css by correcting typo of 'STATIC\_DIRS' to 'STATICFILES\_DIRS' in settings.py</li><li>Set images to load from static links rather than external sources</li></ul>|Fixed
Pages not scrolling correctly when required|On smaller screen heights the contents of the page will not scroll correctly to show content hidden behind the footer|<ul><li>Add margin-bottom to body under media query</li><li>Add margin-bottom divs on relevant pages where required e.g. Menu page</li></ul>|Fixed
Booking form not recording submissions on database|Form is rendering correctly as a functional object but not storing data to the database|<ul><li>'Status' included on form as a hidden field to ensure this present when form is submitted</li><li>Code added to form_valid to automatically set contact info (form.instance.contact_id = self.request.user.id)as this was also missing from the form</li>|Fixed




## Accessibility

[Wave Accessibility](https://wave.webaim.org/) tool was used throughout development and for final testing of the deployed website to check for any aid accessibility testing.

Testing was focused to ensure the following criteria were met:

- All forms have associated labels or aria-labels so that this is read out on a screen reader to users who tab to form inputs
- Color contrasts meet a minimum ratio as specified in [WCAG 2.1 Contrast Guidelines](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
- Heading levels are not missed or skipped to ensure the importance of content is relayed correctly to the end user
- All content is contained within landmarks to ensure ease of use for assistive technology, allowing the user to navigate by page regions
- All not textual content had alternative text or titles so descriptions are read out to screen readers
- HTML page lang attribute has been set
- Aria properties have been implemented correctly
- WCAG 2.1 Coding best practices being followed

## Validator Testing

All pages were run through the [w3 HTML Validator](https://validator.w3.org/). Initially there were some errors due to stray script tags, misuse of headings within spans and some unclosed elements. All of these issues were corrected and all pages passed validation.

Due to the django templating language code used in the HTML files, these could not be copy and pasted into the validator and due to the secured views, pages with login required or a secured view cannot be validated by direct URI. To test the validation on the files, open the page to validate, right click and view page source. Paste the raw html code into the validator as this will be only the HTML rendered code.

![HTML Validator](docs/testing/html.PNG)

All pages were run through the official [Pep8](http://pep8online.com/) validator to ensure all code was pep8 compliant. Some errors were shown due to blank spacing and lines too long, 1 line instead of 2 expected. All of these errors were resolved and code passed through validators with the exception of the settings.py file.

The django auto generated code for AUTH_PASSWORD_VALIDATORS were showing up as lines too long. I could not find a way to split these lines but since they were auto generated and not my own custom code, I hope this is acceptable.

![PEP8](docs/testing/pep8.PNG)

JavaScript code was run through [JSHINT](https://jshint.com) javascript validator. lIt flagged up issues with undefined variables as I jad forgotten to use the let keyword. This was fixed and the only warnings remained were that they were unused variables. The functions were called via onclick from the html elements themselves, so are in fact being used.

![JS validator](docs/testing/javascript.PNG)

## Lighthouse Report

Lighthouse report showed areas for improvement on SEO and Best practices. Meta descriptions and keywords were added to boost the SEO to 100 but the best practice warnings were coming from the use of an embedded iframe's javascript. Unfortunately I did not find a way to improve this as I am not initialising the google map iframe with javascript.

![Lighthouse v1](docs/testing/light-house-v2.PNG)