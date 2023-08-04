var rootDBUser = process.env["NOTIF_MONGO_INITDB_ROOT_USERNAME"];
var rootDBPassword = process.env["NOTIF_MONGO_INITDB_ROOT_PASSWORD"];
var dbPassword = process.env["NOTIF_DBPASSWORD"];
var dbUser = process.env["NOTIF_DBUSER"];
var dbName = process.env["NOTIF_DBNAME"];

db.auth(rootDBUser, rootDBPassword);

db = db.getSiblingDB(dbName);

db.createUser({
  user: dbUser,
  pwd: dbPassword,
  roles: [{ role: "dbOwner", db: dbName }],
});
