import redis from "redis";
const client = redis.createClient();
const { promisify } = require("util");
const getAsync = promisify(client.get).bind(client);

client.on("connect", function() {
    console.log('Redis client connected to the server');
});

client.on("error", function(error) {
    console.log(`Redis client not connected to the server: ${error.toString()}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
    const res = await getAsync(schoolName);
    console.log(res);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');