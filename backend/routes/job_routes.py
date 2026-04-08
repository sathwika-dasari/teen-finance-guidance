from flask import Blueprint, jsonify, request
from ..models.job_model import JobModel

job_bp = Blueprint('jobs', __name__)

@job_bp.route('/', methods=['GET'])
def get_jobs():
    domain_filter = request.args.get('domain')
    
    # Simple validation allowing only certain domains or fetch all if not provided
    valid_domains = ["Writing", "Design", "Tutoring", "Tech", "Offline Jobs", "Cyber", "Frontend Developer", "Summer Internships"]
    if domain_filter and domain_filter not in valid_domains:
        domain_filter = None 

    # Retrieve active jobs that are not expired from DB
    jobs = JobModel.get_active_jobs(domain_filter)
    companies = JobModel.get_companies()
    
    return jsonify({
        "status": "success",
        "jobs": jobs,
        "companies": companies
    }), 200
