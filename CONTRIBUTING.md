> (the content of this file was inspired by and adopted from psf/black and opengovernment - shout out to whomever this may concern)

Bug reports and fixes are always welcome! Please follow the issue template on GitHub for best results.

Before you suggest a new feature, ask yourself why you want it. 
If it enables better integration with some workflow, fixes an inconsistency, speeds things up, and so on - go for it! 
On the other hand, if your answer is "because I don't like a particular formatting" then you're not ready to embrace Black (shout out to psf/black!!) yet. Such changes are unlikely to get accepted. 
You can still try but prepare to be disappointed. ;)

## Submitting changes

Please send a GitHub Pull Request with a clear list of what you've done. 
When you send a pull request, make sure to consider test coverage and usage examples. We can always use more test coverage! 

Please follow our coding conventions (below) and make sure all of your commits are atomic (one feature per commit).

Always write a clear log message for your commits. One-line messages are fine for small changes, but bigger changes should look like this:

```
$ git commit -m "A brief summary of the commit
> 
> A paragraph describing what changed and its impact."
```

### Before submitting pull requests, run tests with:

```
$ python setup.py test
```

# (Coding) Standards

## Hygiene

If you're fixing a bug, add a test. Run it first to confirm it fails, then fix the bug, run it again to confirm it's really fixed.
If adding a new feature, add a test. In fact, always add a test. But wait, before adding any large feature, first open an issue for us to discuss the idea first.

## Write readable code

Follow PEP standards where applicable, use a linter. Get inspired by the code already present in the library.

# Finally

Thanks again for your interest in improving the project!
