import redis from "redis";
const subscriber = redis.createClient();

subscriber.on("connect", function() {
    console.log('Redis client connected to the server');
});

subscriber.on("error", function(error) {
    console.log(`Redis client not connected to the server: ${error.toString()}`);
});

subscriber.subscribe("holberton school channel");

subscriber.on("message", function(channel, message) {
    if (channel === 'holberton school channel') {
	console.log(message);
	if (message === 'KILL_SERVER') {
	    subscriber.unsubscribe();
	    subscriber.quit();
	}
    }
});