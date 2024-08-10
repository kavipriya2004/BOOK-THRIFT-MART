# BOOK-THRIFT-MART
---
# Bookstore Application

A simple Flask application for managing user registrations and providing access to various book genres. Users can register, log in, and explore different categories of books.

## Features

- **User Registration:** Users can register with personal details.
- **User Login:** Users can log in using their registered email and password.
- **Book Genres:** Provides access to various book genres including Horror, Thriller, Romance, Fantasy, and more.
- **Responsive Pages:** Dynamic pages for each book genre.

## Technologies Used

- **Flask:** Web framework for the application.
- **Flask-MySQLdb:** For MySQL database connection.
- **HTML/CSS:** For front-end templates.

## Installation

To set up and run the application, follow these steps:

### Set Up the Environment

Create a virtual environment (recommended) and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

Install the required Python libraries:

```bash
pip install Flask Flask-MySQLdb
```

### Configure MySQL Database

Ensure you have a MySQL database named `form` and a table named `info` with the following schema:

```sql
CREATE TABLE info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sname VARCHAR(100),
    age INT,
    dob DATE,
    phone VARCHAR(15),
    mail VARCHAR(100) UNIQUE,
    Gender VARCHAR(10),
    fpass VARCHAR(100),
    lpass VARCHAR(100),
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50)
);
```

### Update Database Credentials

Update the database credentials in `app.py`:

```python
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "your_mysql_password"
app.config["MYSQL_DB"] = "form"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
```

### Run the Flask Application

Start the Flask application:

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000/`. Open this URL in your web browser to access the application.

## File Structure

- `app.py`: The main Flask application file.
- `templates/`: Contains HTML templates for the web pages.
  - `first.html`: The homepage template.
  - `signup.html`: The registration page template.
  - `login.html`: The login page template.
  - `recommendation.html`: The page shown after successful login.
  - Various genre templates (e.g., `horror.html`, `thriller.html`, etc.).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
