Search launch shortcut
CMD + SHIFT + P

Set the linelength per language:
Use CMD+SHIFT+P type in `settings.json` select "Preferences: Open Settings (JSON)"
Add:
```
    "[git-commit]": {"editor.rulers": [50]},
    "[python]": {"editor.rulers": [79]},
    "telemetry.telemetryLevel": "off",
```
