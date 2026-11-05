# LIBRARY MANAGEMENT SYSTEM USING DJANGO & DRF

This is a robust RESTful API for library management system, built with Django and DRF (Django Rest Framework). Uses default DRF's authentication tokens, Role Based Access Control (RBAC) for librarians only, books filtering opiton using author name and genre.

## Tech Stacks
- **Framework:** Django and DRF (Django REST Framework)
- **Authentication and Authorization:** DRF's auth tokens
- **Filtering:** uses `django-filter` any version
- **Database:** SQLite
- **Python:** version 3.10+
- **black:** any version
- **flake8:** any version  

## Features
* **Access list of books and authors:** Books and Author details are acessible for public.
* **Authentication and Authorization:** Uses DRF tokens to authenticate libararians, and allow them to modify data (put/delete).
* **Role Based Access Control:**
    *  `(/library_api/admin)` used to manage all librarians and accessed only by admin.
    *  `(/library_api/books/ or /{id})` use to read only lists of books and author details for any user.
    *  `(/library_api/books/{id})` authenticated librarians can use this endpoint to update or delete books.

## Setup and installation
**Prerequsites**
* python 3.10+
* Git

### Clone repository
``` bash
git clone https://github.com/Amlakyalew/LibraryManagementAPI.git
cd LibraryManagementAPI
```

### Install required packages
```
pipenv install
```

### Activate virtual environment and run the program
```
pipenv shell
python manage.py runserver
```
## Main endpoints

```
METHOD                         ENDPOINT                           ROUTE DESCRIPTION                          AUTH REQUIRED
GET                           /library_api/authors/              List all authors in catalog                      No
POST                          /library_api/authors/              Create a new author entry                        Yes
GET                           /library_api/authors/{id}/         Retrieve an author with their books list         No
PUT                           /library_api/authors/{id}/         Update author information                        Yes
DELETE                        /library_api/authors/{id}/         Delete an author record                          Yes
GET                           /library_api/books/                List all books in catalog                        No
POST                          /library_api/books/                Create a new book & assign to author             Yes
GET                           /library_api/books/{id}/           Retrieve single book with author details         No
PUT                           /library_api/books/{id}/           Update book catalog attributes                   Yes
DELETE                        /library_api/books/{id}/           Delete a book record                             Yes
GET                           /library_api/books/?author={id}    Filter catalog books by Author ID                No
GET                           /library_api/books/?genre={name}   Filter catalog books by genre name               No
