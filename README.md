# boilerplate

A Python script that outputs bare source files.

```
Usage:
    python3 bp.py -n [relevant name] [language]
    
Examples:
    python3 bp.py -n Homepage html
    
    python3 bp.py cpp
```

Specifying a relevant name will insert the name into the output in the appropriate places.

The currently supported languages are available in the templates folder.

## Template Format

The first line of all template files must be a valid JSON string. This should at least be an empty object `{}`. This can be used to specify the default name if the `-n` parameter is not given.

Currently the only template keyword is `%%name%%`.