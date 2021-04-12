require('dotenv').config()

const pg = require('pg');


const config = {
    host: process.env.PSQL_HOST,
    user: process.env.PSQL_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.PSQL_DATABASE,
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


