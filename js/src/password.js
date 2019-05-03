const low = require('lowdb')
const FileSync = require('lowdb/adapters/FileSync')
const crypto = require('crypto')
const uuidv4 = require('uuid/v4');

const adapter = new FileSync('db.json')
const db = low(adapter)

// Set some defaults (required if your JSON file is empty)
db.defaults({ profiles: [], user: {}})
  .write()

function createUserProfile (userId, password) {
  const salt = crypto.randomBytes(32).toString('HEX')
  const key = crypto.pbkdf2Sync(password, salt, 1000, 32, 'sha512')
  const profileId = uuidv4()
  const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
    modulusLength: 4096,
    publicKeyEncoding: {
      type: 'spki',
      format: 'pem'
    },
    privateKeyEncoding: {
      type: 'pkcs8',
      format: 'pem',
      cipher: 'aes-256-cbc',
      passphrase: key.toString('hex')
    }
  });
  db.get('profiles')
    .push({
      id: profileId,
      userId: userId,
      salt: salt,
      publicKey: publicKey,
      encryptedPrivateKey: privateKey,
    })
    .write()
  return profileId
}

// function createPasswordForPrivateKey (password
// Set a user using Lodash shorthand syntax

function addGroup (password) {

}

// console.log(CryptoJS.PBKDF2("password", "abc").toString())
// console.log(CryptoJS.HmacSHA1("Message", "Key").toString());
// console.log(typeof CryptoJS.HmacSHA1("Message", "Key"));
const profileId = createUserProfile(1, 'p@$$W0rD')
const profile = db.get('profiles').find({ id: profileId }).value()
console.log(profile)

module.exports = {
  addGroup
}
