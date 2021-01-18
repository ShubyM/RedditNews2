# RedditNews2
A website that uses Django + React to generate a score of the day based off of the news subreddit (https://www.reddit.com/r/news)!

# Setup
Inorder to run this locally you will need to create a credentials.py file in the redditnews/reddit/credentials.py 
containing the ID, SECRET and USER_AGENT fields necessaray for util.py to run. 

# Notes
Django is made up of a series of components that help it receive and respond to user requests. Here's a quick overview of how that works.

A Request/Response System
One way to describe Django is as a set of software components that aid in the receiving of web requests, and the returning of web responses. More simply, Django can accept requests for URLs like www.example.com, and return all of the HTML needed for a web browser to render a page. That page could be plain text or something much richer.

Web Requests Enter Django Applications via URLs
The entry point to Django applications are URLs. Django developers have full control of what URLs are available in their application. URLs could be as simple as www.example.com, or more complex like www.example.com/whatever/you/want/. When a user accesses a URL, Django will pass it to a view for processing.

Requests are Processed by Views
Django Views are custom Python code that get executed when a certain URL is accessed. Views can be as simple as returning a string of text to the user. They can also be made complex, querying databases, processing forms, processing credit cards, etc. Once a view is done processing, a web response is provided back to the user.

Web Responses are Returned
It wouldn't be very helpful if users made a request to an application and didn't see a response. When a user accesses a URL in a browser, what is shown in the window is the web response. Most often this is a HTML web page, showing a combination of text and images. These pages are created using Django's templating system.

Where It Gets Interesting
With these core pieces of Django you have an enormous amount of flexibility to build a wide range of applications. It could be used to build a simple blog, or rich desktop and mobile applications. To give you an idea of what's possible, popular sites like Pinterest, Instagram, and Disqus are powered by the Django framework.

FROM: https://ultimatedjango.com/learn-django/lessons/how-django-works/

More specifics
--------------
Serializers make it possible to convert models (aka things to store in a database) to a JSON format









