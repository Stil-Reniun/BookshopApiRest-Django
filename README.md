# BookshopApiRest
"BookshopApiRest is a REST API based on Django 5 and its Rest-framework library, designed to provide a wide range of functionalities for an online bookstore. From publishing books to making purchases and interacting through comments, the API encompasses all essential features of a modern bookshop. With the use of JWT access tokens for authentication across all operations, comprehensive security for data and transactions is ensured."

## Key Features

- **CRUD Operations for Books:** Allows creating, reading, updating, and deleting books.
- **Authentication and Authorization:** Employs JWT for handling access tokens, ensuring that only authorized users can perform certain operations.
- **User Management:** Enables user creation and provides login functionalities.
- **Comment Posting:** Users can post comments on books available in the store.
- **Book Upload:** Users have the ability to upload their own books for sale on the platform.

## Documentation

The API is documented using Swagger or drf-yasg, facilitating its understanding and use. 
Detailed documentation is available for all operations, easing integration with the frontend and subsequent deployment in production.

## Technologies Used

- Django: High-level Python web framework.
- Django REST Framework (DRF): Powerful toolkit for building web APIs.
- JSON Web Tokens (JWT): Mechanism used for authentication and authorization.
- Swagger / drf-yasg: Tools for API documentation.

## Installation and Usage

To install and use this project, follow these steps:

1. Clone this repository to your local machine.
2. Install dependencies using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

3. Perform database migrations:

    ```bash
    python manage.py migrate
    ```

4. Start the development server:

    ```bash
    python manage.py runserver
    ```

5. Access the API documentation via the URL provided by Swagger or drf-yasg.

## Contribution

If you'd like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a branch for your new feature (`git checkout -b feature/new-feature`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. For more details, please read the [LICENSE](LICENSE) file.

## Contact

If you have any questions or comments about the project, feel free to contact us via [email](mailto:email@example.com) or by opening an issue in this repository.
