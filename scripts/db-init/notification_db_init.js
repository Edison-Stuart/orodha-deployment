var rootDBUser = process.env["MONGO_INITDB_ROOT_USERNAME"];
var rootDBPassword = process.env["MONGO_INITDB_ROOT_PASSWORD"];
var dbPassword = process.env["NOTIFICATION_DBPASSWORD"];
var dbUser = process.env["NOTIFICATION_DBUSER"];
var dbName = process.env["NOTIFICATION_DBNAME"];

db.auth(rootDBUser, rootDBPassword);

db = db.getSiblingDB(dbName);

db.createUser({
  user: dbUser,
  pwd: dbPassword,
  roles: [{ role: "dbOwner", db: dbName }],
});
