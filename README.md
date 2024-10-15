# PCAP Analyzer Web Application

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-1.1.2-green.svg)](https://flask.palletsprojects.com/)
[![PyShark](https://img.shields.io/badge/PyShark-0.4.2.9-yellow.svg)](https://kiminewt.github.io/pyshark/)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The **PCAP Analyzer Web Application** is a powerful and user-friendly tool designed for network analysts, security professionals, and enthusiasts. It allows users to upload PCAP files for detailed analysis, providing insights through summaries and interactive data.

A video showing the demo of the application is available here:

[![Video](tests/main.png)](https://github.com/muhammadov-q/PortScanDetect/tests/demo-video.mp4)


## Features

- **User-Friendly Interface**: Modern and responsive design.
- **Advanced PCAP Analysis**:
  - Detects different types of TCP scans: Null, Xmas, Half-Open.
  - Identifies UDP scans using ICMP Port Unreachable messages.
  - Tracks ICMP Echo Requests.
- **Interactive Visualization**:
  - Protocol distribution.
  - Source and destination IP analysis.
  - Detailed packet information.
- **Enhanced UI/UX**:
  - **Drag-and-Drop File Upload**: Easily upload files by dragging them onto the upload area.
  - **Progress Bar**: Visual feedback during file uploads.
  - **Dark Mode**: Toggle between light and dark themes.
  - **Breadcrumb Navigation**: Navigate through the app effortlessly.
- **Security**:
  - Validates uploaded files.
  - Secure file handling with unique filenames.
- **Extensibility**: Modular codebase allowing for easy feature additions.

## Installation

### Prerequisites

- **Python 3.6+**
- **pip** (Python package installer)
- **tshark** (Part of Wireshark)

### Install Python Packages

```bash
pip install -r requirements.txt
```

*Alternatively, manually install the packages:*

```bash
pip install flask pyshark werkzeug
```

### Install tshark

- **Windows**: Download and install [Wireshark](https://www.wireshark.org/download.html).
- **macOS**:

  ```bash
  brew install wireshark
  ```

- **Linux**:

  ```bash
  sudo apt-get install wireshark
  ```

**Note**: Ensure `tshark` is added to your system's PATH.

## Usage

### Running the Application

```bash
python app.py
```

**Note**: For production, use a WSGI server like Gunicorn or uWSGI.

### Accessing the Application

Open your web browser and navigate to:

```
http://localhost:5001
```

### Uploading and Analyzing a PCAP File

1. **Upload**: Click on "Select PCAP File" or drag and drop your file into the upload area.
2. **Analyze**: The application will process the file and redirect you to the results page.
3. **View Results**:
   - **Scan Summary**: Shows results of various scans and analysis types.
   - **Interactive Data**: Visualize protocol distribution and IP frequencies.
4. **Switch Theme**: Use the toggle switch to switch between light and dark modes.

## File Structure

```
pcap-analyzer-web/
│
├── app.py
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── upload.html
│   └── results.html
├── static/
│   ├── css/
│   │   ├── styles.css
│   │   └── dark_mode.css
│   ├── js/
│   │   └── main.js
├── uploads/
│   └── (Uploaded files stored here)
└── README.md
```

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**.
2. **Create a new branch** for your feature or bug fix:

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Commit your changes**:

   ```bash
   git commit -am 'Add new feature'
   ```

4. **Push to the branch**:

   ```bash
   git push origin feature/YourFeatureName
   ```

5. **Open a Pull Request**.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **GitHub**: [YourUsername](https://github.com/YourUsername)
- **Email**: [your.email@example.com](mailto:your.email@example.com)
- **LinkedIn**: [Your Name](https://www.linkedin.com/in/yourprofile/)

---

*Developed with ❤️ by [Your Name](https://github.com/YourUsername)*

## Advanced Features

### Drag-and-Drop File Upload

- **Implementation**: Users can drag files onto the designated area, which highlights upon file hover.
- **Fallback**: For browsers that don't support drag-and-drop, users can click to select files.

### Upload Progress Bar

- **Functionality**: Visual feedback during file upload, showing percentage completion.
- **Technical Details**: Utilizes the `XMLHttpRequest` API's `progress` event.

### Dark Mode Toggle

- **User Preference**: Allows users to switch between light and dark themes.
- **Persistence**: User preference is saved in `localStorage` and applied on subsequent visits.
- **Accessibility**: Improves readability in low-light conditions.

### Breadcrumb Navigation

- **Purpose**: Enhances navigation by showing the user's current position within the app.
- **Implementation**: Uses Bootstrap's breadcrumb component.

### Interactive Charts

- **Libraries Used**: [Chart.js](https://www.chartjs.org/) for rendering charts.
- **Charts Included**:
  - **Protocol Distribution**: Pie chart showing the percentage of each protocol.
  - **Source IP Frequencies**: Bar chart displaying the number of packets from each source IP.

### DataTables Integration

- **Functionality**: Enhances the packet details table with features like pagination, searching, and sorting.
- **Implementation**: Utilizes [DataTables](https://datatables.net/) jQuery plugin.

## Code Highlights

### `app.py`

- **Flask Application**: Serves as the backend, handling routes and file processing.
- **PCAP Analysis**: Uses PyShark to read and analyze the uploaded PCAP files.
- **Security Measures**:
  - File validation to prevent malicious uploads.
  - Unique filenames to prevent overwriting.

### Templates

- **`base.html`**:
  - Base template that includes common elements like the navbar, footer, and scripts.
  - Uses Bootstrap for styling and responsiveness.
- **`upload.html`**:
  - Inherits from `base.html`.
  - Contains the file upload form and drag-and-drop area.
- **`results.html`**:
  - Displays the analysis results with charts and tables.
  - Includes scripts to render charts using data passed from the backend.

### Static Files

- **Stylesheets**:
  - **`styles.css`**: Custom styles for the application.
  - **`dark_mode.css`**: Styles applied when dark mode is enabled.
- **JavaScript**:
  - **`main.js`**: Contains scripts for theme switching and other interactive features.

## Extensibility

The application's modular structure allows for easy addition of new features, such as:

- **Additional Charts**: Visualize more aspects of the data, like destination IPs or port usage.
- **User Authentication**: Implement login functionality for user-specific analysis history.
- **Database Integration**: Store analysis results for future reference or aggregation.

## Best Practices

- **Code Organization**: Separates concerns by dividing code into routes, templates, and static files.
- **Error Handling**: Provides user feedback for common errors, enhancing user experience.
- **Resource Management**: Properly closes file handles and captures to free up resources.
- **Security**: Implements basic security measures, with recommendations for production readiness.

## Feedback and Support

If you encounter any issues or have suggestions for improvement, please open an issue on the GitHub repository or contact me directly.

---

*This README was generated to provide a comprehensive guide to the PCAP Analyzer Web Application, showcasing its features, usage, and development details to enhance user understanding and encourage contributions.*