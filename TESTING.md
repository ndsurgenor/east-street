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

These tests ensure that a user can successfully navigate the site using the provided navbar links, buttons, and footer icons. Pages in the booking area of the site require a username and password to access; the username _testname_ and password _test#123_ have specifically been registered for this purpose.

**Test**|**Steps**|**Expected**|**Outcome**
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
Gmail opens in a new tab/window when clicking footer icon|<ol><li>Click email icon in footer|Gmail opens in a new tab/window</li></ol>|Pass
Instagram opens in a new tab/window when clicking footer icon|<ol><li>Click Instagram icon in footer</li></ol>|Instagram opens in a new tab/window|Pass
Facebook opens in a new tab/window when clicking footer icon|<ol><li>Click Facebook icon in footer</li></ol>|Facebook opens in a new tab/window|Pass

### Responsiveness

### Authentication

These tests check the sign up, sign in, and sign out functionality of the site which are essential for secure access to the booking area. The username _testname_ and password _test#123_ have specifically been registered to help determine the outcome of these tests.

**Test**|**Steps**|**Expected**|**Outcome**
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

**Test**|**Steps**|**Expected**|**Outcome**
-----|-----|-----|:-----:
User can make a booking|Navigate|User directed to 'Current Bookings' page with success alert and booking added to list|Pass
User cannot make a booking unless a valid date is entered|Navigate|Booking form will not submit|Pass
User cannot make a booking unless a time is selected|Navigate|Booking form will not submit|Pass
User cannot make a booking on today's date or before|Navigate|Booking form will not submit with message reading "A booking cannot be made any earlier than tomorrow" |Pass
User cannot make a booking on a Monday or Tuesday|Navigate|Booking form will not submit with message reading "Sorry, the restaurant is closed on a Monday/Tuesday" |Pass
User can view their previously made bookings|Navigate|'Current Bookings' page displays user-made bookings alongside appropriate action buttons|Pass
User can update a booking|Navigate|User directed to 'Current Bookings' page with success alert and booking updated on list|Pass
User cannot update a booking unless a valid date is entered|Navigate|Booking form will not submit|Pass
User cannot update a booking unless a time is selected|Navigate|Booking form will not submit|Pass
User cannot update a booking to today's date or before|Navigate|Booking form will not submit with message reading "A booking cannot be made any earlier than tomorrow" |Pass
User cannot update a booking to a Monday or Tuesday|Navigate|Booking form will not submit with message reading "Sorry, the restaurant is closed on a Monday/Tuesday" |Pass
User cannot update other users' bookings|Navigate|User automatically directed to 'Current Bookings' page instead of update form|Pass
Bookings marked as 'Confirmed' change to 'Pending' when updated|Navigate|'Current Bookings' page displays booking with updated status|Pass
User can delete a booking|Navigate|User directed to 'Current Bookings' page with success alert and booking removed from list|Pass
User cannot delete other users' bookings|Navigate|User automatically directed to 'Current Bookings' page instead of deletion dialog|Pass

## Unit Testing

## Accessibility

## Validator Testing

## Performance

## Bugs



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

## Responsiveness

All pages were tested to ensure responsiveness on screen sizes from 320px and upwards as defined in WCAG 2.1 Reflow criteria for responsive design on Chrome, Edge, Firefox and Opera browsers.

Steps to test:

- Open browser and navigate to [sizzle-and-steak](https://sizzle-and-steak.herokuapp.com/)
- Open the developer tools (right click and inspect)
- Set to responsive and decrease width to 320px
- Set the zoom to 50%
-  Click and drag the responsive window to maximum width

Expected:

Website is responsive on all screen sizes and no images are pixelated or stretched. No horizontal scroll is present. No elements overlap.

Actual:

Website behaved as expected.

Website was also opened on the following devices and no responsive issues were seen:

Oukitel C21 Pro
TCL 30 Pro
iPhone SE


## Bugs

Logic has been implemented to ensure that when a booking is created that it books the table with the capacity lowest to suit the number of guests. When a user updates a booking, this does not function correctly on the edit and will reassign the booking to another table with the next lowest capacity. It should keep the booking on the current table if it is a lower capacity but unfortunately does not work correctly and has not been resolved in time for submission.