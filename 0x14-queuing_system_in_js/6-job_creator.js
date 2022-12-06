import kue from 'kue';
const queue = kue.createQueue();

const jobData = {
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account',
}

const job = queue.create('push_notification_code', jobData);

job.save();

job.on('enqueue', function(id, type){
    console.log(`Notification job created: ${job.id}`);
}).on('complete', function(result){
    console.log('Notification job completed');
}).on('failed', function(errorMessage){
    console.log('Notification job failed');
});