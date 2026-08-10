@echo off
REM Deep security scan of this repo.
REM Run weekly, or before pushing anything significant.

cd /d "%~dp0"

echo.
echo === Bandit ^(Python code patterns^) ===
bandit -r .
if errorlevel 1 (
    echo.
    echo ^>^>^> Bandit found issues. Fix before pushing.
) else (
    echo ^>^>^> Bandit clean.
)

echo.
echo === Trufflehog ^(secrets in git history^) ===
trufflehog --regex --entropy=True --max_depth 100 file://%CD%
echo ^>^>^> If you see "Reason:", you have a secret in history. Rotate the key, then use git-filter-repo to scrub it.

echo.
echo === Done ===
pause
