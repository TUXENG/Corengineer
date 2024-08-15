course_scheme = {
    "type": "object",
    "properties": {
        "courses": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "image": {"type": "string"},
                    "alt": {"type": "string"},
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "state": {"type": "string"},
                    "cost": {"type": "string"}
                },
                "required": 
                [
                    "image", 
                    "alt", 
                    "title", 
                    "description", 
                    "state", 
                    "cost"
                ]
            }
        }
    },
    "required": ["courses"]
}

service_scheme = {
    "type": "object",
    "properties": {
        "services": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "image": {"type": "string"},
                    "alt": {"type": "string"},
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "state": {"type": "string"},
                    "personal": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                },
                "required": 
                [
                    "image", 
                    "alt", 
                    "title", 
                    "description", 
                    "state", 
                    "personal"
                ]
            }
        }
    },
    "required": ["services"]
}

profile_scheme = {
    "type": "object",
    "properties": {
        "profiles": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "image": {"type": "string"},
                    "alt": {"type": "string"},
                    "name": {"type": "string"},
                    "job_title": {"type": "string"},
                    "email": {"type": "string"},
                    "cel": {"type": "string"},
                    "description": {"type": "string"},
                    "linkedin": {"type": "string"},
                    "github": {"type": "string"}
                },
                "required": 
                [
                    "image", 
                    "alt", 
                    "name", 
                    "job_title", 
                    "email", 
                    "cel", 
                    "description", 
                    "linkedin", 
                    "github"
                ]
            }
        }
    },
    "required": ["profiles"]
}
