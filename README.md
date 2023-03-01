# py-patch-demo

## Patching using string target
patch('target-string'), think target string as namespace, it where the function is being
used, not where it's defined. 

## Patching module direct
patch.dict(), patch.object(), under the test file, import the module you want to override, and patching diretly. 

