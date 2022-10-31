# Flaskr Blog
A blog application done to apply core concepts as learned from the official flask documentation. It involved:

- Blog (Users are able to register, log in, create posts, and edit or delete their own posts.)
- Authentication, registering blueprints, sessions and cookies, protected routes.
- Template views
- SQLite database for users and posts
- Tests
- Deployment or packaging and installing the application on other computers.<br/>

<table border="0">
 <tr>
    <td><b style="font-size:20px">Index</b></td>
    <td><b style="font-size:20px">Create post</b></td>
 </tr>
 <tr>
    <td><img src="flaskr/img/index.jpg"/></td>
    <td><img src="flaskr/img/crete.jpg"/></td>
 </tr>
</table>

## Install the Project
### Use pip to install the project in the virtual environment.
    pip install -e .

## Running the app locally
### Initialise the db
    flask --app flaskr init-db
### then run
    flask --app flaskr run

## Tests
### Install pytest and coverage then:
    coverage run -m pytest && coverage report

