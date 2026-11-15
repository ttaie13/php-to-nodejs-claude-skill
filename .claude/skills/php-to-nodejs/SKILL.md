---
name: php-to-nodejs
description: Migrate general PHP applications (plain PHP, Laravel, Symfony, CodeIgniter and custom frameworks) to Node.js/TypeScript using audited incremental parity checks.
---
# PHP to Node.js migration

Created by Tariq Al-Taie.

## Operating principles
- Work only on user-provided source and authorized infrastructure.
- Inspect before rewriting. Preserve user-facing design, URLs, business rules, access control, data and external integrations.
- Never claim a complete migration based only on syntax or build success.
- Do not modify production, overwrite a database, or deploy without explicit approval.
- Do not commit secrets, production dumps, uploaded private files or credentials.

## Workflow
1. Run `python scripts/php_inventory.py SOURCE --output migration-inventory.json` from repository root.
2. Read `references/migration-playbook.md`; inspect PHP source, composer.json, routes, templates, SQL, cron, queues and external services.
3. Create `MIGRATION_PLAN.md` mapping each route, screen, form, job, database table, role and integration to its Node.js counterpart. Mark unknowns as blockers.
4. Select architecture based on evidence: Express/Fastify for APIs, Next.js for SSR/UI, Prisma or native SQL for data. Avoid changing database semantics casually.
5. Implement feature-by-feature on a new branch, with unit/integration/visual tests. Never assume PHP and JS truthiness, dates, currency, password hashes or session handling are equivalent.
6. Provide repeatable, reversible database migration scripts, verified on an isolated sanitized staging copy.
7. Run build, tests, parity comparisons, security checks and performance checks. Report any incomplete features.
8. Prepare a PR with migration plan, test evidence, rollback procedure and known gaps. Ask approval before deployment.

## Output requirements
- migration-inventory.json
- MIGRATION_PLAN.md
- Node.js application source
- migration scripts and test evidence
- MIGRATION_REPORT.md with feature parity and unresolved blockers
