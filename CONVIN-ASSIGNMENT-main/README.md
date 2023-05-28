# CONVIN ASSIGNMENT
## Integrating Google Calendar API with OAuth 2.0 and Django Rest Framework

[![HACNAY]](https://www.linkedin.com/in/hacnay/)



Challenge: The goal of this project is to integrate Google Calendar into a Django Rest API using OAuth 2.0 authorization.

- To run the program, simply run this command:

 ```
 pip install -r requirements.txt
 ```

- Endpoint:
```
/rest/v1/calendar/init/ -> GoogleCalendarInitView()
```
This view should start step 1 of the OAuth. Which will prompt user for his/her credentials

```
/rest/v1/calendar/redirect/ -> GoogleCalendarRedirectView()
```
This view will do two things
1. Handle redirect request sent by google with code for token. You
need to implement mechanism to get access_token from given
code
2. Once got the access_token get list of events in users calendar

###### Note: To run this assignment need google account credentials which need to save in the project directory and add a redirect URL in your google cloud. Please read below documents and references section.

#### Documents and References

##### Name - Sources 

- Google Identity: Using OAuth 2.0 for Web Server Applications: https://developers.google.com/identity/protocols/oauth2/web-server
- Google Calendar API: https://developers.google.com/calendar/api/v3/reference
- Google Account Credentials: https://developers.google.com/identity/protocols/oauth2/web-server#exchange-authorization-code 


[PlDb]: <https://developers.google.com/identity/protocols/oauth2/web-server>
[PlGh]: <https://developers.google.com/calendar/api/v3/reference>
[PlIa]: <https://developers.google.com/identity/protocols/oauth2/web-server#exchange-authorization-codee>
#### The Google Calendar API OAuth 2.0 for Web Server Applications Integration project has the following features:

- OAuth2 mechanism for user's calendar access: The project uses the OAuth2 mechanism to get users' calendar access, which ensures secure authorization of user data.

- Django Rest API integration: The project integrates with the Django Rest Framework to provide RESTful API endpoints for calendar integration.

- Two API endpoints: There are two API endpoints provided in the project, /rest/v1/calendar/init/ and /rest/v1/calendar/redirect/, that handle the different stages of the OAuth2 authorization process.

- Google Calendar events: The project retrieves a list of events in the user's calendar once access is granted through the OAuth2 authorization process.

- Requirements: The project requires the installation of the packages specified in the requirements.txt file.

- Google account credentials: A valid Google account with API credentials is required to run the project, and the user must also set a redirect URL in the Google Cloud.

- Well-documented: The project includes references and links to Google's official documentation for OAuth2 for web server applications and the Google Calendar API.

#### The scope of improvement
- Improving the UI/UX of the authorization flow to make it more user-friendly.

- Adding more functionalities to the Calendar API integration, such as the ability to create, update, and delete events.

- Adding support for more Google Calendar features, such as recurring events, event reminders, and time zones.

- Improving error handling and providing more detailed error messages to users.

- Integrating the calendar integration with other services or APIs to provide a more comprehensive solution.

- Implementing security measures, such as encryption and authentication, to protect users' data.

- Adding support for multiple users and providing options to control access and privacy.

- Improving performance and reducing latency in retrieving and updating events in real-time.

- Automating the deployment process to make it easier for users to integrate the calendar API into their projects.

- Adding analytics and reporting capabilities to help users better understand how they are using the calendar integration.


