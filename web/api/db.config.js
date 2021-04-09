require('dotenv').config()

const pg = require('pg');

const config = {
    host: 'spiderpostgres.postgres.database.azure.com',
    // Do not hard code your username and password.
    // Consider using Node environment variables.
    user: 'adminadmin@spiderpostgres',     
    password: process.env.DB_PASSWORD,
    database: 'postgres',
    port: 5432,
    ssl: true
};


const client = new pg.Client(config);

client.connect(err => {
    if (err) throw err;
    else {
        queryDatabase();
    }
});

function queryDatabase() {
    const query = `
    CREATE DATABASE api;
    `;

    client
        .query(query)
        .then(() => {
            console.log('Table created successfully!');
            client.end(console.log('Closed client connection'));
        })
        .catch(err => console.log(err))
        .then(() => {
            console.log('Finished execution, exiting now');
            process.exit();
        });
}

// psql --host=spiderpostgres.postgres.database.azure.com --port=5432 --username=adminadmin@spiderpostgres --dbname=postgres 
