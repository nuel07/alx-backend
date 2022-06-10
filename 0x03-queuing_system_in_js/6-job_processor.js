const kue = require('kue');
const queue = kue.createQueue();

const jobData = {
    phoneNumber: '256783195776',
    message: 'message received'
}

const sendNotification = (phoneNumber, message) => {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
});
