# Portfolio Website

A personal portfolio website built with Flask, featuring a contact form that sends emails directly to your inbox.

## Features

- Clean and responsive design
- Contact form with email functionality
- Static asset management

## Technologies Used

- Python 3.x
- Flask 3.1.2
- Jinja2 3.1.6
- HTML/CSS
- JavaScript

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd portfolio
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory and add:
```
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
```

## Running the Application

To run the development server:
```bash
python app.py
```

The website will be available at `http://localhost:5000`

## Project Structure

```
.
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── static/            # Static files (CSS, JS, images)
├── template/          # HTML templates
└── assets/           # Project assets
```

## Configuration

- SMTP server settings can be configured in `app.py`
- Static files are served from the `static` directory
- Templates are stored in the `template` directory

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.