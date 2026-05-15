# api/routes/health_routes.py

from app_context import repo
from api.response import success, error
from logger import log

def health_check(handler):
    try:
        # Check database connection
        db_ok = repo.check_health()

        if db_ok:
            success(handler, {"status": "ok", "database": "connected"})
        else:
            log.error("Health check failed: Database connection issue")
            handler.send_response(503)
            handler.send_header("Content-Type", "application/json")
            handler.end_headers()
            handler.wfile.write(b'{"success": false, "error": {"message": "Service Unavailable"}}')
            
    except Exception as e:
        log.error(f"Health check exception: {str(e)}")
        error(handler, "Internal Server Error", status=500)
