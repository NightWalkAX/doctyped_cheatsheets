# Doctyped Cheatsheets 📚

> **Multilanguage Frappe Framework Cheatsheets** - Your comprehensive reference guide for Frappe development

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Frappe](https://img.shields.io/badge/frappe-framework-orange.svg)](https://github.com/frappe/frappe)

## 🎯 Overview

**Doctyped Cheatsheets** is a comprehensive Frappe Framework application that provides multilingual cheatsheets for developers working with Frappe, ERPNext, and related technologies. This app serves as a centralized knowledge base with practical code examples, commands, and best practices available in both English and Spanish.

### 🌟 Key Features

- **📖 Multilingual Support**: Complete documentation in English and Spanish
- **🔧 Comprehensive Coverage**: Includes cheatsheets for:
  - Frappe Framework APIs (Python & JavaScript)
  - Bench commands and operations
  - Document and DocType operations
  - Form scripts and client-side development
  - Database operations and queries
  - Custom controls and UI components
  - Git workflows and best practices
  - Python fundamentals and advanced concepts
- **🎨 Structured Data Format**: Well-organized JSON structure for easy consumption
- **🔍 Searchable Content**: Easy-to-navigate and searchable cheatsheet database
- **📱 Developer-Friendly**: Designed specifically for Frappe developers' daily workflow

## 📦 Installation

### Prerequisites
- Frappe Framework (v14.0.0 or higher)
- Python 3.10+
- Valid Frappe bench setup

### Quick Install

```bash
# Navigate to your bench directory
cd /path/to/your/bench

# Get the app from repository
bench get-app https://github.com/YOUR_USERNAME/doctyped_cheatsheets

# Install the app on your site
bench --site your-site.local install-app doctyped_cheatsheets

# Migrate to apply changes
bench --site your-site.local migrate
```

### Manual Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/doctyped_cheatsheets.git apps/doctyped_cheatsheets

# Install the app
bench --site your-site.local install-app doctyped_cheatsheets
```

## 🚀 Usage

### Accessing Cheatsheets

Once installed, you can access the cheatsheets through:

1. **Frappe Desk**: Navigate to the Cheatsheets module
2. **API Access**: Use the built-in processing functions to retrieve structured data
3. **Direct File Access**: Browse JSON files in the `data/` directory

### Available Cheatsheet Categories

| Category | Description | Languages |
|----------|-------------|-----------|
| **Frappe Framework** | Core APIs, hooks, utilities | 🇪🇸 🇬🇧 |
| **Bench Commands** | CLI operations and workflows | 🇪🇸 🇬🇧 |
| **JavaScript APIs** | Client-side development | 🇪🇸 🇬🇧 |
| **Python Utilities** | Server-side development | 🇪🇸 🇬🇧 |
| **Database Operations** | Query builder and ORM | 🇪🇸 🇬🇧 |
| **Git Workflows** | Version control best practices | 🇪🇸 🇬🇧 |
| **Development Tools** | NPM, logging, debugging | 🇪🇸 🇬🇧 |

### Code Examples

```python
# Example: Processing cheatsheets programmatically
from doctyped_cheatsheets.src.process_cheatsheets import process_cheatsheets

# Get all processed cheatsheet data
cheatsheets_data = process_cheatsheets()

# Access specific cheatsheet items
for item in cheatsheets_data:
    print(f"Title: {item['title']}")
    print(f"Language: {item['language']}")
    print(f"Tags: {', '.join(item['tags'])}")
```

## 🛠️ Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/doctyped_cheatsheets.git
cd doctyped_cheatsheets

# Install development dependencies
pip install pre-commit

# Set up pre-commit hooks
pre-commit install
```

### Code Quality Tools

This project uses the following tools to maintain code quality:

- **Ruff**: Fast Python linter and formatter
- **ESLint**: JavaScript/TypeScript linting
- **Prettier**: Code formatting
- **PyUpgrade**: Python syntax modernization

### Project Structure

```
doctyped_cheatsheets/
├── doctyped_cheatsheets/
│   ├── doctyped_cheatsheets/
│   │   ├── data/                 # JSON cheatsheet files
│   │   ├── doctype/             # Frappe DocTypes
│   │   │   ├── cheat/           # Individual cheat entries
│   │   │   └── cheatsheet/      # Cheatsheet collections
│   │   └── src/                 # Processing utilities
│   ├── hooks.py                 # Frappe hooks configuration
│   └── install.py              # Installation scripts
├── pyproject.toml              # Project configuration
└── README.md                   # This file
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Adding New Cheatsheets

1. **Create JSON files** in the `data/` directory following the existing format:
   ```json
   {
     "title": "Your Cheatsheet Title",
     "language": "es", // or "en"
     "tags": ["tag1", "tag2"],
     "items": [
       {
         "code": "sample_code()",
         "description": "Description of what this code does",
         "example": "# Example usage\nsample_code()\n# Expected output"
       }
     ]
   }
   ```

2. **Create both language versions**: `filename.json` (Spanish) and `filename-en.json` (English)

3. **Follow naming conventions**: Use descriptive, kebab-case filenames

### Contribution Workflow

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-cheatsheet`
3. Add your changes and commit: `git commit -m "Add: New cheatsheet for XYZ"`
4. Push to your fork: `git push origin feature/new-cheatsheet`
5. Create a Pull Request

### Code Standards

- Follow existing JSON structure and formatting
- Ensure both English and Spanish versions are provided
- Add meaningful tags for categorization
- Include practical, working code examples
- Test your additions before submitting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors & Acknowledgments

- **NightWalkAX** - *Initial work and maintenance* - [jymendev@gmail.com](mailto:jymendev@gmail.com)

### Special Thanks

- Frappe Technologies for the excellent framework
- The open-source community for continuous inspiration
- All contributors who help improve this resource

## 📞 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/YOUR_USERNAME/doctyped_cheatsheets/issues)
- **Email**: [jymendev@gmail.com](mailto:jymendev@gmail.com)
- **Documentation**: [Frappe Framework Docs](https://frappeframework.com/docs)

---

<div align="center">
Made with ❤️ for the Frappe developer community
</div>
