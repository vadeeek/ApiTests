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