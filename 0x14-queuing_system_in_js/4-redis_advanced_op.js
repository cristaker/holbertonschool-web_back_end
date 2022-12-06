import redis from "redis";
const client = redis.createClient();

const school = 'HolbertonSchools'
client.hset(school, "Portland", 50, redis.print);
client.hset(school, "Seattle", 80, redis.print);
client.hset(school, "New York", 20, redis.print);
client.hset(school, "Bogota", 20, redis.print);
client.hset(school, "Cali", 40, redis.print);
client.hset(school, "Paris", 2, redis.print);


client.hgetall(school, function(err, res) {
    console.log(res);
});