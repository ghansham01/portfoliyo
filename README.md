# Personal Portfolio Website

A modern, responsive portfolio website built with Flask, featuring a dynamic contact form with email integration.

## 🚀 Features

- Responsive design that works on desktop and mobile
- Interactive contact form with email notifications
- Dynamic project showcase section
- Modern UI with smooth animations
- SEO optimized structure

## 🛠 Technologies Used

- **Backend:**
  - Python 3.x
  - Flask 3.1.2
  - Jinja2 3.1.6
  - SMTP email integration

- **Frontend:**
  - HTML5
  - CSS3
  - JavaScript (ES6+)
  - Responsive Design

## 📋 Prerequisites

- Python 3.8 or higher
- Gmail account with App Password enabled
- Git

## ⚙️ Installation

1. **Clone the repository:**
```bash
git clone https://github.com/ghansham01/portfoliyo.git
cd portfolio
```

2. **Set up virtual environment:**
```bash
python -m venv .venv
.venv\Scripts\activate  # For Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**
Create a `.env` file in the root directory:
```plaintext
EMAIL_USER=your-gmail@gmail.com
EMAIL_PASSWORD=your-gmail-app-password
RECEIVER_EMAIL=your-receiving-email@domain.com
```

## 🚦 Running the Application

1. **Start the development server:**
```bash
python app.py
```

2. **Access the website:**
Open your browser and navigate to `http://localhost:5000`

## 📁 Project Structure

```
portfolio/
│
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── .env                 # Environment variables (git-ignored)
├── .gitignore          # Git ignore rules
│
├── static/             # Static files
│   ├── css/           # Stylesheets
│   ├── js/            # JavaScript files
│   └── images/        # Image assets
│
├── template/          # HTML templates
│   ├── index.html    # Main portfolio page
│   └── includes/     # Reusable template parts
│
└── assets/           # Project assets and resources
```

## ⚡ Quick Start Guide

1. **Gmail Setup:**
   - Enable 2-Factor Authentication
   - Generate App Password
   - Update `.env` file with credentials

2. **Customize Content:**
   - Modify `template/index.html` for content
   - Update styles in `static/css`
   - Add your projects and images

3. **Test Email Function:**
   - Fill out contact form
   - Check both sending and receiving emails
   - Verify SMTP settings if needed

## 🔧 Configuration Options

- **Email Settings:** Update SMTP configuration in `app.py`
- **Development Mode:** Set `debug=True` for development
- **Static Files:** Served from `static` directory
- **Templates:** Stored in `template` directory

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit changes: `git commit -m 'Add AmazingFeature'`
4. Push to branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Troubleshooting

- **Email not sending?** Check:
  - Gmail App Password is correct
  - Environment variables are loaded
  - SMTP settings in `app.py`
  
- **Style issues?**
  - Clear browser cache
  - Check CSS file paths
  - Verify responsive breakpoints

## 📫 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/portfolio](https://github.com/yourusername/portfolio)