from fastapi import FastAPI
import psutil
import platform
import uvicorn
import time

app = FastAPI(title="RthOS-Pulse", description="AI Backend for RethoughtOS")

# System Health Endpoint
@app.get("/system/health")
def get_system_health():
    uptime_seconds = time.time() - psutil.boot_time()
    uptime = {
        "days": int(uptime_seconds // 86400),
        "hours": int((uptime_seconds % 86400) // 3600),
        "minutes": int((uptime_seconds % 3600) // 60),
        "seconds": int(uptime_seconds % 60)
    }
    
    return {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent,
        "uptime": uptime,
        "os": platform.system(),
        "os_version": platform.version()
    }

# Service Status Endpoint
@app.get("/service/status")
def service_status():
    return {"status": "RthOS-Pulse is running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
