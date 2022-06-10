import redis from 'redis';
import { createClient } from 'redis';
const client = createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('ready', () => console.log('Redis client connected to the server'));

function setNewSchool (schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
	redis.print(`Reply: ${reply}`)
    });
}

function displaySchoolValue (schoolName) {
    client.get(schoolName, (err, reply) => {
	console.log(reply);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
