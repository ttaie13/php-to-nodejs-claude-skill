# PHP to Node.js — Claude Skill

**Created by Tariq Al-Taie**

A reusable Claude Code skill for analysing and incrementally migrating **general PHP applications** to Node.js and TypeScript. Not a WordPress plugin.

Supports plain PHP, Laravel, Symfony, CodeIgniter and custom PHP MVC projects. It inventories source code and provides a migration workflow with feature parity, security, data migration and rollback checks.

## Install

Clone this repository and open it in Claude Code. The project skill is at `.claude/skills/php-to-nodejs/SKILL.md`. For use in another project, copy the `php-to-nodejs` skill folder to that project's `.claude/skills/` directory, and copy `scripts/php_inventory.py` to its scripts directory.

## Usage

```bash
python scripts/php_inventory.py /path/to/php-app --output migration-inventory.json
```

In Claude Code, ask:

> Use the php-to-nodejs skill to analyse this PHP application, create a route-by-route migration plan, rebuild it in Node.js/TypeScript with tests, and prepare a reviewable pull request. Do not touch production.

## Scope and limitations

This repository provides a **skill and a read-only scanner**, not a one-click automatic converter. Claude needs access to the actual PHP source and (for database parity) a safe schema/sample dataset. Framework-specific behaviour, authentication, business logic and integrations require careful implementation and verification.

Do not upload secrets or customer databases to public repositories. Production cutover always requires explicit approval.

## License

MIT. Copyright (c) 2026 Tariq Al-Taie.
