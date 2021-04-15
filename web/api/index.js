const express = require("express")
const bodyParser = require('body-parser')
const app = express()
const PORT = 4000
const db = require('./pool')
// const cors = require('cors')

// app.use(cors())
app.use(bodyParser.json())
app.use(
  bodyParser.urlencoded({
    extended: true,
  })
)


app.get('/servicename', db.getServiceName)

app.get('/servicename/:id', db.getServiceById)
console.log(db.getServiceById);

app.post('/servicename', db.createService)
app.put('/servicename/:id', db.updateService)
app.delete('/servicename/:id', db.deleteService)



app.get('/', (request, response) => {
    response.json({ info: 'Node.js, Express, and Postgres API' })
  })

app.listen(PORT, (req,res) => {
    console.log(`Server up and running in port: ${PORT}`)
})

