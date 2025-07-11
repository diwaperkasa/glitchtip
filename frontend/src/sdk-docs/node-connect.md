Use `yarn` or `npm` to add `@sentry/node` to your project:

```bash
# Using yarn
$ yarn add @sentry/node

# Using npm
$ npm install @sentry/node
```

```javascript
const connect = require("connect");
const Sentry = require("@sentry/node");

// Must configure Sentry before doing anything else with it
Sentry.init({ dsn: "YOUR-GLITCHTIP-DSN-HERE" });

function mainHandler(req, res) {
  throw new Error("My first GlitchTip error!");
}

function onError(err, req, res, next) {
  // The error id is attached to `res.sentry` to be returned
  // and optionally displayed to the user for support.
  res.statusCode = 500;
  res.end(res.sentry + "\n");
}

connect(
  // The request handler be the first item
  Sentry.handlers.requestHandler(),

  connect.bodyParser(),
  connect.cookieParser(),
  mainHandler,

  // The error handler must be before any other error middleware
  Sentry.handlers.errorHandler(),

  // Optional fallthrough error handler
  onError,
).listen(3000);
```

`requestHandler` accepts some options that let you decide what data should be included in the event sent to GlitchTip.

Possible options are:

```js
// keys to be extracted from req
request?: boolean | string[]; // default: true = ['cookies', 'data', 'headers', 'method', 'query_string', 'url']
// server name
serverName?: boolean; // default: true
// generate transaction name
//   path == request.path (eg. "/foo")
//   methodPath == request.method + request.path (eg. "GET|/foo")
//   handler == function name (eg. "fooHandler")
transaction?: boolean | 'path' | 'methodPath' | 'handler'; // default: true = 'methodPath'
// keys to be extracted from req.user
user?: boolean | string[]; // default: true = ['id', 'username', 'email']
// node version
version?: boolean; // default: true
// timeout for fatal route errors to be delivered
flushTimeout?: number; // default: 2000
```

For example, if you want to skip the server name and add just user, you would use `requestHandler` like this:

```js
app.use(
  Sentry.handlers.requestHandler({
    serverName: false,
    user: ["email"],
  }),
);
```

By default, `errorHandler` will capture only errors with a status code of `500` or higher. If you want to change it, provide it with the `shouldHandleError` callback, which accepts middleware errors as its argument and decides, whether an error should be sent or not, by returning an appropriate boolean value.

```js
app.use(
  Sentry.handlers.errorHandler({
    shouldHandleError(error) {
      // Capture all 404 and 500 errors
      if (error.status === 404 || error.status === 500) {
        return true;
      }
      return false;
    },
  }),
);
```
