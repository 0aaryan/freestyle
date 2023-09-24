# Freestyle E-commerce App (Django)
<!---

{
  "show_on_portfolio : true,
  "featured:true,
  "items": [
    {
      "title": "Freestyle E-commerce App (Django)",
      "content": "A full-stack e-commerce app built with Django. Users can shop, manage profiles, and view order history.",
      "image": "/path/to/your/image.png",
      "featured": {
        "name": "Demo",
        "link": "https://your-project-demo-url.com"
      },
      "badges": [
        "Django",
        "E-commerce"
      ],
      "links": [
        {
          "icon": "fab fa-github",
          "url": "https://github.com/your-username/your-project-repo"
        },
        {
          "icon": "fas fa-external-link-alt",
          "url": "https://your-project-website.com"
        }
      ]
    }
  ]
}

--->
Freestyle is a full-stack e-commerce application developed using Django, a popular web framework in Python. The app allows users to browse through a variety of products, add them to their cart, and proceed to checkout for payment. Registered users can manage their profiles and view their order history.

## Technical Details

### Dependencies

The application relies on the following dependencies:

- Django: The core web framework used for building the application.
- Django Forms: Used for user registration and login.
- Django Views: The views are responsible for handling user requests and rendering appropriate templates.
- Django Models: Used to define the database schema and interact with the database.
- Django Messages: Used for displaying flash messages.
- Django Authentication: Used for user authentication and managing user sessions.
- Django CSRF: Provides CSRF protection for forms.
- Django Cache Control: Used for cache control in views.
- Django JSON Response: Used for returning JSON responses.
- Django Authentication Decorators: Used to restrict access to certain views to authenticated users.
- Django CSRF Exempt: Used to exempt views from CSRF protection when necessary.

### File Structure

The project has the following file structure:

```
.
├── [other files and directories...]
├── freestyle
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── location.py
│   ├── migrations
│   ├── models.py
│   ├── static
│   ├── templates
│   └── templatetags
├── [other files and directories...]
```

- `freestyle`: The main app directory that contains various components of the e-commerce app.
  - `__init__.py`: An empty file that makes the `freestyle` directory a Python package.
  - `admin.py`: Configuration for Django admin interface to manage app models.
  - `apps.py`: Configuration for the app itself.
  - `forms.py`: Contains the form classes used for user registration and login.
  - `location.py`: [Description of the file]
  - `migrations`: Directory containing database migrations for managing changes to the database schema.
  - `models.py`: Contains the database models used in the app.
  - `static`: Directory to store static files (e.g., CSS, JS) used in the app.
  - `templates`: Directory to store HTML templates for rendering views.
  - `templatetags`: [Description of the directory]

### Views

The views are defined in the `views.py` file and handle user requests and interactions with the application. The main views are:

- `index1`: Renders the home page with products filtered by category.
- `index2`: Redirects to the home page with all products displayed.
- `register`: Handles user registration.
- `login`: Renders the login page.
- `profile`: Renders the user's profile page.
- `product`: Renders the product details page and handles adding products to the cart.
- `cartView`: Renders the shopping cart page.
- `addtocart`: Adds a product to the cart.
- `removefromcart`: Removes a product from the cart.
- `addProfile`: Renders the page for adding billing details to the profile.
- `editProfile`: Renders the page for editing billing details in the profile.
- `checkout`: Renders the checkout page.
- `placeorder`: Places an order and saves it to the database.
- `orders`: Renders the order history page for users and the order management page for admins.
- `payment`: Renders the payment page for completing the transaction.
- `handlerequest`: Handles Paytm payment requests (stub function).

### Authentication and User Management

The application uses Django's built-in authentication system for user registration, login, and managing user sessions. Users can register for an account, log in, and update their profile information. Authenticated users can add products to the cart, place orders, and view their order history.

### Database

The application uses the default SQLite database provided by Django. It defines models for products, categories, shopping carts, orders, and billing details. These models are used to store and retrieve data from the database.

### Templates

HTML templates are stored in the `templates` directory. They are used to render views and display content to users.

### Static Files

CSS, JS, and other static files are stored in the `static` directory. These files control the styling and interactivity of the application.

### Payments

The application supports payments using the Paytm payment gateway. However, the `handlerequest` view is currently empty and needs to be implemented to handle payment requests from Paytm.
