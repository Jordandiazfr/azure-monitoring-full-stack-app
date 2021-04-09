const Pool = require('pg').Pool
const pool = new Pool({
    host: 'spiderpostgres.postgres.database.azure.com',
    // Do not hard code your username and password.
    // Consider using Node environment variables.
    user: 'adminadmin@spiderpostgres',     
    password: process.env.DB_PASSWORD,
    database: 'postgres',
    port: 5432,
    ssl: true
})