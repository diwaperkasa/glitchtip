export const noReverseMatch = {
  level: "error",
  exception: {
    values: [
      {
        module: "django.urls.exceptions",
        type: "NoReverseMatch",
        value:
          "Reverse for 'nope' not found. 'nope' is not a valid view function or pattern name.",
        mechanism: {
          type: "django",
          handled: false,
        },
        stacktrace: {
          frames: [
            {
              filename: "django/core/handlers/exception.py",
              abs_path:
                "/usr/local/lib/python3.8/site-packages/django/core/handlers/exception.py",
              function: "inner",
              module: "django.core.handlers.exception",
              lineno: 34,
              pre_context: [
                "    can rely on getting a response instead of an exception.",
                '    """',
                "    @wraps(get_response)",
                "    def inner(request):",
                "        try:",
              ],
              context_line: "            response = get_response(request)",
              post_context: [
                "        except Exception as exc:",
                "            response = response_for_exception(request, exc)",
                "        return response",
                "    return inner",
                "",
              ],
              vars: {
                request: "<WSGIRequest: GET '/template-error/'>",
                exc: "NoReverseMatch(\"Reverse for 'nope' not found. 'nope' is not a valid view function or pattern name.\")",
                get_response:
                  "<bound method BaseHandler._get_response of <django.core.handlers.wsgi.WSGIHandler object at 0x7fc14cb6efa0>>",
              },
            },
            {
              filename: "django/core/handlers/base.py",
              abs_path:
                "/usr/local/lib/python3.8/site-packages/django/core/handlers/base.py",
              function: "_get_response",
              module: "django.core.handlers.base",
              lineno: 145,
              pre_context: [
                "                    )",
                "",
                "            try:",
                "                response = response.render()",
                "            except Exception as e:",
              ],
              context_line:
                "                response = self.process_exception_by_middleware(e, request)",
              post_context: [
                "",
                "        return response",
                "",
                "    def process_exception_by_middleware(self, exception, request):",
                '        """',
              ],
              vars: {
                self: "<django.core.handlers.wsgi.WSGIHandler object at 0x7fc14cb6efa0>",
                request: "<WSGIRequest: GET '/template-error/'>",
                response:
                  '<TemplateResponse status_code=200, "text/html; charset=utf-8">',
                resolver:
                  "<URLResolver 'django_error_factory.urls' (None:None) '^/'>",
                resolver_match:
                  "ResolverMatch(func=errors.views.TemplateErrorView, args=(), kwargs={}, url_name=template_error, app_names=[], namespaces=[], route=template-error/)",
                callback: "<function TemplateErrorView at 0x7fc14c63f940>",
                callback_args: [],
                callback_kwargs: {},
                middleware_method:
                  "<function CsrfViewMiddleware.process_view at 0x7fc14bc8ce50>",
                wrapped_callback:
                  "<function TemplateErrorView at 0x7fc14c63f940>",
              },
            },
            {
              filename: "django/core/handlers/base.py",
              abs_path:
                "/usr/local/lib/python3.8/site-packages/django/core/handlers/base.py",
              function: "_get_response",
              module: "django.core.handlers.base",
              lineno: 143,
              pre_context: [
                '                        "HttpResponse object. It returned None instead."',
                "                        % (middleware_method.__self__.__class__.__name__)",
                "                    )",
                "",
                "            try:",
              ],
              context_line: "                response = response.render()",
              post_context: [
                "            except Exception as e:",
                "                response = self.process_exception_by_middleware(e, request)",
                "",
                "        return response",
                "",
              ],
              vars: {
                self: "<django.core.handlers.wsgi.WSGIHandler object at 0x7fc14cb6efa0>",
                request: "<WSGIRequest: GET '/template-error/'>",
                response:
                  '<TemplateResponse status_code=200, "text/html; charset=utf-8">',
                resolver:
                  "<URLResolver 'django_error_factory.urls' (None:None) '^/'>",
                resolver_match:
                  "ResolverMatch(func=errors.views.TemplateErrorView, args=(), kwargs={}, url_name=template_error, app_names=[], namespaces=[], route=template-error/)",
                callback: "<function TemplateErrorView at 0x7fc14c63f940>",
                callback_args: [],
                callback_kwargs: {},
                middleware_method:
                  "<function CsrfViewMiddleware.process_view at 0x7fc14bc8ce50>",
                wrapped_callback:
                  "<function TemplateErrorView at 0x7fc14c63f940>",
              },
            },
            {
              filename: "django/template/response.py",
              abs_path:
                "/usr/local/lib/python3.8/site-packages/django/template/response.py",
              function: "render",
              module: "django.template.response",
              lineno: 105,
              pre_context: [
                "",
                "        Return the baked response instance.",
                '        """',
                "        retval = self",
                "        if not self._is_rendered:",
              ],
              context_line: "            self.content = self.rendered_content",
              post_context: [
                "            for post_callback in self._post_render_callbacks:",
                "                newretval = post_callback(retval)",
                "                if newretval is not None:",
                "                    retval = newretval",
                "        return retval",
              ],
              vars: {
                self: '<TemplateResponse status_code=200, "text/html; charset=utf-8">',
                retval:
                  '<TemplateResponse status_code=200, "text/html; charset=utf-8">',
              },
            },
            {
              filename: "django/urls/base.py",
              abs_path:
                "/usr/local/lib/python3.8/site-packages/django/urls/base.py",
              function: "reverse",
              module: "django.urls.base",
              lineno: 87,
              pre_context: [
                "                else:",
                '                    raise NoReverseMatch("%s is not a registered namespace" % key)',
                "        if ns_pattern:",
                "            resolver = get_ns_resolver(ns_pattern, resolver, tuple(ns_converters.items()))",
                "",
              ],
              context_line:
                "    return iri_to_uri(resolver._reverse_with_prefix(view, prefix, *args, **kwargs))",
              post_context: [
                "",
                "",
                "reverse_lazy = lazy(reverse, str)",
                "",
                "",
              ],
              vars: {
                viewname: "'nope'",
                urlconf: "'django_error_factory.urls'",
                args: [],
                kwargs: {},
                current_app: "''",
                resolver:
                  "<URLResolver 'django_error_factory.urls' (None:None) '^/'>",
                prefix: "'/'",
                view: "'nope'",
                path: [],
                current_path: "None",
              },
            },
            {
              filename: "django/urls/resolvers.py",
              abs_path:
                "/usr/local/lib/python3.8/site-packages/django/urls/resolvers.py",
              function: "_reverse_with_prefix",
              module: "django.urls.resolvers",
              lineno: 677,
              pre_context: [
                "        else:",
                "            msg = (",
                "                \"Reverse for '%(view)s' not found. '%(view)s' is not \"",
                "                \"a valid view function or pattern name.\" % {'view': lookup_view_s}",
                "            )",
              ],
              context_line: "        raise NoReverseMatch(msg)",
              post_context: [],
              vars: {
                self: "<URLResolver 'django_error_factory.urls' (None:None) '^/'>",
                lookup_view: "'nope'",
                _prefix: "'/'",
                args: [],
                possibilities: [],
                m: "None",
                n: "None",
                lookup_view_s: "'nope'",
                patterns: [],
                msg: "\"Reverse for 'nope' not found. 'nope' is not a valid view function or pattern name.\"",
              },
            },
          ],
        },
      },
    ],
  },
  event_id: "3e7c1345914d4924926d795ade8240cb",
  timestamp: "2020-05-13T00:37:49.130239Z",
  breadcrumbs: [],
  transaction: "/template-error/",
  contexts: {
    trace: {
      trace_id: "7f6b76eac5d042b78752db640a848008",
      span_id: "802ffce6fe075f40",
      parent_span_id: "be0f515132150c50",
      op: "django.middleware",
      description:
        "django.middleware.clickjacking.XFrameOptionsMiddleware.__call__",
    },
    runtime: {
      name: "CPython",
      version: "3.8.2",
      build: "3.8.2 (default, Apr 23 2020, 14:32:57) \n[GCC 8.3.0]",
    },
  },
  modules: {
    wheel: "0.34.2",
    webencodings: "0.5.1",
    attrs: "19.3.0",
    asgiref: "3.2.7",
    appdirs: "1.4.3",
  },
  extra: {
    "sys.argv": ["./manage.py", "runserver", "0.0.0.0:8001"],
  },
  request: {
    url: "http://localhost:8001/template-error/",
    query_string: "",
    method: "GET",
    env: {
      SERVER_NAME: "4c55e9e8d666",
      SERVER_PORT: "8001",
    },
    headers: {
      "Content-Length": "",
      "Content-Type": "text/plain",
      Host: "localhost:8001",
      "User-Agent":
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0",
      Accept:
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
      "Accept-Language": "en-US,en;q=0.5",
      "Accept-Encoding": "gzip, deflate",
      Connection: "keep-alive",
      Referer: "http://localhost:8001/",
      Cookie: "",
      "Upgrade-Insecure-Requests": "1",
      Dnt: "1",
    },
  },
  server_name: "4c55e9e8d666",
  sdk: {
    name: "sentry.python",
    version: "0.14.3",
    packages: [
      {
        name: "pypi:sentry-sdk",
        version: "0.14.3",
      },
    ],
    integrations: [
      "argv",
      "atexit",
      "dedupe",
      "django",
      "excepthook",
      "logging",
      "modules",
      "stdlib",
      "threading",
    ],
  },
  platform: "python",
  _meta: {
    exception: {
      values: {
        "0": {
          stacktrace: {
            frames: {
              "12": {
                vars: {
                  "": {
                    len: 13,
                  },
                },
              },
              "13": {
                vars: {
                  "": {
                    len: 11,
                  },
                },
              },
            },
          },
        },
      },
    },
    request: {
      headers: {
        Cookie: {
          "": {
            rem: [["!config", "x", 0, 373]],
          },
        },
      },
    },
  },
};

export const logging = {
  level: "warning",
  logger: "errors.views",
  logentry: { message: "Server warning: better have a look", params: [] },
  extra: { "sys.argv": ["./manage.py", "runserver", "0.0.0.0:8001"] },
  event_id: "78d24ed7495c46fc8dbde72c1f20679b",
  timestamp: "2020-04-24T18:23:02.950832Z",
  breadcrumbs: [],
  transaction: "/warning/",
  contexts: {
    trace: {
      trace_id: "1022e5e9d8e44d2ebafddfa839b58c5f",
      span_id: "9d329137b651e5ce",
      parent_span_id: "b18a82b300d6699d",
      op: "django.middleware",
      description:
        "django.middleware.clickjacking.XFrameOptionsMiddleware.__call__",
    },
    runtime: {
      name: "CPython",
      version: "3.8.2",
      build: "3.8.2 (default, Feb 26 2020, 15:09:34) \n[GCC 8.3.0]",
    },
  },
  modules: {
    wheel: "0.34.2",
    webencodings: "0.5.1",
    wcwidth: "0.1.8",
    urllib3: "1.25.8",
    "typed-ast": "1.4.1",
    traitlets: "4.3.3",
    tomlkit: "0.5.11",
    toml: "0.10.0",
    sqlparse: "0.3.1",
    six: "1.14.0",
    appdirs: "1.4.3",
  },
  request: {
    url: "http://localhost:8001/warning/",
    query_string: "",
    method: "GET",
    env: { SERVER_NAME: "5949a3cc0cd4", SERVER_PORT: "8001" },
    headers: {
      "Content-Length": "",
      "Content-Type": "text/plain",
      Host: "localhost:8001",
      "User-Agent":
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0",
      Accept:
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
      "Accept-Language": "en-US,en;q=0.5",
      "Accept-Encoding": "gzip, deflate",
      Referer: "http://localhost:8001/",
      Connection: "keep-alive",
      Cookie: "",
      "Upgrade-Insecure-Requests": "1",
      "Cache-Control": "max-age=0",
    },
  },
  server_name: "5949a3cc0cd4",
  sdk: {
    name: "sentry.python",
    version: "0.14.2",
    packages: [{ name: "pypi:sentry-sdk", version: "0.14.2" }],
    integrations: [
      "argv",
      "atexit",
      "dedupe",
      "django",
      "excepthook",
      "logging",
      "modules",
      "stdlib",
      "threading",
    ],
  },
  platform: "python",
  _meta: {
    request: {
      headers: { Cookie: { "": { rem: [["!config", "x", 0, 1110]] } } },
    },
  },
};
