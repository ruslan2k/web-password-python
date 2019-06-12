const express = require('express')
const dotenv = require('dotenv')
const path = require('path')
dotenv.config()
const app = express()

app.use(express.static(path.join(__dirname, '../client/build')))
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../client/build/index.html'))
})

const server = app.listen(process.env.PORT || 3000, () => {
  console.log('Listening on port: ' + server.address().port)
})
