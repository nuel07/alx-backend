import redis from 'redis';
import { createClient } from 'redis';
const client = createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('ready', () => console.log('Redis client connected to the server'));

const the_key = 'HolbertonSchools';
const the_values = {
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2
}
for (const [key, value] of Object.entries(the_values)) {
    client.hset(the_key, key, value, (error, reply) => {
	redis.print(`Reply: ${reply}`);
    });
}
client.hgetall(the_key, (error, object) => console.log(object));
