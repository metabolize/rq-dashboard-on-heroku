# rq-dashboard-on-heroku

[![rq-dashboard](https://img.shields.io/github/pipenv/locked/dependency-version/metabolize/rq-dashboard-on-heroku/rq-dashboard?style=flat-square)][pipfile]
[![python](https://img.shields.io/github/pipenv/locked/python-version/metabolize/rq-dashboard-on-heroku?style=flat-square)][pipfile]
![](https://img.shields.io/github/license/metabolize/rq-dashboard-on-heroku?style=flat-square)
[![build](https://img.shields.io/circleci/project/github/metabolize/rq-dashboard-on-heroku?style=flat-square)][build]
[![code style](https://img.shields.io/badge/code%20style-black-black.svg?style=flat-square)][black]

[pipfile]: https://github.com/metabolize/rq-dashboard-on-heroku/blob/master/Pipfile
[build]: https://circleci.com/gh/metabolize/rq-dashboard-on-heroku/tree/master
[black]: https://black.readthedocs.io/en/stable/

A version of [RQ Dashboard][] that can be deployed to Heroku.

[rq dashboard]: https://github.com/eoranged/rq-dashboard


## Deployment

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


## Configuration

Three settings must be configured:

- `RQ_DASHBOARD_REDIS_URL=rediss://redis:6379`
- `RQ_DASHBOARD_USERNAME=user`
- `RQ_DASHBOARD_PASSWORD=pass`


## License

This project is licensed under the 2-clause BSD license.
