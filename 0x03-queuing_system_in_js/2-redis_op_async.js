import redis from 'redis';
import { createClient } from 'redis';
const client = createClient();
const util = require('util');
const clientGet = util.promisify(client.get).bind(client);

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('ready', () => console.log('Redis client connected to the server'));

function setNewSchool (schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
	redis.print(`Reply: ${reply}`);
    });
}

async function displaySchoolValue(schoolName) {
    const value = await clientGet(schoolName);
    console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
