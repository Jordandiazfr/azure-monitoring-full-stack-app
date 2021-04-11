require('dotenv').config()
// console.log(process.env.DB_PASSWORD)
const Pool = require('pg').Pool



const pool = new Pool({
    host: 'spiderpostgres.postgres.database.azure.com',
    // Do not hard code your username and password.
    // Consider using Node environment variables.
    user: 'adminadmin@spiderpostgres',
    password: process.env.DB_PASSWORD,
    database: 'monitoring',
    port: 5432,
    ssl: true
})

const getServiceName = (request, response) => {
    pool.query('SELECT * FROM resource', (error, results) => {
        if (error) {
            throw error
        }
        response.status(200).json(results.rows)
    })
}

const getServiceById = (request, response) => {
    const id = parseInt(request.params.id)

    pool.query('SELECT * FROM resource WHERE id = $1', [id], (error, results) => {
        if (error) {
            throw error
        }
        response.status(200).json(results.rows)
    })
}

//post function

const createService = (request, response) => {
    const {
        date,
        servicename,
        serviceresource,
        quantity,
        cost
    } = request.body

    pool.query(`INSERT INTO resource (date, servicename,serviceresource, quantity, cost) VALUES ($1,$2,$3,$4,$5);`, [date, servicename, serviceresource, quantity, cost], (error, results) => {
        if (error) {
            throw error
        }
        response.status(201).send(`Service added`)
    })
}
const updateService = (request, response) => {
    const {
        date,
        servicename,
        serviceresource,
        quantity,
        cost
    } = request.body

    pool.query(
        'UPDATE resource SET date = $1, servicename = $2, serviceresource=$3, quantity = $4, cost =$5 WHERE id = $6', [date, servicename, serviceresource, quantity, cost],
        (error, results) => {
            if (error) {
                throw error
            }
            response.status(200).send(`Service modified with ID: ${id}`)
        }
    )
}
const deleteService = (request, response) => {
    const id = parseInt(request.params.id)
  
    pool.query('DELETE FROM resource WHERE id = $1', [id], (error, results) => {
      if (error) {
        throw error
      }
      response.status(200).send(`Service deleted with ID: ${id}`)
    })
  }

module.exports = {
    getServiceName,
    getServiceById,
    createService,
    updateService,
    deleteService
}

// CREATE TABLE resource (
//     ID SERIAL PRIMARY KEY,
//     date VARCHAR(30),
//     ServiceName VARCHAR(30),
//     ServiceResource VARCHAR(60),
//     quantity INT,
//     cost INT
//   );



// INSERT INTO resource (date, ServiceName,ServiceResource, quantity, cost) VALUES ('01/01/2021', 'SERVICE NAME 1', 'Service Resource 1',32,3098), ('01/01/2021', 'SERVICE NAME 2', 'Service Resource 2',32223322,12322);