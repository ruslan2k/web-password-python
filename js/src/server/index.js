const express = require('express')
const dotenv = require('dotenv')
dotenv.config()
const app = express()

app.get('/', (req, res) => res.json({ ok: true }))

const server = app.listen(process.env.PORT || 3000, () => {
  console.log('Listening on port: ' + server.address().port)
})
