// 'use strict'

// // https://nodejsdev.ru/doc/cluster/#nodejs

// const cluster = require('cluster');
// const numCPUs = require('os').cpus().length;

// const path = require('path')
// const AutoLoad = require('fastify-autoload')

// module.exports = async function (fastify, opts) {
//   // Place here your custom code!

//   // Do not touch the following lines

//   // This loads all plugins defined in plugins
//   // those should be support plugins that are reused
//   // through your application
//   fastify.register(AutoLoad, {
//     dir: path.join(__dirname, 'plugins'),
//     options: Object.assign({}, opts)
//   })

//   // This loads all plugins defined in routes
//   // define your routes in one of these
//   fastify.register(AutoLoad, {
//     dir: path.join(__dirname, 'routes'),
//     options: Object.assign({}, opts)
//   })

//   if (cluster.isMaster) {
//     for (let i = 0; i < numCPUs; i++) {
//       cluster.fork();
//     }
//   }

// }


'use strict'

const cluster = require('cluster');
const numCPUs = require('os').cpus().length;
const port = 3000;

module.exports = async function (fastify, opts) {

  fastify.get('/', async (request, reply) => {
    return { hello: 'world' }
  })

  // if (cluster.isMaster) {
  //   console.log(`Master ${process.pid} is running`);
  //   for (let i = 0; i < numCPUs; i++) {
  //     cluster.fork();
  //   }
  //   cluster.on('exit', worker => {
  //     console.log(`Worker ${worker.process.pid} died`);
  //   });
  // } else {
  //   console.log(`Child ${process.pid} is running`);
  //   fastify.get('/', (req, res) => {
  //     res.send('Hello World');
  //   });
  //   fastify.listen(port, () => {
  //     console.log(`Fastify "Hello World" listening on port ${port}, PID: ${process.pid}`);
  //   });
  // }
}


// const cluster = require('cluster');
// const numCPUs = require('os').cpus().length;
// const fastify = require('fastify')();
// const port = 8123;


// if (cluster.isMaster) {
//   console.log(`Master ${process.pid} is running`);
//   for (let i = 0; i < numCPUs; i++) {
//     cluster.fork();
//   }
//   cluster.on('exit', worker => {
//     console.log(`Worker ${worker.process.pid} died`);
//   });
// } else {
//   fastify.get('*', (req, res) => {
//     res.send('Hello World');
//   });
//   fastify.listen(port, () => {
//     console.log(`Fastify "Hello World" listening on port ${port}, PID: ${process.pid}`);
//   });
// }