#!/usr/bin/node
// A script that computes the number of tasks completed by user id
const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const users = {};
    todos.forEach((todo) => {
      if (todo.completed) {
        const userId = todo.userId;
        users[userId] = users[userId] ? users[userId] + 1 : 1;
      }
    });
    console.log(users);
  }
});
