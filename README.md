# Readme

> [!INFORMATION]
> 
> Social Blog application with DRF and React.

## Overview 

> [!INFORMATION]
> 
> This project combines Django REST Framework (DRF) for the backend and React for the frontend to build a social application. The application implements essential features such as user authentication, post creation, liking, commenting, and associated CRUD operations. The frontend in React interacts with the backend API built using DRF, making the application efficient and scalable.

**Key Features:**
* *Login and Register System:*
  * User Registration: Allows new users to sign up.
  * Login/Logout: User authentication system using token-based authentication (e.g., JWT).
* *CRUD Post:*
  * Users can create, read, update, and delete posts.
* *Post Like Feature (CRUD):*
  * Users can like or unlike posts.
  * The like count is stored and displayed.
* *Comment System (CRUD):*
  * Users can comment on posts.
  * The system supports creating, reading, updating, and deleting comments.
  * Comments are displayed in relation to their respective posts.
* *Like Comment (CRUD):*
  * Similar to post likes, users can like or unlike comments.
  * The like count for comments is displayed and updated accordingly.

## Packages

| Packages                                  | Description | Installation/Note |
| ----------------------------------------- | ----------- | ----------------- |
| `Django`                                  |
| `django-cors-headers`                     |
| `django-debug-toolbar`                    |
| `django-extensions/pydotplus/ pygraphviz` |
| `django-filter`                           |
| `django-redis /redis`                     |
| `djangorestframework`                     |
| `djangorestframework-simplejwt`           |
| `drf-nested-routers`                      |
| `pillow`                                  |
| `psycopg[binary]`                         |
| `PyJWT`                                   |
| `pytest`                                  |
| `pytest-django`                           |
| `python-decouple`                         |


## Demo API

> [!INFORMATON]
> 
> API Lists

| Method | URL | Description | Example/Result |
| -------| -------- | ----------- | -------------- |
| GET | api/user/ |  Lists all the users |
| GET | api/user/user_pk | Retrieves a specific user |
| PATCH | api/user/user_pk | Modifies a user |
| POST | api/auth/login/ | 
| GET | api/auth/logout/ |
| ...|




* `python3 manage.py show_urls`
```
/api/auth/login/        core.auth.viewsets.login.LoginViewSet   core-api:auth-login-list
/api/auth/logout/       core.auth.viewsets.logout.LogoutViewSet core-api:auth-logout-list
/api/auth/refresh/      core.auth.viewsets.refresh.RefreshViewSet       core-api:auth-refresh-list
/api/auth/register/     core.auth.viewsets.register.RegisterViewSet     core-api:auth-register-list
/api/post/      core.post.viewsets.PostViewSet  core-api:post-list
/api/post/<pk>/ core.post.viewsets.PostViewSet  core-api:post-detail
/api/post/<pk>/like/    core.post.viewsets.PostViewSet  core-api:post-like
/api/post/<pk>/remove_like/     core.post.viewsets.PostViewSet  core-api:post-remove-like
/api/post/<post_pk>/comment/    core.comment.viewsets.CommentViewSet    core-api:post-comment-list
/api/post/<post_pk>/comment/<pk>/       core.comment.viewsets.CommentViewSet    core-api:post-comment-detail
/api/post/<post_pk>/comment/<pk>/like/  core.comment.viewsets.CommentViewSet    core-api:post-comment-like
/api/post/<post_pk>/comment/<pk>/remove_like/   core.comment.viewsets.CommentViewSetcore-api:post-comment-remove-like
/api/user/      core.user.viewsets.UserViewSet  core-api:user-list
/api/user/<pk>/ core.user.viewsets.UserViewSet  core-api:user-detail
```

> [!INFORMATION]
> 
> Demo



## Testing

> [!INFORMATION]
> 
> Using pytest with django.

Setup:

```
setup
```

Description: (Overview)
* Test 1
* Test 2

Result (backend testing):

```
pytest core/user
==================================================================================================== test session starts =====================================================================================================
platform linux -- Python 3.10.12, pytest-8.3.3, pluggy-1.5.0
django: version: 5.1.1, settings: backend.settings (from ini)
rootdir: /home/dev/django-learning/src_example/full_stack_django_react/backend
configfile: pytest.ini
plugins: django-4.9.0
collected 6 items                                                                                                                                                                                                            

core/user/tests.py ......                                                                                                                                                                                              [100%]

===================================================================================================== 6 passed in 1.84s ======================================================================================================
```
## Run 

* Clone repository: git clone
* Create virtual environment: `python3 -m venv env`
* Activate virtual environment: `source enn/bin/activate`
* Install requirments.txt: `pip install -r requirements.txt`
* Run postgres with docker: `docker run --name=blog_db -e POSRGRES_DB=blog -e POSTGRES_USER=blog -e POSTGRES_PASSWORD=xxxxx -p 5432:5432 -d postgres:16.2`
* Run backend: `python3 manage.py migrate && python3 manage.py runserver`
* Run redis docker: `docker run -it --rm --name redis -p 6379:6379 redis:7.2.4`
* Install node, npm, yarn
* Install package: `yarn install`
* Run frontend: `yarn start`

## References 
* Django 5 documentation
* Django Rest Framework