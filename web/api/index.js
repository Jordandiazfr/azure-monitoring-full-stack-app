const express = require("express")
const app = express()
const PORT = 4000

app.get("/", (req,res) => {
    res.send("Test up")
})

app.listen(PORT, (req,res) => {
    console.log(`Server up and running in port: ${PORT}`)
})