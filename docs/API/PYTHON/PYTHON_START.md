# Python 3 API Description

This document contains information regarding functions and values used in this test application.

## Preface
Thanks to Django Framework this web application is split in several modules consisting of related models and functions.
 The documentation of Django framework calls them *apps*.

Typical Django app is started using ```django-admin``` application. This application may be installed on your system, 
if not, please proceed to section
 [Installation of Django and related frameworks in different environments](../KB/KB1000.md)

## Modules

Application consists of following modules:

### [simple_shop](modules/simple_shop2.md)
Simple shop is a module consisting logic and presentation foundation for REST framework for End Users / integration.
### [staff_zone](modules/staff_zone.md)
Staff zone is a module containing logic and presentation foundation for staff zone, where shop staff may edit parameters
for products and orders.
 
