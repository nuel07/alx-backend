import redis from 'redis';
import { createClient } from 'redis';
const client = createClient();

client.on('error', (err) => console.log(`Redis client not connected to server: ${err}`));
client.on('ready', () => console.log('Redis client connected to the server'));

client.subscribe('holberton school channel');
client.on('message', (channel, msg) => {
    console.log(msg);
    if (msg === 'KILL_SERVER') {
	client.unsubscribe(channel);
	process.exit(0);
    }
});
