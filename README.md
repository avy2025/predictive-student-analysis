# Predictive Student Analysis - Career Roadmap Generator

## **Overview**
A modern web application that generates comprehensive career roadmaps for students and career switchers. Select your target career field, experience level, and timeline to get a complete breakdown of technical skills, tools, soft skills, daily habits, and a 12-month learning timeline.

Built with Flask (Python) backend and a beautiful, responsive frontend using Tailwind CSS.

---

## **Features**
1. **6 Career Paths**: Fullstack Developer, ML Engineer, Data Analyst, Content Creator, Digital Marketing, Startup Founder
2. **Complete Skill Breakdowns**: 
   - Technical skills and technologies
   - Essential tools and software
   - Soft skills required
   - Daily habits for success
   - 12-month learning timeline
   - Recommended resources
3. **Customizable Roadmaps**: Based on experience level (Beginner/Intermediate/Advanced) and timeline goals
4. **Modern UI**: Dark theme with smooth animations and responsive design
5. **Real-time Results**: Beautifully formatted roadmap display with all details

---

## **Technology Stack**
- **Backend**: Flask 3.0+ (Python)
- **Frontend**: HTML5, JavaScript (ES6+), Tailwind CSS
- **Styling**: Tailwind CSS (CDN) with custom dark theme

---

## **Project Structure**
```
predictive-student-analysis/
├── app.py                # Flask backend with career roadmaps database
├── templates/
│   └── index.html         # Main frontend HTML file
├── requirements.txt       # Python dependencies
├── run.bat               # Windows startup script
├── run.sh                # Linux/Mac startup script
└── README.md             # This file
```

---

## **Installation & Setup**

### **Prerequisites**
1. Python 3.8 or higher
2. pip (Python package manager)

### **Quick Start**

1. **Navigate to the project directory:**
   ```bash
   cd predictive-student-analysis
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   
   **Windows:**
   ```bash
   python app.py
   ```
   Or double-click `run.bat`
   
   **Linux/Mac:**
   ```bash
   python app.py
   ```
   Or run `./run.sh` (make it executable first: `chmod +x run.sh`)

4. **Open your browser:**
   ```
   http://localhost:5000
   ```

---

## **How to Use**

1. **Select Your Career**: Choose from 6 available career paths
2. **Set Your Level**: Select your current experience level (Beginner/Intermediate/Advanced)
3. **Choose Timeline**: Pick your target timeline (3 months, 6 months, 12 months, or 2 years)
4. **Add Background** (Optional): Describe your current skills or background
5. **Generate Roadmap**: Click the button to get your complete career roadmap
6. **Review Results**: Scroll through your personalized roadmap with all skills, tools, habits, and timeline

---

## **API Endpoints**

### `GET /`
Serves the main webpage.

### `POST /api/roadmap`
Generates a career roadmap based on user input.

**Request Body:**
```json
{
  "career": "fullstack-dev",
  "level": "beginner",
  "timeline": "12m",
  "background": "Know basic Python"
}
```

**Response:**
```json
{
  "success": true,
  "roadmap": {
    "name": "Fullstack Developer",
    "salary_range": "₹6-25 LPA (Freshers: ₹6-12L)",
    "technical": [...],
    "tools": [...],
    "soft_skills": [...],
    "daily_habits": [...],
    "timeline": [...],
    "resources": [...]
  },
  "message": "Complete roadmap for Fullstack Developer generated!"
}
```

### `GET /api/careers`
Returns a list of all available careers.

---

## **Available Career Paths**

1. **Fullstack Developer** - React, Node.js, MongoDB, PostgreSQL
2. **ML Engineer** - Python, TensorFlow, PyTorch, Data Science
3. **Data Analyst** - SQL, Power BI, Tableau, Excel
4. **Content Creator** - YouTube, Instagram, Video Editing, SEO
5. **Digital Marketing** - Google Analytics, SEO, Social Media
6. **Startup Founder** - Entrepreneurship, MVP Building, Customer Validation

---

## **Development**

### **Running in Development Mode**
The app runs with `debug=True` by default, which enables:
- Auto-reload on code changes
- Detailed error messages
- Debug mode

### **Customization**
- **Add New Careers**: Edit the `CAREER_ROADMAPS` dictionary in `app.py`
- **Modify UI**: Edit `templates/index.html` (uses Tailwind CSS)
- **Change Styling**: Modify Tailwind config in the HTML head section

---

## **Troubleshooting**

### **Port Already in Use**
If port 5000 is already in use, modify `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change port number
```

### **Module Not Found Error**
Make sure Flask is installed:
```bash
pip install Flask>=3.0.0
```

### **Template Not Found**
Ensure `templates/index.html` exists in the correct location.

---

## **Future Enhancements**
- [ ] Add more career paths
- [ ] User authentication and saved roadmaps
- [ ] Export roadmap as PDF
- [ ] Progress tracking
- [ ] Integration with learning platforms
- [ ] Database for dynamic career data

---

## **License**
This project is open source and available for educational purposes.

---

## **Support**
For issues or questions, please check the code comments or create an issue in the repository.

**Happy Learning! 🚀**
