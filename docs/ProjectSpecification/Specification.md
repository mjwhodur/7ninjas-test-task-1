# Task
Description: Simple selling platform with REST support

## Task
Mid Level

Write REST api for simple selling platform.
Use Python 3.6+, Django 1.11+, DRF 3.6+, Frontend is not needed

### Entities
Product:
```
Title, image, description, price (both value and currency), 
category, likes (user likes product and it gets added to user's wish list
```
Type of Deliveries:
```commandline
Title, Price, could be fixed value or percent of product's price
```

Category
```text
Title
```

Order
```text
Product (which is ordered), user (who orders), chosen delivery, total price (product's price and delivery price)
count of products

```


### Endpoints
- List of products with pagination, simple filtering by category and simple search by title of the product
- User's wish list
- Create new order
- Oauth / JWT
- Admin panel, where staff user can add/edit/remove products, categories, users and see the list of orders