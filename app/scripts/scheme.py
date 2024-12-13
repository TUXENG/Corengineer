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

welcome_scheme = {
    "type": "object",
    "properties": {
        "welcome": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "image_bg": {"type": "string"},
                    "alt_bg": {"type": "string"},
                    "image_logo": {"type": "string"},
                    "alt_logo": {"type": "string"},
                    "description": {"type": "string"}
                },
                "required": 
                [
                    "image_bg", 
                    "alt_bg", 
                    "image_logo", 
                    "alt_logo", 
                    "description"                    
                ]
            }
        }
    },
    "required": ["welcome"]
}

info_scheme = {
    "type": "object",
    "properties": {
        "info": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "image": {"type": "string"},
                    "alt": {"type": "string"},
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "url": {"type": "string"}
                },
                "required": 
                [
                    "image", 
                    "alt", 
                    "title",
                    "description",
                    "url"
                ]
            }
        }
    },
    "required": ["info"]
}
