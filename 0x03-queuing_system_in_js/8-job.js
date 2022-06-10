const kue = require('kue');
const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
	throw new Error ('Jobs is not an array');
    }

    jobs.forEach((theJob) => {
	let job = queue.crate('push_notification_code_3', theJob);
	job.on('complete', () => console.log(`Notification job ${job.id} completed`));
	job.on('failed', (error) => console.log(`Notification job ${job.id} failed: ${error}`));
	job.on('progress', (progress, data) => console.log(`Notification job ${job.id} ${progress}% complete`));
	job.save((error) => {
	    if (!error) console.log(`Notification job created: ${job.id}`);
	});
    });
}

module.exports = createPushNotificationsJobs;
