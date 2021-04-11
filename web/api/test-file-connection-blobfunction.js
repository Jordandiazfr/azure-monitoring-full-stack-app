// const pg = require('pg');


// module.exports = async function (context, myBlob) {

//     context.log('Start function!');

//     const config = {
//         host: 'spiderpostgres.postgres.database.azure.com',
//         // Do not hard code your username and password.
//         // Consider using Node environment variables.
//         user: 'adminadmin@spiderpostgres',
//         database: 'monitoring',
//         password: process.env["DB_PASSWORD"],
//         port: 5432,
//         ssl: true
//     };

//     const client = new pg.Client(config);
//     client.connect(err => {
//         if (err) throw err;
//         else {
//             queryDatabase();
//         }
//     });

//     function queryDatabase() {
//         const query = "INSERT INTO resource (date, ServiceName,ServiceResource, quantity, cost) VALUES ('01/01/2021', 'SERVICE NAME 3', 'Service Resource 3',32655353627,733663563533098);";
//         client
//             .query(query)
//             .then(() => {
//                 console.log('ok');
//                 client.end(console.log('Closed client connection'));
//             })
//             .catch(err => console.log(err))
//             .then(() => {
//                 console.log('Finished execution, exiting now');
//                 process.exit();
//             });
//     };
// }




// VERSION 1

const pg = require('pg');
require('dotenv').config()


// module.exports = async function (context, myBlob) {
    try {
        console.log('Start function!');

        const config = {
            host: 'spiderpostgres.postgres.database.azure.com',
            // Do not hard code your username and password.
            // Consider using Node environment variables.
            user: 'adminadmin@spiderpostgres',
            database: 'monitoring',
            password: process.env.DB_PASSWORD,
            port: 5432,
            ssl: true
        };

        const client = new pg.Client(config);
        const query = "INSERT INTO resource (date, ServiceName,ServiceResource, quantity, cost) VALUES ('01/01/2021', 'SERVICE NAME 3', 'Service Resource 3',2,1);";
        console.log(query);

        client.connect(err => {
            if (err) {
                console.log('connection error', err.stack);
            } else {
                console.log('connected');
                client.query(query, (err, res) => {
                    if (err) throw err;
                    console.log(res);
                    client.end();
                })
            }
        });

    } catch (e) {
        console.log(e);
    } finally {
        console.res = {
            status: 200,
            body: "ok"
        };
    }
// };