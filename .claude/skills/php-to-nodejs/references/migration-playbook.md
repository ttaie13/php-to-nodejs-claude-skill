# Migration playbook

## Inventory
Trace entry points, route dispatch, controllers, PHP includes, templating, JS/CSS, composer packages, config, environment variables, SQL schema, stored procedures, file uploads, mail, payments, queues, scheduled tasks and webhooks.

## Security
Preserve role checks, CSRF protections, session lifetimes, password verification and rate limits. Use least-privilege database accounts. Keep credentials outside version control. Never export real customer data to a public repository.

## Data
Capture table structures, indexes, foreign keys, collation, timezone, decimal precision, nullability and cascade rules. Plan idempotent scripts and rollback. Validate row counts and referential integrity on staging.

## Parity
For each route record method, inputs, auth, status codes, output, redirects and side effects. Test happy path and failure modes. Screenshot representative pages at mobile and desktop sizes. Do not mark a feature migrated without evidence.

## Framework-specific
Laravel: routes, middleware, Eloquent, policies, Blade, queues, scheduler, artisan commands.
Symfony: routing, controllers, Doctrine, security voters, Twig, messenger.
CodeIgniter: routes, controllers, models, helpers, sessions, hooks.
Plain PHP: include graphs, global state, superglobals, raw SQL and filesystem dependencies.
