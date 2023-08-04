var rootDBUser = process.env["LIST_MONGO_INITDB_ROOT_USERNAME"];
var rootDBPassword = process.env["LIST_MONGO_INITDB_ROOT_PASSWORD"];
var dbPassword = process.env["LIST_DBPASSWORD"];
var dbUser = process.env["LIST_DBUSER"];
var dbName = process.env["LIST_DBNAME"];

db.auth(rootDBUser, rootDBPassword);

db = db.getSiblingDB(dbName);

db.createUser({
  user: dbUser,
  pwd: dbPassword,
  roles: [{ role: "dbOwner", db: dbName }],
});
