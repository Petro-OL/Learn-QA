**QA Automation Project**

This project created for the final homework assignment of the **QA Automation**

(online course on platform **Prometeus** developed in partnership with **GlobalLogic**)

Framework covering:

**API testing =** for GitHub about users repo for validate response fields and status codes

**Database testing** = for verify data storage with non-typical case

**UI automation** = for verify functionality web-sities (e.g. login or seach) GitHub, Rozetka

Tools and technologies:

Programming language **Python**,

framework **Pytest** for writing automated tests,

**Requests** for HTTP API tests,

**SQLite3** for database storage

and **Selenium WebDriver** for browser automation and UI tests.

Structure of Project

- config - common settings
- modules
  - api / clients - classes for API clients (github API).
  - common - classes for common modules (work with database)
  - ui / page_objects - PageObject classes for tested pages
- tests
  - api - API and HTTP tests
  - database - database test
  - ui - UI automation tests for web-sities GitHub and Rozetka
- conftest.py - Pytest fixtures
- pytest.ini - Pytest markers
- additional files - database, cromedriver

Disclamer

- you need to install all the necessary components and change local path
- the cromedriver and code is written for the Chrome browser version 109.0.5414
