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

SUCCESSFUL_REGISTERED_USER_SCHEME = {
    "type" : "object",
    "properties" : {
        "id" : {"type" : "number"},
        "token" : {"type" : "string"}
    },
    "requires" : ["id", "token"]
}

UNSUCCESSFUL_REGISTERED_USER_SCHEME = {
    "type" : "object",
    "properties" : {
        "error" : {"type" : "string"}
    },
    "requires" : ["error"]
}

SUCCESSFUL_LOGIN_USER_SCHEME = {
    "type" : "object",
    "properties" : {
        "token" : {"type" : "string"}
    },
    "requires" : ["token"]
}

UNSUCCESSFUL_LOGIN_USER_SCHEME = {
    "type" : "object",
    "properties" : {
        "error" : {"type" : "string"}
    },
    "requires" : ["error"]
}