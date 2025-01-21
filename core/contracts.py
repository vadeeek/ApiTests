USER_DATA_SCHEME = {
    "type" : "object",
    "properties" : {
        "id" : {"type" : "number"},
        "email" : {"type" : "string"},
        "first_name" : {"type" : "string"},
        "last_name" : {"type" : "string"},
        "avatar" : {"type" : "string"}
    },
    "requires" : ["id", "email", "first_name", "last_name", "avatar"]
}

RESOURCE_DATA_SCHEME = {
    "type" : "object",
    "properties" : {
        "id" : {"type" : "number"},
        "name" : {"type" : "string"},
        "year" : {"type" : "number"},
        "color" : {"type" : "string"},
        "pantone_value" : {"type" : "string"}
    },
    "requires" : ["id", "name", "year", "color", "pantone_value"]
}

CREATED_USER_SCHEME = {
    "type" : "object",
    "properties" : {
        "name" : {"type" : "string"},
        "job" : {"type" : "string"},
        "id" : {"type" : "string"}
    },
    "requires" : ["id"]
}

UPDATED_USER_SCHEME = {
    "type" : "object",
    "properties" : {
        "name" : {"type" : "string"},
        "job" : {"type" : "string"}
    }
}