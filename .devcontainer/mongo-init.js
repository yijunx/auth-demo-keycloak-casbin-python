// db.auth('admin', 'password')

// db = db.getSiblingDB('featurestore')

db.createUser(
    {
        user: "yijun",
        pwd: "password",
        roles: [
            {
                role: "readWrite",
                db: "featurestore" 
            }
        ]
    }
)
  