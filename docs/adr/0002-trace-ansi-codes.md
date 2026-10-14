# ADR-0002: Trace the foreground ANSI codes

- Status: Proposed
- Date: 2026-10-14
- Deciders: maintainers
- Related: ADR-0001
- Requirements: REQ-101
- Protected classes: docs/requirements.md

## Context

ADR-0001 adopted agk. The adoption pull request is the first governed change. The first change to this repository's
own behaviour is a requirement with a test marker, so that the traceability matrix has a project entry.

## Decision

The foreground ANSI codes are a requirement of this repository: `Fore.RED` is `ESC[31m` and `Fore.RESET` is
`ESC[39m`. The requirement is recorded as REQ-101 in `docs/requirements.md` (a protected path class), with status
`planned`, and the test `colorama/tests/trace_test.py` carries the marker `REQ-101 AC1`. No product source file
changes; the test asserts existing behaviour.

## Consequences

- `docs/requirements.md` gains REQ-101, and the traceability matrix lists REQ-101 with the test.
- The project's own CI (`test.yml`) runs the new test on its matrix.
- Marking REQ-101 `in-progress` or `done` is a reviewers' decision, not part of this change.

## Residual

None.
