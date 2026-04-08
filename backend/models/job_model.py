from ..utils.db_connection import get_db_connection
from datetime import datetime, timedelta

class JobModel:
    @staticmethod
    def seed_sample_jobs():
        conn = get_db_connection()
        try:
            # Check if jobs already exist
            count = conn.execute('SELECT COUNT(*) FROM jobs').fetchone()[0]
            if count > 0:
                print("Jobs already seeded.")
                return

            print("Seeding demo jobs with different expiry dates...")
            today = datetime.now()
            
            jobs_data = [
                # Active jobs
                ("Content Writing Intern", "Bright Future", "Writing", "Learn to write SEO optimized content for teen blogs.", "Online", "14-16", today, today + timedelta(days=10), True, "https://example.com/apply"),
                ("UI/UX Basics", "DesignStudio", "Design", "Assist in making wireframes for simple mobile screens.", "Online", "16+", today, today + timedelta(days=5), True, "https://example.com/apply"),
                ("Peer Math Tutor", "Local School Board", "Tutoring", "Help kids with primary school math.", "Offline", "16+", today, today + timedelta(days=15), True, "https://example.com/apply"),
                ("Python Scripting", "Tech Innovators", "Tech", "Write simple scripts for data automation.", "Online", "15+", today, today + timedelta(days=30), True, "https://example.com/apply"),
                
                # New Domains and College Links jobs
                ("Cybersecurity Analyst Intern", "CyberDefend", "Cyber", "Intro to network traffic analysis and basic penetration testing.", "Online", "16+", today, today + timedelta(days=45), True, "https://example-cyber.com/careers"),
                ("Frontend Developer Intern", "WebWorks", "Frontend Developer", "Build responsive UI components using HTML/CSS/JS.", "Online", "16+", today, today + timedelta(days=25), True, "https://example-frontend.com/interns"),
                ("Summer Web Intern", "Stanford Summer Research", "Summer Internships", "Contribute to open-source college projects over the summer.", "Online", "17+", today, today + timedelta(days=60), True, "https://summer.stanford.edu"),
                ("High School Scholars", "MIT Summer Program", "Summer Internships", "Intensive STEM and coding bootcamp.", "Offline", "15+", today, today + timedelta(days=50), True, "https://mit.edu/summer-programs"),

                # Expired job (should be filtered out by logically comparing current_date <= expiry_date)
                ("Past Event Coordinator", "Community Center", "Offline Jobs", "Help coordinate local fair events.", "Offline", "14+", today - timedelta(days=20), today - timedelta(days=2), True, "https://example.com/closed"),
                
                # Inactive job explicitly set to inactive
                ("Old Graphic Design", "ArtWorks", "Design", "Create banners (Project Closed).", "Online", "14+", today, today + timedelta(days=30), False, "https://example.com/closed")
            ]

            conn.executemany(
                'INSERT INTO jobs (title, company, domain, description, type, eligibility, posted_date, expiry_date, is_active, apply_link) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                [(title, company, domain, desc, type_, elig, posted.strftime('%Y-%m-%d'), expiry.strftime('%Y-%m-%d'), is_active, apply_link) for title, company, domain, desc, type_, elig, posted, expiry, is_active, apply_link in jobs_data]
            )
            conn.commit()
            print("Jobs seeded successfully.")
        except Exception as e:
            print(f"Error seeding jobs: {e}")
        finally:
            conn.close()

    @staticmethod
    def get_active_jobs(domain_filter=None):
        conn = get_db_connection()
        today_str = datetime.now().strftime('%Y-%m-%d')
        
        query = 'SELECT * FROM jobs WHERE is_active = 1 AND expiry_date >= ?'
        params = [today_str]
        
        if domain_filter:
            query += ' AND domain = ?'
            params.append(domain_filter)
            
        # Get active jobs ordered by expiry
        query += ' ORDER BY expiry_date ASC'
        
        jobs = conn.execute(query, params).fetchall()
        
        # Calculate days left
        results = []
        for job in jobs:
            job_dict = dict(job)
            expiry_date = datetime.strptime(job_dict['expiry_date'], '%Y-%m-%d')
            days_left = (expiry_date - datetime.now()).days
            
            # Format display
            if days_left > 0:
                job_dict['expires_in_display'] = f"Expires in {days_left} days"
            elif days_left == 0:
                job_dict['expires_in_display'] = "Closing Today"
            else:
                job_dict['expires_in_display'] = "Expired"
            
            job_dict['is_closing_soon'] = days_left <= 3
            results.append(job_dict)
            
        conn.close()
        return results

    @staticmethod
    def get_companies():
        return [
            {"name": "Zerodha", "industry": "Finance", "reason": "Great for learning stock markets", "link": "https://zerodha.com/careers"},
            {"name": "Razorpay", "industry": "Fintech", "reason": "Best in class payment industry exposure", "link": "https://razorpay.com/jobs/"},
            {"name": "Cred", "industry": "Fintech", "reason": "Fast paced environment to grow", "link": "https://careers.cred.club/"},
            {"name": "Stanford Summer Research", "industry": "Education", "reason": "Excellent pre-college experience", "link": "https://summer.stanford.edu"},
            {"name": "TCS", "industry": "Technology", "reason": "Industry standard training for youth", "link": "https://www.tcs.com/careers"}
        ]
