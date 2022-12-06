export default function createPushNotificationsJobs (jobs, queue) {
    if (!Array.isArray(jobs)) throw Error('Jobs is not an array');
    jobs.forEach((job) => createJob(job.phoneNumber, job.message, queue) )
}

function createJob (phoneNumber, message, queue) {
    const jobData = {
	    phoneNumber: phoneNumber,
	    message: message
    }

    const job = queue.create('push_notification_code_3', jobData);

    job.save();

    job.on('enqueue', function(id, type){
	console.log(`Notification job created: ${job.id}`);
    }).on('complete', function(result){
	console.log(`Notification job #${job.id} completed`);
    }).on('failed', function(errorMessage){
	console.log(`Notification job #${job.id} failed: ${errorMessage}`);
    }).on('progress', function(progress, data){
	console.log(`Notification job #${job.id} ${progress}% complete`);
    });
}