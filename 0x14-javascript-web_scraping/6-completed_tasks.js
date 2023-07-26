#!/usr/bin/node
// script that display the status code of a GET request.

const URL = process.argv[2];
const request = require('request');
request(URL, function (err, response, body) {
  if (!err && response.statusCode === 200) {
    const json = JSON.parse(body);
    const task = {};
    for (const x in json) {
      const data = json[x];
      if (data.completed === true) {
        const id = data.userId;
        if (id in task) {
          task[id]++;
        } else {
          task[id] = 1;
        }
      }
    }
    console.log(task);
  }
});
