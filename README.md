# Description

This repository is a fork of the HACS integration.
It addresses the backlog of unreviewed PRs often encountered in the main repository, aiming to provide a more up-to-date collection of custom components for the user.

This is achieved by an automated process that fetches daily all open Pull Requests from the original repository.


# How to use

The default repository of HACS integration has to be changed manually by editing the file `config/custom_components/hacs/enums.py` at line 23 to look like this:
```python
class HacsGitHubRepo(StrEnum):
    """HacsGitHubRepo."""

    DEFAULT = "bkbilly/hacs-default"
    INTEGRATION = "hacs/integration"
```

Home Assistant has to be restarted for the changes to take affect.


# Disclaimer

This repository is automatically updated with the latest open pull requests (PRs) from the `hacs/default` repository. However, it's important to note that these PRs may not have undergone the same level of testing and review as those in the official HACS repository. **I would recommend using this repository at your own discretion and carefully evaluating any custom components before installing it.**


# Default repositories

This is where HACS gets its default repositories from to show in the "store".

If you want to publish your repositories as default in HACS have a look here:

- https://hacs.xyz/docs/publish/start
- https://hacs.xyz/docs/publish/include
