# Marketplace

Marketplace is a web application that allows users to buy and sell various types of stuffs online. Users can create an account and login and publish their posts along with an image for the stuff they are selling with the price. They can see all their stuffs up for sale in a dashboard. Also, users can filter the thing they are searching for in a browse section where they can use filter option. Finally, the user can contact the seller in a two-way communication fashion. The project is based on Django and HTML with Tailwind CSS.

## Features

- **User authentication** : Users can register and login using their email and password.
- **Post creation** : Users can create a new post by filling a form with the title, description, category, price and image of the stuff they want to sell. They can also edit or delete their posts.
- **Dashboard** : Users can see all their posts in a dashboard where they can see all the post hey made. They can also mark their posts as sold or unsold.
- **Browse** : Users can browse all the available posts in different categories such as electronics, books, clothing, etc. They can also use a search bar or a filter option to narrow down their results by keyword, price range or description.
- **Messaging** : Users can contact the seller of a post by sending a message through the web application. They can also see all their conversations with other users in a message section.

## Technologies

- **Django** : Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It provides features such as user authentication, database management, template engine, etc.
- **HTML** : HTML is the standard markup language for creating web pages and web applications. It defines the structure and content of the web pages.
- **Tailwind CSS** : Tailwind CSS is a utility-first CSS framework that provides low-level class names that let you build any design without writing any custom CSS. It offers responsive design, custom colors, typography, etc.

## Installation

To run this project locally, you need to have Python 3 and pip installed on your machine. Then follow these steps:

1. Clone this repository to your local machine using `git clone https://github.com/SwastikGorai/marketplace.git`.
2. Navigate to the project directory using `cd marketplace`.
3. Create a virtual environment using `python -m venv venv`.
4. Activate the virtual environment using `source venv/bin/activate` on Linux or `venv\Scripts\activate` on Windows.
5. Install the required dependencies using `pip install -r requirements.txt`.
6. Make migrations to create the database tables using `python manage.py makemigrations` and `python manage.py migrate`.
7. Create a superuser account using `python manage.py createsuperuser` and follow the prompts.
8. Run the development server using `python manage.py runserver`.
9. Open your browser and go to `http://localhost:8000/` (or something similar) to see the web application.

## Todos
- Add logout option
- Add a feature to delete and edit messages
- Hosting the project

## Contribution

Contributions are always welcome! To make a comtribution, simply create a pull request with a new branch with all the necessary changes and describing the changes in the PR.
