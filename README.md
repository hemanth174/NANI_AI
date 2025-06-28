# NANI Voice Assistant

This is a Django project for a voice assistant named NANI. The project aims to provide a user-friendly interface for interacting with various voice commands.

## Project Structure

```
nani
├── manage.py
├── nani
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── assistant
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
├── static
│   └── index.html
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd nani
   ```

3. Create a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required packages:
   ```
   pip install django
   ```

## Running the Project

1. Apply migrations:
   ```
   python manage.py migrate
   ```

2. Run the development server:
   ```
   python manage.py runserver
   ```

3. Access the application at `http://127.0.0.1:8000/`.

## Usage

The NANI voice assistant can respond to various commands such as:
- Open YouTube
- Play any song
- Tell the current time
- Answer questions
- Tell jokes
- Open Chrome

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.