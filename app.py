from flask import Flask, request, jsonify, render_template
import copy
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  # Preserve dict order in JSON responses

# Comprehensive Career Roadmaps Database
CAREER_ROADMAPS = {
    'fullstack-dev': {
        'name': 'Fullstack Developer',
        'salary_range': '₹6-25 LPA (Freshers: ₹6-12L)',
        'technical': [
            'HTML/CSS/JavaScript (Essential)',
            'React.js / Next.js (Frontend)',
            'Node.js / Express.js (Backend)',
            'MongoDB / PostgreSQL (Database)',
            'Tailwind CSS / Bootstrap (Styling)',
            'Git & GitHub (Version Control)',
            'Docker Basics (Deployment)',
            'REST APIs & Authentication (JWT)'
        ],
        'tools': [
            'VS Code (Editor)',
            'Postman (API Testing)',
            'Vercel/Netlify/Render (Deploy)',
            'GitHub Copilot (AI Assistant)',
            'Figma (UI Design)'
        ],
        'soft_skills': [
            'Problem Solving (80% interviews)',
            'Communication (Client calls)',
            'Time Management (Deadlines)',
            'Learning Agility (New frameworks)'
        ],
        'daily_habits': [
            '2h coding practice daily',
            '1 LeetCode/Frontend Mentor problem',
            '30min docs reading (React/Node)',
            'Build 1 feature every weekend',
            'Deploy weekly to portfolio'
        ],
        'timeline': [
            'Month 1-2: HTML/CSS/JS + Tailwind',
            'Month 3-4: React + State Management',
            'Month 5-6: Node.js + Express APIs',
            'Month 7-8: Database + Authentication',
            'Month 9-10: Fullstack Projects',
            'Month 11-12: Portfolio + Freelance'
        ],
        'resources': [
            'freeCodeCamp (Frontend)',
            'The Odin Project (Fullstack)',
            'Net Ninja (React/Node YouTube)',
            'Build 3 projects: Todo, E-commerce, Chat app'
        ]
    },

    'ml-engineer': {
        'name': 'Machine Learning Engineer',
        'salary_range': '₹8-30 LPA (Freshers: ₹8-15L)',
        'technical': [
            'Python (Essential - 90% ML work)',
            'NumPy, Pandas, Matplotlib (Data)',
            'Scikit-learn (Classical ML)',
            'TensorFlow / PyTorch (Deep Learning)',
            'SQL (Data querying)',
            'Docker + MLflow (Production)',
            'Cloud: AWS/GCP/Azure ML',
            'Git + Jupyter Notebooks'
        ],
        'tools': [
            'Google Colab / Jupyter (Prototyping)',
            'VS Code + Jupyter extension',
            'Kaggle (Datasets/Competitions)',
            'Weights & Biases (Experiment tracking)'
        ],
        'soft_skills': [
            'Math intuition (Linear Algebra, Stats)',
            'Research mindset (Papers/Trends)',
            'Communication (Business impact)',
            'Experimentation (A/B testing)'
        ],
        'daily_habits': [
            '1h math/ML theory (3Blue1Brown)',
            '1 Kaggle dataset exploration',
            'Code 1 ML model daily',
            'Read 1 research paper/week',
            'Update GitHub weekly'
        ],
        'timeline': [
            'Month 1-2: Python + NumPy/Pandas',
            'Month 3-4: Scikit-learn + Projects',
            'Month 5-6: Deep Learning basics',
            'Month 7-8: TensorFlow/PyTorch',
            'Month 9-10: Kaggle competitions',
            'Month 11-12: Production ML projects'
        ],
        'resources': [
            'Andrew Ng Coursera (ML)',
            'Fast.ai (Practical DL)',
            'Kaggle Learn (Free courses)',
            'Build: Titanic, House Prices, Image classifier'
        ]
    },

    'data-analyst': {
        'name': 'Data Analyst',
        'salary_range': '₹5-18 LPA (Freshers: ₹5-10L)',
        'technical': [
            'Excel/Google Sheets (Advanced)',
            'SQL (Essential - 70% job)',
            'Python (Pandas, Matplotlib)',
            'Power BI / Tableau (Visualization)',
            'Google Data Studio/Looker',
            'Statistics basics',
            'ETL processes'
        ],
        'tools': [
            'Excel + Power Query',
            'PostgreSQL/MySQL (SQL)',
            'Power BI Desktop (Free)',
            'Google BigQuery (Free tier)'
        ],
        'soft_skills': [
            'Storytelling with data',
            'Business understanding',
            'Attention to detail',
            'Stakeholder communication'
        ],
        'daily_habits': [
            '30min SQL practice (LeetCode/HackerRank)',
            '1 dataset analysis daily',
            'Build 1 dashboard/week',
            'Read business metrics articles'
        ],
        'timeline': [
            'Month 1: Excel + SQL mastery',
            'Month 2-3: Python Pandas',
            'Month 4-5: Power BI/Tableau',
            'Month 6: Build portfolio dashboards',
            'Month 7-9: Case studies + SQL projects',
            'Month 10-12: Freelance analysis'
        ],
        'resources': [
            'Google Data Analytics Certificate',
            'SQLBolt (Free SQL)',
            'Alex The Analyst YouTube',
            'Build: Sales dashboard, COVID analysis'
        ]
    },

    'content-creator': {
        'name': 'Content Creator (YouTube/Instagram)',
        'salary_range': '₹3-50 LPA (Top 1%: ₹1Cr+)',
        'technical': [
            'Video Editing (Premiere/DaVinci Resolve)',
            'Thumbnail Design (Photoshop/Canva)',
            'SEO (TubeBuddy/VidIQ)',
            'Script Writing & Research',
            'Camera/Lighting basics',
            'Audio Editing (Audacity)',
            'Analytics (YouTube Studio)'
        ],
        'tools': [
            'DaVinci Resolve (Free editing)',
            'Canva Pro (Thumbnails)',
            'CapCut (Mobile editing)',
            'TubeBuddy (SEO)'
        ],
        'soft_skills': [
            'Consistency (80% success)',
            'Audience empathy',
            'Trend spotting',
            'Storytelling',
            'Resilience (Algorithm changes)'
        ],
        'daily_habits': [
            '1h content research',
            'Script 1 video daily',
            'Engage 30min with audience',
            'Analyze 3 competitor videos',
            'Post 3x/week minimum'
        ],
        'timeline': [
            'Month 1-2: Niche research + Equipment',
            'Month 3-4: 50 videos (Practice)',
            'Month 5-6: SEO + Thumbnails optimized',
            'Month 7-9: Consistent posting schedule',
            'Month 10-12: Monetization + Brand deals'
        ],
        'resources': [
            'Think Media (YouTube growth)',
            'Video Influencers (Strategy)',
            'Primal Video (Editing)',
            'Post daily Instagram Reels too'
        ]
    },

    'digital-marketing': {
        'name': 'Digital Marketing Specialist',
        'salary_range': '₹4-20 LPA (Freshers: ₹4-8L)',
        'technical': [
            'Google Analytics 4',
            'Google Ads / Meta Ads',
            'SEO (Ahrefs/SEMrush)',
            'Content Marketing',
            'Email Marketing (Mailchimp)',
            'Social Media Management',
            'WordPress/CMS'
        ],
        'tools': [
            'Google Analytics (Free)',
            'Google Tag Manager',
            'Canva (Social graphics)',
            'Buffer/Hootsuite (Scheduling)'
        ],
        'soft_skills': [
            'Creativity',
            'Data interpretation',
            'Copywriting',
            'Experimentation mindset'
        ],
        'daily_habits': [
            'Check campaign performance',
            'A/B test 1 element daily',
            'Read marketing case studies',
            'Create 1 piece of content'
        ],
        'timeline': [
            'Month 1-2: Google Analytics + Ads',
            'Month 3-4: SEO fundamentals',
            'Month 5-6: Social media mastery',
            'Month 7-9: Paid campaigns',
            'Month 10-12: Full campaigns + Portfolio'
        ],
        'resources': [
            'Google Skillshop (Free certs)',
            'HubSpot Academy',
            'Neil Patel blog'
        ]
    },

    'startup-founder': {
        'name': 'Startup Founder/Entrepreneur',
        'salary_range': '₹0-100Cr+ (High risk, high reward)',
        'technical': [
            'No-code tools (Bubble, Webflow)',
            'Basic MVP building',
            'Customer interviews',
            'Financial modeling (Excel)',
            'Pitch deck creation',
            'Product validation'
        ],
        'tools': [
            'Notion (Planning)',
            'Figma (Prototypes)',
            'Stripe (Payments)',
            'Google Workspace'
        ],
        'soft_skills': [
            'Resilience (95% fail)',
            'Customer obsession',
            'Sales & pitching',
            'Decision making under uncertainty'
        ],
        'daily_habits': [
            'Talk to 3 customers daily',
            'Validate 1 assumption',
            'Network 30min/day',
            'Track key metrics'
        ],
        'timeline': [
            'Month 1-3: Idea validation',
            'Month 4-6: MVP launch',
            'Month 7-9: First 100 customers',
            'Month 10-12: Revenue or pivot'
        ],
        'resources': [
            'Y Combinator Startup School',
            'The Mom Test (Customer interviews)',
            'Indie Hackers community'
        ]
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/roadmap', methods=['POST'])
def get_roadmap():
    try:
        # Validate request has JSON data
        if not request.is_json:
            return jsonify({
                'success': False,
                'error': 'Request must be JSON'
            }), 400
        
        data = request.json or {}
        
        # Input validation
        career = data.get('career', 'fullstack-dev')
        level = data.get('level', 'beginner')
        timeline = data.get('timeline', '12m')
        background = data.get('background', 'Not provided')
        
        # Validate career choice
        if career not in CAREER_ROADMAPS:
            logger.warning(f"Invalid career requested: {career}")
            career = 'fullstack-dev'  # Default fallback
        
        # Validate level
        valid_levels = ['beginner', 'intermediate', 'advanced']
        if level not in valid_levels:
            logger.warning(f"Invalid level requested: {level}")
            level = 'beginner'  # Default fallback
        
        # Create a deep copy to avoid mutating original data
        roadmap = copy.deepcopy(CAREER_ROADMAPS.get(career, CAREER_ROADMAPS['fullstack-dev']))
        
        # Customize based on level/timeline
        if level == 'beginner':
            roadmap['note'] = f"Perfect for {level}! Start from scratch."
        elif level == 'intermediate':
            roadmap['note'] = f"Great! {level} level - focus on advanced projects."
        else:
            roadmap['note'] = f"Advanced level detected. Ready for production work!"
        
        roadmap['customized_for'] = {
            'level': level,
            'timeline': timeline,
            'background': background[:500] if background else 'Not provided'  # Limit length
        }
        
        logger.info(f"Roadmap generated for career: {career}, level: {level}, timeline: {timeline}")
        
        return jsonify({
            'success': True,
            'roadmap': roadmap,
            'message': f"Complete roadmap for {roadmap['name']} generated!"
        })
    
    except KeyError as e:
        logger.error(f"Missing key in roadmap data: {e}")
        return jsonify({
            'success': False,
            'error': f'Data structure error: {str(e)}'
        }), 500
    except Exception as e:
        logger.error(f"Unexpected error in get_roadmap: {e}", exc_info=True)
        return jsonify({
            'success': False,
            'error': 'An unexpected error occurred. Please try again.'
        }), 500

@app.route('/api/careers', methods=['GET'])
def get_careers():
    """Get list of all available career paths"""
    try:
        careers = [
            {'id': k, 'name': v.get('name', 'Unknown'), 'salary': v.get('salary_range', 'N/A')} 
            for k, v in CAREER_ROADMAPS.items()
        ]
        return jsonify({
            'success': True,
            'careers': careers,
            'count': len(careers)
        })
    except Exception as e:
        logger.error(f"Error in get_careers: {e}", exc_info=True)
        return jsonify({
            'success': False,
            'error': 'Failed to retrieve careers'
        }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500

if __name__ == '__main__':
    # In production, set debug=False and use a production WSGI server
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
