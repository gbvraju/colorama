# Fork day 1: adopt agk into colorama

Date: 2026-10-14 (`date -u`)
agk SHA (`gbvraju/agk` `main`, cloned read-only to `../agk-kit`): `d64c42c7e4b713ecf9a337ba63f91b34819829e4`

## Notes

- `agk-test` needed pytest; it ran in a throwaway venv outside the repository (`/home/user/agk-venv`).
- Findings (a) to (c) below.

## Findings

(a) **Missing `origin/HEAD` in session clones.** `adopt.py` refused (`cannot tell the default branch from
TARGET/.git`) because the clone had no `refs/remotes/origin/HEAD`. I created it locally with
`git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/master`; the change is inside `.git` only and no
tracked file is affected.

(b) **`--codeowners` prints to stdout.** `reviewers.py --codeowners` writes the rendering to stdout and does not
write `.github/CODEOWNERS`, unlike the brief ("writes the whole file when adopt created it"). I redirected its output
into the file (`... --codeowners > .github/CODEOWNERS`); `--check-codeowners` then passed.

(c) **Adoption adds a new lint failure.** The project's `lint_python.yml` already fails on upstream master (since
2026-05-13, verified by the reviewer from the upstream Actions page). Adoption adds a separate failure on top: the CI
step `bandit --recursive --skip B311 .` reports 255 findings in kit files on this branch and 0 on `master`
(checked locally with bandit run from the throwaway venv, same flags, on `origin/master` and on `adopt-agk`).

| Test | Count | Where |
| ---- | ----- | ----- |
| B101 (assert) | 224 | `tests/kit` |
| B603 (subprocess call) | 17 | `tests/kit` 12, `scripts/agk` 4, `.claude/hooks` 1 |
| B607 (partial executable path) | 9 | `tests/kit` 4, `scripts/agk` 4, `.claude/hooks` 1 |
| B404 (subprocess import) | 5 | `tests/kit` 3, `scripts/agk` 1, `.claude/hooks` 1 |

Without `--skip B311`, bandit counts 6 B311 findings (`demos/demo06.py`) on both `master` and the branch; they are
not new. No kit file or workflow was changed to silence the findings. Ruling on Q-FK-3: the red `lint_python` is
accepted for this PR (already red upstream; the kit's part is recorded here); the fix goes in agk.

## Zero-touch proof

`git ls-files -s` before (49 files) against after `git add -A` (96 files). Pre-existing tracked files whose entry
differs: exactly one.

- `.gitignore`: only the appended `# >>> agk` ... `# <<< agk` block (5 ignore patterns).

All other 48 pre-existing files are byte-identical. 46 new files were added.

## `adopt.py . --dry-run` output

```
create .claude/agents/drift-auditor.md
create .claude/hooks/stop_check.py
create .claude/settings.json
create .github/CODEOWNERS
create .github/PULL_REQUEST_TEMPLATE.md
create .github/workflows/governance.yml
append .gitignore
create CLAUDE.md
create agk.mk
create agk.toml
create config/neutrality.txt
create config/protected-paths.txt
create config/reviewers.yaml
create constitution/principles.md
create constitution/vision.md
create docs/adr/0001-adopt-agk.md
create docs/adr/TEMPLATE.md
create docs/briefs/TEMPLATE.md
create docs/build-state.md
create docs/requirements.md
create docs/runs/decisions-log.md
create docs/specs/TEMPLATE.md
create scripts/agk/check_adrs.py
create scripts/agk/check_build_state.py
create scripts/agk/check_neutrality.py
create scripts/agk/check_pr_body.py
create scripts/agk/check_protected_changes.py
create scripts/agk/check_requirements.py
create scripts/agk/check_specs.py
create scripts/agk/common.py
create scripts/agk/config.py
create scripts/agk/reviewers.py
create scripts/agk/traceability.py
create tests/kit/conftest.py
create tests/kit/pytest.ini
create tests/kit/test_agk_config.py
create tests/kit/test_agk_mk.py
create tests/kit/test_check_adrs.py
create tests/kit/test_check_build_state.py
create tests/kit/test_check_neutrality.py
create tests/kit/test_check_pr_body.py
create tests/kit/test_check_protected_changes.py
create tests/kit/test_check_requirements.py
create tests/kit/test_check_specs.py
create tests/kit/test_reviewers.py
create tests/kit/test_stop_hook.py
create tests/kit/test_workflow.py
dry run: 47 files would change; nothing was written
notice: config/reviewers.yaml maps `maintainers` to the placeholder @REPLACE-ME
Apply by hand on GitHub to the default branch `master` (adopt configures nothing):
The ruleset `main` is exactly: Active; no bypass; target the default branch; restrict deletions; require linear history; require a pull request (0 approvals, dismiss stale approvals, squash merge only); block force pushes; required status check `governance`.
Repository settings: allow auto-merge; auto-delete head branches.
```

## `adopt.py .` output

```
create .claude/agents/drift-auditor.md
create .claude/hooks/stop_check.py
create .claude/settings.json
create .github/CODEOWNERS
create .github/PULL_REQUEST_TEMPLATE.md
create .github/workflows/governance.yml
append .gitignore
create CLAUDE.md
create agk.mk
create agk.toml
create config/neutrality.txt
create config/protected-paths.txt
create config/reviewers.yaml
create constitution/principles.md
create constitution/vision.md
create docs/adr/0001-adopt-agk.md
create docs/adr/TEMPLATE.md
create docs/briefs/TEMPLATE.md
create docs/build-state.md
create docs/requirements.md
create docs/runs/decisions-log.md
create docs/specs/TEMPLATE.md
create scripts/agk/check_adrs.py
create scripts/agk/check_build_state.py
create scripts/agk/check_neutrality.py
create scripts/agk/check_pr_body.py
create scripts/agk/check_protected_changes.py
create scripts/agk/check_requirements.py
create scripts/agk/check_specs.py
create scripts/agk/common.py
create scripts/agk/config.py
create scripts/agk/reviewers.py
create scripts/agk/traceability.py
create tests/kit/conftest.py
create tests/kit/pytest.ini
create tests/kit/test_agk_config.py
create tests/kit/test_agk_mk.py
create tests/kit/test_check_adrs.py
create tests/kit/test_check_build_state.py
create tests/kit/test_check_neutrality.py
create tests/kit/test_check_pr_body.py
create tests/kit/test_check_protected_changes.py
create tests/kit/test_check_requirements.py
create tests/kit/test_check_specs.py
create tests/kit/test_reviewers.py
create tests/kit/test_stop_hook.py
create tests/kit/test_workflow.py
installed 47 files
notice: config/reviewers.yaml maps `maintainers` to the placeholder @REPLACE-ME
Apply by hand on GitHub to the default branch `master` (adopt configures nothing):
The ruleset `main` is exactly: Active; no bypass; target the default branch; restrict deletions; require linear history; require a pull request (0 approvals, dismiss stale approvals, squash merge only); block force pushes; required status check `governance`.
Repository settings: allow auto-merge; auto-delete head branches.
```

## Verification

```
python3 scripts/agk/check_protected_changes.py
ok protected-changes (protected change covered by an ADR)
python3 scripts/agk/check_requirements.py
ok requirements (3 requirements)
python3 scripts/agk/check_adrs.py
ok adrs (1 ADRs)
python3 scripts/agk/check_specs.py
ok specs
python3 scripts/agk/check_neutrality.py
ok neutrality (0 tokens)
python3 scripts/agk/check_build_state.py
ok build-state (file created)
python3 scripts/agk/reviewers.py --check
ok reviewers
python3 scripts/agk/reviewers.py --check-codeowners
ok reviewers (.github/CODEOWNERS matches)
```

```
ruff check --isolated --line-length 100 --target-version py311 --select E,F,I,B,UP scripts/agk tests/kit .claude/hooks
All checks passed!
```

```
AGK_KIT_TESTS=1 python3 -m pytest -c tests/kit/pytest.ini tests/kit  -q
........................................................................ [ 48%]
........................................................................ [ 96%]
......                                                                   [100%]
150 passed in 10.77s
```
