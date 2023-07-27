# Fibonacci Number Web Application

The Fibonacci Number Generator is a simple web application that allows users to generate the first 'n' Fibonacci numbers, where 'n' is an integer provided by the user. The application is built using Django on the backend and Bootstrap for the frontend.

## Features

- Users can input an integer 'n' to generate the first 'n' Fibonacci numbers.
- The application stores previously calculated Fibonacci sequences in a relational database to avoid recomputation.
- The frontend has two pages:
    - Fibonacci Form Page: This page contains a simple form with an input field for the user to enter the value of 'n' and a submit button to request the Fibonacci numbers.
    - Fibonacci Result Page: After submitting the form, the user is redirected to this page, which displays the first 'n' Fibonacci numbers as a comma-separated list.

## Installation and Setup

1. Clone the repository to your local machine.
2. Ensure you have Python and Django installed.
3. Apply the database migrations:
```
python manage.py makemigrations fibonacci_app
python manage.py migrate
```
4. Run the development server:
```
python manage.py runserver
```
5. Access the application in your web browser at http://127.0.0.1:8000/ (or at your local server).

## How to Use

1. Open your web browser and navigate to http://127.0.0.1:8000/.
2. On the homepage (Fibonacci Form Page), enter a positive integer 'n' in the input field.
3. Click the "Generate" button to calculate and display the first 'n' Fibonacci numbers.
4. You will be redirected to the Fibonacci Result Page, where the sequence is shown.


## Databse

The application uses a relational database to store previously calculated Fibonacci sequences. The FibonacciNumber model in the fibonacci_app/models.py file is responsible for storing the data. The database configuration is defined in the Django settings.

## Known Issues

Large Fibonacci numbers may encounter overflow errors, especially when 'n' is quite large. To handle this, the application uses Django's DecimalField to store large numbers with high precision.

## Contributions

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, feel free to open a pull request or submit an issue. Create by Het Patel (hetpatel0199@gmail.com)