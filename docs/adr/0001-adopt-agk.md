# ADR-0001: colorama adopts agk

- Status: Proposed
- Date: 2026-10-14
- Deciders: maintainers
- Related: none
- Requirements: REQ-001, REQ-002, REQ-003

## Context

colorama is an existing repository. It adopts agk so that agent output stays consistent: rules live in committed
settings, hooks, CI checks and branch rules, and the method (requirements, specs, ADRs, reviewer groups, briefs) is
part of the repository. History before 2026-10-14 is not governed. The adoption pull request is the first governed
change.

Existing files of the project that fall in a protected class once agk is adopted. They are left as they are, and
changing them now needs an ADR that names the class:

- `.github/FUNDING.yml`
- `.github/workflows/lint_python.yml`
- `.github/workflows/test.yml`

## Decision

1. Install agk 0.4.0 on 2026-10-14 without changing any product file. New files: `agk.mk`, `agk.toml`,
   `scripts/agk/` (checks), `tests/kit/` (tests of the checks), `.claude/` (settings, hook, agent),
   `.github/workflows/governance.yml`, `config/`, `constitution/`, and `docs/` (requirements, ADRs, specs, briefs,
   runs, build-state). One marked agk block is appended to an existing `.gitignore`, `CLAUDE.md`,
   `.github/CODEOWNERS` and `.github/PULL_REQUEST_TEMPLATE.md`; absent ones are created. The project's `Makefile`,
   `pyproject.toml`, tests and build configuration are not touched.
2. Protected paths are listed in `config/protected-paths.txt`: `constitution/`, `config/`, `.claude/`, `.github/`,
   `docs/requirements.md`, `CLAUDE.md`, `scripts/agk/`, `tests/kit/`, `agk.mk`, `agk.toml`. They change only with an
   ADR in the same PR that names each changed path class. A change that touches only `- Status:` lines of
   `docs/requirements.md` is exempt.
3. The default branch is `master`. Everything from the adoption pull request on goes through a pull
   request that passes the `governance` job. The ruleset for the default branch (`master`) is exactly: Active; no bypass; target the default branch; restrict deletions; require linear history; require a pull request (0 approvals, dismiss stale approvals, squash merge only); block force pushes; required status check `governance`.
   Repository settings: allow auto-merge; auto-delete head branches.
4. Reviewer model: path classes map to reviewer groups in `config/reviewers.yaml`; approvers are teams, never
   personal names. Agents implement; maintainers decide.
5. The kit's tests run through `agk.mk` and the checks read `agk.toml`; the project keeps running its own tests and
   its own lint in its own CI.

## Consequences

- Weakening a check requires an ADR, which makes the weakening visible and reviewable.
- The project's existing workflows under `.github/` are now protected.

## Residual

- 2026-10-14: `config/reviewers.yaml` maps `maintainers` to a placeholder handle; replace it with a real team or user.
- 2026-10-14: the ruleset is a GitHub setting, not a file; apply it by hand.
