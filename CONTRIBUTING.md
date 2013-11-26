## Contributing
### The Short Version
Please:

* Obey [PEP 8][1] and [PEP 257][2].
* Write [good commit messages][3].
* For small items and fixes, [squash][4] your commits, i.e. make your pull
  requests just one commit.
* *Always* add tests and docs for your code.
* Use [Semantic versioning][5].
* Use appropriate branching strategy:
    * [GitHub Flow][14] for small projects.
    * [Vincent Driessen's][6] branching model for large projects.
* Add yourself to the [AUTHORS][7] file in an alphabetical order.

## In Detail
### Getting Started
* Make sure you have a [GitHub account][8].
* Submit a ticket for your issue, assuming one does not already exist.
    * Clearly describe the issue including steps to reproduce when it is a bug.
    * Make sure you fill in the earliest version that you know has the issue.
* Fork the repository on GitHub.
* Clone the repository onto your local machine:

    `git clone https://github.com/username/project.git`

### Making Changes
#### Small Projects
The branching strategy for small projects is inspired by GitHub's own
[GitHub Flow][14]:

* Make a descriptively named topic branch off of the `master` branch.

    `git branch my_contribution master`

    Then checkout with:

    `git checkout my_contribution`
    
    Or all at once:

    `git checkout -b my_contribution master`

#### Large Projects
For larger projects, inspiration is from Vincent Driessen's [branching
model][6].

* Make a sub-topic branch based on the `develop` topic-branch. So you would
  prefix your topic branch with "develop":

    `git checkout -b develop/my_contribution master`

* If other supporting branches are present, use the appropriate sub-topic
  branch as your prefix:

    `git checkout -b feature/my_contribution develop`

    or:

    `git checkout -b hotfix/my_contribution master`

    etc.

* If you are working on a particular issue, include that number in your topic
  branch:

    `git checkout -b develop/123-fixing-an-issue develop`

#### For All Projects
* Please avoid working directly on the "master" branch.
* Make commits of logical units.
* Check for unnecessary whitespace with `git diff --check` before committing.
* Please use spaces for all indentation and alignment, _no tabs_.
* Make sure your commit messages are in the [proper format][3]:

````
    (#99999) Make the example in CONTRIBUTING imperative and concrete

    Without this patch applied the example commit message in the CONTRIBUTING
    document is not a concrete example.  This is a problem because the
    contributor is left to imagine what the commit message should look like
    based on a description rather than an example.  This patch fixes the
    problem by making the example concrete and imperative.

    The first line is a real life imperative statement with a ticket number
    from our issue tracker.  The body describes the behavior without the patch,
    why this is a problem, and how the patch fixes the problem when applied.
````

* Make sure you have added the necessary tests for your changes.
* Run _all_ the tests to assure nothing else was accidentally broken:

    `$ python setup.py test`

#### Trivial Documentation Changes
For changes of a trivial nature to comments and documentation, it is not
always necessary to create a new ticket. In this case, it is
appropriate to start the first line of a commit with '(doc)' instead of
a ticket number:

````
    (doc) Add documentation commit example to CONTRIBUTING

    There is no example for contributing a documentation commit
    to the Puppet repository. This is a problem because the contributor
    is left to assume how a commit of this nature may appear.

    The first line is a real life imperative statement with '(doc)' in
    place of what would have been the ticket number in a 
    non-documentation related commit. The body describes the nature of
    the new documentation or comments added.
````

### Submitting Changes
Before submitting, make sure you have reviewed the [standard GitHub
workflow][13] and understand the difference between your fork (origin) and
repository from which you forked from (upstream).

* [Squash][4] your commits if needed first.

* [Push][9] your changes to a topic branch in your fork of the repository:

    `git push origin develop/my_contribution`

* Submit a [pull request][10] to the upstream repository.

## Versioning Policy
This project supports exactly one stable release at any given time and follows
the [Semantic Versioning][5] for its releases:
`(Major).(Minor).(Patch)`.

* **Major version**: Whenever there is something significant or any
    backwards-incompatible changes are introduced.
* **Minor version**: When new backwards-compatible functionality is introduced,
    a minor feature is introduced, or when a set of smaller features are
    rolled out.
* **Patch number**: When backwards compatible bug fixes are introduced that fix
    incorrect behavior.

The current stable release will receive security patches and bug fixes
(eg. `5.0` -> `5.0.1`).  Feature releases will mark the next supported stable
release where the minor version is increased numerically by increments of one
(eg. `5.0 -> 5.1`).

## Additional Resources
* [GitHub documentation][11]
* [Git documentation][12]

Thank you for your involvement!
[1]: http://www.python.org/dev/peps/pep-0008
[2]: http://www.python.org/dev/peps/pep-0257
[3]: http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
[4]: http://gitready.com/advanced/2009/02/10/squashing-commits-with-rebase.html 
[5]: http://semver.org
[6]: http://nvie.com/posts/a-successful-git-branching-model
[7]: AUTHORS.md "AUTHORS.md"
[8]: https://github.com/signup/free
[9]: https://help.github.com/articles/pushing-to-a-remote 
[10]: https://help.github.com/articles/using-pull-requests 
[11]: http://help.github.com
[12]: http://git-scm.com/documentation 
[13]: http://stackoverflow.com/q/9257533/2607578
[14]: http://scottchacon.com/2011/08/31/github-flow.html
