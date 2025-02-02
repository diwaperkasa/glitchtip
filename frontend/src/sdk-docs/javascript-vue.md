To use GlitchTip with your Vue application, you will need to use the `@sentry/browser` SDK.

```bash
# Using yarn
$ yarn add @sentry/browser

# Using npm
$ npm install @sentry/browser
```

On its own, `@sentry/browser` will report any uncaught exceptions triggered by your application.

Additionally, the Vue _integration_ will capture the name and props state of the active component where the error was thrown. This is reported via Vue’s `config.errorHandler` hook.

Starting with version `5.x`, the `Vue` integration lives in the `@sentry/integrations` package.
You can install it with `npm` / `yarn`:

```bash
# Using yarn
yarn add @sentry/integrations

# Using npm
npm install @sentry/integrations
```

Then add this to your `app.js`:

```javascript
import Vue from "vue";
import * as Sentry from "@sentry/browser";
import * as Integrations from "@sentry/integrations";

Sentry.init({
  dsn: "YOUR-GLITCHTIP-DSN-HERE",
  integrations: [new Integrations.Vue({ Vue, attachProps: true })],
});
```

Additionally, `Integrations.Vue` accepts a few different configuration options that let you change its behavior:

- Passing in `Vue` is optional, if you do not pass it `window.Vue` must be present.
- Passing in `attachProps` is optional and is `true` if it is not provided. If you set it to `false`, the SDK will suppress sending all Vue components' props for logging.
- Passing in `logErrors` is optional and is `false` if it is not provided. If you set it to `true`, the SDK will call original Vue's `logError` function as well.

{% capture __alert %}
Please note that if you enable this integration, Vue will not call its `logError` internally. This means that errors occurring in the Vue renderer will not show up in the developer console.
If you want to preserve this functionality, make sure to pass the `logErrors: true` option.
{% endcapture %}

{% include components/alert.html
  title="Vue Error Handling"
  content=__alert
  level="warning"
%}

In case you are using the CDN version or the Loader, we provide a standalone file for every integration, you can use it
like this:

```html
<!-- Note that we now also provide a es6 build only -->
<!-- <script src="https://browser.sentry-cdn.com/5.27.6/bundle.es6.min.js" integrity="{% sdk_cdn_checksum sentry.javascript.browser latest bundle.es6.min.js %}" crossorigin="anonymous"></script> -->
<script src="https://browser.sentry-cdn.com/5.27.6/bundle.min.js"></script>

<!-- If you include the integration it will be available under Sentry.Integrations.Vue -->
<script src="https://browser.sentry-cdn.com/5.27.6/vue.min.js" crossorigin="anonymous"></script>

<script>
  Sentry.init({
    dsn: "YOUR-GLITCHTIP-DSN-HERE",
    integrations: [new Sentry.Integrations.Vue({ Vue, attachProps: true })],
  });
</script>
```
