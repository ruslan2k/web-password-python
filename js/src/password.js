const low = require('lowdb')
const FileSync = require('lowdb/adapters/FileSync')
const crypto = require('crypto')
const uuidv4 = require('uuid/v4');

const adapter = new FileSync('db.json')
const db = low(adapter)

// Set some defaults (required if your JSON file is empty)
db.defaults({ profiles: [], user: {}, count: 0 })
  .write()
// Add a post
// db.get('posts')
//   .push({ id: 1, title: 'lowdb is awesome'})
//   .write()
// Set a user using Lodash shorthand syntax
// var retVal = db.set('user.name', 'typicode')
//   .write()
// Increment count
// db.update('count', n => n + 1)
//   .write()

function createUserProfile (userId) {
  db.get('profiles')
    .push({ id: uuidv4(), userId: userId, salt: crypto.randomBytes(25).toString('HEX') })
    .write()
}
// Set a user using Lodash shorthand syntax

function addGroup (password) {

}

// console.log(CryptoJS.PBKDF2("password", "abc").toString())
// console.log(CryptoJS.HmacSHA1("Message", "Key").toString());
// console.log(typeof CryptoJS.HmacSHA1("Message", "Key"));
createUserProfile(1)
module.exports = {
  addGroup
}
