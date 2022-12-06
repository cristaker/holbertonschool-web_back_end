import kue from 'kue';
import {expect, assert} from 'chai';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

before(function() {
    queue.testMode.enter();
});
  
afterEach(function() {
    queue.testMode.clear();
});
  
after(function() {
    queue.testMode.exit()
});
  
it('display a error message if jobs is not an array', function() {
    expect(() => createPushNotificationsJobs(undefined, queue)).to.throw(Error, 'Jobs is not an array');
});

it('create two new jobs to the queue', function() {
    const list = [
        {
            phoneNumber: '4153518780',
            message: 'This is the code 1234 to verify your account'
        },
        {
            phoneNumber: '4153518780',
            message: 'This is the code 1234 to verify your account'
        }
    ];
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
});

it('create new job of type "push_notification_code_3"', function() {
    const list = [
        {
            phoneNumber: '4153518780',
            message: 'This is the code 1234 to verify your account'
        }
    ];
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
});

it('create new job with data', function() {
    const list = [
        {
            phoneNumber: '4153518780',
            message: 'This is the code 1234 to verify your account'
        }
    ];
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs[0].data).to.eql(list[0]);
});