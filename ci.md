# Continuous Integration

Continuous Integration (CI) is implemented using [Travis](https://travis-ci.org) (and [Codecov](https://codecov.io/)). The `.travis.yml` file in this repository specifies what is to be executed as part of continuous integration - setting up a `conda` environment, running a series of tests and reporting coverage to Codecov (no further setup is required on the Codecov site). A [webhook](https://github.com/ScottishCovidResponse/simple_network_sim/settings/hooks) is present on GitHub, configured such that Travis CI is triggered on particular events (e.g. pull requests). Travis was enabled by switching on the repository using the appropriate [settings page](https://travis-ci.org/organizations/ScottishCovidResponse/repositories). This required action by an SCRC organisation member with appropriate privileges.