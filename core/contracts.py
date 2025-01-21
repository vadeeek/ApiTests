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