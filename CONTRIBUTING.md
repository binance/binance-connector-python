# Contributing

Love this package and want to help? Thanks so much, there's something to do for everybody!

Please take a moment to review this document in order to make the contribution process easy and effective for everyone involved.

Following these guidelines helps to communicate that you respect the time of the developers managing and developing this open source project. In return, they should reciprocate that respect in addressing your issue or assessing patches and features.

## Using the issue tracker

The [issue tracker](https://github.com/binance/binance-connector-python/issues) is the preferred channel for [bug reports](#bug-reports), [features requests](#feature-requests) and [submitting pull requests](#pull-requests).

<a name="bugs"></a>

## Bug reports

A bug is a _demonstrable problem_ that is caused by the code in the repository.
Good bug reports are extremely helpful - thank you!

Guidelines for bug reports:

1.  **Use the GitHub issue search** &mdash; check if the issue has already been reported.

2.  **Check if the issue has been fixed** &mdash; try to reproduce it using the latest `master` or development branch in the repository.

3.  **Isolate the problem** &mdash; ideally create a [reduced test case](https://css-tricks.com/reduced-test-cases/) and a live example.

4.  **Use the bug report template** &mdash; please fill in the template which appears when you open a new issue.

A good bug report shouldn't leave others needing to chase you up for more information. Please try to be as detailed as possible in your report. What is your environment? What steps will reproduce the issue? What browser(s) and OS
experience the problem? What would you expect to be the outcome? All these details will help people to fix any potential bugs.

<a name="features"></a>

## Feature requests

Feature requests are welcome. But take a moment to find out whether your idea fits with the scope and aims of the project. It's up to _you_ to make a strong case to convince the project's developers of the merits of this feature. Please provide as many details and as much context as possible.

<a name="pull-requests"></a>

## Pull requests

Good pull requests - patches, improvements, new features - are a fantastic help. They should remain focused in scope and avoid containing unrelated commits.

**Please ask first** before embarking on any significant pull request (e.g. implementing features, refactoring code, porting to a different language), otherwise you risk spending a lot of time working on something that the project's developers might not want to merge into the project.

Since the `master` branch is what people actually use in production, we have release candidate branches, which are usually name after `rc-`, that unstable changes get merged into first. Only when we consider that stable we merge it into the `master` branch and release the changes officially.

Adhering to the following process is the best way to get your work included in the project:

1.  [Fork](https://help.github.com/articles/fork-a-repo/) the project, clone your fork, and configure the remotes:

    ```bash
    # Clone your fork of the repo into the current directory
    git clone https://github.com/<your-username>/binance-connector-python.git
    # Navigate to the newly cloned directory
    cd binance-connector-python
    # Assign the original repo to a remote called "upstream"
    git remote add upstream https://github.com/binance/binance-connector-python.git
    ```

2.  If you cloned a while ago, get the latest changes from upstream:

    ```bash
    git checkout <latest_rc_branch>
    git pull upstream <latest_rc_branch>
    ```

3.  Create a new topic branch (off the `rc-` branch) to contain your feature, change, or fix:

    ```bash
    git checkout -b <topic-branch-name>
    ```

4.  Work on your code, but please don't forget:
    - Add [Docstring](https://www.python.org/dev/peps/pep-0257/) to any new module, function, class, or method. You can consult files within `/binance` for references;
    - If reasonable (ex: new endpoint), add example file to the `/examples` folder - please use `logging`/`logger` with ideal logging level to log the messages;
    - If reasonable (ex: new endpoint), add test file to the `/tests` folder - use [pytest](https://docs.pytest.org/en/6.2.x/contents.html) to check if all tests are passed.
    - If reasonable (ex: new endpoint), add documentation to the `/docs` folder - please refer to [reStructuredText](https://devguide.python.org/documenting/);
    - Write changes to `CHANGELOG.md` and `CHANGELOG.rst` under the `Unreleased` section - please create the section if not existing yet, this is later to be converted into the verion and date of release;
    - Make sure there's no typos and the namings are simple and not ambiguous; 

5.  Commit your changes, taking in attention these [git commit message guidelines](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)

6.  Locally merge (or rebase) the upstream rc branch into your topic branch:

    ```bash
    git pull [--rebase] upstream <latest_rc_branch>
    ```


7.  Push your topic branch up to your fork:

    ```bash
    git push origin <topic-branch-name>
    ```

8.  [Open a Pull Request](https://help.github.com/articles/using-pull-requests/) with a clear title and description.

**IMPORTANT**: By submitting a patch, you agree to allow the project
owners to license your work under the terms of the MIT License.
